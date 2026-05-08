from __future__ import annotations

import logging
import re
import time
import urllib.request
from collections.abc import Iterable
from datetime import datetime, timezone
from typing import Any

import feedparser
from bs4 import BeautifulSoup

from src.models import Article

logger = logging.getLogger(__name__)

GEEKNEWS_RSS_URL = "https://news.hada.io/rss/news"
GEEKNEWS_TOPIC_URL = "https://news.hada.io/topic?id={id}"
USER_AGENT = "article-collector/0.1 (+https://news.hada.io reader; personal learning use)"
TOPIC_FETCH_DELAY_SEC = 0.7  # 점잖게


def fetch_rss_entries(rss_url: str = GEEKNEWS_RSS_URL) -> list[dict[str, Any]]:
    """Parse the GeekNews Atom feed and return one dict per entry.

    feedparser sets a default User-Agent that origin server blocks, so we set ours.
    """
    feedparser.USER_AGENT = USER_AGENT
    parsed = feedparser.parse(rss_url)
    if parsed.bozo and not parsed.entries:
        raise RuntimeError(f"Failed to parse RSS feed: {parsed.bozo_exception!r}")

    entries: list[dict[str, Any]] = []
    for e in parsed.entries:
        topic_id = _extract_topic_id(e.get("id") or e.get("link", ""))
        if topic_id is None:
            continue
        published = _parse_published(e.get("published") or e.get("updated"))
        entries.append(
            {
                "topic_id": topic_id,
                "title": e.get("title", "").strip(),
                "geeknews_url": e.get("link", "").strip(),
                "published": published,
            }
        )
    return entries


def fetch_articles(skip_ids: Iterable[str] = ()) -> list[Article]:
    """Fetch RSS entries and hydrate each with topic-page metadata.

    Skips topic_ids whose canonical id (e.g. "hada-29273") is already in skip_ids.
    """
    skip = set(skip_ids)
    rss_entries = fetch_rss_entries()
    logger.info("RSS returned %d entries", len(rss_entries))

    articles: list[Article] = []
    for i, entry in enumerate(rss_entries):
        canonical_id = f"hada-{entry['topic_id']}"
        if canonical_id in skip:
            logger.debug("skipping already-collected %s", canonical_id)
            continue
        try:
            article = _hydrate_topic(entry, canonical_id)
        except Exception:  # don't let one bad topic kill the run
            logger.exception("failed to hydrate topic %s", canonical_id)
            continue
        articles.append(article)
        if i < len(rss_entries) - 1:
            time.sleep(TOPIC_FETCH_DELAY_SEC)
    return articles


def _hydrate_topic(entry: dict[str, Any], canonical_id: str) -> Article:
    topic_id = entry["topic_id"]
    url = GEEKNEWS_TOPIC_URL.format(id=topic_id)
    html = _http_get(url)
    soup = BeautifulSoup(html, "lxml")

    external_url, source_domain = _extract_external_link(soup, fallback_url=entry["geeknews_url"])
    score = _extract_score(soup, topic_id)
    comments = _extract_comment_count(soup)
    summary_html = _extract_summary_html(soup)
    summary_text = _html_to_text(summary_html)

    return Article(
        id=canonical_id,
        title=entry["title"],
        url=external_url,
        geeknews_url=entry["geeknews_url"],
        source="geeknews",
        collected_at=entry["published"] or datetime.now(timezone.utc),
        geeknews_summary=summary_text,
        geeknews_score=score,
        geeknews_comments=comments,
        tags=[t for t in [source_domain] if t],
    )


def _extract_topic_id(url_or_id: str) -> str | None:
    m = re.search(r"id=(\d+)", url_or_id)
    return m.group(1) if m else None


def _parse_published(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def _http_get(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def _extract_external_link(soup: BeautifulSoup, fallback_url: str) -> tuple[str, str]:
    """The external article URL lives in the topictitle anchor; domain in `.topicurl` span."""
    title_div = soup.select_one("div.topictitle a")
    href = title_div.get("href") if title_div else None
    domain_span = soup.select_one("span.topicurl")
    domain = domain_span.get_text(strip=True).strip("()") if domain_span else ""
    if href and isinstance(href, str) and href.startswith("http"):
        return href, domain
    return fallback_url, domain


def _extract_score(soup: BeautifulSoup, topic_id: str) -> int:
    span = soup.select_one(f"#tp{topic_id}")
    if not span:
        return 0
    txt = span.get_text(strip=True)
    return int(txt) if txt.isdigit() else 0


def _extract_comment_count(soup: BeautifulSoup) -> int:
    a = soup.select_one("a#topic-comment-link[data-topic-comment-count]")
    if not a:
        return 0
    raw = a.get("data-topic-comment-count", "0")
    if isinstance(raw, list):
        raw = raw[0] if raw else "0"
    raw_str = str(raw or "0")
    return int(raw_str) if raw_str.isdigit() else 0


def _extract_summary_html(soup: BeautifulSoup) -> str:
    """Return the inner HTML of #topic_contents, the GeekNews-authored Korean summary."""
    node = soup.select_one("#topic_contents")
    if not node:
        return ""
    return node.decode_contents()


def _html_to_text(html: str) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "lxml")
    return soup.get_text("\n", strip=True)

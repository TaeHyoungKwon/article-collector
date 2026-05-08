from __future__ import annotations

import logging
import re
from collections.abc import Iterator
from pathlib import Path

import frontmatter

from src.models import Article, article_from_frontmatter

logger = logging.getLogger(__name__)

ARTICLES_SUBDIR = "articles"

TLDR_HEADER = "## TL;DR"
GEEKNEWS_HEADER = "## GeekNews 요약"
MY_NOTE_HEADER = "## My Note"
MY_NOTE_PLACEHOLDER = "<!-- 한 줄 코멘트 남기기 -->"
TLDR_PLACEHOLDER = "(요약 대기 중)"
GEEKNEWS_PLACEHOLDER = "(요약 없음)"

MARKDOWN_TEMPLATE = """## TL;DR
{tldr_block}

## GeekNews 요약
{geeknews_summary}

## 원문
- [원문]({url})
- [GeekNews 토론]({geeknews_url})

{my_note_section}
"""


def vault_articles_dir(vault_root: Path) -> Path:
    return vault_root / ARTICLES_SUBDIR


def existing_ids(vault_root: Path) -> set[str]:
    """Return the set of article ids already saved under vault_root/articles."""
    articles_dir = vault_articles_dir(vault_root)
    if not articles_dir.exists():
        return set()

    ids: set[str] = set()
    for path in articles_dir.glob("*.md"):
        try:
            post = frontmatter.load(path)
        except Exception:
            logger.warning("could not parse frontmatter in %s; skipping for dedupe", path)
            continue
        article_id = post.metadata.get("id")
        if isinstance(article_id, str):
            ids.add(article_id)
    return ids


def save_article(article: Article, vault_root: Path) -> Path:
    """Write an Article to vault_root/articles/{filename}.

    Idempotent w.r.t. user state: if the file already exists, the user's `read` flag and
    `## My Note` content are preserved (we never overwrite the human's signal).
    """
    articles_dir = vault_articles_dir(vault_root)
    articles_dir.mkdir(parents=True, exist_ok=True)

    target = articles_dir / article.filename()

    preserved_note = ""
    preserved_read = article.read
    if target.exists():
        try:
            existing = frontmatter.load(target)
            preserved_note = _extract_my_note(existing.content)
            if existing.metadata.get("read"):
                preserved_read = True
        except Exception:
            logger.warning("existing file %s unreadable; will overwrite", target)

    article.read = preserved_read
    article.my_note = preserved_note or article.my_note

    body = render_markdown(article)
    post = frontmatter.Post(content=body, **article.to_frontmatter())
    target.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
    return target


def render_markdown(article: Article) -> str:
    tldr_block = (
        "\n".join(f"- {line}" for line in article.tldr) if article.tldr else f"- {TLDR_PLACEHOLDER}"
    )
    note_body = article.my_note.strip() or MY_NOTE_PLACEHOLDER
    my_note_section = f"{MY_NOTE_HEADER}\n{note_body}"
    return MARKDOWN_TEMPLATE.format(
        tldr_block=tldr_block,
        geeknews_summary=article.geeknews_summary.strip() or GEEKNEWS_PLACEHOLDER,
        url=article.url,
        geeknews_url=article.geeknews_url,
        my_note_section=my_note_section,
    )


def iter_articles(vault_root: Path) -> Iterator[Article]:
    """Yield every saved Article, restoring body sections (TL;DR, GeekNews summary, My Note)."""
    articles_dir = vault_articles_dir(vault_root)
    if not articles_dir.exists():
        return
    for path in sorted(articles_dir.glob("*.md")):
        try:
            post = frontmatter.load(path)
        except Exception:
            logger.warning("skipping unparseable %s", path)
            continue
        if "id" not in post.metadata:
            continue
        article = article_from_frontmatter(
            post.metadata,
            my_note=_extract_my_note(post.content),
        )
        article.tldr = _extract_tldr(post.content)
        article.geeknews_summary = _extract_geeknews_summary(post.content)
        yield article


def _extract_section(body: str, header: str) -> str:
    pattern = re.compile(
        rf"^{re.escape(header)}\s*\n(.*?)(?=^##\s|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else ""


def _extract_my_note(body: str) -> str:
    note = _extract_section(body, MY_NOTE_HEADER)
    if note == MY_NOTE_PLACEHOLDER:
        return ""
    return note


def _extract_tldr(body: str) -> list[str]:
    section = _extract_section(body, TLDR_HEADER)
    if not section:
        return []
    bullets: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")):
            bullets.append(line[2:].strip())
    if len(bullets) == 1 and bullets[0] == TLDR_PLACEHOLDER:
        return []
    return bullets


def _extract_geeknews_summary(body: str) -> str:
    section = _extract_section(body, GEEKNEWS_HEADER)
    if section == GEEKNEWS_PLACEHOLDER:
        return ""
    return section

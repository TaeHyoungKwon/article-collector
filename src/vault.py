from __future__ import annotations

import logging
import re
from collections.abc import Iterator
from pathlib import Path

import frontmatter

from src.models import Article, article_from_frontmatter

logger = logging.getLogger(__name__)

ARTICLES_SUBDIR = "articles"

MY_NOTE_HEADER = "## My Note"
MY_NOTE_PLACEHOLDER = "<!-- 한 줄 코멘트 남기기 -->"

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
    tldr_block = "\n".join(f"- {line}" for line in article.tldr) if article.tldr else "- (요약 대기 중)"
    note_body = article.my_note.strip() or MY_NOTE_PLACEHOLDER
    my_note_section = f"{MY_NOTE_HEADER}\n{note_body}"
    return MARKDOWN_TEMPLATE.format(
        tldr_block=tldr_block,
        geeknews_summary=article.geeknews_summary.strip() or "(요약 없음)",
        url=article.url,
        geeknews_url=article.geeknews_url,
        my_note_section=my_note_section,
    )


def iter_articles(vault_root: Path) -> Iterator[Article]:
    """Yield every saved Article in chronological order, with my_note populated from the body."""
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
        my_note = _extract_my_note(post.content)
        yield article_from_frontmatter(post.metadata, my_note=my_note)


def _extract_my_note(body: str) -> str:
    """Pull the contents of the `## My Note` section, ignoring the placeholder."""
    pattern = re.compile(
        rf"^{re.escape(MY_NOTE_HEADER)}\s*\n(.*?)(?=^##\s|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(body)
    if not m:
        return ""
    note = m.group(1).strip()
    if note == MY_NOTE_PLACEHOLDER or not note:
        return ""
    return note

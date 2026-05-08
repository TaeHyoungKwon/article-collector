from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any


@dataclass
class Article:
    id: str
    title: str
    url: str
    geeknews_url: str
    source: str
    collected_at: datetime
    geeknews_summary: str = ""
    geeknews_score: int = 0
    geeknews_comments: int = 0
    tldr: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    matched_keywords: list[str] = field(default_factory=list)
    recommend_score: float = 0.0
    recommended_on: date | None = None
    read: bool = False
    my_note: str = ""

    def to_frontmatter(self) -> dict[str, Any]:
        data: dict[str, Any] = {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "geeknews_url": self.geeknews_url,
            "source": self.source,
            "collected_at": self.collected_at.isoformat(),
            "geeknews_score": self.geeknews_score,
            "geeknews_comments": self.geeknews_comments,
            "tags": self.tags,
            "matched_keywords": self.matched_keywords,
            "recommend_score": round(self.recommend_score, 3),
            "read": self.read,
        }
        if self.recommended_on is not None:
            data["recommended_on"] = self.recommended_on.isoformat()
        return data

    def filename(self) -> str:
        return f"{self.collected_at.date().isoformat()}-{slugify(self.title)}-{self.id}.md"


def slugify(text: str) -> str:
    """Make a filesystem-safe slug. Keep Korean characters; replace whitespace and unsafe chars."""
    normalized = unicodedata.normalize("NFC", text).strip().lower()
    # Replace forbidden filesystem chars and whitespace with hyphens
    normalized = re.sub(r"[\s/\\:*?\"<>|]+", "-", normalized)
    # Drop other ASCII punctuation that's noisy in filenames
    normalized = re.sub(r"[!@#$%^&()=+\[\]{};,'`~]", "", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    return normalized[:60] if len(normalized) > 60 else normalized


def article_from_frontmatter(meta: dict[str, Any], my_note: str = "") -> Article:
    """Reconstruct an Article from a vault file's frontmatter (best-effort, used for feedback scan)."""
    collected_at_raw = meta.get("collected_at")
    if isinstance(collected_at_raw, datetime):
        collected_at = collected_at_raw
    elif isinstance(collected_at_raw, str):
        collected_at = datetime.fromisoformat(collected_at_raw)
    else:
        collected_at = datetime.now()

    recommended_on_raw = meta.get("recommended_on")
    if isinstance(recommended_on_raw, date):
        recommended_on = recommended_on_raw
    elif isinstance(recommended_on_raw, str):
        recommended_on = date.fromisoformat(recommended_on_raw)
    else:
        recommended_on = None

    return Article(
        id=str(meta["id"]),
        title=str(meta.get("title", "")),
        url=str(meta.get("url", "")),
        geeknews_url=str(meta.get("geeknews_url", "")),
        source=str(meta.get("source", "geeknews")),
        collected_at=collected_at,
        geeknews_score=int(meta.get("geeknews_score", 0)),
        geeknews_comments=int(meta.get("geeknews_comments", 0)),
        tags=list(meta.get("tags", []) or []),
        matched_keywords=list(meta.get("matched_keywords", []) or []),
        recommend_score=float(meta.get("recommend_score", 0.0) or 0.0),
        recommended_on=recommended_on,
        read=bool(meta.get("read", False)),
        my_note=my_note,
    )

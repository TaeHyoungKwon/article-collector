from __future__ import annotations

import math
import os
from collections.abc import Iterable
from datetime import date

from src.models import Article

DEFAULT_KEYWORDS: tuple[str, ...] = (
    "backend",
    "AI",
    "distributed system",
    "LLM",
    "RAG",
    "Claude Code",
    "Codex",
)

# Tunable weights. Stored as module constants so they can be tweaked without API churn.
KEYWORD_WEIGHT = 2.0
GEEKNEWS_SCORE_WEIGHT = 1.0
COMMENT_WEIGHT = 0.3
ALREADY_RECOMMENDED_PENALTY = 1000.0  # effectively excludes from recommendation


def configured_keywords() -> tuple[str, ...]:
    """Read KEYWORDS env var (comma-separated) or fall back to DEFAULT_KEYWORDS."""
    raw = os.environ.get("KEYWORDS")
    if not raw:
        return DEFAULT_KEYWORDS
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    return tuple(parts) if parts else DEFAULT_KEYWORDS


def score_articles(
    articles: Iterable[Article],
    keywords: Iterable[str] | None = None,
) -> None:
    """Compute recommend_score and matched_keywords for each article in place."""
    kws = tuple(keywords) if keywords is not None else configured_keywords()

    for a in articles:
        matched = _match_keywords(a, kws)
        a.matched_keywords = matched

        score = 0.0
        score += KEYWORD_WEIGHT * len(matched)
        score += GEEKNEWS_SCORE_WEIGHT * math.log1p(max(0, a.geeknews_score))
        score += COMMENT_WEIGHT * math.log1p(max(0, a.geeknews_comments))
        if a.recommended_on is not None:
            score -= ALREADY_RECOMMENDED_PENALTY
        a.recommend_score = round(score, 3)


def top_n(articles: Iterable[Article], n: int = 10) -> list[Article]:
    """Return the n highest-scoring articles, breaking ties by collected_at desc."""
    return sorted(
        articles,
        key=lambda a: (a.recommend_score, a.collected_at),
        reverse=True,
    )[:n]


def mark_recommended(articles: Iterable[Article], on_date: date) -> None:
    for a in articles:
        a.recommended_on = on_date


def _match_keywords(article: Article, keywords: tuple[str, ...]) -> list[str]:
    haystack = " ".join(
        [
            article.title,
            article.geeknews_summary,
            " ".join(article.tags),
        ]
    ).lower()
    matched: list[str] = []
    for kw in keywords:
        if kw.lower() in haystack:
            matched.append(kw)
    return matched

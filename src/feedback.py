from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from src.models import Article
from src.vault import iter_articles


@dataclass
class FeedbackReport:
    total_articles: int = 0
    total_recommended: int = 0
    total_read: int = 0
    total_commented: int = 0
    keyword_engagement: Counter[str] = field(default_factory=Counter)
    keyword_recommended: Counter[str] = field(default_factory=Counter)

    @property
    def read_rate(self) -> float:
        if self.total_recommended == 0:
            return 0.0
        return self.total_read / self.total_recommended

    @property
    def comment_rate_among_read(self) -> float:
        """The KPI: of articles read (or marked engaged), what fraction got a written note?"""
        if self.total_read == 0:
            return 0.0
        return self.total_commented / self.total_read

    def keyword_lift(self, keyword: str) -> float:
        """Engagement rate for articles tagged with this keyword.

        Returns engaged/recommended; 0 if the keyword never appeared in a recommendation.
        """
        rec = self.keyword_recommended.get(keyword, 0)
        if rec == 0:
            return 0.0
        return self.keyword_engagement.get(keyword, 0) / rec


def is_engaged(a: Article) -> bool:
    return a.read or bool(a.my_note.strip())


def collect_feedback(vault_root: Path) -> FeedbackReport:
    return summarize_articles(iter_articles(vault_root))


def summarize_articles(articles: Iterable[Article]) -> FeedbackReport:
    report = FeedbackReport()
    for a in articles:
        report.total_articles += 1
        recommended = a.recommended_on is not None
        engaged = is_engaged(a)
        commented = bool(a.my_note.strip())

        if recommended:
            report.total_recommended += 1
            for kw in a.matched_keywords:
                report.keyword_recommended[kw] += 1
        if engaged:
            report.total_read += 1
            for kw in a.matched_keywords:
                report.keyword_engagement[kw] += 1
        if commented:
            report.total_commented += 1
    return report

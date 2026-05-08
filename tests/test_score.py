from datetime import date, datetime, timezone

from src.models import Article
from src.score import (
    ALREADY_RECOMMENDED_PENALTY,
    DEFAULT_KEYWORDS,
    categorize_articles,
    configured_keywords,
    mark_recommended,
    score_articles,
    top_n,
)


def make_article(**overrides) -> Article:
    base = dict(
        id="hada-1",
        title="t",
        url="u",
        geeknews_url="g",
        source="geeknews",
        collected_at=datetime(2026, 5, 8, tzinfo=timezone.utc),
        geeknews_summary="",
    )
    base.update(overrides)
    return Article(**base)


def test_keyword_matches_in_title():
    a = make_article(title="Building scalable backend with distributed system patterns")
    score_articles([a], keywords=("backend", "distributed system", "frontend"))
    assert set(a.matched_keywords) == {"backend", "distributed system"}
    assert a.recommend_score > 0


def test_keyword_matches_in_summary():
    a = make_article(
        title="Some Article",
        geeknews_summary="이 글은 RAG와 LLM의 조합을 다룬다.",
    )
    score_articles([a], keywords=("RAG", "LLM", "Codex"))
    assert set(a.matched_keywords) == {"RAG", "LLM"}


def test_keyword_match_is_case_insensitive():
    a = make_article(title="claude code workflow")
    score_articles([a], keywords=("Claude Code",))
    assert a.matched_keywords == ["Claude Code"]


def test_geeknews_score_contributes():
    low = make_article(id="a", title="x", geeknews_score=1)
    high = make_article(id="b", title="x", geeknews_score=100)
    score_articles([low, high], keywords=())
    assert high.recommend_score > low.recommend_score


def test_already_recommended_penalty():
    a = make_article(title="backend system", recommended_on=date(2026, 5, 7))
    score_articles([a], keywords=("backend",))
    assert a.recommend_score < -ALREADY_RECOMMENDED_PENALTY + 100  # heavy penalty applied


def test_top_n_orders_by_score():
    arts = [
        make_article(id="a", title="backend"),
        make_article(id="b", title="AI LLM"),
        make_article(id="c", title="random"),
    ]
    score_articles(arts, keywords=("backend", "AI", "LLM"))
    top = top_n(arts, n=2)
    assert [a.id for a in top] == ["b", "a"]  # b has 2 matches, a has 1


def test_top_n_tie_breaks_by_recency():
    arts = [
        make_article(id="old", title="t", collected_at=datetime(2026, 5, 7, tzinfo=timezone.utc)),
        make_article(id="new", title="t", collected_at=datetime(2026, 5, 8, tzinfo=timezone.utc)),
    ]
    score_articles(arts, keywords=())
    top = top_n(arts, n=1)
    assert top[0].id == "new"


def test_mark_recommended_sets_date():
    a = make_article()
    mark_recommended([a], date(2026, 5, 8))
    assert a.recommended_on == date(2026, 5, 8)


def test_configured_keywords_default(monkeypatch):
    monkeypatch.delenv("KEYWORDS", raising=False)
    assert configured_keywords() == DEFAULT_KEYWORDS


def test_configured_keywords_env_override(monkeypatch):
    monkeypatch.setenv("KEYWORDS", "go, kubernetes,observability")
    assert configured_keywords() == ("go", "kubernetes", "observability")


def test_categorize_ai_takes_priority_over_backend():
    a = make_article(matched_keywords=["AI", "backend"])
    categorize_articles([a])
    assert a.category == "AI"


def test_categorize_dev_tools():
    a = make_article(matched_keywords=["Claude Code"])
    categorize_articles([a])
    assert a.category == "Dev Tools"


def test_categorize_backend_only():
    a = make_article(matched_keywords=["distributed system"])
    categorize_articles([a])
    assert a.category == "Backend"


def test_categorize_no_match_falls_back_to_other():
    a = make_article(matched_keywords=[])
    categorize_articles([a])
    assert a.category == "Other"

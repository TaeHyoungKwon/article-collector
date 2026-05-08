from datetime import date, datetime, timezone

from src.feedback import is_engaged, summarize_articles
from src.models import Article


def make_article(**overrides) -> Article:
    base = dict(
        id="hada-1",
        title="t",
        url="u",
        geeknews_url="g",
        source="geeknews",
        collected_at=datetime(2026, 5, 8, tzinfo=timezone.utc),
    )
    base.update(overrides)
    return Article(**base)


def test_is_engaged_when_read_flag_set():
    assert is_engaged(make_article(read=True))


def test_is_engaged_when_note_written():
    assert is_engaged(make_article(my_note="흥미로운 글"))


def test_not_engaged_when_neither():
    assert not is_engaged(make_article())


def test_not_engaged_for_whitespace_note():
    assert not is_engaged(make_article(my_note="   \n  "))


def test_summarize_counts_correctly():
    arts = [
        make_article(id="a", recommended_on=date(2026, 5, 8), matched_keywords=["backend"]),
        make_article(
            id="b",
            recommended_on=date(2026, 5, 8),
            matched_keywords=["backend", "AI"],
            read=True,
        ),
        make_article(
            id="c",
            recommended_on=date(2026, 5, 8),
            matched_keywords=["AI"],
            read=True,
            my_note="좋다",
        ),
        make_article(id="d"),  # not recommended, not engaged
    ]
    r = summarize_articles(arts)
    assert r.total_articles == 4
    assert r.total_recommended == 3
    assert r.total_read == 2
    assert r.total_commented == 1
    assert r.read_rate == 2 / 3
    assert r.comment_rate_among_read == 1 / 2


def test_keyword_lift():
    arts = [
        make_article(id="a", recommended_on=date(2026, 5, 8), matched_keywords=["backend"]),
        make_article(
            id="b",
            recommended_on=date(2026, 5, 8),
            matched_keywords=["backend"],
            my_note="x",
        ),
        make_article(id="c", recommended_on=date(2026, 5, 8), matched_keywords=["AI"]),
    ]
    r = summarize_articles(arts)
    assert r.keyword_lift("backend") == 0.5
    assert r.keyword_lift("AI") == 0.0
    assert r.keyword_lift("nonexistent") == 0.0

from datetime import datetime

from src.models import Article, article_from_frontmatter, slugify


def test_slugify_korean_preserved():
    assert slugify("Claude Code 새 기능") == "claude-code-새-기능"


def test_slugify_strips_unsafe_chars():
    assert slugify("Hello / World: Foo?") == "hello-world-foo"


def test_filename_uses_date_slug_and_id():
    a = Article(
        id="hada-12345",
        title="Distributed System Patterns",
        url="https://example.com/x",
        geeknews_url="https://news.hada.io/topic?id=12345",
        source="geeknews",
        collected_at=datetime(2026, 5, 8, 8, 0, 0),
    )
    assert a.filename() == "2026-05-08-distributed-system-patterns-hada-12345.md"


def test_to_frontmatter_roundtrip():
    a = Article(
        id="hada-1",
        title="t",
        url="u",
        geeknews_url="g",
        source="geeknews",
        collected_at=datetime(2026, 5, 8, 8, 0, 0),
        tags=["backend", "AI"],
        matched_keywords=["backend"],
        recommend_score=4.5,
        read=True,
    )
    meta = a.to_frontmatter()
    restored = article_from_frontmatter(meta)
    assert restored.id == "hada-1"
    assert restored.tags == ["backend", "AI"]
    assert restored.matched_keywords == ["backend"]
    assert restored.recommend_score == 4.5
    assert restored.read is True

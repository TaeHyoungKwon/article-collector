from datetime import date, datetime, timezone

from src.models import Article
from src.mailer import render_email_html


def make_article(**overrides) -> Article:
    base = dict(
        id="hada-1",
        title="분산 시스템 패턴",
        url="https://example.com/post",
        geeknews_url="https://news.hada.io/topic?id=1",
        source="geeknews",
        collected_at=datetime(2026, 5, 8, tzinfo=timezone.utc),
        geeknews_summary="요약",
        geeknews_score=42,
        geeknews_comments=7,
        tldr=["핵심1", "핵심2", "핵심3"],
        tags=["example.com"],
        matched_keywords=["distributed system"],
        recommend_score=5.5,
    )
    base.update(overrides)
    return Article(**base)


def test_render_email_contains_essentials():
    a = make_article()
    html = render_email_html([a], date(2026, 5, 8))
    assert "오늘의 아티클 추천 — 2026-05-08" in html
    assert "분산 시스템 패턴" in html
    assert "https://example.com/post" in html
    assert "핵심1" in html
    assert "GN점수 42" in html
    assert "댓글 7" in html
    assert "distributed system" in html


def test_render_email_no_obsidian_link_without_vault():
    html = render_email_html([make_article()], date(2026, 5, 8))
    assert "obsidian://" not in html


def test_render_email_with_obsidian_vault():
    a = make_article()
    html = render_email_html([a], date(2026, 5, 8), obsidian_vault_name="articles-vault")
    assert "obsidian://open?" in html
    assert "vault=articles-vault" in html
    assert urlencoded_filename_present(html, a.filename())


def test_render_email_handles_empty_tldr():
    html = render_email_html([make_article(tldr=[])], date(2026, 5, 8))
    assert "분산 시스템 패턴" in html
    # No <ul> bullets when tldr empty
    assert "<ul" not in html


def test_render_email_escapes_html():
    a = make_article(title="<script>alert(1)</script>")
    html = render_email_html([a], date(2026, 5, 8))
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;" in html


def urlencoded_filename_present(html: str, filename: str) -> bool:
    import urllib.parse

    quoted = urllib.parse.quote(f"articles/{filename}", safe="")
    return quoted in html or f"articles/{filename}".replace("/", "%2F") in html

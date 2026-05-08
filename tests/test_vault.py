from datetime import datetime, timezone
from pathlib import Path

from src.models import Article
from src.vault import (
    INDEX_FILENAME,
    MY_NOTE_HEADER,
    MY_NOTE_PLACEHOLDER,
    existing_ids,
    iter_articles,
    render_markdown,
    save_article,
    write_index,
)


def make_article(**overrides) -> Article:
    base = dict(
        id="hada-1",
        title="테스트 글",
        url="https://example.com/x",
        geeknews_url="https://news.hada.io/topic?id=1",
        source="geeknews",
        collected_at=datetime(2026, 5, 8, 8, 0, 0, tzinfo=timezone.utc),
        geeknews_summary="요약 내용",
        geeknews_score=10,
        geeknews_comments=3,
        tldr=["핵심1", "핵심2", "핵심3"],
        tags=["backend", "AI"],
        matched_keywords=["backend"],
        recommend_score=4.2,
    )
    base.update(overrides)
    return Article(**base)


def test_render_markdown_includes_sections():
    a = make_article()
    md = render_markdown(a)
    assert "## TL;DR" in md
    assert "- 핵심1" in md
    assert "## GeekNews 요약" in md
    assert "요약 내용" in md
    assert "## 원문" in md
    assert MY_NOTE_HEADER in md
    assert MY_NOTE_PLACEHOLDER in md


def test_save_and_existing_ids(tmp_path: Path):
    a = make_article()
    save_article(a, tmp_path)
    assert existing_ids(tmp_path) == {"hada-1"}


def test_save_preserves_user_my_note(tmp_path: Path):
    a = make_article()
    path = save_article(a, tmp_path)

    # Simulate user editing My Note
    text = path.read_text(encoding="utf-8")
    text = text.replace(MY_NOTE_PLACEHOLDER, "RSS 정말 죽지 않네, 흥미로움")
    path.write_text(text, encoding="utf-8")

    # Re-save the same article (e.g. re-run pipeline) — user note must survive
    save_article(make_article(geeknews_summary="갱신된 요약"), tmp_path)
    final = path.read_text(encoding="utf-8")
    assert "RSS 정말 죽지 않네, 흥미로움" in final
    assert "갱신된 요약" in final


def test_save_preserves_read_flag(tmp_path: Path):
    save_article(make_article(), tmp_path)
    path = list((tmp_path / "articles").glob("*.md"))[0]

    # User flips read: true
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("read: false", "read: true"), encoding="utf-8")

    # Pipeline re-saves with read=False default — must remain true
    save_article(make_article(read=False), tmp_path)
    final = path.read_text(encoding="utf-8")
    assert "read: true" in final


def test_iter_articles_round_trip(tmp_path: Path):
    save_article(make_article(id="hada-1", title="첫번째"), tmp_path)
    save_article(make_article(id="hada-2", title="두번째"), tmp_path)
    ids = {a.id for a in iter_articles(tmp_path)}
    assert ids == {"hada-1", "hada-2"}


def test_iter_articles_extracts_my_note(tmp_path: Path):
    path = save_article(make_article(), tmp_path)
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace(MY_NOTE_PLACEHOLDER, "내 코멘트"), encoding="utf-8")
    articles = list(iter_articles(tmp_path))
    assert len(articles) == 1
    assert articles[0].my_note == "내 코멘트"


def test_existing_ids_empty_when_no_dir(tmp_path: Path):
    assert existing_ids(tmp_path) == set()


def test_iter_articles_restores_geeknews_summary(tmp_path: Path):
    save_article(make_article(geeknews_summary="원본 GeekNews 요약 본문"), tmp_path)
    arts = list(iter_articles(tmp_path))
    assert arts[0].geeknews_summary == "원본 GeekNews 요약 본문"


def test_iter_articles_restores_tldr(tmp_path: Path):
    save_article(make_article(tldr=["첫째", "둘째", "셋째"]), tmp_path)
    arts = list(iter_articles(tmp_path))
    assert arts[0].tldr == ["첫째", "둘째", "셋째"]


def test_iter_articles_empty_tldr_when_placeholder(tmp_path: Path):
    save_article(make_article(tldr=[]), tmp_path)  # writes placeholder
    arts = list(iter_articles(tmp_path))
    assert arts[0].tldr == []


def test_save_article_prepends_category_to_tags(tmp_path: Path):
    save_article(make_article(category="AI", tags=["anthropic.com"]), tmp_path)
    arts = list(iter_articles(tmp_path))
    assert arts[0].tags[0] == "AI"
    assert "anthropic.com" in arts[0].tags


def test_write_index_creates_file_with_dataview_queries(tmp_path: Path):
    path = write_index(tmp_path)
    assert path.name == INDEX_FILENAME
    content = path.read_text(encoding="utf-8")
    assert "```dataview" in content
    assert 'WHERE category = "AI"' in content
    assert 'WHERE category = "Backend"' in content
    assert 'WHERE category = "Other"' in content
    assert "WHERE recommended_on != null AND read = false" in content

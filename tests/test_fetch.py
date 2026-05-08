from bs4 import BeautifulSoup

from src.fetch import (
    _extract_comment_count,
    _extract_external_link,
    _extract_score,
    _extract_summary_html,
    _extract_topic_id,
    _html_to_text,
    _parse_published,
)

TOPIC_HTML = """
<html><body>
<div class=topic data-topic-state-id='29273'>
  <div class='topictitle link'>
    <a href='https://example.com/post' class='bold ud'><h1>Test Title</h1></a>
    <span class=topicurl>(example.com)</span>
  </div>
  <div class=topicinfo>
    <span id='tp29273'>42</span>P
    <a id='topic-comment-link' data-topic-comment-count='7' href='topic?id=29273'>댓글 7개</a>
  </div>
  <div class=topic_contents>
    <div id='topic_contents'>
      <ul>
        <li>첫 번째 <strong>요약</strong> 항목</li>
        <li>두 번째 항목</li>
      </ul>
    </div>
  </div>
</div>
</body></html>
"""


def test_extract_topic_id():
    assert _extract_topic_id("https://news.hada.io/topic?id=12345") == "12345"
    assert _extract_topic_id("topic?id=42&foo=1") == "42"
    assert _extract_topic_id("https://news.hada.io/about") is None


def test_parse_published_iso():
    dt = _parse_published("2026-05-08T07:33:21+09:00")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 5 and dt.day == 8


def test_parse_published_none():
    assert _parse_published(None) is None
    assert _parse_published("not a date") is None


def test_extract_external_link():
    soup = BeautifulSoup(TOPIC_HTML, "lxml")
    url, domain = _extract_external_link(soup, fallback_url="https://news.hada.io/topic?id=29273")
    assert url == "https://example.com/post"
    assert domain == "example.com"


def test_extract_external_link_fallback_when_missing():
    soup = BeautifulSoup("<html><body></body></html>", "lxml")
    url, domain = _extract_external_link(soup, fallback_url="https://news.hada.io/topic?id=1")
    assert url == "https://news.hada.io/topic?id=1"
    assert domain == ""


def test_extract_score():
    soup = BeautifulSoup(TOPIC_HTML, "lxml")
    assert _extract_score(soup, "29273") == 42


def test_extract_score_missing():
    soup = BeautifulSoup("<html></html>", "lxml")
    assert _extract_score(soup, "29273") == 0


def test_extract_comment_count():
    soup = BeautifulSoup(TOPIC_HTML, "lxml")
    assert _extract_comment_count(soup) == 7


def test_extract_summary_converts_to_markdown():
    soup = BeautifulSoup(TOPIC_HTML, "lxml")
    html = _extract_summary_html(soup)
    text = _html_to_text(html)
    # bullets become "- " markdown lines (inline bold preserved on the same line)
    assert "- 첫 번째 **요약** 항목" in text
    assert "- 두 번째 항목" in text
    # raw HTML tags must not survive
    assert "<strong>" not in text
    assert "<li>" not in text


def test_html_to_text_preserves_links():
    from src.fetch import _html_to_text

    md = _html_to_text('<p>참고: <a href="https://example.com">예시</a> 링크</p>')
    assert "[예시](https://example.com)" in md

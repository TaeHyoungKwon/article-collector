from __future__ import annotations

import logging
import os
from collections.abc import Iterable

from anthropic import Anthropic

from src.models import Article

logger = logging.getLogger(__name__)

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 400

SYSTEM_PROMPT = """당신은 한국어 기술 아티클을 3줄로 요약하는 전문가입니다.

규칙:
- 정확히 3줄. 더도 덜도 안 됨.
- 각 줄은 한 문장의 한국어 불릿. 줄 앞에 "- " 를 붙이세요.
- 첫 줄: 이 글이 다루는 핵심 주제/대상이 무엇인가.
- 둘째 줄: 가장 흥미롭거나 핵심적인 사실/주장 하나.
- 셋째 줄: 독자에게 왜 의미 있는가, 또는 어떤 시사점이 있는가.
- 형용사 남발 금지. 구체적이고 정보 밀도가 높을 것.
- 원문 요약에 없는 사실은 만들지 않을 것.
- 영어 고유명사/기술 용어는 그대로 두되, 설명은 한국어로.
- 출력에는 3개의 불릿 외에 어떤 텍스트도 포함하지 않음 (서두/마무리 멘트 금지).
"""


def summarize_articles(articles: Iterable[Article], client: Anthropic | None = None) -> None:
    """Mutate each Article.tldr in place with a 3-line summary."""
    if client is None:
        client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    for article in articles:
        if not article.geeknews_summary.strip():
            logger.warning("no geeknews_summary for %s; skipping summarization", article.id)
            continue
        try:
            article.tldr = _summarize_one(client, article)
        except Exception:
            logger.exception("summarization failed for %s; leaving tldr empty", article.id)
            article.tldr = []


def _summarize_one(client: Anthropic, article: Article) -> list[str]:
    user_content = (
        f"# 제목\n{article.title}\n\n"
        f"# 출처 도메인\n{', '.join(article.tags) or '(없음)'}\n\n"
        f"# GeekNews 요약\n{article.geeknews_summary}"
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_content}],
    )

    text = "".join(block.text for block in response.content if block.type == "text")
    return _parse_three_bullets(text)


def _parse_three_bullets(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    bullets: list[str] = []
    for line in lines:
        if line.startswith(("- ", "* ", "• ")):
            bullets.append(line[2:].strip())
        elif line[0:2].rstrip(".").isdigit() and "." in line[:3]:
            bullets.append(line.split(".", 1)[1].strip())
        else:
            bullets.append(line)
    return bullets[:3]

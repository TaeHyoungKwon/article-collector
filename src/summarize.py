from __future__ import annotations

import logging
import os
from collections.abc import Iterable

import httpx

from src.models import Article

logger = logging.getLogger(__name__)

GITHUB_MODELS_URL = "https://models.github.ai/inference/chat/completions"
GITHUB_API_VERSION = "2026-03-10"
MODEL = "openai/gpt-4o-mini"
MAX_TOKENS = 400
REQUEST_TIMEOUT = 30.0

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


def summarize_articles(articles: Iterable[Article], client: httpx.Client | None = None) -> None:
    """Mutate each Article.tldr in place with a 3-line summary via GitHub Models.

    Reads token from GITHUB_MODELS_TOKEN (preferred for local dev) or GITHUB_TOKEN
    (auto-provided in GitHub Actions when the workflow has `permissions: models: read`).
    """
    token = os.environ.get("GITHUB_MODELS_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.warning(
            "neither GITHUB_MODELS_TOKEN nor GITHUB_TOKEN set; skipping summarization"
        )
        return

    active_client = client if client is not None else httpx.Client(timeout=REQUEST_TIMEOUT)
    try:
        for article in articles:
            if not article.geeknews_summary.strip():
                logger.warning("no geeknews_summary for %s; skipping", article.id)
                continue
            try:
                article.tldr = _summarize_one(active_client, token, article)
            except Exception:
                logger.exception("summarization failed for %s; leaving tldr empty", article.id)
                article.tldr = []
    finally:
        if client is None:
            active_client.close()


def _summarize_one(client: httpx.Client, token: str, article: Article) -> list[str]:
    user_content = (
        f"# 제목\n{article.title}\n\n"
        f"# 출처 도메인\n{', '.join(article.tags) or '(없음)'}\n\n"
        f"# GeekNews 요약\n{article.geeknews_summary}"
    )

    response = client.post(
        GITHUB_MODELS_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": GITHUB_API_VERSION,
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "max_tokens": MAX_TOKENS,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ],
        },
    )
    response.raise_for_status()
    payload = response.json()
    text = payload["choices"][0]["message"]["content"]
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

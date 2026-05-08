# article-collector

태형님 학습용 아티클 수집/추천 파이프라인.

매일 아침 GeekNews RSS를 수집해 LLM 3줄 요약을 붙이고, Obsidian vault(`vault/`)에 markdown으로 저장한 뒤, 키워드/점수 기반 top 10을 Gmail로 발송한다. 읽고 `## My Note`에 코멘트를 남기면 다음날 추천 알고리즘이 그 시그널을 학습한다.

## 구성

```
src/        # 파이프라인 코드 (Python)
vault/      # Obsidian vault root (articles/ 안에 글 저장)
.github/    # 매일 아침 cron 워크플로
tests/      # pytest
```

## 핵심 결정

- 소스: GeekNews (https://news.hada.io/rss). 이후 확장.
- 요약: GeekNews 자체 한국어 요약 보존 + 최상단에 Claude Haiku 4.5 3줄 요약.
- 본문: 외부 원문 본문은 수집하지 않음 (요약만).
- 추천 점수 v0: GeekNews 점수 + 매칭 키워드 + 다양성 - 중복 페널티.
- 학습 시그널: frontmatter `read: true` 또는 `## My Note` 섹션 비어있지 않음.

## 실행 환경

GitHub Actions cron — UTC 23:00 (KST 08:00). 코드와 vault가 같은 repo에 있어 워크플로가 vault를 직접 commit & push한다.

## 운영 가이드

`.env.example` 참조. 운영 가이드는 step 12에서 채워진다.

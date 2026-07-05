---
category: AI
collected_at: '2026-07-04T10:50:23+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31111
id: hada-31111
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -992.901
recommended_on: '2026-07-05'
source: geeknews
tags:
- AI
- Other
- github.com/owjs3901
title: 'Show GN: Retry-now, 지금 바로 윤회 - 완전 자율 루프 에이전트'
url: https://github.com/owjs3901/retry-now
---

## TL;DR
- 이 글은 윤회형 AI 코딩 에이전트 `retry-now`의 구조와 작동 방식을 설명한다.
- `retry-now`는 매번 새로운 세션에서 코드를 분석하고 개선하여 이전 판단의 영향을 받지 않도록 설계되었다.
- 독자에게 이 시스템은 코드 개선 과정의 효율성을 높이는 방법으로, 개발 환경의 발전에 기여할 수 있다.

## GeekNews 요약
AI 코딩 에이전트를 반복 실행해서 코드베이스를 점진적으로 개선하는 에이전트 `retry-now`를 만들었습니다.

핵심 아이디어는 "매 이터레이션마다 완전히 새로운 컨텍스트 0 세션에서 코드를 다시 보게 하자"입니다.  
기존 장기 실행 에이전트는 이전 판단을 방어하거나, 이미 시도한 방향에 끌려가거나, 긴 컨텍스트 안에서 점점 표류하는 경우가 있다고 느꼈습니다. retry-now는 반대로 매번 새 headless 에이전트 세션을 띄우고, 현재 코드만 보고 분석 → 개선 → 검증 → 기록을 반복합니다.

동작 흐름은 대략 이렇습니다.

1. ANALYZE: 읽기 전용으로 코드베이스를 분석하고, `file:line` 근거가 있는 개선 후보를 만듭니다.
2. IMPROVE: 후보를 항목별로 적용합니다. 각 항목은 백업 후 수정하고, 테스트/린트/벤치마크 검증에서 실패하면 그 항목만 되돌립니다.
3. 여러 번 연속으로 “더 개선할 게 없음”이 나오면 수렴했다고 보고 멈춥니다.

현재 `opencode`, `Codex CLI`, `Claude Code`와 함께 쓸 수 있고, Bun 기반 CLI로 실행합니다.

극한의 성능 최적화와 메모리 사용률을 낮추기 위하여 사용됩니다.

## 원문
- [원문](https://github.com/owjs3901/retry-now)
- [GeekNews 토론](https://news.hada.io/topic?id=31111)

## My Note
<!-- 한 줄 코멘트 남기기 -->

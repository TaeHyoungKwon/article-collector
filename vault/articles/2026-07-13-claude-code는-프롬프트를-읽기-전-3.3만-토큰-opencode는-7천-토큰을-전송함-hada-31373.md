---
category: AI
collected_at: '2026-07-13T09:55:24+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31373
id: hada-31373
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -994.693
recommended_on: '2026-07-13'
source: geeknews
tags:
- AI
- Other
- systima.ai
title: Claude Code는 프롬프트를 읽기 전 3.3만 토큰, OpenCode는 7천 토큰을 전송함
url: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
---

## TL;DR
- 이 글은 Claude Code와 OpenCode의 API 호출 시 고정 오버헤드에 대한 비교 분석이다.
- Claude Code는 첫 요청에서 약 32,800토큰의 고정 오버헤드를 기록해 OpenCode보다 4.7배 많았다.
- 이 정보는 AI 모델 선택 시 성능과 비용 효율성을 고려하는 데 중요한 기준이 될 수 있다.

## GeekNews 요약
- 동일한 모델·머신·작업에서 API 경계를 측정한 결과, Sonnet 4.5 첫 요청의 고정 오버헤드는 **Claude Code 약 32,800토큰**, OpenCode 약 6,900토큰으로 4.7배 차이 났으며 Fable 5에서는 약 3.3배로 줄어듦
- 격차의 대부분은 **도구 스키마**에서 발생함. Claude Code는 27개 도구 정의에 약 24,000토큰, OpenCode는 10개 도구에 약 4,800토큰을 사용했고, 도구를 모두 꺼도 시스템 프롬프트가 각각 약 6,500토큰과 2,000토큰이었음
- 실제 설정에서는 72KB 명령 파일이 요청마다 약 20,000토큰, 소형 MCP 서버 하나가 약 1,000~1,400토큰을 추가해 첫 요청만 **75,000~90,817토큰**에 이를 수 있음
- Claude Code는 동일한 파일 요약 작업에서 OpenCode보다 **캐시 쓰기를 5.9~54배** 많이 발생시켰고, 두 하위 에이전트로 작업을 분산하자 직접 실행 시 121,000토큰이던 사용량이 513,000토큰으로 4.2배 늘어남
- 고정 오버헤드만으로 전체 비용을 판단할 수는 없음. 다단계 작업에서는 Claude Code가 도구 호출을 병렬 배치해 3회 요청으로 약 121,000토큰을 쓴 반면, OpenCode는 직렬 호출 9회로 약 132,000토큰을 사용함

---

## 원문
- [원문](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
- [GeekNews 토론](https://news.hada.io/topic?id=31373)

## My Note
<!-- 한 줄 코멘트 남기기 -->

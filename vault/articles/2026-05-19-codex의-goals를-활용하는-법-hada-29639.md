---
category: AI
collected_at: '2026-05-19T09:18:01+09:00'
geeknews_comments: 2
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=29639
id: hada-29639
matched_keywords:
- AI
- Codex
read: false
recommend_score: 6.275
recommended_on: '2026-05-19'
source: geeknews
tags:
- AI
- Other
- developers.openai.com
title: Codex의 Goals를 활용하는 법
url: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
---

## TL;DR
- 이 글은 Codex의 Goals 기능을 어떻게 활용할 수 있는지에 대해 설명한다.
- Goals는 영속적 목표 기능으로, 여러 턴에 걸쳐 복잡한 작업을 쉽게 처리할 수 있도록 돕는다.
- 이는 사용자가 Codex의 작업을 사용자 통제 하에 효율적으로 관리할 수 있게 하여 실용성을 높인다.

## GeekNews 요약
- **Goals**는 Codex 스레드가 정의된 결과를 향해 여러 턴에 걸쳐 작업을 지속하도록 만드는 **영속적 목표(persistent objective)** 기능
- 단일 프롬프트로 처리하기 어려운 **프로파일링, 패치, 벤치마킹, 플레이키 테스트 재현, 근거 기반 감사** 같은 작업에 적합
- 결과(outcome), 검증 수단(verification surface), 제약(constraints)을 정의하면 Codex가 **증거 기반으로 완료 여부를 자체 판단**
- `/goal`, `/goal pause`, `/goal resume`, `/goal clear` 명령으로 **수명주기 제어** 가능, Codex 0.128.0부터 지원
- 스레드 범위로 제한된 **완료 계약(completion contract)** 구조이며, 무제한 자율 실행이 아닌 **사용자 통제 하의 지속성**이 핵심

---

## 원문
- [원문](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)
- [GeekNews 토론](https://news.hada.io/topic?id=29639)

## My Note
<!-- 한 줄 코멘트 남기기 -->

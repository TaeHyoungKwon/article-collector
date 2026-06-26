---
category: AI
collected_at: '2026-06-26T15:28:52+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30854
id: hada-30854
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.901
recommended_on: '2026-06-26'
source: geeknews
tags:
- AI
- Other
- github.com/Junghoo-developer
title: 'Show GN: SongRyeon Core - LLM이 쓴 말과 코드가 검증한 정보를 분리하는 로컬 에이전트 런타임 실험'
url: https://github.com/Junghoo-developer/SongRyeon
---

## TL;DR
- 이 글은 SongRyeon Core라는 로컬 에이전트 런타임 실험을 통해 LLM의 판단과 코드가 검증한 정보를 구분하는 방법을 다룬다.
- 정보는 절대정보, 상대정보, 혼합정보로 나뉘어, 각 정보를 보다 명확하게 처리할 수 있는 구조를 제공한다.
- 이 실험은 AI 에이전트의 신뢰성을 높이고 사용자가 정보를 올바르게 이해할 수 있도록 돕는 중요한 시도를 의미한다.

## GeekNews 요약
안녕하세요. 코딩을 배우면서 AI 에이전트 런타임을 직접 실험하고 있는 정후입니다.

SongRyeon Core는 “LLM이 말한 판단”과 “코드가 실제로 확인한 사실”을 분리해서 다루는 작은 로컬 우선(agent runtime) 실험입니다.

요즘 LLM 기반 에이전트를 만들다 보면 다음 문제가 자주 생긴다고 느꼈습니다.

- LLM이 추측한 내용을 시스템 사실처럼 보여줌
- 코드가 만든 fallback이나 휴리스틱이 LLM 판단처럼 섞임
- 문서를 몇 개 읽었는지, 어떤 실행이 실제로 일어났는지 화면마다 다르게 보임
- 최종 답변이 내부 런타임 상태와 어긋남

그래서 이 프로젝트에서는 정보를 크게 세 가지로 나눠 다룹니다.

- 절대정보: 코드/trace/schema/tool result로 확인 가능한 값
- 상대정보: 하나의 절대정보에 대응하는 LLM 판단
- 혼합정보: 여러 source bundle에 근거한 LLM 판단

현재는 아직 작은 연습판이지만, 다음 같은 구조를 실험하고 있습니다.

- node\_0 memory supplier
- node\_1 router
- L loop
- node\_3 reporter
- node\_4 verifier
- smoke-test 기반 회귀 검증
- runtime terminal/final renderer 정직성 검사

목표는 “멋진 데모”보다, AI 에이전트가 어떤 근거로 무엇을 말했는지 최대한 숨기지 않는 작은 런타임을 만들어보는 것입니다.

아직 제가 코딩을 배우는 중이라 거친 부분이 많습니다.  
구조, README, 테스트, 용어 정의, agent runtime 설계에 대해 피드백 주시면 정말 감사하겠습니다.

GitHub:  
<https://github.com/Junghoo-developer/SongRyeon>

## 원문
- [원문](https://github.com/Junghoo-developer/SongRyeon)
- [GeekNews 토론](https://news.hada.io/topic?id=30854)

## My Note
<!-- 한 줄 코멘트 남기기 -->

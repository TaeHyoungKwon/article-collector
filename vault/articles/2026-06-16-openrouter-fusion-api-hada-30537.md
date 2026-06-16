---
category: AI
collected_at: '2026-06-16T16:25:29+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30537
id: hada-30537
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-06-16'
source: geeknews
tags:
- AI
- Other
- openrouter.ai
title: OpenRouter Fusion API
url: https://openrouter.ai/openrouter/fusion
---

## TL;DR
- OpenRouter Fusion API는 여러 모델의 결과를 종합해 성능을 향상시키는 기능을 가진 API이다.
- 이 API는 단일 프롬프트에 대해 여러 전문가 모델이 병렬 분석을 수행하고, 심판 모델이 그 결과를 최종 정리하여 제공하는 멀티 모델 심의 방식을 채택하고 있다.
- 다양한 분야에서 단일 모델의 한계를 극복할 수 있는 이 API는 리서치나 전문가 비평 등에 효과적으로 활용될 수 있다.

## GeekNews 요약
- 여러 모델의 결과를 **종합(synthesize)** 하면 개별 모델 단독 성능을 크게 능가할 수 있다는 발견에서 출발
- 단일 프롬프트를 여러 **전문가 모델**이 병렬로 분석한 뒤 **심판 모델(judge model)** 이 결과를 종합해 최종 답변을 작성하는 **멀티 모델 심의(multi-model deliberation)** 방식
- 패널 모델은 **웹 검색**과 **웹 페치**를 활성화한 상태로 **병렬 분석을 수행**하며, 심판 모델이 **합의, 모순, 부분적 일치, 고유 통찰, 사각지대**를 구조화한 분석으로 정리
- 기본값은 **Quality 프리셋**이며, Budget 프리셋으로 저렴한 모델 전환 또는 fusion 플러그인 필드로 패널·심판 완전 재정의 가능
- 단일 모델로 충분치 않은 **리서치, 전문가 비평**, 오답 비용이 추가 완성 비용을 상회하는 상황에 적합
- 패널 구성원 전원과 심판 호출을 모두 실행하므로, 요청 비용은 단일 모델이 아닌 **개별 완성(completion) 합산** 방식으로 책정

---

## 원문
- [원문](https://openrouter.ai/openrouter/fusion)
- [GeekNews 토론](https://news.hada.io/topic?id=30537)

## My Note
<!-- 한 줄 코멘트 남기기 -->

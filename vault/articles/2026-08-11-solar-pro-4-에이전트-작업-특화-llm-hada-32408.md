---
category: AI
collected_at: '2026-08-11T23:17:49+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32408
id: hada-32408
matched_keywords:
- AI
- LLM
read: false
recommend_score: 5.307
recommended_on: '2026-08-12'
source: geeknews
tags:
- AI
- Other
- upstage.ai
title: Solar Pro 4 - 에이전트 작업 특화 LLM
url: https://www.upstage.ai/blog/ko/solar-pro-4
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Upstage가 공개한 에이전트향 LLM으로, 문서 읽기·도구 호출·코드 실행을 거쳐 Excel 분석 자료, Word 보고서, PPT 슬라이드 같은 실제 파일을 만들어내는 업무 흐름에 맞춰 설계
- Artificial Analysis 측정 기준 Terminal-Bench v2.1 57점, GDPval-AA v2 39점, τ³-Banking 23점, AA-LCR 71점
- Hy3, MiMo-V2.5, GLM-5.1, Qwen 3.6 Mini 등 에이전트 용도로 널리 쓰이는 모델들과 비교하면 실무 산출물 평가(GDPval-AA)에서 가장 높고, 멀티턴 도구 사용(τ³-Banking)은 Hy3와 공동 최고 수준
- 가격은 1M 토큰당 입력 $0.30, 캐시 입력 $0.06, 출력 $1.20으로, 문서 읽기·도구 호출·재시도로 호출이 쌓이는 에이전트 워크로드의 상시 운영을 겨냥한 구성
- 512K 컨텍스트와 최대 128K 출력 토큰을 지원하며, 영어·한국어·일본어를 입출력 모두 처리함
- 기본으로 추론(reasoning)을 수행하고 응답에 reasoning trace가 포함됨. reasoning effort 파라미터로 추론 깊이와 응답 속도를 조절 가능
- OpenAI 호환 API로 base\_url과 모델명(solar-pro4)만 바꾸면 기존 코드에서 동작함
- 현재 Hermes Agent에서 8월 18일까지 무료로 쓸 수 있고, Upstage Console과 OpenRouter에서는 9월 10일까지 90% 할인 중

## 원문
- [원문](https://www.upstage.ai/blog/ko/solar-pro-4)
- [GeekNews 토론](https://news.hada.io/topic?id=32408)

## My Note
<!-- 한 줄 코멘트 남기기 -->

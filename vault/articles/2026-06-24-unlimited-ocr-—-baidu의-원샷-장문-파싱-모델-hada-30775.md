---
category: AI
collected_at: '2026-06-24T09:26:40+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30775
id: hada-30775
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-06-24'
source: geeknews
tags:
- AI
- Other
- github.com/baidu
title: Unlimited OCR — Baidu의 원샷 장문 파싱 모델
url: https://github.com/baidu/Unlimited-OCR
---

## TL;DR
- 이 글은 Baidu의 새로운 원샷 장문 파싱 모델인 E2E OCR에 대해 다룬다.
- 이 모델은 참조 슬라이딩 윈도우 어텐션(R-SWA) 기법을 통해 메모리 및 연산 비용을 차단하면서도 SOTA 성능을 달성했다.
- 이는 OCR뿐만 아니라 ASR과 번역 등 다양한 장문 작업에 적용 가능하여 향후 인공지능 기술 발전에 기여할 수 있다.

## GeekNews 요약
- **DeepSeek OCR**를 기반으로 디코더의 모든 어텐션을 교체해, 수십 페이지 문서를 **한 번의 순전파(forward pass)** 로 전사하는 E2E OCR 모델
- 핵심은 **참조 슬라이딩 윈도우 어텐션(R-SWA)** 으로, 디코딩 길이가 늘어도 **KV 캐시를 상수로 유지**해 메모리·연산 비용 증가를 차단
- 책을 베껴 쓰는 인간의 **작업 기억(working memory)** 을 모사해, 멀리 떨어진 출력은 부드럽게 잊고 인접 문맥만 참조하는 방식 채택
- OmniDocBench v1.5에서 **93%** 로 DeepSeek OCR 대비 6% 우위, v1.6에서 93.92%로 end-to-end **SOTA** 달성
- R-SWA는 OCR을 넘어 **ASR·번역** 등 참조 기반 장문 작업에도 적용 가능한 범용 파싱 어텐션 메커니즘

---

## 원문
- [원문](https://github.com/baidu/Unlimited-OCR)
- [GeekNews 토론](https://news.hada.io/topic?id=30775)

## My Note
<!-- 한 줄 코멘트 남기기 -->

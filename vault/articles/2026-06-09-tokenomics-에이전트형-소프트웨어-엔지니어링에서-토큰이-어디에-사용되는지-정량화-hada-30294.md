---
category: AI
collected_at: '2026-06-09T07:35:02+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30294
id: hada-30294
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-06-08'
source: geeknews
tags:
- AI
- Other
- arxiv.org
title: 'Tokenomics: 에이전트형 소프트웨어 엔지니어링에서 토큰이 어디에 사용되는지 정량화'
url: https://arxiv.org/abs/2601.14470
---

## TL;DR
- 이 글은 LLM 기반 다중 에이전트 소프트웨어 개발 시스템에서 토큰 소비 패턴을 정량화한 연구를 다룬다.
- 연구에 따르면 코드 리뷰 단계에서 전체 토큰 소비의 59.4%를 차지하여 주된 소비 영역임을 확인했다.
- 이는 개발 효율성을 높이기 위한 협업 프로토콜과 평가 프레임워크의 필요성을 강조하며, 실무에 적용 가능한 인사이트를 제공한다.

## GeekNews 요약
- LLM 기반 다중 에이전트 소프트웨어 개발 시스템의 실행 추적을 SDLC 단계에 매핑해, 토큰 소비가 초기 생성보다 **코드 리뷰**와 검증에 집중되는 구조를 측정한 연구
- ChatDev가 수행한 30개 소프트웨어 개발 태스크에서 코드 리뷰 단계가 평균 **59.4%** 의 토큰을 사용하며 최대 소비 구간으로 확인
- 전체 태스크 평균 토큰 구성은 입력 53.9%, 출력 24.4%, 추론 21.6%로, 에이전트 간 반복적 맥락 전달이 큰 **communication tax**를 형성
- 코딩 단계는 출력 토큰 비중이 58.0%로 높은 반면, 문서화 단계는 입력 토큰 비중이 80.2%로 높아 개발 단계별 토큰 사용 패턴이 뚜렷하게 구분
- 비용 예측과 워크플로 최적화를 위해 더 토큰 효율적인 에이전트 협업 프로토콜과 표준화된 평가 프레임워크가 필요한 결론

---

## 원문
- [원문](https://arxiv.org/abs/2601.14470)
- [GeekNews 토론](https://news.hada.io/topic?id=30294)

## My Note
<!-- 한 줄 코멘트 남기기 -->

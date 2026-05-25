---
category: AI
collected_at: '2026-05-25T23:48:50+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29861
id: hada-29861
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.901
source: geeknews
tags:
- AI
- Other
- arxiv.org
title: 'Constraint Decay: 백엔드 코드 생성에서 LLM 에이전트의 취약성'
url: https://arxiv.org/abs/2605.06445
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **LLM 에이전트**는 느슨한 명세의 코드 생성에는 강하지만, 운영급 백엔드가 요구하는 API 계약·아키텍처·DB·ORM 제약 준수에는 아직 취약함
- 동일한 **OpenAPI 명세**로 기능 요구를 고정하고, 8개 웹 프레임워크의 80개 그린필드 과제와 20개 기능 구현 과제에 같은 동작 테스트를 적용함
- 비기능 제약은 **프레임워크 선택**, 아키텍처 패턴, 데이터베이스 백엔드, ORM 통합 4개 차원으로 나눠 구조 복잡성의 영향을 분리함
- **제약 붕괴**는 구조 요구가 누적될수록 성능이 급락하는 현상이며, 높은 구성도 완전 지정 과제에서 assertion pass rate가 평균 30포인트 하락함
- 실패의 핵심은 **데이터 계층 결함**으로, 잘못된 쿼리 구성과 ORM 런타임 위반이 에이전트 로직 실패의 약 45%를 차지함

---

## 원문
- [원문](https://arxiv.org/abs/2605.06445)
- [GeekNews 토론](https://news.hada.io/topic?id=29861)

## My Note
<!-- 한 줄 코멘트 남기기 -->

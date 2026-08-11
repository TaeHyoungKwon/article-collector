---
category: AI
collected_at: '2026-08-11T15:20:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32392
id: hada-32392
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- hanakai.org
title: Hanami - Rails를 대체하는 Ruby 프레임워크
url: https://hanakai.org/hanami
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Hanami는 관심사 분리, **명시적인 비즈니스 로직**, 모듈식 아키텍처를 통해 애플리케이션 규모가 커져도 코드를 체계적이고 유지보수하기 쉽게 만드는 Ruby 프레임워크
- 데이터 접근을 전담하는 **데이터베이스 계층**을 두고 relation으로 접근 패턴을 정의하며, repo에서 이를 비즈니스 로직에 맞게 조합하고 struct를 애플리케이션 전반의 값 객체로 사용함
- **Operation**은 하나의 작업에 집중하면서 필요한 의존성을 주입받고 성공/실패 경로를 명시적으로 구성해, 비즈니스 워크플로우를 이해하고 테스트하기 쉽게 만듦
- 라우팅/Action/View를 각각 분리해 URL 구조, HTTP 처리, 화면용 데이터 로직의 역할을 명확히 하며, 각 endpoint마다 하나의 Action 클래스를 두어 HTTP 코드가 비즈니스 로직과 섞이지 않도록 함
- **Slice 기반 모듈화**와 선택 가능한 구성 요소를 지원해 풀스택 웹 앱부터 API/스트림 프로세서까지 다양한 형태를 만들 수 있으며, 스마트 코드 로딩으로 앱 규모가 커져도 콘솔/테스트/서버 시작을 빠르게 유지함

---

## 원문
- [원문](https://hanakai.org/hanami)
- [GeekNews 토론](https://news.hada.io/topic?id=32392)

## My Note
<!-- 한 줄 코멘트 남기기 -->

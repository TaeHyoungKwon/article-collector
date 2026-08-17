---
category: AI
collected_at: '2026-08-17T09:15:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32567
id: hada-32567
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- medium.com
title: Flexible Authentication - 수백만 사용자를 위한 Airbnb의 인증 재설계
url: https://medium.com/airbnb-engineering/flexible-authentication-reimagining-authentication-for-millions-of-users-at-airbnb-3a8a4c917137
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Airbnb는 여행 예약처럼 **로그인 간격이 길고 사용 환경이 다양한 서비스**에서 인증 실패가 예약과 매출 손실로 이어진다고 보고, 10년간 누적된 로그인 방식을 **Flexible Authentication**으로 재설계함
- 핵심은 **Identify first, then Challenge**로, 사용자가 먼저 어떤 계정에 들어가려는지 식별한 뒤 서버의 정책 엔진이 계정 이력/지역/플랫폼 등을 바탕으로 성공 가능성이 높은 인증 방식을 선택함
- 인증 화면마다 **Try another way**를 제공해 막다른 흐름을 없애고, 현재 계정에서 사용할 수 있는 다른 인증 수단을 성공 가능성 순으로 보여줘 처음부터 다시 시작하지 않아도 되게 함
- 인증 흐름 전체를 **서버 주도형 UI**로 바꿔 클라이언트는 화면을 렌더링하고 액션만 전달하도록 단순화했으며, 앱 업데이트 없이 인증 순서/문구/실험을 변경할 수 있게 됨
- 그 결과 클라이언트 코드가 **60% 감소**, 웹 번들이 100KB 줄었고, 인증 성공률은 2.6% 증가, 중복 계정은 27% 감소, SMS OTP 비용은 약 11% 절감됨

---

## 원문
- [원문](https://medium.com/airbnb-engineering/flexible-authentication-reimagining-authentication-for-millions-of-users-at-airbnb-3a8a4c917137)
- [GeekNews 토론](https://news.hada.io/topic?id=32567)

## My Note
<!-- 한 줄 코멘트 남기기 -->

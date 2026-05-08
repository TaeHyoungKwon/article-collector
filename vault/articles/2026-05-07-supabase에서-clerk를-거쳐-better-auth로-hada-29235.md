---
category: Other
collected_at: '2026-05-07T06:52:30+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29235
id: hada-29235
matched_keywords: []
read: false
recommend_score: 1.594
source: geeknews
tags:
- Other
- blog.val.town
title: Supabase에서 Clerk를 거쳐 Better Auth로
url: https://blog.val.town/better-auth
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Val Town은 2023년 Supabase에서 벗어나 데이터베이스는 Render, 인증은 Clerk로 옮겼지만, 사용자·세션 책임을 외부화하는 구조가 맞지 않아 한 달 전 **Better Auth**로 전환함
- Clerk는 사용자 테이블을 없애는 방향을 제안했지만, Val Town은 소셜 기능 때문에 여러 사용자의 콘텐츠, 사용자명, 아바타를 자주 보여줘야 했고, Clerk API 제한과 동기화 때문에 사실상 **사용자 테이블 두 개**를 운영하는 복잡성이 생김
- Clerk가 세션 갱신까지 맡으면서 **단일 장애 지점**이 됐고, Clerk 장애 시 로그인·로그아웃뿐 아니라 이미 로그인한 사용자도 전체 사이트를 쓰기 어려워졌으며, 2025년 5월 이후 상태 페이지 기준 가동률은 99%와 99.9% 사이를 오감
- Val Town은 Clerk의 SDK, 관리 기능, 남용 방지, 대시보드가 유용했기 때문에 즉시 재작성하지 않았지만, 타사 **세션 관리**를 다시 신뢰하지 않겠다는 기준을 세움
- Better Auth는 코드 품질, 프레임워크 통합, 독립적인 오픈소스 핵심이 요구에 맞았고, Val Town은 약 2주 동안 Clerk와 Better Auth를 함께 지원하며 두 종류의 쿠키를 받아 점진적으로 **세션 이전**을 진행함

---

## 원문
- [원문](https://blog.val.town/better-auth)
- [GeekNews 토론](https://news.hada.io/topic?id=29235)

## My Note
<!-- 한 줄 코멘트 남기기 -->

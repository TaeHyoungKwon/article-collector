---
collected_at: '2026-05-07T06:52:30+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29235
id: hada-29235
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
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

## 전환 배경

- Val Town은 2023년에 [Supabase에서 벗어나](https://blog.val.town/blog/migrating-from-supabase) 더 전통적인 데이터베이스 구성으로 이동하면서, 데이터베이스는 [Render](https://render.com/), 인증은 [Clerk](https://clerk.com/)로 대체함
- 2023년 말에는 Clerk에서 벗어나야 한다는 이슈가 등록됐고, 한 달 전 [Better Auth](https://www.better-auth.com/)로 전환하면서 해당 이슈가 닫힘
- Clerk와 Supabase는 각각 [5,000만 달러 투자](https://clerk.com/blog/series-c), [50억 달러 가치로 1억 달러 투자](https://supabase.com/)를 유치한 성공적인 서비스지만, Val Town의 구조는 Clerk의 기대와 크게 충돌했음
- 전환 과정에는 많은 우회책, 버그, 장애가 있었고, 특히 Clerk가 사용자 테이블과 세션 테이블을 모두 대신하려는 구조가 핵심 문제로 드러남

## 핵심 문제: 사용자 테이블과 세션 테이블의 외부화

- ### Clerk를 사용자 테이블로 쓰기 어려웠던 이유

  - Clerk는 2021년 [“Consider dropping your users table”](https://clerk.com/blog/offload_user_table) 글과 2023년 [“DELETE your Users table”](https://www.youtube.com/watch?v=86sFORO-M3Y) 영상처럼 사용자 테이블을 없애는 방향을 강하게 제안함
  - Val Town은 초기 전환 시 사용자 설정, 아바타 URL, 이메일 같은 데이터를 필요할 때마다 Clerk API에서 가져올 수 있다고 봤음
  - Clerk SDK의 `rootAuthLoader`에는 애플리케이션 전체 인증을 처리하면서 사용자 데이터를 요청하는 `loadUser` 옵션이 있었고, 개발 환경에서는 잘 동작함
  - 프로덕션에서 해당 엔드포인트의 제한은 계정 전체, 모든 사용자 합산 **초당 5개 요청**이었고, 이 문제는 나중에 [옵션 제거](https://github.com/clerk/javascript/issues/1043)로 해결됨
  - Val Town처럼 소셜 기능이 있는 서비스는 여러 페이지에서 다른 사용자의 콘텐츠, 사용자명, 아바타를 보여줘야 하므로, 사용자가 자기 아바타와 설정만 JWT에서 읽는다는 Clerk 기본 UI의 가정과 맞지 않았음
  - Clerk 측 조언은 아바타와 기타 정보를 Clerk와 Val Town 사용자 테이블 사이에 동기화하는 것이었고, 결과적으로 같은 정보의 권위가 두 곳으로 나뉘어 **사용자 테이블 두 개**를 운영하는 복잡성이 생김
- ### 웹훅 동기화가 만든 가입 흐름의 복잡성

  - Clerk 데이터를 Val Town 데이터베이스에 동기화하려면 웹훅을 써야 했고, 가입 과정은 복잡하고 까다로워짐
  - 가입 직후 잠시 동안 사용자는 Clerk 계정은 있지만 Val Town 데이터베이스 행은 없는 상태가 될 수 있었음
  - Val Town은 사용자명이 필수이기 때문에, 사용자가 Clerk 계정과 데이터베이스 행은 있지만 계정이 아직 완성되지 않은 상태에도 놓일 수 있었음
  - 사용자 설정은 인증 방식처럼 Clerk가 관리하는 항목과 사용자명, 에디터 설정처럼 Val Town이 필요한 항목으로 나뉘어야 했음

## Clerk가 단일 장애 지점이 된 세션 구조

- 쿠키 기반 사용자 세션은 보통 짧게 유지되고 계속 갱신되며, 그래야 빠르게 무효화할 수 있음
- 이 구조에서는 몇 분마다 사용자가 세션 쿠키를 새 쿠키로 교환해야 했고, Val Town의 서브도메인이 Clerk로 요청을 전달해 갱신을 처리함
- Val Town은 세션 테이블을 갖지 않았고 세션에 대한 책임도 지지 않았음
- 이 방식은 인증 책임을 피하려는 경우에는 좋지만, Clerk가 내려가면 로그인과 로그아웃만 깨지는 것이 아니라 이미 로그인한 사용자에게도 전체 사이트가 사용할 수 없게 됨
- Clerk는 자주, 그리고 긴 시간 동안 장애가 있었고, [2025년 5월 이후 상태 페이지](https://status.clerk.com/) 기준 가동률은 99%와 99.9% 사이를 오감
- 복잡한 시스템의 신뢰성은 중요한 구성 요소들의 결합 신뢰성 중 **최솟값**에 묶임
- 이 두 가지 큰 문제 외에도 [Clerk 관련 다른 버그와 문제](https://github.com/clerk/javascript/issues?q=sort%3Aupdated-desc%20is%3Aissue%20state%3Aclosed%20author%3Atmcw)가 있었고, 대부분은 결국 수정됐지만 자동으로 이슈를 닫는 “Stale Issue Bot”과 씨름해야 했음

## 바로 전환하지 못한 이유

- “X에서 Y로 전환”하는 작업은 개발 속도와 팀의 정신적 안정성을 해칠 수 있어, Val Town은 반드시 필요한 경우가 아니면 재작성하지 않으려 했음
- Clerk는 Remix, Fastify, Express 등 Val Town이 쓰던 기술을 위한 SDK를 제공했고, 해당 프레임워크들의 변화도 꽤 잘 따라감
- Clerk의 관리 기능과 남용 방지 기능은 고객 지원 문제를 해결하고 사기 사용자를 막는 데 도움이 됨
- Clerk가 특히 잘 맞는 영역은 소셜 요소가 없고 사용자 테이블이 필요 없는 비교적 단순한 프런트엔드 중심 앱이었음
- 시작하기 쉽고 가격도 감당 가능했으며, Clerk 대시보드도 꽤 좋았음
- 인증 대안은 많지 않았고, 오픈소스 인증 솔루션 중에는 오래되고 사실상 방치된 것이 많았음
- 인증 서비스형 플랫폼은 공급업체 리스크가 있고 Clerk와 같은 문제가 반복될 수 있었음
- Val Town은 인증을 처음부터 직접 만들어 새롭고 민망한 취약점에 노출되고 싶지는 않았지만, 공급자에게 너무 많은 책임을 넘기고 싶지도 않았음
- 특히 타사 세션 관리를 다시 신뢰하지 않겠다는 기준이 생김

## Better Auth 선택과 전환 방식

- [Better Auth](https://better-auth.com/)는 높은 코드 품질, 여러 프레임워크와의 좋은 통합, 독립적인 오픈소스 프로젝트로 실제 사용 가능하다는 점에서 많은 조건을 충족함
- Better Auth도 대부분 한 회사가 개발하는 크고 복잡한 코드베이스이므로 공급업체 리스크는 남아 있음
- 다만 세션과 사용자 인증이 동작하기 위해 제3자가 계속 온라인 상태여야 하는 의존성은 사라짐
- [WorkOS](https://workos.com/)의 [AuthKit](https://www.authkit.com/)도 강한 후보였고 매우 매끄러웠지만, 두 공급업체를 거친 뒤에는 독립적으로 동작하고 핵심이 오픈소스인 대안이 중요해짐
- Better Auth의 대시보드와 유료 애드온도 Val Town의 요구에 맞았음
- Val Town은 모든 데이터를 직접 관리하고, 플러그인이 Val Town 사이트에 API를 제공해 Better Auth 대시보드가 정보를 가져오고 가벼운 사용자 관리를 할 수 있게 함
- Better Auth의 유료 서비스인 “Infrastructure”는 Val Town의 사용 방식에서는 사실상 상태 비저장에 가깝고 세션 관리에 관여하지 않음
- 전환 기간에는 약 2주 동안 Better Auth와 Clerk를 동시에 지원함
- 인증을 처리하는 모든 엔드포인트가 두 종류의 쿠키를 모두 받아들였고, 로그인 페이지가 Better Auth 세션을 제공하면서 사용자가 점진적으로 Better Auth로 이동함
- 보안과 관련된 작업인 만큼 모든 코드를 꼼꼼히 읽고, 다시 쓰고, 테스트해야 했으며, 최종적인 순수 Better Auth 인증 코드는 전부 직접 작성함
- Better Auth는 Vals와도 잘 맞으며, Val Town 코드에 인증을 추가하려면 [Better Auth starter template](https://www.val.town/x/templates/better-auth-starter)을 사용할 수 있음

## 남은 교훈

- 업스트림 제공자의 가동 시간이 서비스 가동 시간에 직접 영향을 주므로, 그 리스크에 얼마나 노출돼 있는지 신중히 판단해야 함
- 어떤 제품이 많은 사용 사례에 잘 맞고 크게 성공했더라도, 특정 문제에는 맞지 않을 수 있음
- 소프트웨어 환경은 빠르게 바뀌며, 필요한 순간에는 없던 적절한 해법이 1년 뒤에 나타날 수도 있음

## 원문
- [원문](https://blog.val.town/better-auth)
- [GeekNews 토론](https://news.hada.io/topic?id=29235)

## My Note
<!-- 한 줄 코멘트 남기기 -->

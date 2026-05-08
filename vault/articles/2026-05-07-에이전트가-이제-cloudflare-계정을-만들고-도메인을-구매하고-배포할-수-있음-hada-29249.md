---
collected_at: '2026-05-07T09:43:07+09:00'
geeknews_comments: 1
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=29249
id: hada-29249
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- blog.cloudflare.com
title: 에이전트가 이제 Cloudflare 계정을 만들고, 도메인을 구매하고, 배포할 수 있음
url: https://blog.cloudflare.com/agents-stripe-projects/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 코딩 에이전트가 이제 사용자를 대신해 **Cloudflare 계정 생성**, 유료 구독 시작, 도메인 등록, API 토큰 획득, 프로덕션 배포까지 직접 수행할 수 있음
- 사람은 권한 부여와 Cloudflare 서비스 약관 동의에만 참여하면 되며, 대시보드 방문, API 토큰 복사·붙여넣기, **신용카드 정보 입력** 없이 처음부터 끝까지 진행 가능함
- 이 방식은 Cloudflare와 Stripe가 공동 설계한 새 프로토콜로 동작하며, [Stripe Projects](https://projects.dev/) 출시의 일부로 제공되고 [Code Mode MCP server](https://blog.cloudflare.com/code-mode/)와 [Agent Skills](https://github.com/cloudflare/skills)를 함께 쓰면 배포 역량이 더 좋아짐
- 프로토콜은 **Discovery**, Authorization, Payment로 구성되며, Stripe가 신원 공급자 역할을 하고 Cloudflare가 계정을 자동 프로비저닝하며 결제 토큰으로 유료 서비스 구매를 처리함
- 에이전트에는 원본 결제 정보가 공유되지 않고, Stripe는 한 공급자에 대한 기본 사용 한도를 월 **$100.00 USD**로 설정하며, Stripe Projects는 오픈 베타로 제공됨

---

## 에이전트가 Cloudflare를 직접 준비해 배포까지 수행

- 코딩 에이전트는 프로덕션 배포를 위해 호스팅 대상 클라우드의 **계정**, 결제 수단, API 토큰이 필요했고, 기존에는 사람이 직접 처리해야 했음
- 이제 에이전트가 사용자를 대신해 Cloudflare를 프로비저닝할 수 있음
  - Cloudflare 계정 생성
  - 유료 구독 시작
  - 도메인 등록
  - 즉시 배포 가능한 API 토큰 획득
- 사람은 권한 부여와 Cloudflare 서비스 약관 동의 과정에만 참여하면 되며, 그 외에는 대시보드 방문, API 토큰 복사·붙여넣기, 신용카드 정보 입력 없이 처음부터 끝까지 진행 가능함
- Cloudflare의 [Code Mode MCP server](https://blog.cloudflare.com/code-mode/)와 [Agent Skills](https://github.com/cloudflare/skills)를 함께 쓰면 에이전트의 Cloudflare 배포 역량이 더 좋아짐
- 이 방식은 Cloudflare가 Stripe와 공동 설계한 새 프로토콜을 통해 동작하며, [Stripe Projects](https://projects.dev/) 출시의 일부로 제공됨
- Cloudflare는 [Stripe Atlas](https://stripe.com/atlas)로 법인을 설립하는 신규 스타트업 전체에 [$100,000 Cloudflare 크레딧](https://support.stripe.com/questions/stripe-atlas-perks-partners)도 제공함

## 설정 없이 0에서 프로덕션까지 가는 흐름

- [Stripe CLI](https://docs.stripe.com/stripe-cli/install)와 [Stripe Projects plugin](https://docs.stripe.com/projects)을 설치하고 Stripe에 로그인한 뒤 새 프로젝트를 시작함

```
stripe projects init
```

- 이후 에이전트에게 새 앱을 만들고 새 도메인에 배포하라고 요청할 수 있음
- Stripe에 로그인한 이메일에 이미 Cloudflare 계정이 있으면 일반적인 **OAuth 흐름**으로 에이전트 접근 권한을 부여함
- 해당 이메일에 Cloudflare 계정이 없으면 Cloudflare가 사용자와 에이전트를 위해 계정을 자동 프로비저닝함
- 에이전트는 사이트를 빌드해 새 Cloudflare 계정에 배포하고, Stripe Projects CLI를 사용해 도메인을 등록함
- 필요한 경우 에이전트가 입력과 승인을 요청함
  - Stripe 계정에 연결된 결제 수단이 없으면 결제 수단 추가를 요청함
- 최종적으로 앱은 새로 등록된 도메인에서 프로덕션으로 실행됨
- Cloudflare 계정이 전혀 없고 사전 구성된 [Agent Skills](https://github.com/cloudflare/skills)나 [MCP server](https://blog.cloudflare.com/code-mode-mcp/)가 없어도 에이전트가 다음을 완료할 수 있음
  - 새 Cloudflare 계정 프로비저닝
  - API 토큰 획득
  - 도메인 구매
  - 앱을 프로덕션에 배포

## 프로토콜 구성 요소

- 에이전트, Stripe, Cloudflare 사이의 상호작용은 세 가지 구성 요소로 나뉨
- ### Discovery

  - 에이전트가 명령을 호출해 사용할 수 있는 서비스 카탈로그를 조회함
- ### Authorization

  - 플랫폼이 사용자 신원을 증명하고, 공급자가 계정을 프로비저닝하거나 기존 계정을 연결하며, 에이전트에 안전하게 자격 증명을 발급할 수 있게 함
- ### Payment

  - 플랫폼이 공급자가 고객에게 과금할 수 있는 결제 토큰을 제공해, 에이전트가 구독을 시작하고 구매를 수행하며 사용량 기반 과금을 가능하게 함
  - 이 방식은 OAuth, OIDC, 결제 토큰화 같은 기존 표준과 선행 사례를 함께 사용해 사람이 개입해야 했던 여러 단계를 줄임

## Discovery: 에이전트가 직접 프로비저닝 가능한 서비스를 찾는 방식

- 에이전트가 `stripe projects add cloudflare/registrar:domain` CLI 명령을 실행하기 전에 먼저 [Cloudflare Registrar](https://domains.cloudflare.com/) 서비스를 찾아야 했음
- 이를 위해 `stripe projects catalog` 명령을 호출해 사용 가능한 서비스를 반환받음
- [Cloudflare products](https://developers.cloudflare.com/directory/) 전체와 다른 공급자의 서비스 목록은 [계속 늘어나고](https://docs.stripe.com/projects#available-providers) 있으며, 사람에게는 부담스러울 수 있지만 에이전트에는 필요한 문맥이 됨
- 에이전트는 사용자의 요청과 선호에 따라 이 카탈로그에서 사용할 서비스를 선택함
- 사용자는 어떤 공급자가 어떤 서비스를 제공하는지 미리 알 필요가 없고, 별도 입력도 필요하지 않음
- Cloudflare 같은 공급자는 JSON을 반환하는 단순 REST API로 카탈로그를 제공하며, 에이전트는 이를 통해 필요한 정보를 얻음

## Authorization: 신규 사용자의 즉시 계정 생성

- 에이전트가 `stripe projects add cloudflare/registrar:domain` 같은 명령으로 서비스를 선택하고 프로비저닝하면, 해당 리소스는 Cloudflare 계정 안에 생성됨
- 사용자가 처음에 Stripe 계정에 로그인했기 때문에 Stripe가 **신원 공급자** 역할을 하며 사용자 신원을 증명함
- Cloudflare 계정이 없으면 Cloudflare가 새 계정을 자동 프로비저닝하고, Stripe Projects CLI에 자격 증명을 반환함
- 이 자격 증명은 안전하게 저장되며, 에이전트가 Cloudflare에 인증된 요청을 보내는 데 사용할 수 있음
- Cloudflare나 다른 서비스를 처음 쓰는 사용자도 추가 단계 없이 에이전트로 바로 빌드를 시작할 수 있음
- 이미 Cloudflare 계정이 있는 사용자는 표준 OAuth 흐름을 통해 Stripe Projects CLI에 접근 권한을 부여하고, 기존 Cloudflare 계정에서 리소스를 프로비저닝할 수 있음

## Payment: 신용카드 정보를 주지 않고 에이전트에 예산 부여

- 에이전트가 도메인을 대량 구매하거나 큰 청구서를 만들 수 있다는 우려를 프로토콜 차원에서 다룸
- 에이전트가 유료 서비스를 프로비저닝할 때 Stripe는 공급자인 Cloudflare에 대한 요청에 **결제 토큰**을 포함함
- 신용카드 번호 같은 원본 결제 정보는 에이전트에 공유되지 않음
- Stripe는 에이전트가 한 공급자에 사용할 수 있는 기본 한도를 월 **$100.00 USD**로 설정함
- 한도를 높일 준비가 되면 Cloudflare 계정에서 [Budget Alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/)를 설정할 수 있음

## 로그인 사용자가 있는 모든 플랫폼으로 확장 가능

- 로그인 사용자가 있는 플랫폼은 Stripe Projects에서 Stripe가 맡는 것과 같은 **Orchestrator** 역할을 하며 Cloudflare와 통합할 수 있음
- 코딩 에이전트 제품이라면 사용자가 만든 결과물을 Cloudflare와 다른 서비스로 프로덕션에 배포하게 할 수 있음
- 사용자를 복잡한 권한 부여 흐름이나 배포 위치·방식 선택 절차로 보내지 않고, 플랫폼이 이미 로그인한 사용자 기반으로 오케스트레이션함
- 사용자가 [domain](https://domains.cloudflare.com/), [storage bucket](https://developers.cloudflare.com/r2/), 에이전트에 제공할 [sandbox](https://blog.cloudflare.com/dynamic-workers/), 또는 [기타 Cloudflare 리소스](https://workers.cloudflare.com/)가 필요할 때 Cloudflare에 API 호출 한 번으로 새 Cloudflare 계정을 프로비저닝하고 인증 요청용 토큰을 받을 수 있음
- 반대로 Cloudflare 고객이 다른 서비스를 쉽게 프로비저닝하도록 만들 수도 있음
  - Cloudflare와 Planetscale의 협업처럼 [Cloudflare에서 Planetscale Postgres 데이터베이스를 직접 생성](https://blog.cloudflare.com/deploy-planetscale-postgres-with-workers/)하는 방식과 유사함
  - 이 경우 Cloudflare가 Orchestrator로 동작해 PlanetScale 계정 연결, 데이터베이스 생성, 사용자 기존 결제 수단 기반 과금을 가능하게 함
- 새 프로토콜은 여러 플랫폼이 수년간 개별적·맞춤형으로 구현해 온 교차 제품 통합 유형을 표준화하기 시작함
- 표준이 없으면 각 통합마다 엔지니어링 작업이 필요했고, 그 작업을 이후 통합에 재사용하기 어려웠음
- [OAuth standard](https://oauth.net/2/)가 다른 플랫폼에 계정 접근을 위임할 수 있게 한 것처럼, 이 프로토콜은 OAuth를 사용하면서 결제와 계정 생성까지 확장하고 에이전트를 일급 대상으로 다룸
- Cloudflare와 Stripe는 더 공식적인 사양을 공유하는 방향으로 표준을 계속 발전시킬 계획이며, 더 많은 플랫폼과의 통합도 추진함

## 시작 방법

- Stripe Projects는 **오픈 베타**이며, Cloudflare 계정이 없어도 시작할 수 있음
- [Stripe CLI](https://docs.stripe.com/stripe-cli/install)를 설치하고 Stripe에 로그인한 뒤 새 프로젝트를 시작함

```
stripe projects init
```

- 이후 에이전트에게 Cloudflare에서 새 앱을 만들라고 요청하면 됨

## 원문
- [원문](https://blog.cloudflare.com/agents-stripe-projects/)
- [GeekNews 토론](https://news.hada.io/topic?id=29249)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
collected_at: '2026-05-08T10:01:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29283
id: hada-29283
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- developers.cloudflare.com
title: React 및 Next.js에서 다수의 보안 취약점 공개, 즉시 패치 권고
url: https://developers.cloudflare.com/changelog/post/2026-05-06-react-nextjs-vulnerabilities/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- React 팀과 Vercel이 **React Server Components**와 Next.js에 영향을 미치는 12건의 보안 취약점을 동시에 공개하며, 애플리케이션 즉시 업데이트를 강력 권고
- 서비스 거부(DoS), **미들웨어 우회**, SSRF, XSS, 캐시 포이즈닝 등 다양한 공격 벡터가 포함되며 High 심각도 6건, Moderate 4건, Low 2건으로 분류
- 패치 버전으로 React `19.0.6`/`19.1.7`/`19.2.6`과 Next.js `15.5.16`/`16.2.5`가 제공되며, **React 기반 서버 프레임워크**도 함께 업데이트 필요
- 일부 취약점은 WAF 등 네트워크 레벨 방어로는 **차단이 불가능**하여, 애플리케이션 코드 자체의 패치가 필수
- Server Components, Pages Router, Image Optimization API 등 Next.js의 **광범위한 기능 영역**에 걸쳐 취약점이 분포하여 영향 범위가 넓음

---

## 영향받는 패키지 및 패치 버전

- React 관련 패치 대상: `react-server-dom-webpack`, `react-server-dom-parcel`, **`react-server-dom-turbopack`** — 각각 `19.0.6`, `19.1.7`, `19.2.6` 버전으로 업데이트 필요
- Next.js 패치 대상: **`15.5.16`** 및 **`16.2.5`**
- Vinext, OpenNext, **TanStack Start** 등 React 기반 서버 프레임워크 사용 시 해당 프레임워크도 최신 버전으로 함께 업데이트 필요

## High 심각도 취약점 (6건)

- **`CVE-2026-23870`** / `GHSA-8h8q-6873-q5fj` — React Server Components의 서비스 거부(DoS)
  - React와 Next.js 양쪽 모두에 영향을 미치는 취약점
- `GHSA-267c-6grr-h53f` — **segment-prefetch 라우트**를 통한 미들웨어 우회
- `GHSA-mg66-mrh9-m8jx` — **Cache Components**의 연결 고갈(connection exhaustion)을 통한 서비스 거부
- `GHSA-492v-c6pp-mqqv` — 동적 라우트 **파라미터 주입**을 통한 미들웨어 우회
  - WAF 규칙으로 안전하게 차단 불가, 애플리케이션 동작을 깨뜨릴 수 있음
- `GHSA-c4j6-fc7j-m34r` — **WebSocket 업그레이드**를 통한 SSRF(서버 측 요청 위조)
  - WAF 규칙으로 안전하게 차단 불가
- `GHSA-36qx-fr4f-26g5` — **Pages Router i18n**의 미들웨어 우회

## Moderate 심각도 취약점 (4건)

- `GHSA-ffhc-5mcf-pf4q` — **CSP nonce**를 통한 XSS
- `GHSA-gx5p-jg67-6x7h` — **`beforeInteractive` 스크립트**의 XSS
- `GHSA-h64f-5h5j-jqjh` — **Image Optimization API**의 서비스 거부
- `GHSA-wfc6-r584-vfw7` — **RSC 응답**의 캐시 포이즈닝

## Low 심각도 취약점 (2건)

- `GHSA-vfv6-92ff-j949` — RSC **캐시 버스팅 충돌**을 통한 캐시 포이즈닝
- `GHSA-3g8h-86w9-wvmq` — **미들웨어 리다이렉트** 캐시 포이즈닝

## WAF 차단 가능 여부

- 네트워크 레벨(WAF)로 차단 가능한 취약점은 **DoS 계열 일부에 한정**되며, 기존 React Server Component CVE 대응 규칙이 새로운 DoS 취약점에도 적용
- 미들웨어 우회, SSRF, XSS 등 다수의 High 심각도 취약점은 WAF로 **안전하게 차단할 수 없어** 애플리케이션 코드 패치가 유일한 대응 수단
- 커스텀 WAF 규칙으로 대응 가능한 항목도 있으나, 글로벌 managed 규칙으로 적용 시 **애플리케이션 동작을 깨뜨릴 위험**이 존재

## 프레임워크 어댑터별 영향

- **Vinext**: 아키텍처가 기본 Next.js와 달라 공개된 CVE에 취약하지 않음
  - PPR resume 프로토콜 미구현, Pages Router data-route 엔드포인트 미노출, `x-nextjs-data` 등 내부 헤더를 요청 경계에서 제거
  - 추가 방어로 `vinext init` 시 React `19.2.6` 이상을 요구하도록 변경
- **OpenNext**: 어댑터 자체는 직접 취약하지 않으나, 사용자가 애플리케이션의 **Next.js 버전을 직접 업데이트**해야 함
  - 어댑터를 추가 강화한 새 버전 릴리스 완료

## 원문
- [원문](https://developers.cloudflare.com/changelog/post/2026-05-06-react-nextjs-vulnerabilities/)
- [GeekNews 토론](https://news.hada.io/topic?id=29283)

## My Note
<!-- 한 줄 코멘트 남기기 -->

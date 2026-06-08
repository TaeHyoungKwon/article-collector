---
category: AI
collected_at: '2026-05-12T17:04:26+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29427
id: hada-29427
matched_keywords:
- AI
read: false
recommend_score: -996.901
recommended_on: '2026-06-07'
source: geeknews
tags:
- AI
- Other
- stepsecurity.io
title: 'Mini Shai-Hulud의 귀환: npm 생태계를 강타한 자가 전파형 공급망 공격 (5/11)'
url: https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem
---

## TL;DR
- Mini Shai-Hulud 웜이 npm 생태계에서 자가 전파형 공급망 공격을 수행하고 있다.
- 이 공격은 정상적인 npm 패키지의 빌드 프로세스를 이용해 수십만 개의 프로젝트에 악성 코드를 전파할 수 있다.
- 따라서 개발자들은 보안 강화를 통해 CI/CD 파이프라인과 토큰 관리에 대한 주의가 필요하다.

## GeekNews 요약
### 개요

Mini Shai-Hulud 웜이 CI/CD 파이프라인을 탈취하고 개발자의 시크릿(비밀 정보)을 훔치는 방식으로 정상적인 npm 패키지들을 활발하게 감염시키고 있는 사건입니다. StepSecurity의 OSS Package Security Feed가 공식 `@tanstack` 패키지에서 이 공격을 처음 탐지하고 생태계 전반의 확산을 실시간 추적 중입니다.

### 발생 시점 및 규모

2026년 5월 11일 약 19:20 UTC경, 공식 `@tanstack/*` 패키지의 악성 버전 10개가 6분 이내에 npm 레지스트리에 게시되었습니다. 해당 패키지들은 수십만 개의 React 프로젝트에서 사용되는 TanStack Router 프레임워크의 핵심 구성요소입니다.

### 악성 페이로드

2.3MB 크기의 난독화된 자격증명 탈취 페이로드가 주입되어 GitHub 토큰, npm 토큰, CI/CD 시크릿을 수집하도록 설계되어 있었습니다.

### 핵심 위협 — 자가 전파 메커니즘

Shai-Hulud 웜은 저장소에 직접 침입할 필요가 없으며, 정상적인 빌드 프로세스에 올라타 사용자의 토큰을 이용해 스스로를 확산시킵니다. 즉, SLSA provenance, OIDC 기반 게시, 신뢰할 수 있는 CI/CD 파이프라인을 갖춘 패키지조차 무기화될 수 있다는 점이 이 공격의 핵심 시사점입니다.

### 연쇄 감염 위험

npm 생태계의 상호 연결된 구조는 이상적인 전파 매개체이며, 단일 토큰이 침해되면 수 분 내에 수십 개 패키지로 연쇄 감염될 수 있습니다 — 이번 사례에서도 6분 이내에 5개 패키지에 걸쳐 10개의 악성 버전이 배포되었습니다.

## 원문
- [원문](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
- [GeekNews 토론](https://news.hada.io/topic?id=29427)

## My Note
<!-- 한 줄 코멘트 남기기 -->

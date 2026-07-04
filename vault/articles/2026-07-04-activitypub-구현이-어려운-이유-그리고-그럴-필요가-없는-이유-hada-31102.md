---
category: Other
collected_at: '2026-07-04T09:22:48+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31102
id: hada-31102
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- hackers.pub
title: ActivityPub 구현이 어려운 이유, 그리고 그럴 필요가 없는 이유
url: https://hackers.pub/@fedify/2026/why-activitypub-is-hard/ko-KR
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- ActivityPub 서버를 직접 만들면 첫 `Follow` 요청부터 설명 없는 `401 Unauthorized`에 막히기 쉽고, Fedify는 **서명·JSON-LD·전달·보안** 부담을 애플리케이션 코드 밖으로 옮기는 TypeScript 프레임워크임
- 페디버스 인증은 만료 초안 `draft-cavage-http-signatures-12`와 표준 `RFC 9421`이 함께 쓰이며, 문서 서명까지 포함하면 **네 가지 서명 메커니즘**과 RSA·Ed25519 키를 다뤄야 함
- 같은 ActivityPub 활동도 JSON-LD에서는 문자열, 배열, 인라인 객체, URI 참조 등 여러 형태로 도착해, 직접 구현할수록 **방어 코드**가 코드베이스 전체에 퍼짐
- 분산 전달에서는 `Delete`가 `Create`보다 먼저 도착하는 “좀비 포스트” 같은 문제가 생기며, 큐·재시도·멱등성·순서 보장·회로 차단기가 필요함
- Fedify는 13개 웹 프레임워크 통합, KV·메시지 큐 어댑터, CLI·린터·디버거·OpenTelemetry를 제공해 **ActivityPub 세부 지식 없이** 연합 앱 개발을 시작할 수 있게 함

---

## 원문
- [원문](https://hackers.pub/@fedify/2026/why-activitypub-is-hard/ko-KR)
- [GeekNews 토론](https://news.hada.io/topic?id=31102)

## My Note
<!-- 한 줄 코멘트 남기기 -->

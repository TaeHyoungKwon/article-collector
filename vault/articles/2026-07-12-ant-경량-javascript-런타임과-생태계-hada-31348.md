---
category: Other
collected_at: '2026-07-12T18:37:11+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31348
id: hada-31348
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- antjs.org
title: Ant, 경량 JavaScript 런타임과 생태계
url: https://antjs.org
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 자체 개발한 **Ant Silver 엔진**으로 실제 npm 패키지를 실행하며, 약 8.6MB의 단일 바이너리와 빠른 시작 속도를 내세움
- V8·JSC·SpiderMonkey를 감싼 구조가 아니며, **compat-table 100%** 와 WinterTC 준수를 표시하고 Hono·Elysia·TypeScript·React·Rolldown·Wasm 등을 지원함
- Hono를 불러와 라우트 2개를 등록한 뒤 종료하는 콜드 스타트 측정에서 **5.4ms**를 기록해 Bun 12.8ms, Deno 24.8ms, Node.js 31.1ms보다 짧았음
- 패키지를 npm보다 최대 **40배 빠르게 설치**하며, TypeScript 직접 실행과 기본 `fetch` export 서빙으로 별도 빌드나 프레임워크 어댑터가 필요 없음
- 신뢰할 수 없는 코드를 위한 **VM 격리 샌드박스**와 npm 프로토콜 호환 공개 레지스트리 ants.land를 제공하며, macOS·Linux의 arm64 및 x86\_64에서 별도 툴체인 없이 사용할 수 있음

---

## 원문
- [원문](https://antjs.org)
- [GeekNews 토론](https://news.hada.io/topic?id=31348)

## My Note
<!-- 한 줄 코멘트 남기기 -->

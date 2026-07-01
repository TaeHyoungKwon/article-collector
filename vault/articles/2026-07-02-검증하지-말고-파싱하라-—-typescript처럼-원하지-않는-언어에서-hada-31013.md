---
category: AI
collected_at: '2026-07-02T02:04:15+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31013
id: hada-31013
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- cekrem.github.io
title: 검증하지 말고 파싱하라 — TypeScript처럼 원하지 않는 언어에서
url: https://cekrem.github.io/posts/parse-dont-validate-typescript/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- TypeScript 코드에 `if (user.email)` 같은 확인이 흩어지면, 이미 확인한 사실이 타입에 남지 않아 호출 스택 뒤쪽에서 같은 조건을 계속 의심하게 됨
- 파서는 원시 입력을 받아 **더 좁은 타입**이나 실패 정보를 돌려주며, `EmailAddress`처럼 검증된 사실을 프로그램 나머지 부분이 신뢰할 수 있게 만듦
- 구조적 타입 시스템을 쓰는 TypeScript에서는 `string`과 `Email`이 자연스럽게 분리되지 않아, `unique symbol` 기반 **브랜디드 타입**과 제한된 `as` 단언으로 명목적 경계를 흉내 냄
- `Parsed<T>` 같은 **구별된 유니언**은 성공과 실패를 타입 서명에 드러내지만, 전용 `match` 표현식이 없어 `never`를 이용한 exhaustive check를 직접 작성해야 함
- Zod, io-ts, valibot은 스키마에서 파서와 TypeScript 타입을 함께 만들 수 있지만, 외부 입력을 도메인 타입으로 보기 전 **경계마다 파싱**하는 규율은 여전히 개발자에게 남아 있음

---

## 원문
- [원문](https://cekrem.github.io/posts/parse-dont-validate-typescript/)
- [GeekNews 토론](https://news.hada.io/topic?id=31013)

## My Note
<!-- 한 줄 코멘트 남기기 -->

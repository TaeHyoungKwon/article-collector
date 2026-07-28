---
category: AI
collected_at: '2026-07-28T06:33:27+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31884
id: hada-31884
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/vercel-labs
title: Vercel의 Scriptc - 바이너리에 JavaScript 엔진을 포함하지 않는 TypeScript 네이티브 컴파일러
url: https://github.com/vercel-labs/scriptc
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **scriptc**는 일반 TypeScript를 Node·V8·JavaScript 엔진 없이 실행되는 소형 네이티브 바이너리로 컴파일하며, 실제 TypeScript 컴파일러의 타입 검사와 Node 동작 호환성을 유지함
- 코드 구조별로 정적 컴파일 가능 여부를 판정해 기본적으로 네이티브 코드로 만들고, `--dynamic`을 선택한 경우에만 **quickjs-ng**로 npm 패키지의 JavaScript와 `any` 타입 코드를 실행함
- 클래스·제네릭·`async`/`await`·예외·정규식부터 Node 서버 API, `fetch`, npm 의존성까지 지원하며, 미지원 구문은 오류 코드·코드 프레임·수정 힌트와 함께 거부함
- 800개 이상의 프로그램을 Node와 네이티브 바이너리에서 실행해 출력과 종료 코드를 비교하고, **AddressSanitizer**와 참조 횟수 감사로 메모리 오류를 검사함
- Apple M 시리즈 측정에서 시작 시간은 약 **2.4ms**, 정적 바이너리는 170~200KB, 일반적인 RSS는 1~4MB이며, 동적 모드와 내장 의존성을 포함하면 바이너리는 약 3MB가 됨

---

## 원문
- [원문](https://github.com/vercel-labs/scriptc)
- [GeekNews 토론](https://news.hada.io/topic?id=31884)

## My Note
<!-- 한 줄 코멘트 남기기 -->

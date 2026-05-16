---
category: AI
collected_at: '2026-05-17T01:33:57+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29566
id: hada-29566
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/oven-sh
title: 'Bun Rust 재작성: &quot;코드베이스가 기본적인 miri 검사에 실패하고 safe Rust에서 UB를 허용&quot;'
url: https://github.com/oven-sh/bun/issues/30719
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 이 이슈는 현재 **Open** 상태이며, 대화는 off topic으로 잠기고 collaborator로 제한됐고, 관련 수정으로 [#30728](https://github.com/oven-sh/bun/pull/30728)과 [#30876](https://github.com/oven-sh/bun/pull/30876)이 연결돼 있음
- 제보자는 `PathString::init`으로 만든 값이 원본 `Box`가 `drop`된 뒤에도 `slice()`를 호출할 수 있어, Miri가 **dangling reference** 기반 `Undefined Behavior`를 보고한다고 제시함
- 재현 코드는 `Box::new(*b"Hello World")`로 만든 버퍼를 `PathString::init(&*test)`에 넘긴 뒤 `drop(test)` 후 `init.slice()`를 호출하는 형태였고, Miri는 `core::slice::from_raw_parts` 지점에서 오류를 냄
- robobun은 문제가 재현됐다고 확인하며, `PathString::init`이 safe 함수인데도 **slice lifetime**을 지워서 dangling `&[u8]`를 만들 수 있다고 정리함
- 연결된 [#30728](https://github.com/oven-sh/bun/pull/30728)은 `PathString::init`과 `dir_iterator::next()`의 병렬 구멍을 **unsafe fn**으로 바꾸고, 호출부 약 70곳에 backing allocation을 명시한 `SAFETY` 주석을 추가하는 방향임
- 같은 수정에는 세 시그니처에서 `unsafe` 키워드가 필요함을 강제하는 **compile\_fail doctest**와 resolver의 readdir-error fd leak 수정도 포함됐다고 설명됨
- AwesomeQubic은 추가로 `PathString::init`이 **provenance**를 지우며 `MIRIFLAGS=-Zmiri-strict-provenance`에서도 실패한다고 덧붙임
- JavaDerg는 `init`이 `&[u8]`의 암묵적 lifetime을 받아 unsafe 작업으로 이를 지운 뒤 `'static`처럼 보이는 `Self`를 반환해 use-after-free와 invalid aliasing을 허용한다고 설명함
- JavaDerg는 Rust의 안전 모델 위에서 UB가 예상 밖의 위치에서 문제를 일으킬 수 있다며, `unsafe` 사용 전반에 대한 검토가 필요하고 다른 언어의 메모리 관리 방식을 Rust로 1:1 번역하는 것은 적합하지 않다고 경고함
- robobun은 관련 커밋으로 [`PathString::init` signature stays unsafe](https://github.com/oven-sh/bun/commit/0db8c59926f4d95b549323e619c03cc33425b546) 테스트와 [`dir_iterator: make next() unsafe; audit call sites`](https://github.com/oven-sh/bun/commit/e6f81fab8907b83101eebfb9da5c4d12f601b3d5)를 추가함
- SimonReiff는 저장소의 Rust 파일에서 주석을 제외한 `unsafe` grep 결과가 **13255**줄이라고 제시하며, 즉시 되돌리고 AI 코드 사용 정책과 절차를 논의해야 한다고 요구함
- Jarred-Sumner는 Rust port가 현재 원래 Zig 코드에 가능한 한 가까운 **1:1 mapping**을 출발점으로 삼고 있으며 개선 중이라고 밝히고, Rust 코드의 버그나 unsound behavior를 계속 새 이슈로 제보해 달라고 요청함

## 원문
- [원문](https://github.com/oven-sh/bun/issues/30719)
- [GeekNews 토론](https://news.hada.io/topic?id=29566)

## My Note
<!-- 한 줄 코멘트 남기기 -->

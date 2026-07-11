---
category: Other
collected_at: '2026-07-11T09:01:09+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31314
id: hada-31314
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/Cpp2Rust
title: 'Cpp2Rust: C++를 안전한 Rust로 자동 번역'
url: https://github.com/Cpp2Rust/cpp2rust
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Cpp2Rust**는 clang AST 기반의 구문 주도 번역기로, C++ 입력을 자동으로 완전히 안전한 Rust 코드로 변환함
- 번역 과정은 clang으로 C++ 파일을 파싱해 AST를 만들고, AST를 순회하며 Rust 코드를 문자열로 생성한 뒤 `rustfmt`로 단일 `.rs` 파일을 출력함
- 기본값은 **참조 카운팅 모델**이며, 디버깅과 성능 비교를 위해 `--model=unsafe`로 unsafe Rust 생성도 가능함
- 생성된 코드는 `libcc2rs` 런타임 라이브러리에 의존하며, C 포인터는 null, 산술, 별칭을 모델링하는 `Ptr<T>`로 변환됨
- 전체 프로그램 번역에는 `compile_commands.json`이 필요하며, CMake 프로젝트는 `CMAKE_EXPORT_COMPILE_COMMANDS=ON` 플래그로 생성할 수 있음

---

## 원문
- [원문](https://github.com/Cpp2Rust/cpp2rust)
- [GeekNews 토론](https://news.hada.io/topic?id=31314)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-07-17T07:52:17+09:00'
geeknews_comments: 2
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31507
id: hada-31507
matched_keywords: []
read: false
recommend_score: 1.023
source: geeknews
tags:
- Other
- rtfeldman.com
title: Roc 컴파일러의 Rust→Zig 재작성 진행기
url: https://rtfeldman.com/rust-to-zig
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 기존 구현의 **구조적 결함을 해결**하기 위해 Rust 30만 줄을 Zig로 다시 작성했으며, 487일 만에 기능 동등성에 도달해 올해 후반 첫 정식 번호 릴리스인 0.1.0을 목표로 함
- 새 컴파일러는 **핫 코드 로딩**과 재현 가능한 크로스 컴파일, 패턴 매칭 안의 문자열 보간, HTTP 라우팅의 힙 할당 제거를 지원하며 `Rocci Bird`의 wasm 크기도 절반 이하인 31KB로 줄임
- Zig를 선택한 핵심 이유는 빌드 시간, 세분화된 할당자와 데이터 배치 제어, 컴파일러 개발에 적합한 생태계, 메모리 비안전 코드 검사였으며 Zig 0.17.0의 증분 빌드는 약 46만 줄을 **35ms**에 다시 빌드함
- 실제 버그 분류에서 Rust 컴파일러는 메모리 손상 21건, Zig 컴파일러는 10건이었지만 대부분 잘못된 코드 생성 때문이었고, Zig 컴파일러 자체의 메모리 안전성 오류는 파일명을 깨뜨린 **use-after-free 2건**이었음
- Zig는 포인터 없는 데이터 구조, 무파싱 역직렬화, LLVM bitcode 직렬화기 재사용에 잘 맞았지만 테스트의 자동 메모리 해제, 다형성, 비공개 구조체 필드, 죽은 코드 탐지, 릴리스 간 호환성에서는 Rust의 개발 경험이 더 나았음

---

## 원문
- [원문](https://rtfeldman.com/rust-to-zig)
- [GeekNews 토론](https://news.hada.io/topic?id=31507)

## My Note
<!-- 한 줄 코멘트 남기기 -->

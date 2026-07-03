---
category: Other
collected_at: '2026-07-03T22:02:11+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31088
id: hada-31088
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/FractalFir
title: 'crustc: rustc 전체를 C로 변환'
url: https://github.com/FractalFir/crustc
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- `crustc`는 `rustc 1.98.0-nightly (c712ea946 2026-06-16)` 전체를 **4,600만 줄 C 코드**로 변환한 데모이며, `GCC`와 `make`로 빌드하면 동작하는 Rust 컴파일러가 생성됨
- 기반 도구인 `cilly`는 Rust를 C로 컴파일하는 **Rust 컴파일러 백엔드**이며, 이 저장소는 컴파일러가 자기 자신을 컴파일하는 가장 눈에 띄는 쇼케이스로 구성됨
- `cilly`는 대상 C 컴파일러와 플랫폼의 타입 레이아웃, 크기, 정렬, 문자 인코딩, 정수 형식 등을 **witness 프로그램**으로 질의해, 특정 C 컴파일러가 받아들일 수 있는 C 코드를 생성함
- 주요 목표는 LLVM/GCC 지원이 없지만 C 컴파일러는 있는 **오래되거나 특이한 하드웨어**에서 Rust 사용을 가능하게 하는 것이며, TCP로 원격 C 컴파일러와 통신하는 네트워크 투명성도 포함함
- 현재 생성된 C는 작성자의 워크스테이션 ISA인 **ARM64 Linux**를 대상으로 하며, `cilly` 전체 도구체인은 아직 공개 사용 준비가 되지 않았고 최적화 관련 버그도 추적 중임

---

## 원문
- [원문](https://github.com/FractalFir/crustc)
- [GeekNews 토론](https://news.hada.io/topic?id=31088)

## My Note
<!-- 한 줄 코멘트 남기기 -->

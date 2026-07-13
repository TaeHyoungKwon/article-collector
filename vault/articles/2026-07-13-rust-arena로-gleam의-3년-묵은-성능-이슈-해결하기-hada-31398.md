---
category: Other
collected_at: '2026-07-13T23:02:43+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31398
id: hada-31398
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- giacomocavalieri.me
title: Rust arena로 Gleam의 3년 묵은 성능 이슈 해결하기
url: https://giacomocavalieri.me/writing/gleam-rust-arenas
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Gleam 포매터의 재귀적 `Document` 구조에서 반복되던 **개별 힙 할당**을 arena 기반 참조로 바꿔, 3년간 남아 있던 성능 개선 이슈를 해결함
- `Box<Self>`를 arena에 저장된 `&Self`로 교체하고, Rust의 **수명 검사**로 arena가 제거된 뒤 내부 데이터가 참조되지 않도록 보장함
- 언어 키워드와 쉼표처럼 반복되는 `Document` 수백 개를 **한 번만 할당해 재사용**하면서 프리티 프린터 실행 시간이 13ms에서 9.8ms로 줄어 24% 빨라짐
- 소스 읽기와 파싱을 포함한 전체 `gleam format` 실행 시간도 **13% 단축**됐으며, 최대 메모리 사용량은 8.4MB에서 7.6MB로 약 10% 감소함
- arena를 전달하도록 함수와 호출부를 광범위하게 고쳐야 해 `+2963/-1032` 규모의 수작업이 필요했지만, **반복적인 개별 할당을 줄이는 방식**으로 속도와 메모리 사용량을 함께 개선할 수 있었음

---

## 원문
- [원문](https://giacomocavalieri.me/writing/gleam-rust-arenas)
- [GeekNews 토론](https://news.hada.io/topic?id=31398)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-03T14:02:43+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30141
id: hada-30141
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.901
recommended_on: '2026-06-03'
source: geeknews
tags:
- AI
- Other
- oxide.computer
title: iddqd, 또는 가장 어려운 종류의 unsafe Rust
url: https://oxide.computer/blog/iddqd-unsafe
---

## TL;DR
- 이 글은 Rust 프로그래밍 언어의 값을 관리하는 라이브러리 iddqd와 그 안전성에 대해 다루고 있다.
- iddqd는 IdOrdMap을 통해 키와 값을 효율적으로 연결하며, unsafe Rust의 도전 과제를 보여준다.
- 이는 Rust의 메모리 안전성을 유지하면서도 복잡한 데이터 관리 문제를 해결하는 방법에 대한 인사이트를 제공한다.

## GeekNews 요약
- **iddqd**는 값에서 키를 빌려오는 Rust 맵 라이브러리로, Oxide의 Omicron 제어 평면에서 디스크와 sled inventory 같은 큰 레코드의 인메모리 인덱스를 유지해 정확성이 중요함
- 표준 `BTreeMap`은 키와 값을 따로 저장해 전달이 번거롭거나 중복 키가 어긋날 수 있지만, **IdOrdMap**은 레코드 안의 필드에서 키를 추출해 조회함
- **unsafe Rust**는 컴파일러가 증명하지 못하는 안전한 프로그램을 표현하는 탈출구이며, 제네릭 코드가 사용자 제공 trait 구현을 호출할 때 병적인 안전 Rust까지 견뎌야 함
- `iddqd`의 mutable iteration은 인덱스가 모두 다르다는 불변식에 의존해 수명을 확장하며, 병적인 **Ord** 구현이 B-tree와 item set을 어긋나게 만들어 같은 항목에 대한 중복 인덱스를 만들 수 있었음
- 수정은 키와 인덱스를 함께 비교하고 실패 시 사용자 코드를 호출하지 않는 선형 스캔으로 되돌아가며, **Miri**·모델 기반 테스트·panic fault injection·LLM 적대적 리뷰를 함께 써야 충분한 신뢰를 얻음

---

## 원문
- [원문](https://oxide.computer/blog/iddqd-unsafe)
- [GeekNews 토론](https://news.hada.io/topic?id=30141)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-08-14T09:11:52+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32482
id: hada-32482
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- domenkozar.com
title: Rust에서 안전하게 C를 호출하는 extern &quot;fil-c&quot; 제안
url: https://domenkozar.com/2026/08/13/i-want-extern-fil-c/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Rust의 C FFI는 `unsafe` 경계 너머의 계약을 강제하지 못하므로, 기존 C/C++ 코드를 **Fil-C의 런타임 메모리 안전성** 아래에서 호출하는 새 FFI가 필요함
- 초기 버전은 스칼라 값, 복사된 문자열·슬라이스, 불투명 핸들만 지원하며, 전체 C 의존성 그래프를 Fil-C로 컴파일해 **일반 C로 빠지는 경로**를 차단함
- Fil-C는 C 소스와 호환되지만 ABI는 호환되지 않아 단순한 `bindgen` 옵션으로 구현할 수 없으며, 보장을 유지한 채 값을 교환하는 **새 Rust 브리지**가 필요함
- `filnix`는 100개가 넘는 nixpkgs 패키지를 Fil-C 플랫폼으로 이식했고, Zig도 전체 C/C++ 의존성 트리에 런타임 메모리 안전성을 적용하는 선택적 **`fil` ABI**를 제안함
- 기존 C는 포인터 검사와 가비지 컬렉션의 **런타임 비용을 내는 안전한 호환 경로**가 되며, 병목을 Rust로 재작성할수록 그 비용이 사라져 마이그레이션 유인이 커짐

---

## 원문
- [원문](https://domenkozar.com/2026/08/13/i-want-extern-fil-c/)
- [GeekNews 토론](https://news.hada.io/topic?id=32482)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-07-16T01:02:00+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31466
id: hada-31466
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- crates.io
title: qr-swastika-avoider v0.1.0 — QR 코드의 우발적 스와스티카 문양 회피
url: https://crates.io/crates/qr-swastika-avoider
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- QR 코드에 우연히 생길 수 있는 **스와스티카 문양을 탐지**하고, 선택적으로 문양 없는 QR 코드를 생성하는 Rust 크레이트임
- QR 표준의 **8개 마스크 패턴**을 모두 렌더링해 문양 없는 후보를 추린 뒤, ISO/IEC 18004 페널티가 가장 낮은 마스크를 선택함
- 파인더·타이밍·정렬·포맷·버전 모듈을 검사에서 제외하고 **주변 대비**를 고려해, 기능 요소나 눈에 보이지 않는 형태를 오인하지 않도록 함
- 기본 탐지기는 **외부 의존성이 없고 `unsafe` 코드를 금지**하며, 여러 QR 라이브러리와 `Vec<Vec<bool>>` 표현을 지원함
- 탐지 범위는 축에 정렬된 **5×5·7×7 갈고리 십자형**의 양쪽 방향과 두 색상 극성으로 한정되며, 45도·대각선 형태와 임의 회전은 지원하지 않음

---

## 원문
- [원문](https://crates.io/crates/qr-swastika-avoider)
- [GeekNews 토론](https://news.hada.io/topic?id=31466)

## My Note
<!-- 한 줄 코멘트 남기기 -->

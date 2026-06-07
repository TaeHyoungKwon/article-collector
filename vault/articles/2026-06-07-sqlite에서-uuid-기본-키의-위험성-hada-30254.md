---
category: Other
collected_at: '2026-06-07T20:01:53+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30254
id: hada-30254
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- andersmurphy.com
title: SQLite에서 UUID 기본 키의 위험성
url: https://andersmurphy.com/2026/06/05/the-perils-of-uuid-primary-keys-in-sqlite.html
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- SQLite의 기본 키 구현은 일반 rowid 테이블과 WITHOUT ROWID 테이블에서 물리 저장 순서를 달리 만들며, **랜덤 UUID4**를 클러스터드 인덱스로 쓰면 B-tree 재균형과 추가 페이징 비용 발생
- 정수 rowid 기준선은 100만 행 단위 삽입에서 대략 초당 100만 건 수준이며, **UUID4 WITHOUT ROWID**는 14~16배 느린 삽입 시간 기록
- UUID4의 무순서 특성은 행을 B-tree에 무작위로 삽입하게 만들고, 프로파일 결과에서 트리 균형 조정과 읽기·쓰기에 더 많은 시간 사용
- **UUID7 WITHOUT ROWID**는 시간 순서 UUID로 UUID4의 정렬 문제를 줄여 더 합리적인 삽입 시간을 보였지만, 16바이트 BLOB 키라 8바이트 정수 키보다 여전히 느림
- UUID4 WITH ROWID는 숨은 rowid의 순차성을 얻지만 두 인덱스로 인한 **쓰기 증폭**과 랜덤 인덱스 삽입 비용이 남아 UUID7 WITHOUT ROWID보다 낮은 성능

---

## 원문
- [원문](https://andersmurphy.com/2026/06/05/the-perils-of-uuid-primary-keys-in-sqlite.html)
- [GeekNews 토론](https://news.hada.io/topic?id=30254)

## My Note
<!-- 한 줄 코멘트 남기기 -->

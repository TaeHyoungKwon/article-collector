---
category: Other
collected_at: '2026-05-30T09:34:02+09:00'
geeknews_comments: 2
geeknews_score: 10
geeknews_url: https://news.hada.io/topic?id=30006
id: hada-30006
matched_keywords: []
read: false
recommend_score: 2.727
source: geeknews
tags:
- Other
- shopify.engineering
title: Shopify, 재고 예약 시스템을 Redis에서 MySQL로 교체
url: https://shopify.engineering/scaling-inventory-reservations
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **재고 예약 시스템**은 결제 처리 중 동일 상품이 두 번 판매되는 오버셀을 방지하는 핵심 인프라로, Shopify는 수년간 Redis 기반으로 운영해왔음
- MySQL 8의 **`SKIP LOCKED`** 기능을 활용해 아이템당 수량 컬럼 대신 판매 단위당 1개 행 구조로 재설계, Redis 없이도 고성능 처리 달성
- **복합 기본 키**, `READ COMMITTED` 격리 수준, 일관된 잠금 순서, `UNION ALL` 배치 처리 등 MySQL 최적화 기법을 조합해 락 경합과 데드락을 해소
- 실제 병목은 예약 쿼리가 아닌 **커넥션 점유**에 있었으며, 체크아웃 경로 전체를 계측해 DB 읽기 50%, 트랜잭션 33% 감소 달성
- **2025년 블랙프라이데이** 피크 기준 분당 $510만 매출을 처리하면서 writer CPU 50% 미만, reader CPU 16% 미만을 유지하며 목표 처방량 초과 달성

---

## 원문
- [원문](https://shopify.engineering/scaling-inventory-reservations)
- [GeekNews 토론](https://news.hada.io/topic?id=30006)

## My Note
<!-- 한 줄 코멘트 남기기 -->

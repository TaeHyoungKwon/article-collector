---
category: Other
collected_at: '2026-08-10T00:33:45+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32303
id: hada-32303
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- shopify.engineering
title: Shopify가 재고 예약 시스템을 Redis에서 MySQL로 교체해 대규모 트래픽을 처리한 방법
url: https://shopify.engineering/scaling-inventory-reservations
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 결제 과정의 재고 중복 판매를 막는 예약 시스템을 Redis에서 MySQL로 이전해 **2025년 피크 트래픽**에서도 처리량과 정확성 목표를 달성함
- MySQL 8의 **`SKIP LOCKED`** 와 재고 1개당 1행 구조를 사용하되, 품목·위치별 행을 최대 1,000개로 제한하고 부족할 때 원장에서 보충해 잠금 경합과 테이블 크기를 통제함
- 복합 기본 키로 행당 잠금을 2개에서 1개로 줄이고, **`READ COMMITTED`** 로 갭 잠금을 피했으며, 일관된 잠금 순서와 `UNION ALL` 배치로 교착 상태와 왕복 비용을 낮춤
- 실제 처리량을 제한한 원인은 쿼리나 CPU가 아니라 다른 결제 프로세스의 **DB 연결 점유 시간**이었으며, SQL 태그와 ProxySQL 추적으로 이를 찾아 기본 DB 읽기의 50%와 트랜잭션의 33%를 제거함
- Redis와 MySQL에 동시에 기록하는 섀도 모드와 **kill switch**로 점진 전환했으며, 고부하 플래시 세일에서도 writer CPU 50% 미만, reader CPU 16% 미만을 유지해 기존 데이터베이스만으로 고처리량 상호 배제를 구현함

---

## 원문
- [원문](https://shopify.engineering/scaling-inventory-reservations)
- [GeekNews 토론](https://news.hada.io/topic?id=32303)

## My Note
<!-- 한 줄 코멘트 남기기 -->

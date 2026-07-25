---
category: Other
collected_at: '2026-07-26T03:34:47+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31808
id: hada-31808
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- dbos.dev
title: Postgres LISTEN/NOTIFY는 실제로 확장 가능함
url: https://www.dbos.dev/blog/postgres-listen-notify-scalability
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Postgres LISTEN/NOTIFY의 **전역 배타적 잠금**은 단순 구현의 처리량을 제한하지만, 알림을 버퍼링해 일괄 전송하면 단일 서버에서 초당 최대 **6만 건의 스트림 쓰기**를 처리할 수 있음
- NOTIFY를 호출한 트랜잭션은 알림의 커밋 순서를 보장하기 위해 커밋과 `fsync()`가 끝날 때까지 **전역 잠금**을 유지하며, 이로 인해 커밋이 직렬화되고 그룹 커밋도 활용하지 못함
- 스트림 테이블의 모든 쓰기마다 트리거로 NOTIFY를 호출한 초기 구현은 낮은 지연 시간을 제공했지만, CPU·메모리·IOPS를 충분히 사용하지 못한 채 초당 **2,900건**에서 병목을 맞음
- 알림이 아닌 데이터베이스 테이블을 **진실의 원천**으로 삼고, 메모리에 모은 알림을 주기적으로 하나의 트랜잭션에서 전송하면 잠금 획득 횟수를 크게 줄일 수 있음
- 프로세스 장애로 버퍼의 알림이 유실될 가능성은 낮은 빈도의 폴링으로 보완하며, 동시 읽기 환경에서도 **15~100ms의 지연 시간**과 기존 대비 20배의 처리량을 달성함

---

## 원문
- [원문](https://www.dbos.dev/blog/postgres-listen-notify-scalability)
- [GeekNews 토론](https://news.hada.io/topic?id=31808)

## My Note
<!-- 한 줄 코멘트 남기기 -->

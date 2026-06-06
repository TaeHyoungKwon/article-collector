---
category: Other
collected_at: '2026-06-06T11:29:05+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30225
id: hada-30225
matched_keywords: []
read: false
recommend_score: 1.594
source: geeknews
tags:
- Other
- github.com/microsoft
title: pg_durable - PostgreSQL을 위한 내구성 SQL 함수
url: https://github.com/microsoft/pg_durable
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- PostgreSQL 내부에서 **재시도, 스케줄링, 병렬 fan-out, 조건 분기**를 작은 SQL DSL만으로 처리하는 **durable function** 확장
- 컨테이너나 외부 서비스 없이 **Postgres와 백그라운드 워커**만으로 동작
- 모든 단계가 PostgreSQL에 상태를 체크포인트로 기록해 **크래시·재시작·연결 끊김에도 중단 지점부터 재개**
- 큐 관리, 상태 추적, 크래시 복구, 단계 조정, 재시도를 직접 구현할 필요 없이 **SQL만 작성하면 오케스트레이션 엔진이 처리**
- 직접 구현 시 **300줄 이상의 보일러플레이트**가 필요한 작업을 단일 DSL 호출로 대체, **PostgreSQL 17**에서 오픈소스로 즉시 사용 가능

---

## 원문
- [원문](https://github.com/microsoft/pg_durable)
- [GeekNews 토론](https://news.hada.io/topic?id=30225)

## My Note
<!-- 한 줄 코멘트 남기기 -->

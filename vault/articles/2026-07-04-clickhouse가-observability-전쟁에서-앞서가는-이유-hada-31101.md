---
category: Other
collected_at: '2026-07-04T09:19:48+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31101
id: hada-31101
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- matduggan.com
title: ClickHouse가 Observability 전쟁에서 앞서가는 이유
url: https://matduggan.com/clickhouse-is-winning-the-observability-wars/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 로그는 작은 시스템의 `grep` 경험과 달리, 서비스와 소비자가 늘면 **대용량·비정형·예측 불가 쿼리**가 겹쳐 Observability에서 가장 다루기 어려운 데이터가 됨
- ClickHouse는 클릭스트림 분석용 DB로 출발했지만, **고볼륨·추가 중심·시간 순서·집계 읽기**라는 로그의 사용 패턴과 잘 맞음
- 컬럼 지향 저장 방식은 필요한 컬럼만 읽게 해주며, 실제 Observability 데이터에서 **10–14x 압축률**을 보여 Elasticsearch의 2–3x와 대비됨
- 1 TB/일 규모에서는 여러 스택이 모두 가능하지만, 5 TB/일과 10 TB/일로 커질수록 Elasticsearch·LGTM·Datadog은 구조나 비용이 크게 바뀌고 ClickHouse는 주로 **샤드 추가**로 확장됨
- ClickHouse는 초기 **스키마 설계**와 쿼리 엔진 복잡도를 요구하지만, 데이터가 한두 자릿수로 늘어도 운영 모델이 크게 흔들리지 않음

---

## 원문
- [원문](https://matduggan.com/clickhouse-is-winning-the-observability-wars/)
- [GeekNews 토론](https://news.hada.io/topic?id=31101)

## My Note
<!-- 한 줄 코멘트 남기기 -->

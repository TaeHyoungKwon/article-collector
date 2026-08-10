---
category: Other
collected_at: '2026-08-10T09:32:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=32319
id: hada-32319
matched_keywords: []
read: false
recommend_score: 1.386
source: geeknews
tags:
- Other
- planetscale.com
title: PlanetScale은 이전 백업을 복원해서 다음 백업을 만든다
url: https://planetscale.com/blog/massively-parallel-postgres-backups
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Postgres 병렬 백업**은 12시간마다 전체 데이터를 다시 복사하지 않고, **이전 백업을 임시 노드에 복원**한 뒤 **WAL을 재생**해 현재 상태까지 따라잡아 새로운 백업을 만드는 방식
- 무거운 데이터 복원과 WAL 재생 대부분을 **S3와 임시 백업 노드에서 처리**하고, primary에서는 아직 아카이브되지 않은 **최근 몇 분의 WAL**만 가져와 프로덕션 부하를 최소화함
- 샤드마다 별도 임시 노드를 띄워 동시에 처리하므로 데이터베이스가 커져도 **샤드 수만큼 백업을 병렬화**할 수 있으며, 32TB 기준 22시간이 8샤드에서 2.8시간, 32샤드에서 42분으로 줄어듦
- 다음 백업을 만들 때마다 이전 백업을 실제로 복원하므로, 단순히 백업 파일을 저장하는 것과 달리 **기존 백업이 복구 가능한지도 매 주기 검증**됨
- 같은 **백업 복원 → WAL 따라잡기** 구조를 데이터베이스 리사이징과 장애 노드 교체에도 사용해, 백업을 재해 복구뿐 아니라 일상적인 데이터베이스 운영의 기반으로 활용함

---

## 원문
- [원문](https://planetscale.com/blog/massively-parallel-postgres-backups)
- [GeekNews 토론](https://news.hada.io/topic?id=32319)

## My Note
<!-- 한 줄 코멘트 남기기 -->

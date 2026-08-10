---
category: Other
collected_at: '2026-08-10T10:15:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32326
id: hada-32326
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- boringsql.com
title: PostgreSQL의 MVCC는 나쁘다. 다른 DB도 마찬가지다
url: https://boringsql.com/posts/mvcc-bad-bad/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- PostgreSQL의 **쓰기 증폭, 테이블 팽창, VACUUM 부담, 32-bit XID wraparound**는 실제 문제지만, 이는 MVCC 자체의 결함이라기보다 과거 버전을 테이블에 남기고 나중에 정리하는 설계 선택에서 비롯됨
- reader가 writer를 막지 않으려면 어느 DB든 과거 버전을 어딘가에 보관해야 하며, 차이는 **과거 버전을 어디에 두고 / 어떻게 찾고 / 누가 언제 치우는지**에 있음
- Oracle/InnoDB는 undo log, SQL Server는 version store, MongoDB는 cache/history store, CockroachDB 같은 LSM 엔진은 timestamped key와 compaction을 사용해 PostgreSQL의 비용을 없애기보다 **writer, reader, cache, tempdb, compactor 쪽으로 이동**시킴
- 특히 오래 열린 snapshot은 모든 설계에서 문제가 되며, PostgreSQL은 garbage가 쌓이고, Oracle은 `snapshot too old`, InnoDB는 undo 증가, SQL Server는 tempdb 증가, WiredTiger는 cache pressure, LSM은 GC window 초과 같은 서로 다른 형태로 실패함
- 결국 **MVCC의 비용은 보존됨**: PostgreSQL은 garbage가 눈에 보이고 VACUUM을 직접 관리해야 하는 대신 reader를 막지 않고, 오래된 snapshot을 기본적으로 취소하지 않으며, 큰 transaction도 거의 즉시 rollback할 수 있는 쪽을 선택함

---

## 원문
- [원문](https://boringsql.com/posts/mvcc-bad-bad/)
- [GeekNews 토론](https://news.hada.io/topic?id=32326)

## My Note
<!-- 한 줄 코멘트 남기기 -->

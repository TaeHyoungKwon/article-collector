---
category: AI
collected_at: '2026-07-16T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=31475
id: hada-31475
matched_keywords:
- backend
- AI
read: false
recommend_score: 5.386
source: geeknews
tags:
- AI
- Other
- github.com/lesovsky
title: noisia - PostgreSQL용 유해한 워크로드 생성기
url: https://github.com/lesovsky/noisia
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **연결 고갈/잠금 대기/교착 상태/OOM/디스크 부족** 같은 장애 상황을 의도적으로 만들어 테스트하는 실패 주입 도구
- 유휴 트랜잭션/롤백/교착 상태/임시 파일/백엔드 종료부터 **WAL 폭증/테이블 팽창**까지 다양한 워크로드를 지원함
- 일부 워크로드는 max\_connections 고갈/복제 지연/스토리지 성능 저하를 넘어 PostgreSQL 인스턴스의 **PANIC 또는 전체 재시작**을 일으킬 수 있음
- Docker 이미지로 바로 실행하거나 Go 코드에서 개별 워크로드를 가져올 수 있으며, 무한 실행을 피하도록 **context와 제한 시간** 사용 필수
- 지원 워크로드
  - **idle transactions**: 트랜잭션을 열어두고 아무 일도 안 시켜서, 정리(VACUUM)를 방해하고 테이블/인덱스를 부풀림
  - **rollbacks**: 일부러 틀린 쿼리를 던져 에러를 내고 rollback 횟수를 늘림
  - **waiting transactions**: 한 세션이 테이블을 잠그고, 뒤에 연결들이 줄줄이 대기하다 결국 접속 한도(`max_connections`)에 도달해 새 접속 막기
  - **deadlocks**: 두 트랜잭션을 서로 락을 원하는 교착상태에 빠뜨리기
  - **temporary files**: 메모리(`work_mem`)보다 큰 데이터를 정렬시켜 디스크에 임시 파일을 쏟아내게 만들기 (`work_mem` 키우면 사라짐)
  - **terminate backends**: `pg_terminate_backend()` 등으로 실행 중인 세션/쿼리를 랜덤하게 강제 종료
  - **failed connections**: 모든 연결을 다 붙잡아 다른 클라이언트가 아예 접속 못 하게 만듦. `max_connections` 한도 소진
  - **fork connections**: 매번 새 연결로 짧은 쿼리만 날려 Postgres가 자식 프로세스를 과하게 생성하게 만들기
  - **backend-killer**: 한 세션이 prepared statement를 계속 쌓아 메모리를 부풀리다 OOM-kill로 인스턴스 전체를 재시작시키게 만들기
  - **slot-bloat**: 아무도 안 읽는 replication slot이 WAL을 붙잡아 `pg_wal`을 디스크 풀까지 채워 인스턴스를 PANIC시킴
  - **wal-flood**: 병렬 `UPDATE` 워커로 WAL을 폭주시켜 복제 지연/IO 압박을 생성 (slot-bloat의 "눈에 보이는" 버전, 디스크 풀은 환경에 따라 다름)
  - **bloat-churn**: 병렬 `UPDATE`로 autovacuum보다 빨리 테이블을 부풀리되, 멈춘 뒤엔 `VACUUM FULL`/`pg_repack`/`REINDEX CONCURRENTLY`로 되돌릴 수 있음
- 완전히 이해하지 못한 채 실행 금지, **테스트 목적 한정**으로 사용해야함
- BSD-3-Clause 라이선스

## 원문
- [원문](https://github.com/lesovsky/noisia)
- [GeekNews 토론](https://news.hada.io/topic?id=31475)

## My Note
<!-- 한 줄 코멘트 남기기 -->

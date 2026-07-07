---
category: AI
collected_at: '2026-07-06T09:50:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=31159
id: hada-31159
matched_keywords:
- AI
read: false
recommend_score: -996.614
recommended_on: '2026-07-07'
source: geeknews
tags:
- AI
- Other
- github.com/dbtrail
title: dbtrail - 모든 행 변경을 기억하고 되돌리기 가능한 MySQL용 타임머신
url: https://github.com/dbtrail/dbtrail
---

## TL;DR
- 이 글은 MySQL용 데이터 복구 도구인 dbtrail의 기능과 이점을 다룬다.
- dbtrail은 바이너리 로그를 통해 모든 행 변경을 추적하고, 특정 시점으로의 복원을 지원하여 정밀한 데이터 관리를 가능하게 한다.
- 이 도구는 데이터 손실 방지와 감사 기능 강화에 기여하여 데이터베이스 관리의 효율성을 향상시킨다.

## GeekNews 요약
- MySQL의 **바이너리 로그(binary log)** 를 tail 하여 모든 행 변경을 완전한 **before/after 이미지**와 함께 검색 가능한 인덱스로 보관
- Lock/스키마 변경/복원 대기 없이 특정 시점으로 되돌리는 **point-in-time recovery** 지원
- **모든 변경 조회 가능**: 어떤 행이 언제 무엇으로 바뀌었는지 before → after diff로 확인
- **정밀 Undo**: 손상된 행만 골라 정확한 역방향(reversal) SQL 생성
- **Cascade delete 복구**: `ON DELETE CASCADE`로 삭제된 자식 행을 재구성하고, `ON DELETE SET NULL`로 지워진 FK를 복원
  - InnoDB가 binlog 아래 단계에서 제거해 대부분의 도구가 감지하지 못하는 변경까지 포함
- **Time-travel**: 웹 콘솔 또는 `reconstruct` CLI로 임의 시점의 행·테이블 상태 조회
  - 라이브 SQL `AS OF` 인터페이스는 추가로 **ProxySQL** 필요
- **누가 바꿨지?**: 특정 변경이 어떤 데이터베이스 사용자·호스트·클라이언트 프로그램에서 비롯됐는지 식별(attribute)하며, audit plugin 유무에 따라 증명 가능 범위를 구분
- **안전망 검증**: `bintrail verify`가 오프라인/drift 없이 복구가 원본을 재현하는지 검사, `bintrail status`가 캡처 스트림의 누락 구간 표시
- **웹 콘솔**: 변경 탐색, 복구, 모니터링 서버 추가를 UI에서 처리
- **MCP 서버 제공**: Claude 또는 모든 MCP 클라이언트가 이력을 검색하고 복구안 초안 작성 가능
- 지원 대상: **MySQL**, Percona Server for MySQL, Amazon RDS for MySQL, Amazon Aurora MySQL, Google Cloud SQL for MySQL
  - 복제 프로토콜로 연결되어 디스크상의 binlog 파일 불필요
- 요구 사항: MySQL 8.0 이상, `binlog_format=ROW`, `binlog_row_image=FULL` (`bintrail doctor`가 점검 후 수정 방법 알려줌)
- 아파치 2.0 라이선스 (상업용/프로덕션 포함 자유 사용)

## 원문
- [원문](https://github.com/dbtrail/dbtrail)
- [GeekNews 토론](https://news.hada.io/topic?id=31159)

## My Note
<!-- 한 줄 코멘트 남기기 -->

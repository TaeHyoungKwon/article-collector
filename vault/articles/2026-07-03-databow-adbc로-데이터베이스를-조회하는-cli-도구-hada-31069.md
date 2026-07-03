---
category: Other
collected_at: '2026-07-03T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31069
id: hada-31069
matched_keywords: []
read: false
recommend_score: 1.609
source: geeknews
tags:
- Other
- github.com/columnar-tech
title: databow - ADBC로 데이터베이스를 조회하는 CLI 도구
url: https://github.com/columnar-tech/databow
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **ADBC(Arrow Database Connectivity)** 를 통해 데이터베이스에 연결하고 SQL을 실행하는 커맨드라인 도구
- 호환 ADBC 드라이버가 있는 모든 데이터베이스에 연결 가능
- **대화형 SQL 셸**을 제공해 명령 히스토리 및 직관적인 네비게이션 지원
- SQL 쿼리 하이라이팅 지원
- 동적 컬럼 너비로 **깔끔하게 정렬된 테이블** 형태의 결과 표시
- 쿼리 결과를 JSON, CSV, Arrow IPC **파일로 익스포트**
- 대화형 사용 외에 `--query`로 쿼리 직접 실행도 지원
  - **stdin** 입력 이나 `--file`로 파일 실행, `--output`으로 결과 파일 저장 등 비대화형 사용 지원
- Apache-2.0 라이선스 / Rust로 구현
- **ADBC(Arrow Database Connectivity)** 는 Apache Arrow 프로젝트의 하위 표준
  - 서로 다른 데이터베이스에서 **Arrow 데이터**를 넣고 빼기 위한 단일 API
  - **JDBC/ODBC의 컬럼 지향 대안** - 결과를 행(row) 단위가 아닌 컬럼 단위 **Arrow 데이터**로 반환
  - 대량 컬럼 분석 워크플로우에서 행 지향 형식으로 변환했다가 되돌리는 비용을 피할 수 있어 ODBC/JDBC 대비해서 효율적임
  - 2023년에 1.0.0 발표, 현재버전 1.1.0
  - 지원 하는 데이터베이스 (드라이버)
    - 공식: PostgreSQL, SQLite, DuckDB, Snowflake, BigQuery, Flight SQL 지원 DB
    - ADBC Driver Foundry 확장: Amazon Redshift, Apache DataFusion, Apache Spark, ClickHouse, Databricks, Exasol, Microsoft SQL Server

## 원문
- [원문](https://github.com/columnar-tech/databow)
- [GeekNews 토론](https://news.hada.io/topic?id=31069)

## My Note
<!-- 한 줄 코멘트 남기기 -->

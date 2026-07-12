---
category: AI
collected_at: '2026-07-11T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31315
id: hada-31315
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
recommended_on: '2026-07-12'
source: geeknews
tags:
- AI
- Other
- github.com/typedef-ai
title: fenic - 사람과 에이전트를 위한 시맨틱 데이터프레임(Semantic DataFrames)
url: https://github.com/typedef-ai/fenic
---

## TL;DR
- fenic은 사람과 에이전트를 위한 시맨틱 데이터프레임 쿼리 엔진으로, 다양한 연산자를 통합적으로 처리한다.
- AI 연산자는 쿼리에 내장되어 자동 최적화 기능을 사용하여 LLM 호출 비용을 줄인다.
- 이 기술은 비정형 데이터 처리와 파이프라인의 재사용성을 높여, 데이터 작업의 효율성을 개선할 수 있다.

## GeekNews 요약
- **PySpark/SQL 스타일 연산**(`select`, `filter`, `join`, `group_by`, `agg`)과 언어 모델을 호출하는 **시맨틱 연산자**를 하나의 쿼리 모델 안에서 함께 다루는 DataFrame 쿼리 엔진
  - 문서/트랜스크립트/로그/eval 트레이스/티켓/테이블/API를 **타입 지정된 행(typed rows)** 과 반복 가능한 워크플로로 변환
- `extract`, `classify`, `summarize`, `embed`, 시맨틱 `join` 등 **AI 연산자가 쿼리 모델에 내장**되어 스키마와 타입을 가진 연산자로 동작
  - 일반 필터를 시맨틱 필터보다 먼저 실행하고, 자동 배칭/레이트 리미팅/재시도/캐싱으로 **불필요한 LLM 호출과 비용을 줄임**
- **파이프라인 자체가 산출물** — 행 단위 lineage, `explain`, 쿼리별 토큰/비용 지표로 검사 가능
  - 지연 실행과 캐싱으로 재실행 가능하며, 명명된 테이블/뷰/MCP 도구로 승격 가능
  - 탐색 결과가 채팅 기록으로 사라지지 않고 **코드/데이터/파이프라인으로 남음**
- 비정형 텍스트를 **Pydantic 스키마**에 바인딩해 조회 가능한 구조화 컬럼으로 반환
  - **정확한 키가 아닌 의미 기반 조인**(semantic join) 지원
  - Markdown/Transcript/JSON(`jq`)/HTML/임베딩을 **일급 논리 타입**으로 처리하고 PDF 파싱 지원
  - S3/Hugging Face의 CSV·Parquet 데이터 읽기 지원
- 자체 쿼리 계획과 추론 실행 계층을 갖추고, 일반 데이터 연산에는 **Polars/DuckDB**를 활용
  - Apache Arrow로 데이터를 교환하며 로컬 환경에서 간단히 실행 가능
- 추론 특유의 레이트 리미트/타임아웃/비결정적 출력을 다루기 위해 **비동기 실행/재시도+백오프/캐싱/타입 검사**에 집중
- **사람과 에이전트가 같은 파이프라인을 작성·검사·재사용**하도록 설계
  - 코딩 에이전트용 `fenic skill install`과 정적 검사기 `fenic check` 제공
- 파이프라인을 **카탈로그에 도구로 등록해 MCP로 노출**
  - 데이터 파이프라인을 에이전트가 호출할 수 있는 타입 지정 도구로 전환
  - 스스로를 **에이전트를 위한 선언적 컨텍스트 엔지니어링**으로 정의
- 무거운 배치 추론을 에이전트 런타임 밖으로 **분리(decoupled)**
  - 더 예측 가능하고 반응성 좋은 에이전트와 개선된 자원 활용 제공
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/typedef-ai/fenic)
- [GeekNews 토론](https://news.hada.io/topic?id=31315)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-05-14T07:49:47+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29477
id: hada-29477
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- duckdb.org
title: 'Quack: DuckDB 클라이언트-서버 프로토콜'
url: https://duckdb.org/2026/05/12/quack-remote-protocol
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Quack**은 DuckDB 인스턴스 간 통신을 제공해 클라이언트-서버 구성과 여러 동시 작성자의 같은 데이터베이스 사용을 가능하게 함
- DuckDB는 **인프로세스 아키텍처**를 유지하면서, 여러 프로세스가 같은 파일을 수정할 때 필요한 상태 동기화를 원격 프로토콜로 처리함
- Quack은 **HTTP** 기반 요청-응답 프로토콜이며, `application/duckdb` 직렬화와 토큰 인증을 쓰고 기본 포트는 `9494`임
- 벤치마크에서 Quack은 **6천만 행**을 4.94초에 전송했고, 작은 append 테스트에서도 8스레드 기준 약 5,434 tx/s를 기록함
- Quack은 DuckLake 통합, 원격 **Catalog 서버**, 자동 설치·로드, 프로토콜 확장, 복제 프로토콜을 계획하며 DuckDB v2.0 시기 프로덕션 릴리스를 목표로 함

---

## 원문
- [원문](https://duckdb.org/2026/05/12/quack-remote-protocol)
- [GeekNews 토론](https://news.hada.io/topic?id=29477)

## My Note
<!-- 한 줄 코멘트 남기기 -->

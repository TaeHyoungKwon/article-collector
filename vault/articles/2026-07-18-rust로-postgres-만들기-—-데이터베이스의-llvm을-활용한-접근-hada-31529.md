---
category: Other
collected_at: '2026-07-18T07:03:23+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31529
id: hada-31529
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- turso.tech
title: Rust로 Postgres 만들기 — 데이터베이스의 LLVM을 활용한 접근
url: https://turso.tech/blog/a-new-modern-version-of-postgres-in-rust
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Turso는 Rust 기반 데이터베이스 코어에 **Postgres 호환 프런트엔드**를 연결해, 하나의 실행 엔진이 여러 데이터베이스 언어를 처리하는 **데이터베이스의 LLVM** 구조로 확장함
- Postgres SQL을 공통 AST로 파싱해 **VDBE 바이트코드**로 컴파일하며, 가능성을 검증한 pgmicro를 메인 코드 트리에 병합해 공식 개발 기반으로 삼음
- 기존 코어는 SQLite 파일 호환성, MVCC 동시 쓰기, 비동기 실행, 풍부한 타입 시스템, **자동 갱신 구체화 뷰**를 지원하며 여러 테스트 기법으로 신뢰성을 검증함
- 브라우저·모바일·각종 장치에서 임베디드 또는 단일 파일로 실행하면서도 기존 애플리케이션, ORM, `psql`이 **Postgres 와이어 프로토콜**로 접속할 수 있도록 설계함
- 100% 일치보다 널리 쓰이는 핵심 기능으로 기존 애플리케이션 대부분을 수정 없이 실행하는 데 집중하며, 확장 기능과 PL/pgSQL에는 **WASM 및 호환 계층** 적용을 검토하고 MIT 라이선스로 개발함

---

## 원문
- [원문](https://turso.tech/blog/a-new-modern-version-of-postgres-in-rust)
- [GeekNews 토론](https://news.hada.io/topic?id=31529)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-16T18:36:51+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31495
id: hada-31495
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.693
recommended_on: '2026-07-17'
source: geeknews
tags:
- AI
- Other
- github.com/beginner-jhj
title: 'Show GN: 온디바이스 벡터 데이터베이스를 C로 만들었습니다 (LSM-tree + HNSW)'
url: https://github.com/beginner-jhj/livero
---

## TL;DR
- 이 글은 대학생이 C 언어로 개발한 온디바이스 벡터 데이터베이스에 대해 설명한다.
- LSM-tree와 HNSW 인덱스를 결합하여 외부 의존성 없이 기기에서 직접 구동되는 벡터 스토어를 구현하였다.
- 이 데이터베이스는 임베디드 환경에서 RAG 및 시맨틱 검색을 가능하게 하여 다양한 애플리케이션에 활용될 수 있다.

## GeekNews 요약
대학 1학년이고, 데이터베이스 엔진이 실제로 어떻게 동작하는지 궁금해서 4개월 전에 직접 만들어보기 시작했습니다. 처음엔 학습용 LSM-tree 키-값 스토어였는데, 벡터 레이어를 붙이고 HNSW 인덱스를 얹으면서 온디바이스 벡터 데이터베이스가 됐습니다.

전부 C로 작성했고, 외부 의존성은 없습니다. 서버 없이 앱에 링크해서 기기 안에서 바로 도는 임베디드 라이브러리라, 온디바이스 RAG나 시맨틱 검색을 목표로 하고 있습니다.

주요 구성:

- LSM-tree 스토리지 (WAL + memtable + SST + 컴팩션)
- HNSW 벡터 인덱스 (근사 최근접 검색)
- ARM NEON SIMD 거리 커널 (float32 / int8, L2 / dot)
- 문자열 기반 쿼리 API (필터가 결합된 벡터 검색, FFI 바인딩 용이)

현재 기능은 기본적인 CRUD와 query기능이 있습니다.

아직 v1이라 최적화나 채울 부분이 남아 있고(x86 지원, 동시성, 모바일 바인딩 등), 한계와 로드맵은 README에 적혀있습니다.

이름은 livero (libero, 이탈리아어로 "자유로운" + vector)입니다. 서버로부터, 의존성으로부터 자유롭고, 기기 위에서 자유롭게 도는 벡터 스토어라는 뜻으로 지었습니다:)

## 원문
- [원문](https://github.com/beginner-jhj/livero)
- [GeekNews 토론](https://news.hada.io/topic?id=31495)

## My Note
<!-- 한 줄 코멘트 남기기 -->

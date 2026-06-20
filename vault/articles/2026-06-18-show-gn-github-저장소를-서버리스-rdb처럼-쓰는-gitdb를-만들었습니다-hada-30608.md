---
category: AI
collected_at: '2026-06-18T23:51:56+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=30608
id: hada-30608
matched_keywords:
- backend
- AI
- RAG
read: false
recommend_score: -992.391
recommended_on: '2026-06-19'
source: geeknews
tags:
- AI
- Other
- github.com/3x-haust
title: 'Show GN: GitHub 저장소를 서버리스 RDB처럼 쓰는 GitDB를 만들었습니다'
url: https://github.com/3x-haust/gitdb
---

## TL;DR
- 이 글은 GitHub 저장소를 서버리스 RDB처럼 활용하는 GitDB TypeScript 라이브러리에 대해 설명하고 있다.
- GitDB는 데이터 변경 이력을 Git history로 관리하며, SQL 쿼리와 다양한 API를 지원한다.
- 이는 GitHub를 데이터 저장소로 활용할 수 있는 새로운 방법을 제공하여 경량 애플리케이션 개발에 유용하다.

## GeekNews 요약
GitDB라는 TypeScript 라이브러리를 만들고 있습니다.

GitHub 저장소를 backend로 쓰는 서버리스 RDB식 데이터베이스입니다. 데이터는 repo 안에 manifest, mutation log, snapshot 같은 파일로 커밋되고, Git history가 그대로 데이터 변경 이력이 됩니다.

지원하는 것들:

- table API: insert, upsert, select, deleteWhere
- SQL식 query: SELECT, JOIN, GROUP BY, aggregate 등
- index 기반 select
- transaction
- plaintext / encrypted storage
- browser export: extension, static app에서 사용 가능
- Node/CLI 지원

목표는 Postgres 같은 일반 DB를 대체하는 게 아니라, 익스텐션/정적 앱/에이전트/작은 툴에서 “DB 서버 없이 GitHub repo 하나를 데이터 저장소로 쓰는” 선택지를 만드는 것입니다.

GitHub API latency와 rate limit이 있어서 hot OLTP나 realtime multi-writer에는 맞지 않습니다. 대신 저빈도 앱 데이터, demo, internal tool처럼 변경 이력과 배포 단순성이 더 중요한 경우를 생각하고 만들었습니다.

GitHub:  
<https://github.com/3x-haust/gitdb>

npm:  
<https://www.npmjs.com/package/@3xhaust/gitdb>

## 원문
- [원문](https://github.com/3x-haust/gitdb)
- [GeekNews 토론](https://news.hada.io/topic?id=30608)

## My Note
<!-- 한 줄 코멘트 남기기 -->

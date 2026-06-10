---
category: AI
collected_at: '2026-06-11T00:15:11+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30363
id: hada-30363
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/Munsunty
title: 'Show GN: Bundis – Bun.RedisClient를 위한 SQLite 기반 Redis 호환 서버'
url: https://github.com/Munsunty/bundis
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Bun 앱에서 Redis 스타일 API와 pub/sub이 필요하지만, 별도 Redis 서버를 운영하고 싶지 않을 때를 위한 프로젝트입니다.

순정 Bun.RedisClient의 접속 URL만 이 서버로 돌리면 코드 수정 없이 그대로 동작합니다. Redis 설치도, 네이티브 의존성도 없습니다. 데이터는 SQLite 파일(WAL)에 영속화되어 재시작 후에도 살아남고, 읽기는 인메모리 핫 캐시로 가속됩니다.

### 핵심

- 의존성 0 — bun:sqlite, Bun.listen 모두 Bun 내장. 별도 설치 불필요
- 영속성 — 데이터가 SQLite 단일 파일에 저장, 재시작 후 생존
- 콜드 스타트 ~13ms — 데이터 크기와 무관 (Redis의 RDB/AOF 재생과 달리 기동 시 데이터 재생이 없음)
- 핫 캐시 — write-through + 적응형 idle eviction + LRU 바이트 상한. 캐시는 순수 읽기 가속이고 SQLite가 항상 진실
- 3가지 실행 방식 — 프로세스 내 embed / 사이드카 spawn / 독립 데몬(bunx)

### 사용 예

import { RedisClient } from "bun";  
import { embedServer } from "bundis";

const server = embedServer({ dbPath: "./data.db" });  
const client = new RedisClient(server.url);  
await client.set("k", "v");

### 명확히 비목적인 것들

- Bun 외 런타임(Node.js/Deno 등)과 Bun.RedisClient 외 클라이언트(ioredis, node-redis, redis-py 등)는 지원하지 않습니다. 와이어 계약("올바른 바이트가 들어오면 올바른 바이트로 답한다")이 보증 대상입니다
- Redis Cluster/Sentinel, 다중 프로세스 .db 공유, HA/failover는 범위 밖 (단일 writer 가정)
- Lua 스크립팅(EVAL), list/sorted-set 명령군은 미구현 (계획됨)

인터페이스 호환이 목표지 Redis 성능 클론이 아닙니다. 처리량은 Redis가 우위이며, Bundis가 파는 것은 "Redis 설치 없이 Bun에서 디스크 영속 + Redis API"라는 운영 편의입니다. 성능 수치는 실제 Bun.RedisClient로 loopback TCP를 거쳐 측정한 호환 경로 벤치이며, 방법론과 before/after 수치는 저장소의 PERFORMANCE.md에 공개되어 있습니다.

GitHub: <https://github.com/Munsunty/bundis>  
설치: bun add bundis

## 원문
- [원문](https://github.com/Munsunty/bundis)
- [GeekNews 토론](https://news.hada.io/topic?id=30363)

## My Note
<!-- 한 줄 코멘트 남기기 -->

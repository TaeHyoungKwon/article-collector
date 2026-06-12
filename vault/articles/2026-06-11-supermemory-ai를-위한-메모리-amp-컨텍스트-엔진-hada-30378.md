---
category: AI
collected_at: '2026-06-11T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30378
id: hada-30378
matched_keywords:
- AI
- RAG
- Claude Code
read: false
recommend_score: -992.901
recommended_on: '2026-06-11'
source: geeknews
tags:
- AI
- Other
- github.com/supermemoryai
title: Supermemory - AI를 위한 메모리 &amp; 컨텍스트 엔진
url: https://github.com/supermemoryai/supermemory
---

## TL;DR
- Supermemory는 AI를 위한 메모리 및 컨텍스트 엔진으로, 대화 간 정보를 기억하지 못하는 AI의 한계를 극복한다.
- 이 시스템은 사용자 프로필을 자동으로 유지하며, 사실의 업데이트와 초과 정보를 삭제하는 기능을 제공한다.
- 개발자들은 단일 API를 통해 메모리 및 다양한 기능을 쉽게 통합할 수 있어 AI의 개인화 및 효율성을 높일 수 있다.

## GeekNews 요약
- 대화에서 **사실(facts)을 자동 추출**하고 사용자 프로필을 구축하는 AI용 메모리·컨텍스트 레이어로, 대화 간 정보를 기억하지 못하는 AI의 한계를 보완
- **지식을 업데이트하고, 모순을 처리하고, 만료된 정보를 삭제(자동 망각)** 까지 처리함
  - "방금 SF로 이사함"이 "NYC에 거주함"을 대체한다는 걸 이해하며, "내일 시험 있음" 같은 임시 사실은 날짜 경과 후 만료 처리
- **Memory + RAG를 단일 쿼리로 결합한 Hybrid Search** 제공, 지식 베이스 문서와 개인화된 컨텍스트를 함께 반환
- **User Profiles** 자동 유지 — 안정적 사실(static) + 최근 활동(dynamic)을 한 번의 호출(약 50ms)로 제공
- **Connectors**를 통해 Google Drive, Gmail, Notion, OneDrive, GitHub를 실시간 webhook으로 자동 동기화
- **Multi-modal Extractors** 내장 — PDF, 이미지(OCR), 비디오(전사), 코드(AST 인식 청킹)를 업로드만으로 처리
- 개발자는 **단일 API**로 메모리/RAG/프로필/커넥터 추가 가능, vector DB 설정 이나 임베딩 파이프라인/청킹 전략 필요없음
- **MCP 서버·플러그인** 제공 — Claude Code, Cursor, VS Code, OpenCode, OpenClaw, Hermes 등 지원, `memory`/`recall`/`context` 도구 제공
- 단일 바이너리로 제공되어 설정필요없이 바로 `localhost:6767`에서 동작, Ollama 연동 시 완전 오프라인 사용
- Vercel AI SDK, LangChain, LangGraph, OpenAI Agents SDK, Mastra, Agno, n8n 등 **드롭인 래퍼** 제공
- **LongMemEval(81.6%), LoCoMo, ConvoMem** 등 AI 메모리 주요 벤치마크 3종에서 1위를 차지
  - 자체 오픈소스 벤치마크 프레임워크 **MemoryBench**도 공개
- MIT 라이선스

## 원문
- [원문](https://github.com/supermemoryai/supermemory)
- [GeekNews 토론](https://news.hada.io/topic?id=30378)

## My Note
<!-- 한 줄 코멘트 남기기 -->

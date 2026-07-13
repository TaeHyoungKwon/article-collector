---
category: AI
collected_at: '2026-07-13T09:31:01+09:00'
geeknews_comments: 1
geeknews_score: 5
geeknews_url: https://news.hada.io/topic?id=31370
id: hada-31370
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 10.0
source: geeknews
tags:
- AI
- Other
- github.com/kenn-io
title: AgentsView - 여러 AI 코딩 에이전트의 세션 검색/분석/비용 추적 도구
url: https://github.com/kenn-io/agentsview
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code, Codex, Cursor, Gemini CLI, OpenCode 등 다양한 코딩 에이전트의 **세션을 자동 수집**
- 대화 검색, 토큰/비용 통계, 활동 분석, 변경 파일 추적을 로컬 웹 UI 및 CLI에서 제공
- **Go 단일 바이너리**로 실행되며, 처음 시작하면 로컬 세션 파일을 찾아 SQLite에 색인하고 `127.0.0.1:8080`에서 대시보드 제공
- **통합 세션 검색**: SQLite FTS5 전체 텍스트 검색을 기본으로 하며, OpenAI 호환 임베딩을 연결하면 의미 검색과 하이브리드 검색도 사용 가능
- **토큰/비용 추적**: 에이전트/날짜/모델별 사용량을 집계하고, LiteLLM 가격표와 프롬프트 캐시 생성/읽기 토큰을 반영해 비용을 계산
  - `agentsview usage daily`, `agentsview session usage <id>`로 전체 사용량과 개별 세션 비용을 확인 가능
  - 이미 색인된 SQLite를 조회하므로 원본 세션을 매번 파싱하는 방식보다 100배 이상 빠름
- 세션을 자동화/짧은 작업/표준/깊은 작업/장시간 작업으로 분류하고, 세션 시간, 메시지 수, 최대 컨텍스트, 턴당 도구 사용량, 캐시 효율 등을 제공
- **Recent Edits**에서 여러 에이전트가 최근 수정한 파일을 프로젝트와 경로별로 모아서 보여주고, 실제 변경을 만든 대화 메시지까지 추적 가능
- **실시간 대시보드**를 통해 SSE로 진행 중인 세션을 갱신해 보여주고, 활동 히트맵, 프로젝트별 통계, 도구/모델 사용량, 일별 지출 차트를 제공
- **다양한 세션 형식**을 지원하며, Aider의 저장소별 Markdown 로그, JetBrains Copilot 내보내기 파일, Antigravity CLI 사이드카 등 에이전트별 예외 형식도 지원
  - 일부 에이전트는 로컬에 전체 대화가 남지 않아 요약 정보만 제공될 수 있음
- 공유 및 확장을 위해 로컬 SQLite 데이터를 **PostgreSQL 팀 대시보드나 DuckDB 미러**로 보낼 수 있고, Claude/Codex 세션은 S3 호환 저장소에서도 읽기 가능
- Go 서버와 CLI, Svelte 5 웹 UI, Tauri 데스크톱 앱으로 구성
- MIT 라이선스로 공개

## 원문
- [원문](https://github.com/kenn-io/agentsview)
- [GeekNews 토론](https://news.hada.io/topic?id=31370)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-08-14T01:31:41+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32474
id: hada-32474
matched_keywords:
- AI
- LLM
- Codex
read: false
recommend_score: 7.307
source: geeknews
tags:
- AI
- Other
- github.com/deepseek-ai
title: DeepSeek Harness - 모든 구성 요소를 플러그인으로 만든 오픈소스 코딩 에이전트
url: https://github.com/deepseek-ai/deepseek-harness
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 핵심은 **“Everything is a Plugin”** 구조로, Model Adapter와 Tool뿐 아니라 Session Log, Agent Loop 자체까지 플러그인으로 구성
- 고정된 Core를 직접 수정하는 대신 필요한 플러그인을 추가하거나 기존 구현을 교체해 **에이전트의 동작과 실행 환경 전체를 조립**할 수 있도록 설계
- 기본적으로 프로젝트 파일을 읽고 수정하며 명령 실행, 작업 위임, 계획 관리 등을 수행하는 **코딩 에이전트** 기능을 제공
- 파일시스템, Shell/Terminal, Sandbox, 권한 승인, Subagent, Background Job 등도 독립된 구성 요소라 **필요한 구현만 교체하거나 새 기능을 추가**할 수 있음
- 기반에는 [Cordis](https://github.com/cordiverse/cordis)를 사용하며, 플러그인이 Service/Event/Tool 등을 등록하고 제거될 때 관련 리소스도 함께 정리됨
- **Profile과 Bundle**로 플러그인 구성을 조합하며 기본 `web`/`headless` 구성 위에 사용자 설정을 덮어써 자신만의 에이전트 환경을 만들 수 있음
- DeepSeek뿐 아니라 Anthropic/OpenAI와 Bedrock/Vertex/Azure/Codex 등을 지원하고 **사내 Gateway나 자체 OpenAI-compatible endpoint**도 등록 가능
- `npx @deepseek-ai/dsh web`으로 **Web UI**를 바로 실행할 수 있으며, Workspace를 지정한 뒤 에이전트 세션을 시작 가능
- Web UI 외에 **Headless 실행과 Python SDK**도 제공해 CLI 자동화나 자체 애플리케이션 안에 같은 에이전트 런타임을 내장할 수 있음
- Tool 실행은 권한 정책을 거치며, Web UI에서는 현재 정책상 승인이 필요한 작업을 사용자에게 확인하도록 구성
- 세션은 append-only **Event Log**를 중심으로 기록해 모델이 본 입력과 Tool 호출을 재구성할 수 있고, Resume/Fork/Transcript 같은 기능도 이 기록을 기반으로 동작
- Python SDK는 동일한 런타임을 프로그램에서 호출하며 세션을 유지하면 **대화뿐 아니라 Persistent Shell 상태까지 이어서 사용**할 수 있음
- 새로운 Tool/LLM Adapter/UI 연동/Command/Background Job/Subagent 등을 플러그인으로 추가할 수 있어, 특정 코딩 에이전트라기보다 **자신의 에이전트를 조립하기 위한 플랫폼**에 가까움
- 현재는 **Developer Preview** 단계. MIT 라이선스

## 원문
- [원문](https://github.com/deepseek-ai/deepseek-harness)
- [GeekNews 토론](https://news.hada.io/topic?id=32474)

## My Note
<!-- 한 줄 코멘트 남기기 -->

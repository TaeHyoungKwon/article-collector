---
category: AI
collected_at: '2026-05-08T03:25:56+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29268
id: hada-29268
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- github.com/PriuS2
title: 'Show GN: Hermes KanbanWebUI - Hermes Agent Kanban에 AI Workflow Designer를 더한
  칸반보드 스타일 WebUI'
url: https://github.com/PriuS2/HermesKanban
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Hermes Agent의 Kanban 기능을 브라우저에서 보기 쉽고 사용이 간편하게 하고 싶어서 Hermes KanbanWebUI를 만들었습니다.

Hermes Agent에는 task를 `triage`, `todo`, `ready`, `running`, `blocked`, `done` 같은 상태로 관리하는 Kanban 기능이 있는데, 기본 사용 흐름은 CLI 중심입니다. 저는 여러 task의 상태와 의존성을 한눈에 보고 싶어서 이 기능을 Trello 같은 칸반보드 UX로 감싸봤습니다.

이 프로젝트는 별도의 task 시스템을 새로 만드는 것이 아니라, Hermes Agent가 쓰는 기존 `hermes_cli.kanban_db` SQLite DB를 그대로 읽고 씁니다. 그래서 CLI / 대시보드에서 보던 task와 WebUI에서 보는 task가 같은 데이터입니다.

주요 기능은 다음과 같습니다.

- Hermes Kanban task를 Trello 스타일 보드로 보기
- task 생성, 상태 변경, 담당 agent profile 지정
- `running`, `blocked`, `done` 등 Hermes Kanban 상태 표시
- parent-child dependency를 선으로 시각화
- 실행 중인 task의 진행 상황, run, log, event 확인
- 여러 board 전환, 검색, 필터, bulk create 지원

기존 Hermes Kanban에서 추가로 구현된건 AI Workflow Designer입니다.

목표나 요구사항을 프롬프트로 입력하면, AI가 일을 여러 단계의 task로 쪼개고 task 간 의존성을 가진 DAG 초안을 만듭니다. 각 task 성격에 맞는 Hermes Agent profile도 같이 배정합니다.

예를 들어 “이 기능을 설계하고, 구현하고, QA하고, 문서화해줘” 같은 요청을 넣으면 기획/개발/QA/문서화 task로 나누고, 각 task를 적절한 agent profile에 배정한 뒤, 선행 작업 관계까지 만들어주는 식입니다.

생성된 workflow는 바로 적용되지 않고 먼저 초안으로 보여줍니다. 내용을 확인하고 수정한 뒤 적용하면 실제 Hermes Kanban task와 dependency로 생성됩니다.

## 원문
- [원문](https://github.com/PriuS2/HermesKanban)
- [GeekNews 토론](https://news.hada.io/topic?id=29268)

## My Note
<!-- 한 줄 코멘트 남기기 -->

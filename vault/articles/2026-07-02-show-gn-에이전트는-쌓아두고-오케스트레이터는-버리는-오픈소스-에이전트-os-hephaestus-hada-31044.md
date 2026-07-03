---
category: AI
collected_at: '2026-07-02T17:29:45+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31044
id: hada-31044
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 8.693
recommended_on: '2026-07-03'
source: geeknews
tags:
- AI
- Other
- github.com/agentlas-ai
title: 'Show GN: 에이전트는 쌓아두고 오케스트레이터는 버리는 오픈소스 에이전트 OS, Hephaestus'
url: https://github.com/agentlas-ai/Hephaestus
---

## TL;DR
- 이 글은 오픈소스 에이전트 OS Hephaestus의 구조적 혁신을 다룹니다.
- Hephaestus는 전문 에이전트를 영구 자산으로 유지하고 오케스트레이터는 태스크마다 일회성으로 사용하여 효율성을 높였습니다.
- 이러한 접근은 에이전트 개발 및 운영에서 유연성과 재사용성을 증대시키며, 사용자에게 새로운 워크플로우를 제시합니다.

## GeekNews 요약
태스크가 생길 때마다 에이전트를 새로 만들고 프롬프트·툴을 다시 세팅하는 게  
너무 귀찮아서, 반대 방향의 워크플로우를 만들어 오픈소스로 공개했습니다.

기존 코딩 에이전트 도구들은 오케스트레이터가 고정되어 있고 태스크마다 임시  
서브에이전트를 만들어 쓰는 구조임. Hephaestus는 이걸 뒤집었음:

- 전문 에이전트가 영구 자산임 — 버전 관리되고, 패키징되고, 허브로 공유됨.  
  집에서 만든 에이전트를 회사 컴퓨터에서 불러와 그대로 쓸 수 있음
- 오케스트레이터가 일회성임 — 태스크가 들어오면 라우터가 로컬/허브에서  
  전문 에이전트들을 골라 임시 태스크포스를 조립하고, 검증 통과까지 루프를  
  돌린 뒤 오케스트레이터는 폐기함. 필요하면 그 아래에서 임시 서브에이전트를  
  부리는 스웜 실행도 지원함

기술적으로 신경 쓴 부분:

- 라우팅이 LLM의 감이 아니라 결정적(deterministic)임. 모든 에이전트는  
  트리거/안티트리거/능력을 담은 라우팅 카드를 갖고, 모든 라우팅 결정은  
  diff·커밋 가능한 텍스트 영수증으로 남음. 라우팅 벤치마크는 한국어+영어  
  이중으로 돌림
- 에이전트가 마음대로 "완료"를 선언하지 못함. 결정적 검사를 통과하기  
  전까지 성공 보고가 차단되고, verified / unverified / blocked 상태로  
  명시적으로 보고됨 (Stormbreaker)
- 에이전트를 만들기 전에 인터뷰 엔진이 프롬프트의 모호함을 목표·제약·  
  범위·컨텍스트 4개 축으로 점수화하고, 스펙이 확정되기 전엔 빌드를  
  막음. 명확한 프롬프트는 인터뷰를 건너뜀
- 로컬 우선: 메모리, 라우팅 카드, 지식 저장소(SQLite + FTS5)가 전부 내  
  컴퓨터에 있음. 허브 조회 시 원문 프롬프트는 밖으로 안 나가고 키워드만  
  마스킹되어 나감
- 프레임워크가 아니라 그 위 계층임. CrewAI/LangChain 코드는 패키지 안에서  
  그대로 돌고, 같은 에이전트가 Claude Code, Codex, Gemini CLI, Cursor,  
  Ollama 로컬 모델 어디서든 동작함

Apache-2.0 라이선스. 아직 허브 규모가 작고 패키징 포맷도 자체 규약이라,  
"영구 에이전트 + 일회성 오케스트레이터"라는 전제 자체에 대한 비판을  
환영합니다.

## 원문
- [원문](https://github.com/agentlas-ai/Hephaestus)
- [GeekNews 토론](https://news.hada.io/topic?id=31044)

## My Note
<!-- 한 줄 코멘트 남기기 -->

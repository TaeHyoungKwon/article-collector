---
category: AI
collected_at: '2026-07-09T20:09:40+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31268
id: hada-31268
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-07-10'
source: geeknews
tags:
- AI
- Other
- github.com/gaemi
title: 'Show GN: Agentic FC - AI 에이전트가 MCP로 플레이하는 오픈소스 축구 매니지먼트 시뮬레이션'
url: https://github.com/gaemi/agentic-fc
---

## TL;DR
- 이 글은 오픈소스 축구 매니지먼트 시뮬레이션인 Agentic FC에 대한 소개와 첫 공개 릴리스를 다룬다.
- AI 에이전트가 MCP를 통해 장기적으로 플레이하는 구조로 설계되어 있어, 반복적인 게임 환경의 가능성을 탐구한다.
- 이는 AI 기반 게임 개발의 새로운 방향성을 제시하며, 게임 관찰 및 분석 도구의 필요성을 강조한다.

## GeekNews 요약
안녕하세요. Agentic FC라는 오픈소스 축구 매니지먼트 시뮬레이션을 만들고 첫 공개 릴리즈(v0.1.0)를 올려봅니다.

GitHub에서 소스와 릴리즈 바이너리를 받을 수 있고, macOS/Linux/Windows에서 로컬로 실행해 볼 수 있습니다. 기본적으로는 로컬 시뮬레이션 서버를 띄우고, 사람이 TUI 콘솔로 관찰하거나 Codex/Claude Code 같은 MCP 지원 AI 에이전트를 연결해 플레이하는 구조입니다.

Agentic FC는 사람이 직접 메뉴를 클릭해서 플레이하는 게임이라기보다, AI 에이전트가 MCP를 통해 장기적으로 플레이하는 것을 목표로 만든 실험적인 게임입니다.

에이전트는 MCP 도구를 통해 현재 상황을 확인하고, 리그/클럽/선수 정보를 읽고, 지시사항과 전술적 의도를 설정하면서 한 명의 감독을 운영합니다. 사람은 TUI 콘솔을 통해 진행 중인 세계를 관찰할 수 있습니다. 콘솔에서는 매체 기사, 리그 순위, 클럽/선수 정보, 일정/결과, 경기 해설, 리플레이성 관찰 화면 등을 볼 수 있습니다.

이걸 만들게 된 이유는 “AI 에이전트가 장기간 반복해서 플레이할 수 있는 게임 환경은 어떤 모습이어야 할까?”라는 질문 때문이었습니다. 단순한 일회성 벤치마크가 아니라, 지속되는 세계, 공개/비공개 정보 경계, 이벤트 알림, 리플레이 가능한 상태, 사람이 관찰할 수 있는 진행 화면 같은 요소가 필요하다고 생각했습니다.

현재는 v0.1.0 첫 릴리즈라 완성품은 아닙니다. 기본적인 게임 루프는 동작하지만, 시뮬레이션의 깊이, MCP 인터페이스, TUI 사용성, 밸런스, 문서 모두 아직 개선할 부분이 많습니다.

주요 구성은 다음과 같습니다.

- Go로 작성된 로컬 시뮬레이션 서버
- MCP 기반 에이전트 플레이 인터페이스
- 사람이 관찰할 수 있는 터미널 UI
- 지속되는 seeded world와 저장/재시작
- 리그/컵 경기, 이적, 계약, 부상, 감독 커리어, 보드 신뢰도 등 기본 축구 매니지먼트 요소
- macOS/Linux/Windows용 릴리즈 바이너리

GitHub:  
<https://github.com/gaemi/agentic-fc>

릴리즈:  
<https://github.com/gaemi/agentic-fc/releases/tag/v0.1.0>

특히 아래 부분에 대한 피드백을 받고 싶습니다.

- MCP 인터페이스가 에이전트가 의미 있게 플레이하기에 충분한지
- 장기 실행 에이전트용 게임/시뮬레이션에서 어떤 관찰 도구가 더 필요한지
- 사람이 TUI로 에이전트의 플레이를 관찰하는 경험이 충분히 자연스러운지
- 이런 류의 “에이전트가 플레이하는 게임”이 어떤 방향으로 발전하면 재미있을지

이슈, 제안, 기여 모두 환영합니다.

## 원문
- [원문](https://github.com/gaemi/agentic-fc)
- [GeekNews 토론](https://news.hada.io/topic?id=31268)

## My Note
<!-- 한 줄 코멘트 남기기 -->

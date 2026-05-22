---
category: AI
collected_at: '2026-05-22T02:03:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29738
id: hada-29738
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-05-21'
source: geeknews
tags:
- AI
- Other
- herdr.dev
title: Herdr - AI Agent 시대를 위한 tmux 스타일 터미널 워크스페이스
url: https://herdr.dev/
---

## TL;DR
- Herdr는 AI 에이전트를 통합 관리할 수 있는 터미널 워크스페이스 매니저입니다.
- 각 AI agent의 상태를 자동으로 인식하고 시각적으로 표시하는 기능이 특징적입니다.
- 이는 복잡한 개발 환경에서 여러 AI agent를 효율적으로 운영할 수 있는 솔루션을 제공합니다.

## GeekNews 요약
Herdr는 터미널 안에서 동작하는 “agent-native” 워크스페이스 매니저입니다. tmux처럼 세션 유지(detach/reattach), pane 분할, SSH 환경 지원을 제공하면서도, Claude Code·Codex·OpenCode 같은 AI coding agent들을 여러 개 동시에 관리하는 데 최적화되어 있습니다.

특히 단순한 terminal multiplexer를 넘어서, 각 agent의 상태를 working / blocked / done 형태로 자동 인식하고 사이드바에서 한눈에 보여주는 점이 인상적입니다. 여러 AI agent를 병렬로 돌리는 개발 workflow에 꽤 잘 맞습니다.

또한 Electron 기반 GUI 앱이 아니라 Rust 기반 단일 바이너리로 동작해서 가볍고, 기존에 사용하던 Ghostty, iTerm, Kitty 같은 터미널 환경을 그대로 유지할 수 있습니다. CLI와 Socket API도 제공해서 agent가 직접 pane 생성·명령 실행·출력 확인까지 자동화할 수 있습니다.

## 원문
- [원문](https://herdr.dev/)
- [GeekNews 토론](https://news.hada.io/topic?id=29738)

## My Note
<!-- 한 줄 코멘트 남기기 -->

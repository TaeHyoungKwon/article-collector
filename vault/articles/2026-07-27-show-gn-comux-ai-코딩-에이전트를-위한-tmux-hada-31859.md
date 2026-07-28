---
category: AI
collected_at: '2026-07-27T12:17:24+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31859
id: hada-31859
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-07-28'
source: geeknews
tags:
- AI
- Other
- github.com/marshallku
title: 'Show GN: comux - AI 코딩 에이전트를 위한 tmux'
url: https://github.com/marshallku/copad
---

## TL;DR
- 이 글은 AI 코딩 에이전트를 관리하기 위한 도구인 comux에 대해 설명한다.
- comux는 tmux의 기능을 개선하여 AI 에이전트의 상태를 실시간으로 모니터링하고 알림을 제공한다.
- 이는 여러 에이전트를 동시에 운영하는 개발자들에게 중요한 효율성을 제공하며, 사용 경험을 향상시킨다.

## GeekNews 요약
Claude Code, Codex 같은 AI 코딩 에이전트를 tmux 세션 여러 개에 띄워놓고 동시에 굴리다 보니 문제가 생겼습니다. 어떤 세션이 끝났는지, 어떤 게 저를 기다리며 막혀 있는지 놓치고, 백그라운드에서 돌아가는 에이전트는 usage limit도 걸리고 나서야 알게 되더라고요.  
tmux로는 여기까지가 한계라 comux를 만들었습니다.

comux는 AI 에이전트를 굴리기 위한 tmux 스타일 멀티플렉서입니다.

- 모든 세션의 에이전트 상태(working / ready / blocked)를 사이드바에 실시간 표시합니다
- 에이전트가 턴을 끝내거나 입력을 기다리면 즉시 데스크톱 알림을 발송합니다
- 서버를 죽이거나 재부팅해도, 재시작 시 각 에이전트를 대화 중이던 지점으로 복원(tmux-resurrect와 달리 session을 재시작합니다)됩니다
- 에이전트들의 usage와, 쌓여있는 알림을 status bar에서 실시간으로 확인할 수 있습니다

의존성 없는 단일 정적 바이너리라 SSH 헤드리스 서버 등 어디서나 돌아갑니다.  
더 큰 터미널 프로젝트(copad)의 일부지만 comux만 따로 설치할 수 있습니다:

```
# Comux만 설치  
curl -fsSL https://raw.githubusercontent.com/marshallku/copad/… | bash  
  
# Copad까지 설치 (Linux & MacOS)  
curl -fsSL https://raw.githubusercontent.com/marshallku/copad/master/install.sh | bash
```

4개월간의 제작기: <https://marshallku.com/dev/road-to-making-my-own-terminal/>

에이전트 여러 개 굴리시는 분들 피드백 환영합니다.

## 원문
- [원문](https://github.com/marshallku/copad)
- [GeekNews 토론](https://news.hada.io/topic?id=31859)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-05-09T22:08:30+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29323
id: hada-29323
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-05-09'
source: geeknews
tags:
- AI
- Other
- github.com/Younkyum
title: 'Show GN: LociTerm - AI 에이전트 SSH 세션이 계속 끊겨서 persistent 웹 터미널을 만들었습니다'
url: https://github.com/Younkyum/Loci-Terminal
---

## TL;DR
- 이 글은 LociTerm이라는 persistent 웹 터미널을 소개한다.
- LociTerm은 tmux 세션을 기반으로 모바일과 브라우저 환경에서 AI 코딩 워크플로우를 지원한다.
- 사용자는 브라우저에서 끊김 없이 작업을 이어갈 수 있어 더욱 효율적인 개발 환경을 경험할 수 있다.

## GeekNews 요약
노트북에서 클로드코드나 오픈코드를 돌리면, 작업하다가 노트북을 닫고 이동할 수가 없는 상황이 계속 불편했습니다.

SSH + tmux 조합으로 버티고 있었지만, 모바일 접근성이나 브라우저 기반 사용 경험은 여전히 아쉬운 부분이 많았고, 브라우저 터미널들은 대부분 세션이 일회성처럼 느껴졌습니다.

특히 cmux나 Warp 같은 최근 AI 시대의 터미널 UX들을 보면서, “이런 경험을 웹 기반 + self-hosted 형태로 쓸 수 있으면 좋겠다”라는 생각을 계속 하게 되었습니다.

그래서 persistent tmux 세션 기반의 self-hosted 웹 터미널인 LociTerm을 만들었습니다.

Claude Code, Codex, OpenCode 같은 AI 코딩 워크플로우를 브라우저에서 끊김 없이 이어서 사용할 수 있도록 만드는 것이 목표입니다.

주요 기능:

- Persistent tmux 세션 기반 작업 환경
- 브라우저 기반 다중 터미널
- 모바일 / 태블릿 접근 지원
- Self-hosted 단일 바이너리 구조
- 세션 자동 복구 및 유지
- AI coding workflow 최적화
- 원격 서버 / 홈랩 환경 대응

오픈소스로 개발 중이라, 사용해보시고 불편한 점이나 아이디어가 있다면 자유롭게 이슈 남겨주시면 감사하겠습니다.  
<https://www.loci.my/>

## 원문
- [원문](https://github.com/Younkyum/Loci-Terminal)
- [GeekNews 토론](https://news.hada.io/topic?id=29323)

## My Note
<!-- 한 줄 코멘트 남기기 -->

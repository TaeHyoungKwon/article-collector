---
category: AI
collected_at: '2026-08-05T15:02:15+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32167
id: hada-32167
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
source: geeknews
tags:
- AI
- Other
- github.com/greekr4
title: 'Show GN: rever-browser – 웹 리버싱하는 AI 에이전트 브라우저'
url: https://github.com/greekr4/rever-browser
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
AI 에이전트가 네트워크 트래픽을 보면서 사이트의 API를 리버싱하도록 도와주는 오픈소스 데스크톱 브라우저

- 대상 사이트를 그냥 브라우저에서 평소처럼 탐색하면, 뒤에서 모든 요청을 자동으로 기록합니다.
- AI 에이전트가 그 트래픽을 읽고, 사이트의 JS 번들을 뜯어보고(역난독화 포함), 페이지를 직접 클릭·입력하면서 동작을 확인합니다.
- "이 사이트가 무슨 요청을 보내지?"에서 "이 API를 그대로 재현하는 코드"까지, 앱 밖으로 나가지 않고 한 번에 이어집니다.
- 내가 만든 사이트의 보안검사를 해보세요!

Electron 기반, 3-프로세스 분리 구조

앱 안에 MCP 서버를 띄워 리피터·인트루더·헤더 오버라이드·HAR 내보내기·번들 역난독화· WebSocket 검사 등 약 46개 도구

기본 에이전트는 Claude Code, Codex도 지원

Apache-2.0 오픈소스

초기 단계라 피드백 환영합니다. 데모 영상과 소개는 Readme.md 혹은 렌딩페이지에 있습니다!

## 원문
- [원문](https://github.com/greekr4/rever-browser)
- [GeekNews 토론](https://news.hada.io/topic?id=32167)

## My Note
<!-- 한 줄 코멘트 남기기 -->

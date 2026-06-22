---
category: AI
collected_at: '2026-06-22T13:09:45+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30715
id: hada-30715
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 8.693
recommended_on: '2026-06-22'
source: geeknews
tags:
- AI
- Other
- github.com/hmmhmmhm
title: 'Show GN: ax-grep, 에이전트 웹 검색 토큰 사용량을 3배 개선 해주는 웹 리서치 툴'
url: https://github.com/hmmhmmhm/ax-grep
---

## TL;DR
- 이 글은 ax-grep이라는 웹 리서치 툴의 기능과 효과를 설명한다.
- ax-grep은 접근성 트리를 재현하여 에이전트 웹 검색 시 토큰 사용량을 3배 개선하고 메모리 소모를 15배 줄인다.
- 이 도구는 웹 데이터 수집에 효율성을 높여주며, 개발자에게 유용한 라이브러리로 활용될 수 있다.

## GeekNews 요약
안녕하세요 이번엔 ax-grep 이라는 에이전트 웹리서치 툴을 만들어 와봤습니다~!

ax-grep 은 브라우저에서 제공하는 접근성 트리 (Accessibility Tree) 와 유사한 트리를 브라우저 없이 재현합니다, 이 방식을 통해서 에이전트 웹 검색 시 토큰 사용량을 개선해주며, 약 15배 메모리를 적게 사용합니다.

agent-browser 랑 같이 사용하면 가장 좋게끔 구성해보았어요, 둘 다 설치해놓으면 ax-grep 만으로 충분한 사이트들은 ax-grep 이 사용되고, 좀 더 데이터 수집이 필요한 경우나 뭔가 제어가 필요한 경우에는 agent-browser 가 이후 동작하는 형태로 에이전트가 알아서 사용합니다.

또한 모바일 앱 내 웹뷰나 서버, 웹페이지 내에서도 접근성 트리를 모방한 데이터를 얻을 수 있게 해놔서 sLLM 에이전트나 자체 에이전트 개발하시는 분들께도 도움이 될 수 있게 라이브러리 화도 준비해보았습니다 ㅎㅎ

Codex, Claude Code, Antigravity 모두 지원합니다 피드백이나 개선 요청사항 있으면 언제든 부탁드리겠습니다!

## 원문
- [원문](https://github.com/hmmhmmhm/ax-grep)
- [GeekNews 토론](https://news.hada.io/topic?id=30715)

## My Note
<!-- 한 줄 코멘트 남기기 -->

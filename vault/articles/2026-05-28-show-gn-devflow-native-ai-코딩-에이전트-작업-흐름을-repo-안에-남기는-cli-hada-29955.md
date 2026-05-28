---
category: AI
collected_at: '2026-05-28T22:36:00+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29955
id: hada-29955
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
recommended_on: '2026-05-28'
source: geeknews
tags:
- AI
- Other
- github.com/Sungblab
title: 'Show GN: Devflow Native - AI 코딩 에이전트 작업 흐름을 repo 안에 남기는 CLI'
url: https://github.com/Sungblab/devflow-native
---

## TL;DR
- 이 글은 Devflow Native라는 CLI 도구의 기능과 목적을 설명하고 있다.
- Devflow Native는 AI 코딩 에이전트의 작업 흐름을 로컬 상태로 기록하여 개발자들이 작업의 진행 상황을 쉽게 파악할 수 있도록 돕는다.
- 이 도구는 작업 흐름 기록이 AI 코딩에 실질적인 도움이 될 수 있음을 시사하며, 개발자들에게 새로운 작업 방식의 필요성을 제기한다.

## GeekNews 요약
Devflow Native는 Codex, Claude Code 같은 AI 코딩 에이전트를 대체하는 도구가 아니라, 그 주변에 붙는 local-first workflow harness입니다.

AI coding을 하다 보면 코드 생성 자체보다 “작업이 어디까지 왔는지”, “무엇을 실제로 검증했는지”, “다음 세션이 어디서 이어가야 하는지”가 더 자주 문제가 됩니다.

Devflow는 이 정보를 repo 안에 남기려고 만든 CLI입니다.

현재 할 수 있는 일은 대략 이런 것들입니다.

- 프로젝트에 .devflow/config.json과 기본 workflow 문서 생성
- Codex/Claude용 harness inspect/install/health check
- 현재 repo 상태, 변경 파일, gate, session, handoff 상태 확인
- review evidence 기록
- finish 전에 “완료라고 말해도 되는지” dry-run 점검
- 다음 세션이 이어받을 prompt 생성
- MCP stdio server로 agent host에서 호출 가능

Superpowers가 agent가 따라야 할 개발 습관에 가깝고, CodeGraph가 repo를 이해하기 위한 context layer에 가깝다면, Devflow는 “이 작업이 실제로 어디까지 진행됐고 무엇이 검증됐는지”를 repo-local state로 남기는 쪽에 가깝습니다.

아직 alpha에 가깝고, 제가 직접 OpenCairn 같은 repo에 dogfood하면서 고치는 중입니다.

직접 써보려면 README의 “Agent-native setup” 흐름을 따라 Codex나 Claude Code에게 설치와 health check를 맡기는 방식이 가장 의도에 맞습니다.

피드백 받고 싶습니다:

- 이런 작업 흐름 기록이 실제 AI coding에 도움이 될지
- repo에 남겨야 하는 정보와 local-only로 둬야 하는 정보의 경계가 맞는지
- Codex/Claude 외에 어떤 agent host를 먼저 지원하면 좋을지

## 원문
- [원문](https://github.com/Sungblab/devflow-native)
- [GeekNews 토론](https://news.hada.io/topic?id=29955)

## My Note
<!-- 한 줄 코멘트 남기기 -->

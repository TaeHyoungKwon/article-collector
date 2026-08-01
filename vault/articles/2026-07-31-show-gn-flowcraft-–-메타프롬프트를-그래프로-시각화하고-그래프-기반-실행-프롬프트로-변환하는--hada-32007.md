---
category: AI
collected_at: '2026-07-31T09:36:58+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32007
id: hada-32007
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: -991.307
recommended_on: '2026-08-01'
source: geeknews
tags:
- AI
- Other
- github.com/sleeplesshan
title: 'Show GN: FlowCraft – 메타프롬프트를 그래프로 시각화하고 그래프 기반 실행 프롬프트로 변환하는 도구'
url: https://github.com/sleeplesshan/flowcraft-task-studio
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요,

Claude Code나 코덱스의 Plan 모드에서 만든 긴 계획을 보다 쉽게 검토하고,  
AI에게 전달하기 위해 만든 FlowCraft Task Studio를 공유합니다.

긴 메타프롬프트를 그대로 넘기면 어떤 작업이 먼저인지, 무엇을 병렬로 처리할 수 있는지,  
특정 서브에이전트에게 일이 너무 몰리지는 않았는지 파악하기 어려울 때가 있습니다.

저는 FlowCraft를 그래프 엔지니어링의 방식에서 영감받아 만들었습니다.  
계획을 작업 노드와 의존 관계로 나누고, 작업 순서와 병렬 구조를 눈으로 확인하고 보완할 수 있게 만든 도구입니다.

🧩 어떤 기능이 있나요?

- 메타프롬프트를 FlowCraft용 작업 JSON으로 변환하는 LLM 설계 프롬프트 생성
- 작업 노드 추가·이동·복제·삭제와 노드 간 연결 관계 직접 수정
- 작업별 담당, 입력, 결과물, 완료 조건과 파일 범위 편집
- 지나치게 많은 서브에이전트나 한 작업에 몰린 병목 검토
- Codex나 Claude Code에 전달할 Markdown 작업 지시서 생성
- 전체 작업 흐름을 이미지로 복사

서브에이전트가 단순히 오래 걸리는 경우와 실제로 멈춘 경우도 구분하도록 했습니다.  
원본 계획, Markdown 지시서, 노드 이미지를 함께 전달하는 Codex 스킬 제공

🚂 어떻게 사용하나요?

1. Codex나 Claude Code의 Plan 모드에서 만든 계획을 FlowCraft에 붙여넣습니다.
2. FlowCraft가 만든 LLM용 설계 프롬프트를 GPT나 Claude에 전달합니다. (Codex나 Claude Code에 바로 전달해도 됩니다.)
3. 반환된 JSON을 FlowCraft에 붙여넣어 작업 흐름을 확인하고 수정합니다.
4. 완성된 Markdown 작업 지시서와 노드 이미지를 Codex나 Claude Code에 전달합니다.

조금 더 간단하게 사용하고 싶다면 GitHub에 포함된 flowcraft-codex-handoff 스킬을 Codex에 등록할 수도 있습니다.  
스킬을 등록한 뒤 Plan 모드에서 만든 계획을 전달하면 다음 세 가지가 한 번에 준비됩니다.

- 기존 계획 메타프롬프트 원문
- 그래프 구조가 반영된 Markdown 작업 지시서
- 작업 노드와 의존 관계를 보여주는 SVG 이미지

앱에서 노드와 연결 관계를 직접 확인하거나 수정하고 싶을 때는 FlowCraft 화면을 사용하고,  
빠르게 Codex에 전달하고 싶을 때는 스킬을 사용하는 방식입니다.

FlowCraft 자체가 AI를 실행하거나 API를 호출하지는 않습니다.  
설치 없이 먼저 사용해 보실 분은 아래 Netlify 데모를 사용해 보셔도 되고,  
코드와 함께 제공되는 Codex 스킬을 살펴보고 싶으신 분은 GitHub를 확인해 주세요.

Netlify 데모: <https://flowtaskstudio.netlify.app>  
GitHub: <https://github.com/sleeplesshan/flowcraft-task-studio>

멀티 에이전트 작업을 설계할 때 그래프 시각화가 실제로 도움이 되는지,  
작업 분배나 프롬프트 구조에서 더 보완할 부분이 있는지 다양한 의견 주시면 감사하겠습니다!

## 원문
- [원문](https://github.com/sleeplesshan/flowcraft-task-studio)
- [GeekNews 토론](https://news.hada.io/topic?id=32007)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-14T19:24:30+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31435
id: hada-31435
matched_keywords:
- AI
- LLM
- RAG
read: false
recommend_score: -993.099
recommended_on: '2026-07-14'
source: geeknews
tags:
- AI
- Other
- github.com/Hahyun-Lee
title: 'Show GN: Brain-AI Memory – 장기 실행 LLM 에이전트의 메모리 실패를 진단하는 오픈 아키텍처'
url: https://github.com/Hahyun-Lee/brain-ai-memory
---

## TL;DR
- 이 글은 Brain-AI Memory 프로젝트를 통해 LLM 에이전트의 메모리 실패를 진단하는 방법론을 소개한다.
- 프로젝트는 다양한 메모리 유형과 그 실패 조건을 구분하여, 이전에는 파악하기 어려웠던 retrieval 문제를 체계적으로 분석한다.
- 독자는 실질적인 피드백을 통해 에이전트 시스템 개선과 메모리 처리 방식의 발전 여부를 판단할 수 있다.

## GeekNews 요약
에이전트가 오래된 기억을 사용하거나, 이미 기록한 것을 다시 묻거나, 규칙을 무시하거나, fallback 절차를 중간에 포기하는 문제를 모두 “retrieval 문제”로 보면 원인을 찾기 어렵습니다.  
Brain-AI Memory는 RAG, hook, guard, harness, loop를 새 이름으로 부르는 프로젝트가 아닙니다. 이들을 episodic·semantic memory, procedural rule·execution, numerical state, routing, input gate로 구분하고 각각의 실패 조건과 lifecycle을 연결합니다.  
몇 달간 실제 multi-project agent system에서 사용한 구조를 clean-room 방식으로 공개했습니다. 60초 실행 예제, 재사용 가능한 hook과 memory template, 운영 근거, 500문항 LongMemEval-S retrieval 결과를 포함합니다.  
Benchmark의 부정적 결과도 그대로 공개했습니다. 96-keyword pointer는 indexed text를 93% 줄였지만 recall@3는 full BM25의 86.1%에서 71.0%로 낮아졌습니다.  
특히 실제 agent failure가 이 component mapping에 잘 들어맞는지, 어디에서 맞지 않는지에 대한 피드백을 받고 싶습니다.

## 원문
- [원문](https://github.com/Hahyun-Lee/brain-ai-memory)
- [GeekNews 토론](https://news.hada.io/topic?id=31435)

## My Note
<!-- 한 줄 코멘트 남기기 -->

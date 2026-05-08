---
collected_at: '2026-05-08T00:14:04+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29263
id: hada-29263
matched_keywords:
- AI
- LLM
- Codex
read: false
recommend_score: 6.693
recommended_on: '2026-05-08'
source: geeknews
tags:
- github.com/computerphilosopher
title: 'Show GN: ElizAPI – 챗봇 Eliza(1966)를 OpenAI compatible api로 구현'
url: https://github.com/computerphilosopher/elizapi
---

## TL;DR
- 이 글은 챗봇 Eliza를 OpenAI와 호환되는 API로 구현한 ElizAPI에 대해 다룹니다.
- ElizAPI는 역사적 챗봇의 단순함을 활용해 비용 효율적으로 작동하는 정적 챗봇을 제안합니다.
- 이 프로젝트는 LLM에 의존하지 않고도 챗봇의 유용성을 보여주는 사례로, 기술 개발에 대한 새로운 관점을 제공합니다.

## GeekNews 요약
### Eliza란?

1966년 MIT에서 개발한 역사상 최초의 챗봇입니다. 상대방이 제시한 키워드를 이용해 문장을 발화하는 방식으로 구현되었습니다. 이러한 발화 방식은 환자를 상담하는 심리치료사의 방식을 흉내낸 것이라고 합니다.

예를 들면 이렇습니다.

- 만약 환자가 "나는 X가 필요해요"라고 말하면 다음 중 하나로 대답한다.
  - 왜 X가 필요한가요?
  - 만약 X가 있다면 정말 도움이 될까요?
  - 정말 X가 꼭 있어야 한다고 생각하세요?
- 만약 환자가 "나는 X(에)요"라고 말하면 다음 중 하나로 대답한다.
- 환자분이 X여서 의사를 보러 오셨나요?
- 얼마나 오랫동안 X였나요?
- 스스로가 X인데 대해 어떤 기분이 드나요?

(단 영어로 해야 함)

지금의 LLM에 비할바가 못되는 단순한 방식이지만, 당시 일부 사용자들은 Eliza를 감정이 있는 사람처럼 느꼈다고 합니다. 이러한 현상은 챗봇이 기계임을 알고 있음에도 감정이 있는 사람처럼 대하는 Eliza effect의 어원이 되었습니다.

### 만든 이유

OpenAI compatible API를 지원하는 챗봇이 꼭 LLM일 필요는 없다는 점에 착안했습니다.

이 프로젝트 자체는 장난삼아 만든 것이지만 'LLM처럼 행동하는 정적 챗봇'은 어딘가 쓸모가 있을거라 생각합니다.

비용이 거의 발생하지 않는 구조이기 때문에 AI에게 대체되어 실직하기 전까진 데모 사이트를 유지할 계획입니다.

### 사용 기술

- Eliza의 javascript 구현은 기존 구현 재사용(elizabot.js)
- 프론트엔드 구현: React 18
- 개발 도구: gemini cli, codex
- 배포: 비용 최소화를 위해 API 서버와 데모 사이트 모두 Cloudflare worker를 이용해 서비스합니다.

## 원문
- [원문](https://github.com/computerphilosopher/elizapi)
- [GeekNews 토론](https://news.hada.io/topic?id=29263)

## My Note
<!-- 한 줄 코멘트 남기기 -->

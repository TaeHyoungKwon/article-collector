---
category: AI
collected_at: '2026-08-06T08:32:15+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32189
id: hada-32189
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
recommended_on: '2026-08-06'
source: geeknews
tags:
- AI
- Other
- github.com/maestrojeong
title: 'Show GN: Ephemeral System Prompt - 실행마다 달라지는 지시사항을 넣고도 프롬프트 캐시 유지하기'
url: https://github.com/maestrojeong/maestro-agent-sdk/pull/51
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
LLM 에이전트를 만들다 보면 시스템 프롬프트는 유지하면서도 현재 시각, 세션 상태, 호스트 정책처럼 **실행마다 달라지는 지시사항**을 추가해야 할 때가 있습니다.

하지만 이런 내용을 시스템 프롬프트에 직접 합치면 매번 프롬프트 prefix가 달라져 provider의 prompt caching을 제대로 활용하기 어렵습니다.

`maestro-agent-sdk` v0.2.3에 추가한 `ephemeralSystemPrompt`는 이를 위해 만든 기능입니다.

```
for await (const event of maestroProvider({  
  agent: "maestro",  
  systemPrompt: stableBasePrompt,  
  ephemeralSystemPrompt: currentRuntimeInstructions,  
  prompt: userMessage,  
})) {  
  // ...  
}
```

`ephemeralSystemPrompt`는 실제 system prompt를 수정하지 않고, provider에 요청을 보낼 때 invocation의 첫 user 메시지에 임시로 추가됩니다.

- 안정적인 system prompt와 기존 대화 prefix는 그대로 유지
- tool 호출이 반복되는 동안 같은 위치에 고정되어 cache continuity 유지
- 대화 기록, compaction, session 파일에는 저장되지 않음
- subagent에는 자동으로 전달되지 않음
- 합쳐진 요청이 context window를 넘으면 provider 호출 전에 오류 처리

단, 이 값은 provider-native system role이 아니라 **host가 신뢰하는 런타임 지시사항**입니다. 보안 규칙이나 반드시 지켜야 하는 정책은 기존 system prompt에 두는 것이 맞습니다.

외부 요청이 새로 시작될 때는 이전 ephemeral instruction이 사라지는 지점부터 한 번 다시 계산해야 하지만, 하나의 tool loop 안에서는 캐시 가능한 prefix가 계속 확장됩니다.

- GitHub: <https://github.com/maestrojeong/maestro-agent-sdk>
- npm: <https://www.npmjs.com/package/maestro-agent-sdk>

## 원문
- [원문](https://github.com/maestrojeong/maestro-agent-sdk/pull/51)
- [GeekNews 토론](https://news.hada.io/topic?id=32189)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-02T10:31:31+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30100
id: hada-30100
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
recommended_on: '2026-06-02'
source: geeknews
tags:
- AI
- Other
- github.com/kyu1204
title: 'Show GN: oh-my-harness - AI 코딩 에이전트를 위한 훅 제너레이터 CLI'
url: https://github.com/kyu1204/oh-my-harness
---

## TL;DR
- 이 글은 AI 코딩 에이전트를 위한 훅 제너레이터 CLI인 oh-my-harness의 개발 배경과 기능을 다룬다.
- oh-my-harness는 프로젝트 규칙을 자동으로 설정하고 검증하여 실수를 줄여주는 안전장치를 제공한다.
- AI 도구의 사용이 증가함에 따라, 이러한 실수 방지 메커니즘이 필수적이라는 점을 강조한다.

## GeekNews 요약
안녕하세요. Claude Code랑 Codex를 쓰면서, 프롬프트에 배신당해(?) 훅 제너레이터인 oh-my-harness라는 CLI를 만들고 있습니다.

처음에는 그냥 CLAUDE.md나 AGENTS.md에 지침들을 아래처럼 추가했었습니다.

> 테스트 먼저 고쳐줘  
> 커밋 전에 테스트 돌려줘  
> main 브랜치에는 커밋하지 마  
> node\_modules나 dist는 건드리지 마  
> .env는 수정하지 마

근데 계속 쓰다 보니 거의 대부분 지침은 무시하고 어느 순간 이행을 안 하더라구요.

특히 TDD로 개발하라고 했지만  
“죄송합니다 테스트를 안 고쳤습니다”  
라고 한다든지,

이미 머지된 브랜치인지 체크하라고 했는데, 커밋 푸시 후  
“아직 머지된 브랜치가 아닙니다”  
라고 우긴다든지(?)

그래서 만든 게 oh-my-harness입니다.

agent를 위한 CLI도 제공하고, 사람을 위한 TUI도 제공합니다.

```
omh init "React app with TDD"
```

또는

```
omh init
```

그러면 프로젝트를 보고 harness.yaml을 만들고, 그걸 기준으로 Claude Code용 CLAUDE.md, Codex용 AGENTS.md와 각 런타임의 hook 설정을 같이 만들어줍니다.

예를 들면 지금은 이런 것들을 막거나 확인할 수 있습니다.

- main이나 이미 머지된 브랜치에서 커밋하려고 하면 막기
- 커밋 전에 테스트나 타입체크 돌리기
- 테스트를 먼저 안 고친 상태에서 소스만 수정하려고 하면 TDD 규칙으로 막기
- node\_modules, dist, .next, .env 같은 파일/폴더 보호하기
- 위험한 shell command 걸러내기

이 모든 것들은 제가 카탈로그라고 부르는, 미리 만들어둔 쉘 스크립트 모음으로 동작합니다.

omh init는 전달받은 자연어에서 알맞은 카탈로그를 골라 선택해주는 역할을 하고 있어요.

개인적으로는 AI 코딩 도구를 쓰면서 “잘 부탁해”라고 말하는 것보다, 실수하면 바로 멈춰주는 안전장치가 훨씬 중요하다고 느꼈습니다.

특히 에이전트가 점점 더 많은 파일을 고치고, 커밋까지 이어지는 흐름이 자연스러워질수록 이런 장치가 필요해질 것 같았습니다.

———

설치: npm install -g oh-my-harness

GitHub: <https://github.com/kyu1204/oh-my-harness>

npm: <https://www.npmjs.com/package/oh-my-harness>

아직 초기라 부족한 부분이 많습니다.  
사용해보시고 많은 의견 부탁드립니다. 기여도 환영합니다!

## 원문
- [원문](https://github.com/kyu1204/oh-my-harness)
- [GeekNews 토론](https://news.hada.io/topic?id=30100)

## My Note
<!-- 한 줄 코멘트 남기기 -->

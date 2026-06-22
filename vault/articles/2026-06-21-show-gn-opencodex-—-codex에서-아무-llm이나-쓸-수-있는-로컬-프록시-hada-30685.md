---
category: AI
collected_at: '2026-06-21T17:29:47+09:00'
geeknews_comments: 0
geeknews_score: 5
geeknews_url: https://news.hada.io/topic?id=30685
id: hada-30685
matched_keywords:
- AI
- LLM
- Codex
read: false
recommend_score: -992.208
recommended_on: '2026-06-21'
source: geeknews
tags:
- AI
- Other
- lidge-jun.github.io
title: 'Show GN: opencodex — Codex에서 아무 LLM이나 쓸 수 있는 로컬 프록시'
url: https://lidge-jun.github.io/opencodex/
---

## TL;DR
- 이 글은 opencodex라는 로컬 프록시에 대해 설명하며, 이를 통해 다양한 LLM을 Codex와 함께 사용할 수 있다.
- opencodex는 Codex와 LLM 프로바이더 간의 프로토콜을 실시간으로 번역하여 양방향으로 작동하도록 구현되었다.
- 독자는 opencodex를 통해 Codex의 기본 제한을 넘어서 다양한 LLM을 활용할 수 있는 가능성을 알게 된다.

## GeekNews 요약
Codex는 OpenAI 모델만 된다. Claude 쓰고 싶으면? GLM-5.2로 코딩하고 싶으면? OpenAI가 추가해줄 때까지 기다려야 한다.

opencodex는 이 문제를 푸는 로컬 프록시다. Codex와 LLM 프로바이더 사이에 끼어서 프로토콜을 실시간으로 번역한다. 스트리밍, 도구 호출, 추론 토큰, 이미지 — 전부 양방향으로 작동한다.

코덱스 앱, cli, sdk  
의 모델 피커에 정상적으로 등록되고  
한 세션안에서 GPT 와 등록된 모델을 전부 사용할수 있다

```
npm install -g @bitkyc08/opencodex  
ocx init      # 프로바이더 선택  
ocx start     # 프록시 시작  
codex -m "anthropic/claude-opus-4-8" "이 버그 고쳐줘"
```

### 어떻게 작동하는지

Codex는 Responses API(`/v1/responses`)라는 자체 프로토콜만 쓴다. 대부분의 LLM은 이걸 구현하지 않는다. opencodex가 5개 프로토콜 어댑터(Anthropic Messages, Google Gemini, Azure, OpenAI passthrough, OpenAI-compatible Chat Completions)로 번역해준다. 40개 이상의 프로바이더가 기본 내장돼 있다.

라우팅된 모델은 Codex 모델 선택기에 네이티브 모델처럼 나타난다. `provider/model` 형식으로 지정하면 된다.

### 만들면서 어려웠던 것

프록시 설계는 많은 오픈소스가 있어 구현이 쉬웠지만  
코덱스의 native한 경험을 위해서 codex-rs의 분해가 필수적이었다

**reasoning effort 매핑.** 프로바이더마다 effort 이름이 다르다. GLM은 "max"를 쓰고 Codex는 "xhigh"라고 부른다. Kimi는 아예 이 파라미터를 거부한다. 모델별로 변환 테이블을 따로 만들어야 했다.

**세션 히스토리.** Codex가 각 쓰레드의 `model_provider`를 DB에 저장한다. opencodex로 전환하면 기존 세션이 전부 안 보인다. SQLite를 직접 열어서 inject/restore 시 `model_provider` 태그를 바꾸는 마이그레이터를 만들었다. 파일 mtime은 보존해서 재개 순서가 흐트러지지 않게 했다.

**사이드카.** OpenAI가 아닌 모델은 웹 검색이나 이미지 이해를 못 한다. ChatGPT 로그인을 통해 gpt-5.4-mini 사이드카로 이 기능을 라우팅해서, Claude나 GLM에서도 실제 웹 검색이 되게 했다.

### 끄면 원래대로

`ocx stop` 누르면 Codex 설정, 카탈로그, 세션 히스토리가 전부 원본으로 복원된다. 잔여물 없다. 대시보드의 Stop 버튼이나 `ocx service uninstall`로도 같은 결과다.

MIT 라이선스. macOS/Linux/Windows 네이티브(WSL 불필요).

> GitHub: <https://github.com/lidge-jun/opencodex>  
> npm: `npm install -g @bitkyc08/opencodex`

## 원문
- [원문](https://lidge-jun.github.io/opencodex/)
- [GeekNews 토론](https://news.hada.io/topic?id=30685)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-09T09:31:01+09:00'
geeknews_comments: 2
geeknews_score: 5
geeknews_url: https://news.hada.io/topic?id=31251
id: hada-31251
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 8.121
recommended_on: '2026-07-10'
source: geeknews
tags:
- AI
- Other
- github.com/workweave
title: Weave Router - 프롬프트마다 최적의 모델로 라우팅하는 에이전트용 모델 라우터
url: https://github.com/workweave/router
---

## TL;DR
- Weave Router는 최적의 모델로 요청을 라우팅하는 에이전트용 모델 라우터이다.
- 이 시스템은 요청을 50ms 이내에 처리하며, 엔드포인트 변경을 통해 비용을 40-70% 절감할 수 있다.
- 다양한 API와 오픈 소스 모델을 지원하여, 개발자들에게 유연성과 비용 효율성을 제공하는 의미가 있다.

## GeekNews 요약
- Anthropic, OpenAI, Gemini를 **단일 엔드포인트**로 묶는 드롭인 프록시. 요청마다 최적 모델을 자동 선택
- 모든 프롬프트를 **50ms** 이내에 올바른 모델로 라우팅하며, 엔드포인트 변경만으로 **비용 40-70% 절감** 가능
- 프롬프트를 감(vibes)이 아닌 **on-box embedder** 기반 클러스터 스코어러로 판단, [Avengers-Pro](https://arxiv.org/abs/2508.12631)에서 파생된 방식으로 매 턴 라우팅 결정
- **Anthropic Messages, OpenAI Chat Completions, Gemini native** API를 모두 지원하며 스트리밍/툴/비젼 지원
- **DeepSeek, Kimi, GLM, Qwen, Llama, Mistral** 등 OSS 모델은 OpenRouter(또는 OpenAI 호환 엔드포인트) 경유해서 사용 가능
- **BYOK 기본**이며 공급자 키는 로컬에 암호화하여 저장
- **OTLP 트레이스** 기본 제공, Weave 대시보드/Honeycomb/Datadog/Grafana 등으로 Observability 확보
- 설치없이 `npx @workweave/router` 로 실행후 **Claude Code, Codex, opencode, Cursor**에 바로 연결 가능하며 on/off/status 전환 지원
  - Claude Code는 `make install-cc` 로 연결. `/router-off`, `/router-on`, `/router-status` 슬래시 명령 제공
  - Codex: `npx @workweave/router --codex` 를 실행하면 `~/.codex/config.toml`을 패치함
  - opencode: `npx @workweave/router --opencode` 하면 번들된 `@ai-sdk/anthropic` 공급자를 라우터 `/v1` 엔드포인트로 지정, Anthropic Messages API 네이티브 지원으로 수정 없이 동작함
  - Cursor: 아직 초기 베타로 성능은 불안정, Settings → Models → Override OpenAI Base URL에 `http://localhost:8080/v1` 입력
- Elastic License 2.0

## 원문
- [원문](https://github.com/workweave/router)
- [GeekNews 토론](https://news.hada.io/topic?id=31251)

## My Note
<!-- 한 줄 코멘트 남기기 -->

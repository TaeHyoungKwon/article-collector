---
category: AI
collected_at: '2026-06-03T01:32:52+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30120
id: hada-30120
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-06-02'
source: geeknews
tags:
- AI
- Other
- github.com/cyberpapiii
title: Chipotlai Max - Chipotle Pepper AI를 기본 모델로 쓰는 밈 AI 코딩 에이전트
url: https://github.com/cyberpapiii/chipotlai-max
---

## TL;DR
- Chipotlai Max는 Chipotle의 고객지원 챗봇 Pepper AI를 기반으로 하는 AI 코딩 에이전트이다.
- 이 에이전트는 리버스 엔지니어링된 백엔드를 통해 사용자에게 밈성 코딩 기능을 제공하며, 비용은 무료로 설정되어 있다.
- 그러나 Chipotle의 정책 위반 가능성과 운영상의 제약으로 인해 프로덕션 환경에서 사용되지 말아야 한다는 경고가 있다.

## GeekNews 요약
- **Chipotlai Max**는 [OpenCode](https://github.com/anomalyco/opencode)를 포크해 Chipotle의 고객지원 챗봇 **Pepper AI**를 기본 모델로 설정한 밈성 AI 코딩 에이전트임
- Pepper는 2026년 3월 12~13일 LeetCode 풀이, Python 작성, 연결 리스트 뒤집기 등을 해내며 바이럴이 됐고, IPsoft Amelia 기반으로 동작함
- [@Gonzih](https://github.com/Gonzih)가 Amelia의 WebSocket/SockJS + STOMP 백엔드를 리버스 엔지니어링해 로컬에서 `http://localhost:3000/v1`을 제공하는 [OpenAI 호환 프록시](https://github.com/Gonzih/chipotle-llm-provider)를 공개함
- 이 프로젝트는 해당 프록시를 전제로 `chipotle-pepper` 제공자, `pepper-1` 모델, `http://localhost:3000/v1` Base URL을 미리 설정해 둠
- API 키는 `burrito-2026`처럼 아무 값이나 동작한다고 되어 있으며, 비용은 `$0.00`으로 표기돼 있음
- 실행은 `git clone --recursive`, `bun install`, `./start-chipotlai.sh`로 프록시와 CLI를 함께 시작하거나, 프록시와 Chipotlai Max를 별도 터미널에서 실행하는 방식임
- **운영 제약**은 큼: Chipotle의 프로덕션 지원 봇을 리버스 엔지니어링하므로 TOS 위반 가능성이 있고, Chipotle이 패치하면 프록시가 언제든 깨질 수 있음
- 익명 세션 기반으로 제한되며 `MAX_POOL_SIZE=5`가 명시돼 있어, 프로덕션 코드베이스에는 쓰지 말라고 경고함
- 기여 섹션은 Chipotle Pepper가 2026년 3월 패치됐다고 전제하고, Home Depot, Lowe’s, Target, Starbucks, Walmart, McDonald’s 같은 다른 기업 챗봇 제공자 프록시를 찾고 있음
- 새 제공자 추가 흐름은 기업 챗봇을 찾고, WebSocket이나 REST API를 리버스 엔지니어링하고, OpenAI 호환 `/v1/chat/completions` 프록시를 만든 뒤 `packages/opencode/src/provider/`에 PR을 보내는 방식임
- 라이선스는 [OpenCode](https://github.com/anomalyco/opencode)에서 이어받은 **MIT**이며, Chipotle과는 제휴 관계가 없다고 명시함

## 원문
- [원문](https://github.com/cyberpapiii/chipotlai-max)
- [GeekNews 토론](https://news.hada.io/topic?id=30120)

## My Note
<!-- 한 줄 코멘트 남기기 -->

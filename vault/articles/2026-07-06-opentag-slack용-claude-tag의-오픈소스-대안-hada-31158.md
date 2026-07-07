---
category: AI
collected_at: '2026-07-06T09:35:02+09:00'
geeknews_comments: 0
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=31158
id: hada-31158
matched_keywords:
- AI
- LLM
read: false
recommend_score: -994.054
recommended_on: '2026-07-07'
source: geeknews
tags:
- AI
- Other
- github.com/CopilotKit
title: OpenTag - Slack용 Claude Tag의 오픈소스 대안
url: https://github.com/CopilotKit/OpenTag
---

## TL;DR
- 이 글은 Slack용 Claude Tag의 오픈소스 대안인 OpenTag에 대해 설명하고 있다.
- OpenTag는 셀프 호스팅 AI 에이전트로서 비종속성 및 다양한 플랫폼에서의 호환성을 제공한다.
- 사용자는 원하는 모델을 연결하고 직접 운영할 수 있어 데이터 소유 및 관리에 유리하다.

## GeekNews 요약
- Slack 스레드를 읽고 답변하며 도구를 호출해 결과를 대화창에 바로 렌더링하는 **셀프 호스팅 AI 에이전트**
- 락인없이 런타임을 소유하며, 원하는 모델을 자신의 도구에 연동 가능
- CopilotKit의 오픈 SDK인 **@copilotkit/bot** 위에 구축되어, 동일 코드가 Slack/Discord/Telegram/WhatsApp에서 동작
- 분석 결과/표/막대 차트를 대화 안에 인라인 표시하는 **generative UI** 지원
- Approve 게이트를 통과한 후에만 티켓을 생성하는 **human-in-the-loop** 흐름 포함
- 셀프 호스팅 시 **agent**(LLM 백엔드)와 **bot**(Slack 연결) 두 프로세스를 구동
- 4개의 필수 패키지로 구성
  - **bot**: 스레딩, 도구 호출, human-in-the-loop 게이트를 담당하는 플랫폼 비종속 봇 엔진
  - **runtime**: LLM과 도구를 실행하는 AG-UI 에이전트 백엔드
  - **bot-ui**: 리치 메시지용 크로스 플랫폼 JSX (Slack의 Block Kit, Discord의 Components V2, Telegram의 HTML)
  - **bot-slack**: Slack 어댑터, 대상 플랫폼에 맞게 교체 가능
- 재시작해도 스레드를 유지하는 **bot-store-redis** 제공 (미사용 시 in-memory 기본값)
- 에이전트 동작은 **runtime.ts** 내 단일 시스템 프롬프트로 제어되며, 이를 재작성하면 다른 에이전트로 전환 가능
- **app/** 디렉터리를 복사해 자체 봇 시작 가능
- MIT 라이선스

## 원문
- [원문](https://github.com/CopilotKit/OpenTag)
- [GeekNews 토론](https://news.hada.io/topic?id=31158)

## My Note
<!-- 한 줄 코멘트 남기기 -->

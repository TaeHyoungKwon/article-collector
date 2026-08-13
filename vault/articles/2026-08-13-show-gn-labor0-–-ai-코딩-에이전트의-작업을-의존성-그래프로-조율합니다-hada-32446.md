---
category: AI
collected_at: '2026-08-13T08:17:15+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32446
id: hada-32446
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-08-12'
source: geeknews
tags:
- AI
- Other
- labor0.com
title: 'Show GN: Labor0 – AI 코딩 에이전트의 작업을 의존성 그래프로 조율합니다'
url: https://labor0.com/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. SWC를 만든 강동윤입니다.

Zephyr Cloud Inc.에서 제가 처음부터 개발을 리드해 온 **Labor0**를 출시했습니다.

Codex, Claude Code, OpenCode 같은 코딩 에이전트는 이미 개별 작업을 꽤 잘 수행합니다. 하지만 실제 프로젝트는 하나의 작업으로 끝나지 않습니다.

기능 하나를 개발하더라도 API 계약, 백엔드와 UI 구현, 테스트, 문서화처럼 서로 의존하는 여러 작업이 필요합니다. 이를 무조건 동시에 시작하면 에이전트가 빠를수록 잘못된 구현과 재작업도 더 빠르게 늘어날 수 있습니다.

Labor0는 이 문제를 **코딩 능력보다 조율의 문제**로 보고 있습니다.

큰 개발 요청을 작은 작업들로 나누고, 작업 사이의 선행 조건을 의존성 그래프로 구성합니다. 각 작업의 준비 여부를 추적하고, 선행 작업이 완료될 때마다 새롭게 실행할 수 있는 작업을 계산합니다. 서로 독립적인 작업만 준비되는 즉시 병렬로 실행됩니다.

Labor0 자체의 새로운 코딩 에이전트를 만드는 대신, 개발자가 이미 사용하는 Codex, Claude Code, OpenCode를 그대로 실행합니다.

주요 기능은 다음과 같습니다.

- 요청을 bounded task와 dependency graph로 구성
- 선행 조건을 충족한 작업만 실행
- 독립적인 작업의 병렬 실행
- Codex, Claude Code, OpenCode 지원
- 일회성 managed cloud 환경에서 실행
- 모바일에서도 hosted 작업 시작 및 상태 확인
- Plan Mode에서 사용자의 판단이 필요하면 Web Push 전송
- 답변을 기다리는 동안 상태를 보존하고, 응답 후 기존 실행을 이어서 진행

중요하게 생각한 부분은 에이전트의 자율성과 사람의 판단을 함께 유지하는 것입니다.

Codex, Claude Code, OpenCode가 Plan Mode에서 사용자에게 질문하면 Labor0가 이를 Web Push로 전달합니다. 사용자는 노트북 앞에서 계속 기다리지 않고도 계획을 승인하거나, 수정을 요청하거나, 작업을 중단할 수 있습니다. 응답을 기다리는 작업은 상태를 유지하고, 지원되는 환경에서는 같은 provider conversation을 이어서 실행합니다.

현재 dependency-aware orchestration, managed cloud execution, 모바일 실행, Plan Mode Web Push를 사용할 수 있습니다. 로컬 실행은 구현되어 있지만 아직 내부 실험 단계이고, Slack과 Discord 연동은 베타입니다.

향후에는 L0 Nexus를 통해 사내 문서와 데이터 소스를 에이전트가 권한 범위 안에서 활용할 수 있게 할 예정입니다. 명백한 오류는 에이전트가 찾되, 중요한 판단은 스크린샷이나 로그처럼 검증 가능한 자료와 함께 사용자에게 묻는 QA 기능도 개발하고 있습니다.

Labor0는 **The AI Platform 제품군**의 새로운 엔지니어링 제품입니다. The AI Platform이 rooms, specialists, model routing, reusable workflows를 중심으로 협업을 구성한다면, Labor0는 소프트웨어 엔지니어링 작업을 dependency graph로 조율하는 다른 접근을 택했습니다. 두 제품을 더 직접적으로 연결하는 작업도 실험하고 있습니다.

출시 배경과 설계 방향은 아래 글에 정리했습니다.

<https://theaiplatform.app/blog/introducing-labor0/>

직접 사용해 보시고, dependency graph가 실제 개발 작업을 조율하는 데 얼마나 유용한지 의견을 주시면 감사하겠습니다.

## 원문
- [원문](https://labor0.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=32446)

## My Note
<!-- 한 줄 코멘트 남기기 -->

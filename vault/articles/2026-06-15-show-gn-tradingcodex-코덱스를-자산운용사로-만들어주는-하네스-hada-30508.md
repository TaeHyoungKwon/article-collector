---
category: AI
collected_at: '2026-06-15T19:13:16+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30508
id: hada-30508
matched_keywords:
- AI
- Codex
read: false
recommend_score: -995.307
recommended_on: '2026-06-15'
source: geeknews
tags:
- AI
- Other
- github.com/monarchjuno
title: 'Show GN: tradingcodex - 코덱스를 자산운용사로 만들어주는 하네스'
url: https://github.com/monarchjuno/tradingcodex
---

## TL;DR
- 이 글은 tradingcodex라는 하네스가 코덱스 플랫폼을 통해 자산운용사로 작동하도록 돕는 방식에 대해 설명한다.
- tradingcodex는 에이전트의 역할 구분과 안전한 주문 실행 구조를 통해 체계적이고 효율적인 투자 분석 및 실행을 지원한다.
- 독자는 이 시스템을 활용해 맞춤형 투자 전략을 개발하고 실행할 수 있으며, 보다 안전한 금융 운영이 가능함을 의미한다.

## GeekNews 요약
코덱스에서 바이브 코딩이 아닌, 바이브 인베스팅을 하기 위한 하네스입니다.

codex 설정파일(23skills, 9 subagent config, hooks) + django서버(mcp 기능 포함)로 구성되어있습니다.

1. 에이전트 구성  
   중앙에는 head manager 에이전트가 있습니다. 사용자 요청을 분석하고 어떤 서브 에이전트가 필요한지 정하고, 전체 workflow를 조율합니다.  
   메인 에이전트 밑에는 펀더멘털, 기술적 분석, 뉴스, 매크로, 상품 구조, 밸류에이션, 포트폴리오, 리스크, 실행 담당 서브 에이전트가 각자 맡은 범위 안에서 산출물을 만듭니다.
2. 리서치 메모리  
   tradingcodex는 분석 결과를 markdown 리포트, source snapshot, 기준 시점, handoff 기록으로 저장합니다. 사람이 읽을 수도 있으며 에이전트가 작업 전달, 복기, 중복 작업 방지 등으로 사용할 수 있습니다.
3. 투자전략을 strategy.md로 관리  
   예를 들어 배당 전략, 퀄리티 성장주 전략, 턴어라운드 전략, ETF 리밸런싱 전략 같은 것을 파일로 만들 수 있습니다. 그러나 이제는 수식이 아닌 md 파일로 사용합니다.  
   Strategy Creator 스킬로 나만의 전략을 에이전트와 만들고, 만들어진 전략은 ${strategy-name}으로 사용할 수 있습니다.
4. 차이니즈 월에서 착안한 information barrier  
   tradingcodex에는 금융권의 차이니즈 월 개념에서 착안한 information barrier가 있습니다.  
   모든 에이전트가 같은 정보를 다 보고, 같은 도구를 다 쓰는 구조가 아닙니다. 역할에 따라 볼 수 있는 정보, 사용할 수 있는 도구, 접근할 수 있는 파일, 실행할 수 있는 행동을 나눕니다.  
   예를 들어 리서치 담당 에이전트는 주문을 실행할 수 없고, 실행 담당 에이전트는 전략 판단을 마음대로 바꿀 수 없습니다. 전략 파일도 판단을 돕는 문서일 뿐, 정책을 우회하거나 승인 권한을 주지 않습니다.
5. Django 서버  
   이 서버는 에이전트, 스킬, 전략 파일, 리서치 문서, 포트폴리오 상태, 주문 티켓, 정책과 감사 기록을 관리합니다. 로컬 대시보드 기능도 제공합니다.
6. 안전한 execution 구조  
   tradingcodex는 에이전트가 멋대로 주문을 내게 하지 않습니다.  
   자체 tradingcodex\_mcp 레이어가 일종의 메자닌(개발자적 관점에서는 라우터) 역할을 합니다. 이 서버에는 각 브로커를 중앙화하여 관리하고  
   에이전트의 요청은 먼저 이 레이어를 통과합니다. 여기서 역할 권한, 정책, restricted symbol, 승인 여부, 주문 payload hash, 중복 요청 여부를 확인합니다.  
   execution은 항상 policy, approval, idempotency, audit trail을 거쳐야 합니다. Codex가 바로 브로커 MCP나 API를 호출해서 주문을 내는 구조가 아닙니다.

tradingcodex는 코덱스 위의 투자 도메인을 위한 하네스이자 OS입니다.  
그냥 써도 되지만 여러분들의 전략과 에이전트별 skill을 추가하여 커스터마이즈할 수 있습니다.

## 원문
- [원문](https://github.com/monarchjuno/tradingcodex)
- [GeekNews 토론](https://news.hada.io/topic?id=30508)

## My Note
<!-- 한 줄 코멘트 남기기 -->

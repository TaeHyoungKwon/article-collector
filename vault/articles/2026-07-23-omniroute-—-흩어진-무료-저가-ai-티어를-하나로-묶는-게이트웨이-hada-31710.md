---
category: AI
collected_at: '2026-07-23T09:31:01+09:00'
geeknews_comments: 2
geeknews_score: 10
geeknews_url: https://news.hada.io/topic?id=31710
id: hada-31710
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -991.273
recommended_on: '2026-07-24'
source: geeknews
tags:
- AI
- Other
- github.com/diegosouzapw
title: OmniRoute — 흩어진 무료/저가 AI 티어를 하나로 묶는 게이트웨이
url: https://github.com/diegosouzapw/OmniRoute
---

## TL;DR
- 이 글은 OmniRoute라는 플랫폼이 다양한 AI 티어와 코딩 툴을 통합하는 방식에 대해 다룬다.
- 이 플랫폼은 90개 이상의 무료 티어를 활용하여 연간 약 14억 개 무료 토큰을 제공하고, 효율적인 자원 관리를 통해 사용자의 비용을 절감한다.
- OmniRoute는 AI 도구를 통합 관리하여 개발자들에게 비용 효율적이고 편리한 작업 환경을 제공할 수 있는 가능성을 제시한다.

## GeekNews 요약
- 하나의 로컬 엔드포인트(`localhost:20128/v1`)로 **271개 프로바이더/500개 이상 모델**을 연결하고 Claude Code/Codex/Cursor/Cline/Copilot 등 26개 코딩 툴을 설정 하나로 사용
- **90개 이상 무료 티어/40개 이상 영구 무료** 계정을 통합해 월 약 14억 개 무료 토큰을 하나의 예산처럼 이용가능
- **자동 폴백으로 티어를 하나처럼 연결** — 이미 결제한 구독을 먼저 소진하고(안 쓰면 손해), 떨어지면 종량제 API → 저가 → 무료 순으로 자동 전환해 한도에 안 걸리고 계속 구동
  - 가격 오름차순이 아니라 "이미 확보한 자원부터 태우는" 순서로 동작, 순수 최저가 우선은 `cost-optimized`/`auto/cheap` 전략으로 별도 지정
- **RTK + Caveman 스택 압축**으로 요청당 토큰을 15~95%(툴 위주 세션 평균 약 89%) 절감, 코드/URL/JSON은 바이트 단위 원형 보존
- **Quota-Share**로 하나의 구독을 팀 여러 키에 분배, 유휴 몫은 대여하는 work-conserving 방식으로 한 명의 급증이 전체를 잠그지 않음
- **18가지 라우팅 전략**과 `auto` 무설정 스마트 라우팅(12요소 실시간 스코어링), `fusion`(패널+판정자), `pipeline`(단계 연결) 등 지원
- **3계층 자가 복구**(프로바이더 서킷 브레이커 / 연결 쿨다운 / 모델 락아웃)로 장애 유형별 대응, 다운타임 최소화
- **MCP(104개 툴)/A2A(JSON-RPC 2.0)** 프로토콜로 에이전트가 게이트웨이를 자율 제어 가능
- **로컬 우선** 구조: 키는 AES-256-GCM 암호화, 텔레메트리 제로, 계정/가입 불필요, 프롬프트 인젝션 가드 내장
- Web/Desktop(Electron)/Android(Termux)/PWA 다중 플랫폼, 43개 로케일 지원
- 설치: `npm install -g omniroute`
- MIT 라이선스

## 원문
- [원문](https://github.com/diegosouzapw/OmniRoute)
- [GeekNews 토론](https://news.hada.io/topic?id=31710)

## My Note
<!-- 한 줄 코멘트 남기기 -->

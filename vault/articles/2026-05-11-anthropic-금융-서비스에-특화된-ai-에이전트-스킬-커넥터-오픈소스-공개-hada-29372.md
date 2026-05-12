---
category: AI
collected_at: '2026-05-11T10:01:02+09:00'
geeknews_comments: 4
geeknews_score: 19
geeknews_url: https://news.hada.io/topic?id=29372
id: hada-29372
matched_keywords:
- AI
- LLM
read: false
recommend_score: -992.521
recommended_on: '2026-05-11'
source: geeknews
tags:
- AI
- Other
- github.com/anthropics
title: Anthropic, 금융 서비스에 특화된 AI 에이전트/스킬/커넥터 오픈소스 공개
url: https://github.com/anthropics/financial-services
---

## TL;DR
- Anthropic이 금융 서비스에 특화된 AI 에이전트 및 스킬을 오픈소스로 공개했다.
- 10종의 워크플로우 에이전트와 11개 금융 데이터 제공업체 커넥터를 통해 자동화된 금융 업무 처리를 지원한다.
- 이 기술은 금융 분야의 업무 효율성을 높이고, 사용자 맞춤형 솔루션을 제공할 수 있는 가능성을 제시한다.

## GeekNews 요약
- **Claude Cowork 플러그인** 또는 **Managed Agents API** 두 가지 방식으로 동일한 에이전트를 실행할 수 있는 금융 서비스 워크플로우 자동화 레퍼런스 레포지토리
- 투자은행, 주식 리서치, 사모펀드, 자산관리 등 주요 금융 분야를 커버하는 **10종의 워크플로우 에이전트** 포함
  - **Pitch Agent**: Comps, 선례 거래, LBO를 기반으로 **브랜딩된 피치 덱**을 엔드 투 엔드로 생성
  - **Meeting Prep Agent**: 모든 고객 미팅 전 **브리핑 팩** 자동 작성
  - **Market Researcher**: 섹터 또는 테마를 입력하면 산업 개요, 경쟁 구도, 피어 비교, 아이디어 숏리스트 생성
  - **Earnings Reviewer**: 어닝 콜 + 공시 자료를 기반으로 모델 업데이트 후 노트 초안 작성
  - **Model Builder**: DCF, LBO, 3-statement, Comps 모델을 **Excel에서 실시간** 작업
  - **Valuation Reviewer**: GP 패키지를 수집하고 밸류에이션 템플릿을 실행해 LP 보고 스테이징
  - **GL Reconciler**: 불일치(break)를 찾아 근본 원인을 추적하고 승인 라우팅
  - **Month-End Closer**: 발생 기준 처리, 롤포워드, 차이 분석 코멘터리
  - **Statement Auditor**: 배포 전 LP 재무제표 감사
  - **KYC Screener**: 온보딩 문서 파싱, 규칙 엔진 실행, 누락 항목 플래그
- **11개 금융 데이터 제공업체 MCP 커넥터**를 코어 플러그인에서 중앙 관리: Daloopa, Morningstar, S&P Global, FactSet, Moody's, LSEG, PitchBook, Chronograph 등
- `/comps`, `/dcf`, `/lbo`, `/earnings`, `/ic-memo` 등 **슬래시 명령어**로 비교 기업 분석, DCF 밸류에이션, IC 메모 작성 등을 즉시 실행 가능
- 7개 **Vertical 플러그인**(financial-analysis, investment-banking, equity-research, private-equity, wealth-management, fund-admin, operations)과 LSEG·S&P Global 파트너 플러그인으로 세분화
- 각 에이전트는 필요한 스킬을 **자체 번들링하는 자기 완결형 구조**로, 에이전트 하나만 설치하면 관련 스킬이 모두 포함됨
- 모든 출력물은 **사람의 검토·승인을 위한 초안**이며, 투자 추천·거래 실행·원장 기록 등은 수행하지 않음
- **Microsoft 365 애드인 프로비저닝 도구**도 포함되어, Excel·PowerPoint·Word·Outlook에서 Vertex AI, Bedrock, 내부 LLM 게이트웨이를 통해 Claude 실행 가능
- `.mcp.json` 커넥터 교체, 스킬 파일에 사내 용어·프로세스 추가, 브랜딩 PPT 템플릿 학습 등 **각 회사 환경에 맞춘 커스터마이징** 지원
- 전체가 **Markdown + JSON 파일 기반**으로 빌드 스텝 없이 구성
- Apache 2.0 라이선스

## 원문
- [원문](https://github.com/anthropics/financial-services)
- [GeekNews 토론](https://news.hada.io/topic?id=29372)

## My Note
<!-- 한 줄 코멘트 남기기 -->

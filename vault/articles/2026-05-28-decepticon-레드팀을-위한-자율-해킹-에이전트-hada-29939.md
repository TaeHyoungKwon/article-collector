---
category: AI
collected_at: '2026-05-28T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 14
geeknews_url: https://news.hada.io/topic?id=29939
id: hada-29939
matched_keywords:
- AI
read: false
recommend_score: 4.708
source: geeknews
tags:
- AI
- Other
- github.com/PurpleAILAB
title: Decepticon - 레드팀을 위한 자율 해킹 에이전트
url: https://github.com/PurpleAILAB/Decepticon
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **자율형 레드팀 에이전트**로, nmap 실행 후 보고서를 출력하는 수준의 데모와 차별화된 **전문 레드팀 운영** 수행
- 실제 적대자가 수행하는 방식의 공격 체인 실행 - **정찰, 익스플로잇, 권한 상승, 측면 이동, C2**
- 패킷 송출 전 **RoE, ConOps, Deconfliction Plan, OPPLAN**으로 구성된 완전한 교전 패키지 생성, **MITRE ATT&CK 매핑** 포함
- **실제 인터랙티브 셸 지원**
  - `msfconsole`, `sliver-client`, `evil-winrm` 등 인터랙티브 도구를 **영구 tmux 세션**에서 실행
  - **자동 프롬프트 감지**로 우회 없이 후속 명령 전송
- **강화된 샌드박스 격리**
  - 모든 명령이 **Kali Linux 샌드박스** 내부에서 실행
  - 작전망(`sandbox-net`)과 관리망(`decepticon-net`) 분리한 이중 네트워크 구조
  - **LangGraph**가 Docker 소켓 통해 샌드박스 구동
- **16개 전문 에이전트** 킬체인 단계별 구성, 목표별 신규 컨텍스트 윈도우로 누적 노이즈 제거
  - Orchestration, Reconnaissance, Exploitation, Post-Exploitation, Vulnerability Research
  - Domain Specialists: AD, Cloud, Smart Contracts, Reversing, Analyst
- **티어 기반 자격증명 인지형 폴백 체인**으로 보유 자격증명 우선순위에 따라 primary→fallback 자동 구성
  - **eco** (기본): 에이전트별 차등 티어, 프로덕션용
  - **max**: 전 에이전트 HIGH 티어, 고가치 타깃용
  - **test**: 전 에이전트 LOW 티어, 개발/CI용
- 지원 프로바이더: **Anthropic, OpenAI, Google Gemini, MiniMax, DeepSeek, xAI, Mistral, OpenRouter, Nvidia NIM, Ollama**
- 지원 OS: macOS (Apple Silicon + Intel), Linux (amd64 + arm64), Windows (WSL2만, 네이티브 Windows는 미지원)
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/PurpleAILAB/Decepticon)
- [GeekNews 토론](https://news.hada.io/topic?id=29939)

## My Note
<!-- 한 줄 코멘트 남기기 -->

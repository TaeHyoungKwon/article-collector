---
category: AI
collected_at: '2026-06-04T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30158
id: hada-30158
matched_keywords:
- AI
read: false
recommend_score: 3.386
source: geeknews
tags:
- AI
- Other
- agentexecutor.io
title: Agent Executor - Google의 분산 에이전트 런타임 오픈소스
url: https://agentexecutor.io/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 신뢰성/안전성/커스터마이징/효율성을 목표로 설계된 **분산 에이전트 런타임**으로, 에이전틱 루프를 조율하고 이벤트 로깅으로 실행을 관리하며 로컬·원격 액터와 통신
- 컨트롤러·스킬·도구·에이전트를 **격리된 액터**로 실행하고, 실패·중단 시 **자동 복구·재개**를 네이티브로 지원
- 도구·스킬과 특정 도메인·워크플로용 **목적 특화 에이전트**로 런타임을 완전히 **커스터마이징** 가능
- **Single-Writer 아키텍처**와 **이벤트 로그**로 일관된 상태 관리와 내구성 있는 실행 상태 확보
  - 클라이언트 연결이 끊기면 마지막 시퀀스 번호로 누락 이벤트만 재생, 대화는 되돌리지 않음
- 프롬프트 기반 텍스트 생성용 **내장 Gemini 에이전트** 포함 (AI Studio 또는 Vertex AI 인증)
- **모델·하니스 비종속** 구조로 소규모·대규모 배포 모두 확장 가능, 실행·내구성·조율은 **AX가 하부에서 처리**
- **Kubernetes 네이티브**: **Agent Substrate** 위에서 동작하도록 설계되어 Kubernetes에 최적화
- **MCP·A2A** 등 에이전틱 프로토콜을 네이티브 지원해, 생태계 전반의 도구·에이전트와 상호운용 가능
- 모든 실행에 대한 전체 **감사 추적(audit trail)**, 관측 훅, 트라젝토리 수집 제공
- CLI 도구(`ax`)로 이용
  - `exec`(실행·재개), `serve`(gRPC 컨트롤러 구동), `fork`(체크포인트 분기), `trace`(Web UI 트레이스 시각화) 등 **CLI 서브커맨드** 제공
- 현재 **얼리 프리뷰**로, 안정 릴리스 전까지 대규모 호환성 변경 예정
- Apache 2.0 라이선스

## 원문
- [원문](https://agentexecutor.io/)
- [GeekNews 토론](https://news.hada.io/topic?id=30158)

## My Note
<!-- 한 줄 코멘트 남기기 -->

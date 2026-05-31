---
category: AI
collected_at: '2026-05-31T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30032
id: hada-30032
matched_keywords:
- AI
- LLM
- Codex
read: false
recommend_score: 6.693
recommended_on: '2026-05-31'
source: geeknews
tags:
- AI
- Other
- clawpatrol.dev
title: Claw Patrol - 에이전트를 위한 보안 방화벽
url: https://clawpatrol.dev/
---

## TL;DR
- Claw Patrol은 에이전트를 위한 보안 방화벽으로, 트래픽을 검사하고 액세스를 게이팅하는 기능을 제공한다.
- 기존 권한 체계의 한계를 보완하며, 에이전트가 소유한 자격 증명을 안전하게 보관하고 다양한 작동 환경에서 전체 감사 로그를 제공하는 점이 가장 주목할 만하다.
- 이는 데이터 보안과 접근 관리를 개선하여 프로덕션 환경에서의 리스크를 줄이는데 기여할 수 있다.

## GeekNews 요약
- 에이전트에게 **프로덕션 접근 권한**을 주면서도 안심할 수 있도록, 에이전트 자격 증명을 대신 보관하고 트래픽을 와이어 레벨에서 파싱하며 사용자가 작성한 규칙으로 모든 액션을 게이팅하는 **에이전트용 보안 방화벽**
- 기존 권한 체계의 한계를 보완하는 **액션 컨트롤 레이어**
  - OAuth 스코프, IAM 역할, k8s RBAC는 "어디에 접근 가능한가"만 결정 - Postgres에 접속 가능한 에이전트는 `SELECT`만큼 쉽게 `DROP TABLE` 실행 가능
  - 프롬프트 인젝션으로 에이전트가 침해당하면 가진 자격 증명도 함께 유출 → 키는 에이전트가 절대 볼 수 없는 곳에 보관
  - Postgres·Kubernetes·GitHub·Slack 등으로 부채꼴처럼 확산되는 에이전트 작업의 **전체 감사 로그**를 한 곳에서 제공
- **WireGuard 또는 Tailscale**로 연결, 에이전트 자체에는 변경 사항 없음 — `clawpatrol join`으로 게이트웨이 가입, `clawpatrol run codex`로 실행
- 룰 엔진이 모든 아웃바운드 요청을 목적지 도달 전에 검사, URL뿐 아니라 **HTTP 메서드·SQL 동사·k8s 리소스·플러그인 facet** 단위로 매칭, 대시보드에서 저장하면 다음 요청부터 **핫 리로드**
  - HTTP: 메서드, 경로, 헤더, 본문 매칭 후 LLM 판사(Judge)로 라우팅 가능 (예: 고객 지원 답변에서 공격적 콘텐츠·인사말 누락·부적절 마크다운 차단)
  - SQL: Postgres·ClickHouse 트래픽을 **동사 단위로 파싱**, 함수명·테이블·구문 부분 문자열로 매칭 (예: `pg_read_file`, `dblink_*` 같은 파일시스템 접근 함수 차단)
  - Kubernetes: 네임스페이스·리소스·동사·이름으로 매칭, `kubectl exec`의 명령 argv를 LLM 저지가 읽어 `ls`/`ps`/`df`는 허용·env 덤프·파드 토큰 접근은 거부
- 모호한 요청에 대한 **승인 흐름(Approval flows)** 제공
  - **LLM 판사(Judge)(`require_llm`)**: 커스텀 프롬프트를 가진 모델이 각 요청에 투표, 판정은 캐시되어 재과금 방지 (예: claude-haiku-4-5로 시크릿 컬럼 SELECT 거부)
  - **Human In The Loop(`require_human`)**: Slack·대시보드·자체 webhook에서 사람이 투표, 응답자 없으면 타임아웃 시 자동 거부
- 배포 전 **회귀 테스트** 지원 - 대시보드에서 실제 액션을 녹화해 JSON fixture로 저장, CI에서 `clawpatrol test` 실행 시 정책 변경으로 판정이 뒤집히면 diff를 출력하고 빌드 실패
- 단일 바이너리로 동작, 게이트웨이·DB·인증 없이 HCL 로드 후 fixture를 룰 엔진에 재생해 판정 일치 단언
- 다른 도구들과의 차별점 — 대부분 한쪽 면만 다루지만 Claw Patrol은 **네 가지를 모두 커버**
  - **Watch LLM calls** (Helicone, Portkey, LiteLLM, NeMo Guardrails, Lakera Guard 등): LLM 응답 이후 에이전트 행동은 시야 밖
  - **Watch tool calls** (Crab Trap, httpjail, proxyline 등): HTTP만 지원, Postgres·k8s·SSH는 우회
  - **Sandbox the process** (NVIDIA OpenShell, agentsh): 무엇을 만질 수 있는지만 제한, 각 액션의 합리성은 판단 안 함
  - **Hold the keys** (Agent Vault, Clawvisor): 시크릿은 외부에 있지만 요청 내용 자체는 통과
  - Claw Patrol은 프로토콜 레이어 도구 호출 감시 + 시크릿 보관 + 위험 호출을 사람/LLM 저지로 라우팅 + 전체 바이트 기록을 동시 제공
- 데모는 `demo.clawpatrol.dev`에서 운영자 UI 워크스루 직접 체험 가능, 요청 단위 드릴다운으로 게이트웨이 캡처 내용 확인
- 지원 대상: Postgres, ClickHouse, Kubernetes, AWS, GCP, GitHub, Slack, Vultr 등 다양한 프로덕션 시스템 / Claude, Codex, OpenClaw 등 주요 에이전트
- 설치는 `curl -fsSL https://clawpatrol.dev/install.sh | sh` 한 줄, GitHub [denoland/clawpatrol](https://github.com/denoland/clawpatrol)
- **MIT 라이선스 오픈소스**

## 원문
- [원문](https://clawpatrol.dev/)
- [GeekNews 토론](https://news.hada.io/topic?id=30032)

## My Note
<!-- 한 줄 코멘트 남기기 -->

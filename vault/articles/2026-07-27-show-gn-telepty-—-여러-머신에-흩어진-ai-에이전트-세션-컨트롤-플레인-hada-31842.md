---
category: AI
collected_at: '2026-07-27T07:52:04+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31842
id: hada-31842
matched_keywords:
- backend
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 10.901
recommended_on: '2026-07-27'
source: geeknews
tags:
- AI
- Other
- github.com/dmsdc-ai
title: 'Show GN: telepty — 여러 머신에 흩어진 AI 에이전트 세션 컨트롤 플레인'
url: https://github.com/dmsdc-ai/aigentry-telepty
---

## TL;DR
- telepty는 여러 머신에서 AI CLI 세션을 원격으로 관리할 수 있는 경량 세션 컨트롤 플레인입니다.
- 이 도구는 세션 간의 지시 전파와 진행 확인을 자동화하여 사용자의 노력을 줄이며, Tailscale을 이용해 보안을 강화합니다.
- 개발자들은 telepty를 통해 효율적이고 안전하게 AI 에이전트를 운영할 수 있으며, 이는 다중 세션 관리를 혁신적으로 변화시킬 수 있습니다.

## GeekNews 요약
telepty는 여러 머신에서 돌아가는 터미널 AI CLI 세션(claude, codex, gemini 등)에 원격으로 지시를 보내고 화면을 읽을 수 있게 해주는 경량 **에이전트 세션 컨트롤 플레인**입니다 — 추론과 작업은 각 에이전트가 그대로 수행하고(data plane), telepty는 그 세션들을 주소로 부르고 전달을 보장하는 층만 담당합니다(PTY 기반 백그라운드 데몬 + 세션 브리지). 세션마다 이름 기반 주소를 부여하고, 지시가 실제로 접수됐는지까지 확인하며, macOS·Linux·Windows를 지원합니다. 크로스머신 전송은 직접 만들지 않고 **이미 검증된 Tailscale(WireGuard) 위에 올렸습니다** — 키 교환·NAT 트래버설·암호화를 새로 구현해 공격면을 늘리는 대신, 수년간 실전 검증된 계층에 위임하는 쪽을 골랐습니다. MIT 라이선스 오픈소스입니다.

```
npm i -g @dmsdc-ai/aigentry-telepty && telepty daemon start  
  
# 이미 쓰던 CLI를 그대로 감싸 이름 붙은 세션으로 만듭니다 (각 머신에서 한 번씩)  
telepty allow --id orchestrator claude    # 이 머신의 claude 세션 → "orchestrator"  
  
telepty inject "backend@100.x.y.z" "인증 미들웨어 리팩터링 시작해줘"   # 원격 세션에 지시  
telepty read-screen "backend@100.x.y.z"                               # 진행 상황 확인  
telepty broadcast "작업 마무리하고 상태 보고해줘"                      # 전체 세션에 공지
```

#### 배경

AI CLI 세션을 여러 개, 여러 머신에 걸쳐 운용하는 개발이 흔해졌습니다. 실행은 세션 수만큼 병렬로 확장되지만, 세션 사이의 전달 — 지시 전파, 진행 확인, 결과 회수 — 은 여전히 사람이 터미널을 오가며 수행합니다. 이 도구의 출발점도 그 병목이었습니다: 세 대의 머신에서 세 개의 AI CLI 세션을 동시에 돌려 보니, 실행보다 지시와 결과를 나르는 "전달" 단계가 먼저 사람에서 막혔습니다.

- **기존**: 터미널 3개를 오가며 포커스 전환 → 지시 복사-붙여넣기 → 진행 확인을 세션마다 반복
- **telepty**: 터미널 1곳에서 `이름@호스트` 주소로 지시를 주입하고 화면을 회수

기존 도구는 이 계층을 채우지 못합니다. tmux/SSH는 세션에 "붙는" 도구라 보내고 확인하는 작업은 여전히 수동이고, 에이전트 프레임워크는 기존 세션과 워크플로우를 자기 방식으로 재작성할 것을 요구합니다. telepty는 그 사이 — 이미 돌아가는 세션을 그대로 두고 전달만 인프라로 내리는 — 얇은 계층을 목표로 합니다.

#### 설계

- **이름으로 세션 지목** — 모든 세션을 `<세션이름>@<호스트>`로 부릅니다. 대상이 어느 머신, 어떤 OS에 있는지 신경 쓸 필요가 없습니다.
- **"보냄"과 "받음"을 구분** — 수신 세션이 작업 중이면 메시지를 큐(mailbox)에 보관하고, 실제로 접수된 시점을 터미널 렌더 상태로 판정해 확정합니다. 보내 놓고 사람이 다시 확인할 필요가 없습니다.
- **데몬을 재시작해도 세션은 유지** — 세션을 쥔 프로세스(bridge)와 라우팅 데몬(daemon)이 분리되어 있어, 데몬 업그레이드가 진행 중인 작업을 끊지 않습니다.
- **전송은 검증된 계층에 위임** — 자체 P2P 프로토콜을 만들지 않았습니다. Tailscale이 있으면 데몬이 tailnet IP를 자동 감지해 그 위에서 바로 붙습니다: 포트 개방 0, 인증서 관리 0, 방화벽 규칙 0. tailnet이 없는 환경은 SSH 터널(`telepty connect user@host`)로 붙습니다 — 어느 쪽이든 암호화와 신원은 이미 검증된 도구가 책임지고, telepty는 그 위에서 세션 주소화와 전달만 합니다.

명령은 `inject` / `read-screen` / `attach` / `send-key` / `broadcast` / `list` 여섯 개로, CLI가 곧 API라 쉘 스크립트에서 바로 조합할 수 있습니다. 그리고 **사람만 쓰라고 만든 게 아닙니다** — Claude Code·Codex·Gemini CLI용 스킬 9종이 패키지에 포함돼 있어(내장 인스톨러로 설치), **에이전트 자신이 telepty를 도구로 씁니다**: 세션을 조회하고, 다른 머신의 에이전트에게 지시를 보내고, 화면을 읽어 옵니다. 아래 데모의 릴레이가 정확히 그 장면입니다 — 사람이 아니라 각 LLM이 직접 `telepty inject`를 실행합니다.

#### 초기 참조 지표 (0.6.11 빌드 측정 — 현재 릴리스 0.7.1 · 네트워크 왕복·PTY 초기화 오버헤드 포함)

- busy 세션 대상 gated inject의 큐잉→접수 확정: Linux 약 487ms · Windows 약 1.2s — 더 많은 측정을 쌓는 중이며, 중요한 건 숫자보다 **HTTP 수락이 아닌 수신 측 ACK 착지를 접수 기준으로 삼는다**는 점입니다.
- macOS·Linux·Windows 3-OS 크로스머신 전달을 같은 기준으로 확인했습니다.

#### 보안

데몬은 **localhost(127.0.0.1)와 tailnet 전용 IP에만 바인드**됩니다 — `0.0.0.0` 노출이 없어 tailnet 밖에서는 포트 스캔으로도 도달할 수 없습니다. tailnet 피어만 신뢰하며, PTY에 쓰는 권한은 세션을 소유한 사용자 범위를 넘지 않습니다. 0.7.1부터는 **브라우저에서 온 요청을 명시적으로 거부**합니다 — 사용자가 방문한 웹페이지가 localhost의 제어 API나 WebSocket으로 세션에 접근하는 경로를 차단했습니다(허용 오리진 기본값 없음).

#### 한계

beta입니다. CLI별 렌더링 엣지케이스가 남아 있고, Windows는 beta 딱지가 붙어 있습니다. 터미널 에뮬레이션을 하지 않기 때문에 `read-screen`은 셀 그리드가 아니라 출력 스트림의 끝부분을 돌려줍니다 — 리페인트가 잦은 TUI에서는 같은 프레임이 반복돼 보일 수 있습니다. 알려진 항목은 README의 Limitations 섹션에 정리되어 있습니다.

#### 링크

- GitHub: <https://github.com/dmsdc-ai/aigentry-telepty>
- README 데모: **3개 머신(macOS·Linux·Windows)의 3개 LLM(Grok·Codex·Claude)이 telepty inject를 직접 실행하며 서로에게 릴레이**하는 장면 — 각 화면은 원본 CLI TUI를 `attach`로 라이브 캡처한 것입니다. 같은 명령이 한 머신 안의 세션 간에도 그대로 동작합니다(동일 머신 릴레이 데모 포함).
- npm: `@dmsdc-ai/aigentry-telepty` (MIT, 0.7.1)

여러 AI CLI 세션을 운용하시는 분들의 전달 계층 해법이 궁금합니다. 피드백 주시면 반영하겠습니다.

## 원문
- [원문](https://github.com/dmsdc-ai/aigentry-telepty)
- [GeekNews 토론](https://news.hada.io/topic?id=31842)

## My Note
<!-- 한 줄 코멘트 남기기 -->

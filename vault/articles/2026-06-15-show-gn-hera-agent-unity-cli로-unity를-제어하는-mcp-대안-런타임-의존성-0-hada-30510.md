---
category: AI
collected_at: '2026-06-15T21:28:33+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30510
id: hada-30510
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 9.099
recommended_on: '2026-06-15'
source: geeknews
tags:
- AI
- Other
- github.com/NotNull92
title: 'Show GN: hera-agent-unity - CLI로 Unity를 제어하는 MCP 대안 (런타임 의존성 0)'
url: https://github.com/NotNull92/hera-agent-unity
---

## TL;DR
- 이 글은 hera-agent-unity라는 CLI 도구를 소개하며, Unity 에디터를 실시간으로 제어하는 방식에 대해 설명한다.
- 해당 도구는 AI가 추측하는 대신 직접 Unity에서 코드를 실행하고 결과를 반환하여 개발 효율성을 높인다.
- 개발자는 프로토타입 제작과 UI 디자인을 더욱 간편하게 진행할 수 있으며, 모든 기능을 무료로 이용할 수 있다.

## GeekNews 요약
- LLM은 여러분의 프로젝트를 모르고, 작년에 학습한 Unity API와 뭉뚱그린 패턴을 기억할 뿐입니다. hera-agent-unity는 AI가 코드를 넘겨짚기 전에 **살아있는 Unity 에디터에서 직접 실행하고 결과를 가져오게** 해줍니다 — 추측 대신 실측
- **Go 바이너리 1개 + C# UPM 패키지 1개, 런타임 의존성 0개.** Unity 에디터를 켜면 localhost HTTP로 이미 연결되어 있음. Python·WebSocket·JSON-RPC 없음
- Claude Code, Codex, Cursor 등 **셸 명령을 실행할 수 있는 모든 AI 에이전트**에서 동작 (특정 MCP 클라이언트에 묶이지 않음)

### 무엇을 할 수 있나

- **exec** — Unity 내부에서 임의의 C# 실행 (에디터 + 런타임 풀 액세스). Roslyn으로 컴파일 후 캐시, 같은 코드는 즉시 재실행
- **console / scene / test / profiler** — 실제 콘솔 로그를 종류별로 읽고, 씬을 조작하고, PlayMode 테스트를 돌리고, 프로파일러를 터미널에서 읽음
- **describe\_type / find\_method / unity\_docs** — 살아있는 어셈블리를 리플렉션으로 들여다보고, 31,581개 Unity 6 ScriptReference를 **오프라인으로** 조회 (패키지에 내장, 네트워크·rate limit 없음)
- **manage\_gameobject / components / prefab / material / ui** — GameObject·컴포넌트·프리팹·머티리얼·uGUI를 C# 보일러플레이트 없이 API로 편집
- **batch** — 여러 명령을 한 번의 HTTP 왕복으로 원자적 실행 (CI·자동화용)
- **커스텀 툴** — `[HeraTool]` 어트리뷰트를 단 C# 클래스를 두면 자동 발견 (등록·코드젠 불필요)

### 최근 플래그십 — UI 목업 → 라이브 Unity UI (ui\_doc)

- AI가 가장 약한 영역이 UI(uGUI의 anchor/pivot/레이아웃). ui\_doc은 에이전트가 **HTML 모양 JSON IR**로 설계하면 Hera가 실제 uGUI로 정확히 번역
- **"추측 대신 실측" 루프**: 레퍼런스 스크린샷에서 색 측정(sample) → IR 작성 → 적용(apply) → 렌더(capture) → 비교 → 수정. 사람 개입 없이 스크린샷 한 장으로 게임 HUD를 재현
- 외부 의존성 0 절차적 스프라이트 생성, `com.unity.ugui` 컴파일타임 의존성 0

### MCP와 비교

- 설치: Python + uv + FastMCP + 설정 파일 → **단일 바이너리**
- 프로토콜: JSON-RPC over stdio → **직접 HTTP POST**
- 도메인 리로드: 복잡한 재연결 로직 → **스테이트리스 (파일시스템 버스)**
- 호환성: MCP 클라이언트 전용 → **어떤 셸·에이전트·스크립트도**

Unity 6 (6000.0+) 지원, MIT 라이선스로 전 기능 무료. 기존 hera-agent(무료) + hera-agent-pro(상용)의 통합 후속작으로, 모든 Pro 기능이 MIT로 풀렸습니다.

## 원문
- [원문](https://github.com/NotNull92/hera-agent-unity)
- [GeekNews 토론](https://news.hada.io/topic?id=30510)

## My Note
<!-- 한 줄 코멘트 남기기 -->

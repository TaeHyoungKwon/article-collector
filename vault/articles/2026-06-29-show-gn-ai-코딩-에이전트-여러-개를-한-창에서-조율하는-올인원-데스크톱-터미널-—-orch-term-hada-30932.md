---
category: AI
collected_at: '2026-06-29T11:05:55+09:00'
geeknews_comments: 4
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=30932
id: hada-30932
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -991.908
recommended_on: '2026-06-29'
source: geeknews
tags:
- AI
- Other
- zendy00.github.io
title: 'Show GN: AI 코딩 에이전트 여러 개를 한 창에서 조율하는 올인원 데스크톱 터미널 — Orch term'
url: https://zendy00.github.io/orch-term-pages/
---

## TL;DR
- 이 글은 AI 코딩 에이전트를 통합하여 여러 작업 환경을 조율할 수 있는 데스크톱 앱, Orch term을 소개합니다.
- 사용자는 여러 AI 에이전트를 동시에 운용하며 효율적으로 코드 개발 및 관리를 진행할 수 있습니다.
- 이 앱은 개발과 협업의 방식에 변화를 가져오며, AI와의 상호작용을 통해 생산성을 높일 수 있는 가능성을 제공합니다.

## GeekNews 요약
터미널·코드 에디터·브라우저·Git을 한 창에 담고, 그 위에서 여러 AI 코딩 에이전트(Claude Code, Codex, Gemini CLI 등)를 동시에 돌려 조율하는 데스크톱 앱입니다. Windows와 macOS를 지원합니다.

왜 만들었나

AI 에이전트로 개발하다 보니, 터미널 하나에 에이전트 하나만 붙여 쓰는 게 답답했습니다. 에이전트가 작업하는 동안 코드를 보려면 에디터를, 결과 화면은 브라우저를, 변경분은 Git 도구를 따로 오가야 했습니다. 이 모든 걸 한 창에 모으고, 나아가 에이전트 여러 명을 각자 격리된 작업공간에서 돌려 한 화면에서 조율하는 환경을 직접 만들기로 했습니다.

올인원 워크스페이스

- 화면을 자유롭게 분할(이진 분할 트리)하고 각 칸에 터미널·에디터·브라우저 탭을 섞어 배치
- "Space"로 작업 묶음 전환
- 내장 코드 에디터(여러 인코딩·줄바꿈 지원), ripgrep 기반 전체 검색(Ctrl+Shift+F)
- Source Control 패널: 커밋 로그·그래프·blame·diff·push/pull
- iframe이 아닌 네이티브 자식 웹뷰 기반 인앱 브라우저
- Space별 할 일 보드(칸반: 할 일·완료) — 작업 단위로 todo를 정리

할 일(TODO) — 사람과 AI가 함께 관리

- 각 Space에 칸반식 할 일 보드가 있어 작업을 직접 정리
- 앱 안의 AI 에이전트가 MCP로 같은 할 일 보드를 직접 읽고 쓸 수 있음 — 에이전트가 자기 작업의 진행 상태를 todo로 갱신하고, 사람은 그걸 그대로 보며 조율
- 즉, 할 일 목록이 사람과 에이전트의 공통 작업판이 됩니다

멀티 에이전트 오케스트레이션

- 워커 에이전트들을 각각 격리된 git worktree에 띄워 병렬 작업
- 한 워커가 막히면 다른 워커에게 위임하고 결과를 되돌림
- 인앱 브라우저를 에이전트와 함께 보는 미러링

AI 게이트웨이

- 앱 안의 AI 에이전트를 로컬 HTTP API(OpenAI 호환 형태)로 노출 — 외부 스크립트·도구가 에이전트를 그대로 호출
- 모든 요청/응답은 날짜별 감사 로그로 기록

기술 스택

Tauri 2(Rust 백엔드) + TypeScript·Vite, 터미널은 xterm.js(WebGL 렌더러), 저장소는 SQLite, 자동 업데이트 내장.

개발하며 어려웠던 점

- Tauri 네이티브 자식 웹뷰(unstable)로 인앱 브라우저 구현 — 동기 커맨드가 메인 스레드를 데드락시키는 함정, 창 복귀 후 키보드 입력이 끊기는 포커스 버그(결국 wry를 직접 패치)
- conpty 환경의 한글 IME·이모지 입력, alt+tab 복귀 시 중복 입력 같은 입력단 버그
- Windows·macOS 양립 — 한 OS를 고치다 다른 OS를 깨뜨리지 않도록 모든 분기를 게이트

다운로드 / 체험

- 소개·다운로드: <https://zendy00.github.io/orch-term-pages/>
- 받기: <https://zendy00.github.io/orch-term-pages/download.html> (Windows 설치 관리자/MSI, macOS DMG·한 줄 설치)
- 아직 코드 서명 전이라 Windows SmartScreen·macOS Gatekeeper 경고가 뜹니다.

## 원문
- [원문](https://zendy00.github.io/orch-term-pages/)
- [GeekNews 토론](https://news.hada.io/topic?id=30932)

## My Note
<!-- 한 줄 코멘트 남기기 -->

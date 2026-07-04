---
category: Dev Tools
collected_at: '2026-07-04T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31104
id: hada-31104
matched_keywords:
- Claude Code
read: false
recommend_score: 2.693
source: geeknews
tags:
- Dev Tools
- Other
- github.com/ljtn
title: epiq - Git 기반 분산형 로컬 CLI 네이티브 이슈 트래커
url: https://github.com/ljtn/epiq
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **터미널 네이티브 이슈 트래커**. 이슈 트래킹을 에디터/터미널 안으로 가져와 잦은 컨텍스트 전환을 없앰
- **로컬 우선(local-first)**: 계정/SaaS/외부 서비스 없이 동작하고, 상태를 로컬에 저장해 편집이 즉시 반영됨
- **Git 백업·버전 관리**: 모든 변경을 추적/복구, worktree를 활용해 동기화가 일반 개발 워크플로우와 격리됨
  - `:sync`로 로컬 상태와 원격 상태 간 변경 동기화, 수동 Git 명령 필요없음
- **터미널 TUI + 브라우저 GUI** 이중 인터페이스를 동일한 Git 기반 이벤트 엔진으로 구동
- **vim 스타일 키보드 UX** 제공, `h` `j` `k` `l` 이동과 `:` 명령줄 모드, `?` command palette로 전체 명령 보기 지원
  - `:new issue|swimlane|board`로 노드 생성, `:comment`·`:close`·`:reopen`·`:filter` 등 컨텍스트 인식형 명령 지원
- **Time travel** 기능으로 1시간/1주/1년 전 앱 상태 보기 지원
- **이벤트 소싱 모델**로 병합 충돌 방지
  - 모든 변경을 사용자별 append-only 이벤트로 저장, 시간 정렬 가능한 ULID와 마지막 이벤트("edge") 참조로 결정적 순서 재생
  - 이벤트는 멱등(idempotent) 설계, 충돌 시 나중 이벤트 우선, 각 사용자가 자신의 로그 파일에 기록해 Git 병합이 독립 파일의 단순 결합으로 처리
- **MCP 서버**(`epiq-mcp` 바이너리)로 에이전트 연동도 지원, `claude mcp add`로 Claude Code에 등록 가능

## 원문
- [원문](https://github.com/ljtn/epiq)
- [GeekNews 토론](https://news.hada.io/topic?id=31104)

## My Note
<!-- 한 줄 코멘트 남기기 -->

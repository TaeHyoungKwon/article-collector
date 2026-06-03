---
category: AI
collected_at: '2026-06-03T13:07:52+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30140
id: hada-30140
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
source: geeknews
tags:
- AI
- Other
- ive.dazzleat.link
title: 'Show GN: Spring IVE 1.5 — Slack에서 코드 맥락 아는 에이전트와 대화, 바이브코딩 작업 이력 관리, 사람+AI
  비...'
url: https://ive.dazzleat.link
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
GitLab/GitHub 이슈를 Claude·Gemini·Codex·OpenCode 같은 AI CLI 에이전트가  
자동으로 감지해 코드 작성 후 MR/PR까지 만들어주는 웹 대시보드, Spring IVE의  
1.5 버전을 출시했습니다. 이번에 추가된 기능들을 공유합니다.

### Slack 통합 — 코드 맥락을 아는 에이전트와 대화

멘션으로 IVE 에이전트와 바로 대화할 수 있습니다. 핵심은 봇이 해당 프로젝트  
레포를 클론해 코드 맥락을 그대로 안다는 점입니다.  
"이 기능 어디서 처리돼?", "이 API 어떻게 동작해?", "왜 이렇게 구현했어?"를  
Slack에서 물으면 실제 코드를 근거로 답합니다. 구현 설명·기능 안내를 해주는  
사내 '콜센터'처럼 쓸 수 있습니다.  
검증대기→검증자, 확인대기→확인자, 완료→생성자로 가는 단계 전이 알림 DM도  
지원합니다(멘션 사용자 언어에 맞춰 다국어).

### 바이브코딩 작업 이력 관리

Claude Code 같은 바이브코딩 툴로 로컬에서 직접 한 작업도 IVE가 자동 인식해  
이력으로 남깁니다. IVE 안에서 돌린 에이전트 작업뿐 아니라, 개발자가  
바이브코딩으로 처리한 것까지 한곳에 모입니다.  
덕분에 개발자 본인도 "언제·무엇을·어떤 툴로·얼마나" 작업했는지를  
흩어지지 않게 체계적으로 관리할 수 있습니다. 일일이 기록하지 않아도  
작업 이력·토큰·비용이 자동으로 정리돼, 회고나 업무 보고에 그대로 활용됩니다.

### 이미지 입력 공통 지원

웹 채팅·Slack 멘션·이슈 본문/코멘트에 붙인 이미지를 에이전트가 분석합니다.  
스크린샷으로 버그 리포트하면 바로 처리됩니다.

### 보고서 — 더 풍부하고 정확해진 비용 분석

비용 모델을 보강해, 에이전트 토큰 비용뿐 아니라 검증·개발에 들인  
사람 시간까지 실측해 원가로 산정합니다.

- 사용자별 단가 배수(rate\_multiplier)로 인건비 차등 반영
- 표시 통화·환율 변환 — 원화(KRW) 등으로 바로 확인
- 비중 누적 분배 막대로 "비용이 어디서 쌓이는지" 시각화  
  사람과 AI가 함께 쓴 비용이 한 화면에서 정확하게 잡힙니다.

### 동작 흐름

1. GitLab/GitHub 프로젝트를 연결하고 대상 레이블(예: IVE)을 설정
2. 스캐너가 이슈를 폴링 — 레이블이 붙은 이슈 발견 시 실행 큐에 등록
3. 배정된 AI 에이전트가 레포를 클론하고 claude / gemini 등의 CLI를 실행
4. 작업 완료 후 MR/PR 생성 및 이슈 코멘트, 단계 전이를 Slack으로 알림

### 다음 (2.0 로드맵)

Linear 연동으로 프로젝트 관리 기능을 보강합니다. WBS(작업 분해 구조) 등  
일정·진척 관리까지 더해, 이슈 자동 처리에서 프로젝트 계획·추적까지  
한곳에서 다룰 수 있게 할 계획입니다.

### 기술 스택

Next.js 16 (App Router), React 19, Tailwind CSS 4, xterm.js /  
Node.js 커스텀 서버(node-pty, WebSocket) / SQLite(better-sqlite3) /  
지원 에이전트: Claude Code, Gemini CLI, Codex, OpenCode

반복성 높은 이슈는 에이전트에게 위임하고, 팀은 검증과 의사결정에 집중하세요.  
이제 그 흐름 전체가 Slack 안에서 돌아가고, 코드 맥락을 아는 에이전트가  
구현·기능까지 설명하며, 사람과 AI가 함께 쓴 비용도 정확히 추적됩니다.

## 원문
- [원문](https://ive.dazzleat.link)
- [GeekNews 토론](https://news.hada.io/topic?id=30140)

## My Note
<!-- 한 줄 코멘트 남기기 -->

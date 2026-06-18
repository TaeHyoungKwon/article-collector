---
category: AI
collected_at: '2026-06-17T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30560
id: hada-30560
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -995.307
recommended_on: '2026-06-17'
source: geeknews
tags:
- AI
- Other
- github.com/tastyeffectco
title: sandboxd - AI 앱-빌더 제품을 위한 오픈소스 샌드박스 엔진
url: https://github.com/tastyeffectco/sandboxd
---

## TL;DR
- sandboxd는 AI 앱 빌더를 위한 오픈소스 샌드박스 엔진으로, 격리된 클라우드 개발 환경을 제공한다.
- HTTP 요청 한 번으로 Linux 컨테이너를 생성하고, AI 코딩 에이전트가 즉시 앱을 빌드하여 미리보기 링크를 생성한다.
- 이는 개발자들이 간편하게 앱을 프로토타입하고 테스트할 수 있는 효율적인 방법을 제시해준다.

## GeekNews 요약
- 사용자별 **격리된 클라우드 개발 환경**, 내장 코딩 에이전트, 라이브 미리보기 URL을 통합해서 제공하는 **AI 앱 빌더용 오픈소스 백엔드 엔진**
- HTTP 요청 한 번으로 격리된 Linux 컨테이너 생성 → AI 코딩 에이전트가 내부에서 코드 작성 → 작성된 앱이 공유 가능한 **미리보기 링크**로 즉시 접근 가능
  - "build me a todo app" 입력 하면 앱이 바로 보여지는 **Lovable, Bolt, v0, Replit** 같은 제품을 자체 서버에서 구현 가능
  - OpenCode와 Claude Code CLI가 모든 샌드박스에 사전 설치되어 프롬프트만 전달하면 바로 빌드
- Idle 시 자동 종료해 메모리 해제, 링크 재접속 즉시 웨이크업, 파일은 디스크에 상시 보존  
  → **한 대의 일반 서버에 다수 사용자 수용 가능**
- Docker를 제어하는 단일 **Go 프로그램**, URL 처리용 Traefik, 데이터베이스용 SQLite로 구성, Kubernetes/별도 DB 서버/메시지 큐 필요없음
- **멀티 테넌트 격리**, 미리보기 라우팅, 슬립/웨이크업 기반 비용 제어, **에이전트 오케스트레이션**을 직접 구축하지 않고도 **AI 앱 빌더 SaaS**를 준비 가능
- 신뢰 불가 외부 코드 실행 시 테넌트별 VM(또는 gVisor/Kata/Firecracker), 프로덕션에서 API 인증 활성화, 멀티 호스트 대비가 확장 시 핵심 강화 포인트
- MIT 라이선스

## 원문
- [원문](https://github.com/tastyeffectco/sandboxd)
- [GeekNews 토론](https://news.hada.io/topic?id=30560)

## My Note
<!-- 한 줄 코멘트 남기기 -->

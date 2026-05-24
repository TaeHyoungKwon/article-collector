---
category: AI
collected_at: '2026-05-25T07:53:25+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29835
id: hada-29835
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- esengine.github.io
title: DeepSeek Reasonix - 높은 캐싱과 낮은 비용의 DeepSeek 네이티브 코딩 에이전트
url: https://esengine.github.io/DeepSeek-Reasonix/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **DeepSeek API 전용**으로 설계된 오픈소스 터미널 코딩 에이전트로, `api.deepseek.com`과 직접 통신
- **Append-only 루프**가 DeepSeek의 byte-stable prefix cache에 최적화되어, 긴 세션에서 **90% 이상 캐시 히트율** 유지 및 입력 토큰 비용 약 1/5 수준으로 절감 (동종 도구 대비 약 1/3 비용 수준)
- 글로벌 설치 필요 없이 `npx reasonix code` 한 줄로 실행 (Node ≥ 22, macOS/Linux/Windows 지원)
- **3대 핵심 설계**
  - **Cache-First Loop**: append-only 구조, 마커 의존 없음, 결정론적 호출 순서로 prefix 캐시 유지
  - **R1 Thought Harvest**: 빠져나간 tool call의 추론 체인 수집
  - **Tool-Call Repair**: schema-aware self-heal 방식 복구
- **터미널 우선(Terminal-first)** 원칙으로 IDE 플러그인 미지원, `git diff`·`ls` 등 터미널 도구를 그대로 활용
  - **TypeScript + Ink TUI** 기반, Tauri 데스크톱 클라이언트도 별도 제공 (Node 런타임 번들)
- **V4 Two-tier 모델 운용**: 기본 V4-Flash로 저비용 반복, `/pro`로 단일 턴 V4-Pro 승격, `/preset max`로 세션 전체 Pro 실행
- **MCP(Model Context Protocol) 1급 지원**: `--mcp "name=cmd args"` 한 줄로 외부 서버 연결, stdio·SSE·Streamable HTTP 전송 방식 지원
- **Sandbox + `/plan` 게이트**: 모든 내장 도구는 실행 디렉터리에 샌드박스, `/plan` 모드는 read-only audit gate로 승인 전 쓰기 차단
  - SEARCH/REPLACE 편집은 pending 큐로 대기, `/apply` 전까지 디스크 미반영
- **Composable Skills**: `.reasonix/skills/<name>.md`에 Markdown 파일 배치, frontmatter `runAs: subagent`·`allowed-tools`로 격리 실행
- **Replay & Events**: 모든 이벤트가 디스크에 기록되어 `reasonix replay / events / stats` 명령으로 과거 세션 재생·통계·감사 가능
- **Plain text 기반 확장성**: `/mcp`·`/skills`·`/memory`·`/config`·`/slash` 디렉터리로 모든 설정을 git 추적 가능한 평문으로 관리
- **자체 호스팅 DeepSeek 엔드포인트 지원**: 0.30부터 비표준 키 prefix 허용, `baseUrl`만 내부 주소로 지정하면 루프·캐시·tool 프로토콜 동일 동작
- DeepSeek API 가격: **V4-Flash $0.07/Mtok (uncached) · $0.014/Mtok (cached)**
- MIT 라이선스

## 원문
- [원문](https://esengine.github.io/DeepSeek-Reasonix/)
- [GeekNews 토론](https://news.hada.io/topic?id=29835)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-28T11:15:35+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=30905
id: hada-30905
matched_keywords:
- RAG
read: false
recommend_score: 3.609
source: geeknews
tags:
- AI
- Other
- github.com/TaewonyNet
title: 'Show GN: ArachneControl – 서버가 브라우저를 원격 제어해 수집하는 오픈소스 데이터 수집 시스템'
url: https://github.com/TaewonyNet/ArachneControl
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
사용자의 **실제 브라우저 세션**으로 데이터를 수집하되, **무엇을 어떻게 수집할지는 서버가 런타임에 동적 발행**하는 self-hosted 수집 시스템입니다. 서버가 클라이언트(브라우저)를 원격 통제하는 **명령-수행-보고(Command-Execute-Report)** 패턴.

크롤러를 새로 짤 때마다 겪는 세 가지 — 타겟 백엔드 부하/차단, 로그인 벽, 수집 로직이 바뀔 때마다 클라이언트 재배포 — 를 설계로 풉니다.

- **Zero-Footprint**: 타겟 서버에 직접 요청하지 않고 *이미 로그인된 사용자 브라우저*가 대신 수집 → 로그인 벽 안쪽도 사람과 동일하게 접근하고, 백엔드 부하·차단을 피함.
- **서버 동적 제어**: 북마크릿은 한 번 등록하면 영구 불변. 수집 규칙(셀렉터·액션·추출)은 서버가 타입 커맨드로 발행 → 로직 변경 시 클라이언트 재배포 0. 단일 소스 Pydantic에서 TS 타입 자동 생성.
- **클릭으로 레시피 작성**: WebUI에서 요소를 클릭하면 셀렉터 자동 생성, 액션 시퀀스(click·drag·scroll·swipe) → extract 레시피 저장. `script` eval 금지(화이트리스트).
- **무손실 적재**: write-ahead(동기 커밋 후 202) + 멱등 + 재시작 시 자동 복구.
- **MCP 에이전트 제어**: 라이브 파이프를 MCP 도구로 노출(host allowlist·rate-limit·op TTL 가드). 단, **봇 회피·대량 스크래핑은 비목표**.
- **secure-by-default**: 관리 인증 기본 ON(Jupyter식 자동 토큰), 서버 응답 eval(`script`)·외부 비콘(`beacon`) 실행 경계, 핑거프린팅 미사용.
- **무비용·이식성**: SQLite + 인메모리 큐 + 단일 FastAPI. 외부 유료 서비스 0. `uv`로 OS 무관 재현. MIT.

공개 사이트 수집은 브라우저 Private Network Access 제약 때문에 공개 URL이 필요한데, `ENABLE_TUNNEL=1`로 cloudflared 임시 터널을 띄워 우회합니다(실측: 실 뉴스 사이트 수집 성공).

## 원문
- [원문](https://github.com/TaewonyNet/ArachneControl)
- [GeekNews 토론](https://news.hada.io/topic?id=30905)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-05-11T11:42:13+09:00'
geeknews_comments: 0
geeknews_score: 7
geeknews_url: https://news.hada.io/topic?id=29376
id: hada-29376
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 8.079
recommended_on: '2026-05-11'
source: geeknews
tags:
- AI
- Other
- github.com/nexu-io
title: Open Design - Claude Design의 로컬 퍼스트 오픈소스 대체제
url: https://github.com/nexu-io/open-design
---

## TL;DR
- 이 글은 Claude Design의 로컬 퍼스트 오픈소스 대체제인 Open Design의 주요 기능과 특징을 설명한다.
- Open Design은 31개 스킬과 129개 브랜드급 디자인 시스템을 제공하며, 인터랙티브 질문 폼을 통해 사용자 요구를 정확히 반영한다.
- 이 시스템은 실시간 협업과 고품질 디자인 작업을 가능하게 하여 개발자와 디자이너의 작업 효율성을 크게 향상시킨다.

## GeekNews 요약
- **에이전트를 내장하지 않고** 사용자의 PATH에 있는 16종 코딩 에이전트 CLI(Claude Code, Codex등)를 자동 감지하여 디자인 엔진으로 활용
- **31개 스킬** 내장: 웹 프로토타입, SaaS 랜딩, 대시보드, 모바일 앱, 소셜 캐러셀, 매거진 포스터, PM 스펙, OKR, 인보이스 등 9개 시나리오별 분류
- **129개 브랜드급 디자인 시스템** 탑재 — Linear, Stripe, Vercel, Airbnb, Tesla, Notion, Apple, Cursor, Supabase, Figma 등 실제 프로덕트 시스템을 Markdown 기반 `DESIGN.md`로 제공
- 첫 턴에서 **인터랙티브 질문 폼**이 강제 실행되어 표면·대상·톤·브랜드·스케일을 30초 만에 확정, AI의 임의 디자인(AI slop) 방지
- **5가지 비주얼 디렉션**(Editorial Monocle, Modern Minimal, Tech Utility, Brutalist, Soft Warm) 중 선택 → 결정론적 OKLch 팔레트 + 폰트 스택 자동 적용
- **미디어 생성** 통합: gpt-image-2(이미지), Seedance 2.0(15초 시네마틱 영상), HyperFrames(HTML→MP4 모션 그래픽) + 93개 프롬프트 템플릿 갤러리
- **BYOK 프록시**로 Anthropic, OpenAI, Azure OpenAI, Google Gemini, Ollama, LM Studio 등 어떤 프로바이더든 연결 가능, SSRF 차단 내장
- **Claude Design ZIP 임포트** 지원 — claude.ai에서 내보낸 파일을 드롭하면 로컬 프로젝트로 변환하여 이어서 편집 가능
- 로컬 데몬이 프로젝트 폴더에서 CLI를 spawn하여 **실제 파일시스템에 Read/Write/Bash/WebFetch** 수행, SQLite로 프로젝트·대화·탭 상태 기억
- **Anti-AI-slop 메커니즘**: 5차원 자기 비평(3/5 미만 시 재작업), P0/P1/P2 체크리스트 게이트, 브랜드 색상 기억 추측 금지, 가짜 지표 금지
- 샌드박스 iframe 프리뷰 + HTML/PDF/PPTX/ZIP/Markdown **내보내기**, stdio MCP 서버로 다른 코딩 에이전트에서 디자인 파일 직접 읽기 가능
- 실행: 데스크톱 앱 다운로드 / Docker(`docker compose up -d`) / 소스(`pnpm tools-dev run web`) 세 가지 방식 지원
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/nexu-io/open-design)
- [GeekNews 토론](https://news.hada.io/topic?id=29376)

## My Note
<!-- 한 줄 코멘트 남기기 -->

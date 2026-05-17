---
category: AI
collected_at: '2026-05-16T15:55:43+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29557
id: hada-29557
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -995.099
recommended_on: '2026-05-16'
source: geeknews
tags:
- AI
- Other
- github.com/anthropics
title: Claude for Legal  - Anthropic의 법률 업무용 AI 플러그인 모음
url: https://github.com/anthropics/claude-for-legal
---

## TL;DR
- 이 글은 Anthropic의 법률 업무용 AI 플러그인 모음을 설명하고 있다.
- 70개 이상의 Named Agent와 20개 이상의 MCP 커넥터를 통해 다양한 법률 업무를 자동화할 수 있다.
- 법률 실무의 효율성을 높이고, 법학 교육에 기여하는 가능성이 있다.

## GeekNews 요약
- 사내 상업계약, 프라이버시, 고용, M&A, 소송, 규제, AI 거버넌스, 지식재산, 법학 교육까지 **법률 실무 전 영역을 커버하는 플러그인 스위트**로, Claude Cowork·Claude Code·Managed Agents API 세 가지 방식으로 배포 가능
- **70개 이상의 Named Agent** 포함 — Vendor Agreement Reviewer, NDA Triager, Termination Reviewer, DSAR Responder, Claim Chart Builder 등 워크플로별로 슬래시 명령어 하나로 실행
- 각 플러그인은 **cold-start interview**를 통해 팀의 플레이북·에스컬레이션 규칙·하우스 스타일을 학습하고, `CLAUDE.md` 프랙티스 프로파일에 기록하여 모든 스킬이 맞춤형 결과 생성
- **20개 이상의 MCP 커넥터** 제공: Slack, Google Drive, Box 등 범용 도구와 Ironclad, DocuSign, iManage, Everlaw, CourtListener, Trellis 등 법률 특화 시스템 연동
- Thomson Reuters의 **CoCounsel Legal** 플러그인으로 Westlaw Deep Research 연동, 판례·법령·규정을 최대 3개 미국 관할권에서 완전 인용 보고서 생성 가능
- 리서치 커넥터를 통한 인용에는 **소스 태그**가, 모델 지식만의 인용에는 **`[verify]` 플래그**가 표시되어 인용 신뢰도를 명시적으로 구분
- 계약 관련 스킬은 **Claude for Word 사이드바에서 tracked changes 모드**로 작동하며, 번호 매기기·정의 조항·교차 참조·스타일 보존. Excel 대상 스킬은 멀티시트 `.xlsx` 워크북으로 출력
- **legal-builder-hub**가 커뮤니티 스킬의 신뢰 레이어 제공 — 숨겨진 콘텐츠 스캔, 인젝션 탐지, allowlist, 라이선스 게이트, freshness 게이트, 업데이트 시 재스캔, 설치 감사 로그
- 법학생용 **Socratic Drill**(정답 미제공 학습 모드), IRAC 채점, 바 시험 대비, 플래시카드, 시험 예측 등 교육 플러그인과 **legal-clinic** 플러그인(ABA Formal Op. 512 기준 설계) 포함
- 모든 출력물은 **변호사 검토를 위한 초안**이며, Anthropic의 법적 입장을 대변하지 않음. 전체가 Markdown과 JSON으로 구성되어 빌드 단계 불필요
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/anthropics/claude-for-legal)
- [GeekNews 토론](https://news.hada.io/topic?id=29557)

## My Note
<!-- 한 줄 코멘트 남기기 -->

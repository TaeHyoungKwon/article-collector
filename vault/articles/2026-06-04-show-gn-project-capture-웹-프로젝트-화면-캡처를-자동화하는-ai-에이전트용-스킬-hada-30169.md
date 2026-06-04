---
category: AI
collected_at: '2026-06-04T14:42:11+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30169
id: hada-30169
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
recommended_on: '2026-06-04'
source: geeknews
tags:
- AI
- Other
- github.com/Kuneosu
title: 'Show GN: Project Capture - 웹 프로젝트 화면 캡처를 자동화하는 AI 에이전트용 스킬'
url: https://github.com/Kuneosu/project-capture
---

## TL;DR
- 이 글은 웹 프로젝트 화면 캡처를 자동화하는 AI 도구, `project-capture`에 대해 설명한다.
- 이 도구는 프로젝트 구조 분석과 화면 캡처 작업을 자동화하며, 사용자가 캡처 범위를 선택할 수 있도록 돕는다.
- 이를 통해 개발자는 반복적인 캡처 작업에서 벗어나 효율성을 높일 수 있다.

## GeekNews 요약
웹 프로젝트 화면 캡처를 반복해서 하다 보니, 라우트 확인, 로그인 처리, 캡처 범위 선택, 결과 정리를 매번 수동으로 하는 게 번거로워서 만들었습니다.

`project-capture`는 AI 코딩 에이전트가 프로젝트를 먼저 분석한 뒤, 어떤 화면을 캡처할지 사용자에게 확인하고 Playwright로 스크린샷과 리포트를 생성하는 도구입니다.

Codex 스킬로 만들었지만 npm 패키지로도 배포해서 Claude Code, Gemini CLI 같은 다른 AI 도구나 일반 터미널에서도 사용할 수 있게 했습니다.

완전 자동 크롤러라기보다는 “프로젝트 분석 → 캡처 범위 확인 → 로그인 처리 → 화면 캡처 → 리포트 생성” 흐름을 안정적으로 진행하도록 돕는 도구에 가깝습니다.

주요 기능은 다음과 같습니다.

- 프로젝트 구조를 분석해 라우트 후보 탐색
- Next.js, Remix, React Router, 일반 SPA 라우트 패턴 지원
- 캡처 범위 선택: 전체 / 핵심 도메인 / 특정 도메인 / 수동 지정
- 로그인 필요 여부 감지 및 수동 로그인 / 환경변수 로그인 지원
- 동적 라우트는 샘플 URL 기반으로 처리
- Playwright로 화면 캡처
- 전체 스크롤 캡처 또는 특정 viewport 캡처 선택
- capture-report.md, capture-results.json 생성

## 원문
- [원문](https://github.com/Kuneosu/project-capture)
- [GeekNews 토론](https://news.hada.io/topic?id=30169)

## My Note
<!-- 한 줄 코멘트 남기기 -->

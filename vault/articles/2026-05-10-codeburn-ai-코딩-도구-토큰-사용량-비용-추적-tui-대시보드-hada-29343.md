---
category: AI
collected_at: '2026-05-10T09:31:02+09:00'
geeknews_comments: 1
geeknews_score: 8
geeknews_url: https://news.hada.io/topic?id=29343
id: hada-29343
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: -989.595
recommended_on: '2026-05-10'
source: geeknews
tags:
- AI
- Other
- github.com/getagentseal
title: CodeBurn - AI 코딩 도구 토큰 사용량/비용 추적 TUI 대시보드
url: https://github.com/getagentseal/codeburn
---

## TL;DR
- 이 글은 AI 코딩 도구의 토큰 사용량과 비용을 추적하는 TUI 대시보드인 CodeBurn에 대해 다룬다.
- CodeBurn은 디스크의 세션 데이터를 직접 읽고 비용을 산정하여 낭비 패턴을 자동으로 탐지하고 수정안을 제공한다.
- 이 도구는 AI 코딩 도구의 효율성을 높여 개발 환경에서의 비용 절감을 가능하게 한다.

## GeekNews 요약
- Claude Code, Codex, Cursor 등 **18개 AI 코딩 도구**의 토큰 사용량과 비용을 자동 추적하는 터미널 대시보드
- 래퍼·프록시·API 키 없이 **디스크의 세션 데이터를 직접 읽어** LiteLLM 가격 데이터로 비용 산정, 모든 처리가 로컬에서 실행
- `codeburn optimize`로 반복 파일 읽기, 미사용 MCP 서버, 비대한 CLAUDE.md, 저가치 고비용 세션 등 **낭비 패턴을 자동 탐지**하고 복사-붙여넣기 가능한 수정안까지 제공
  - 발견 사항마다 예상 토큰·달러 절약량 표시, A~F 등급으로 설정 건강도 평가
- `codeburn compare`로 모델 간 **원샷 성공률, 재시도율, 호출당 비용, 캐시 히트율** 등을 나란히 비교 가능
- `codeburn yield`로 AI 세션과 git 커밋을 연계해 **Productive / Reverted / Abandoned** 지출 분류, 실제 생산성 기여도 확인
- 작업 유형을 13개 카테고리(Coding, Debugging, Feature Dev, Testing 등)로 **LLM 호출 없이 결정론적 분류**, 어디에 토큰이 소모되는지 한눈에 파악
- macOS 메뉴 바 앱 지원: `codeburn menubar` 한 줄이면 설치·실행, 메뉴 바 아이콘에 **오늘 지출 실시간 표시**
- **162개 통화 지원**(Frankfurter 환율 API), `codeburn currency KRW`로 원화 표시 전환 가능
- `--provider`, `--project`, `--exclude`, `--from`/`--to` 등 필터링과 `--format json` 출력으로 **자동화·파이프라인 연동** 편리함
- `npm install -g codeburn` 또는 `brew install codeburn`으로 설치
- MIT 라이선스

## 원문
- [원문](https://github.com/getagentseal/codeburn)
- [GeekNews 토론](https://news.hada.io/topic?id=29343)

## My Note
<!-- 한 줄 코멘트 남기기 -->

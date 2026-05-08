---
collected_at: '2026-05-07T09:46:02+09:00'
geeknews_comments: 0
geeknews_score: 11
geeknews_url: https://news.hada.io/topic?id=29250
id: hada-29250
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 6.485
recommended_on: '2026-05-08'
source: geeknews
tags:
- github.com/nowork-studio
title: Toprank - SEO 및 광고 관리용 Claude Code 플러그인
url: https://github.com/nowork-studio/toprank
---

## TL;DR
- 이 글은 Toprank라는 오픈소스 마케팅 자동화 도구의 기능과 구성 요소를 다룬다.
- Toprank는 Google Ads, Meta Ads, 그리고 SEO 관련 스킬을 포함하여 광고 효율성을 극대화하는 다양한 기능을 제공한다.
- 디지털 마케팅에서의 자동화와 효율적 데이터 분석의 중요성이 증가하는 현재, 이 도구는 마케팅 전문가들에게 유용한 자료가 될 것이다.

## GeekNews 요약
Google Search Console, Google Ads, Meta Ads 데이터에 직접 접근해
트래픽 분석, 낭비 광고비 탐지, 크리에이티브 피로도 진단, 메타 태그 수정
까지 수행하는 오픈소스 마케팅 자동화 도구
Google Ads 스킬 4개 + Meta Ads 스킬 2개 + SEO 스킬 9개 + 크로스 모델 스킬 1개로 구성
Google Ads
: 계정 감사(
7개 건강 지표
평가), 캠페인 관리(입찰·예산·네거티브 키워드 조정), RSA 카피 생성 및 A/B 테스트, 랜딩 페이지 관련성 분석
Meta Ads
: Pixel + CAPI Health, Creative Health, Scaling Readiness 등
Meta 전용 7개 지표
감사, ROAS 분석·빈도 우선 트리아지·Learning Phase 진단
SEO
: GSC 데이터 기반 전체 감사 및 30일 액션 플랜,
E-E-A-T
콘텐츠 작성, 키워드 리서치·토픽 클러스터, 메타 태그 최적화, JSON-LD 스키마 마크업, 단일 페이지 심층 분석, 깨진 링크 점검,
GEO(Generative Engine Optimization)
스코어링
Gemini 크로스 모델
: Google Gemini에게 Google Ads/SEO 결정에 대한 세컨드 오피니언 요청 가능 — review(pass/fail 게이트), challenge(적대적 스트레스 테스트), consult(오픈 Q&A) 모드 지원
OpenClaw/Hermes 적응 레이어
를 통해 크론 기반 완전 자동 SEO 에이전트 구성 가능 — 사이트 모니터링, 메타 태그 재작성, 구조화 데이터 추가를 무인 실행
독립형 원격 MCP 서버도 제공하여 Google Ads ~100개 도구, Meta Ads 읽기·쓰기 도구를 제공하며, Claude Code 외에도
Claude Desktop, Cursor
등 모든 MCP 클라이언트에서 독립 사용 가능
Claude Code에서 두 개 명령어로 설치:
/plugin marketplace add nowork-studio/toprank
/plugin install toprank@nowork-studio
모든 스킬이
/toprank:*
명령어로 즉시 사용 가능
~~category
플레이스홀더 패턴으로
도구 비의존적 설계
— 특정 커넥터가 없으면 graceful degradation(예: GSC 데이터 없이도 기술적 크롤링 가능)
MIT 라이선스

## 원문
- [원문](https://github.com/nowork-studio/toprank)
- [GeekNews 토론](https://news.hada.io/topic?id=29250)

## My Note
<!-- 한 줄 코멘트 남기기 -->

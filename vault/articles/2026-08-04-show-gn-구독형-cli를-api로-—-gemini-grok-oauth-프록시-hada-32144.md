---
category: AI
collected_at: '2026-08-04T23:27:53+09:00'
geeknews_comments: 3
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=32144
id: hada-32144
matched_keywords:
- AI
read: false
recommend_score: 3.802
source: geeknews
tags:
- AI
- Other
- github.com/kimws
title: 'Show GN: 구독형 CLI를 API로 — Gemini/Grok OAuth 프록시'
url: https://github.com/kimws/gemini-oauth
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
ChatGPT의 oauth 정보를 공유하여 OpenAI API와 호환되는 HTTP 프록시를 생성해주는 오픈소스 프로젝트를 애플리케이션 개발에 활용하고 있습니다. 이를 참고하여 다른 CLI 도구에 대해서도 동일한 방식의 프록시를 직접 개발했습니다.

참고 프로젝트

ChatGPT 대상  
<https://github.com/EvanZhouDev/openai-oauth>

개발한 프로젝트

Gemini CLI (Antigravity / agy) 대응  
OpenAI API 호환 HTTP 프록시  
<https://github.com/kimws/gemini-oauth>  
Grok Build 대응  
OpenAI API 호환 HTTP 프록시  
<https://github.com/kimws/grok-oauth>

활용 효과 및 유의사항

이미 결제 중인 구독 서비스를 통해 CLI를 HTTP 프록시 API 형태로 래핑하여 사용할 수 있어, 별도의 API 비용 없이 기존 구독 비용만으로 활용이 가능하다는 점에서 비용 절감 효과가 있습니다.

다만, CLI가 설치된 로컬 환경에서 API를 호출하는 방식은 특별한 문제가 없어 보이나, 원격 환경에서 접근하여 사용하는 경우 각 서비스의 라이선스 정책에 위배될 소지가 있어 주의가 필요합니다.

## 원문
- [원문](https://github.com/kimws/gemini-oauth)
- [GeekNews 토론](https://news.hada.io/topic?id=32144)

## My Note
<!-- 한 줄 코멘트 남기기 -->

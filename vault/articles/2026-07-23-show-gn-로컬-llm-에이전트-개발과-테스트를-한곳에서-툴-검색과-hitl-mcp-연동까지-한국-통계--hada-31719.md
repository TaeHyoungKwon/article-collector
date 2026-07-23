---
category: AI
collected_at: '2026-07-23T11:43:03+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31719
id: hada-31719
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
source: geeknews
tags:
- AI
- Other
- github.com/spring-ai-community
title: 'Show GN: 로컬 LLM 에이전트 개발과 테스트를 한곳에서, 툴 검색과 HITL, MCP 연동까지 (한국 통계 MCP 데모)'
url: https://github.com/spring-ai-community/spring-ai-playground
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
국가통계포털(KOSIS)이 공식 MCP 시범서비스를 열어서, 노트북에서 도는 9B 로컬 모델에 붙여봤습니다. API 키 없이 합계출산율을 찾아 차트를 그리고, CSV로 저장하려는 순간에는 승인 창이 뜹니다. 파일 쓰기처럼 사람이 승인(HITL)해야만 하는 작업은 UI에서 사람이 확인하고 승인하도록 해뒀기 때문입니다.

데모 영상(1분 21초, 한국어 자막): <https://youtu.be/zARRVLg-7xA?cc_load_policy=1&cc_lang_pref=ko>

- "합계출산율 보여줘" 한 마디에 KOSIS 검색 → 통계표 검증 → 실데이터 조회 → area 차트 생성(2015년 1.20 → 2024년 0.73)
- 같은 통계표에서 12개국 비교를 로즈 차트로, 8개국 2015 vs 2024를 히트맵으로
- "요약을 CSV로 저장해줘"에서는 파일 쓰기가 L4 위험 등급이라 승인 창이 뜨고, Approve를 눌러야 실제 저장
- 모델은 로컬에서 실행되므로 프롬프트가 외부로 나가지 않습니다. 사용한 API 키는 0개입니다.

이 데모에 사용한 프로젝트는 Spring AI Playground라는 오픈소스(Spring AI Community 인큐베이팅)입니다.

원래는 Spring AI 기능을 하나씩 눌러보는 플레이그라운드였는데, Spring AI 2.0에서 에이전트와 MCP가 프레임워크 코어로 들어오면서 방향을 바꿨습니다. 이제는 기능 데모보다 로컬 LLM 에이전트를 개발하고 테스트하는 워크벤치에 가깝습니다.

보통 에이전트를 직접 붙여보려면 MCP 연결, 툴 검색, 승인 게이트 등을 각각 코드로 구현해야 합니다. Spring AI Playground는 그런 흐름을 자바 코드를 작성하지 않고도 데스크톱 앱에서 확인하는 데 초점을 맞췄습니다. MCP 프록시 기능을 통해 기존 MCP 툴에도 HITL을 UI에서 설정할 수 있습니다.

필요한 도구는 요청에 맞게 동적으로 검색해 연결(Dynamic Tool Discovery)할 수 있고, 파일 쓰기처럼 위험한 작업은 위험도(L0~L5)에 따라 승인 창이 나타납니다. 승인과 거부가 각각 어떻게 처리되는지도 직접 확인할 수 있습니다. 채팅, 도구 호출, 토큰, 비용, 리스크는 Observability 대시보드에서 함께 볼 수 있습니다.

모델은 로컬(Ollama)에서 실행되므로 프롬프트가 외부로 나가지 않습니다. 자바와 스프링으로 에이전트, MCP 클라이언트/서버, HITL을 어떻게 구현했는지도 코드로 확인할 수 있습니다.

GitHub: <https://github.com/spring-ai-community/spring-ai-playground>  
문서: <https://spring-ai-community.github.io/spring-ai-playground/>  
다운로드(Windows/macOS/Linux): [https://spring-ai-community.github.io/spring-ai-playground/…](https://spring-ai-community.github.io/spring-ai-playground/#1-download-the-desktop-app)

KOSIS MCP는 국가데이터처 시범서비스라 엔드포인트가 변경될 수 있습니다. 이 프로젝트는 해당 서비스를 사용하는 독립 오픈소스입니다.

공공데이터 MCP를 실제 에이전트에 연결해 보신 경험이나, HITL(Human-in-the-Loop) 설계에 대한 의견이 있다면 피드백 부탁드립니다.

## 원문
- [원문](https://github.com/spring-ai-community/spring-ai-playground)
- [GeekNews 토론](https://news.hada.io/topic?id=31719)

## My Note
<!-- 한 줄 코멘트 남기기 -->

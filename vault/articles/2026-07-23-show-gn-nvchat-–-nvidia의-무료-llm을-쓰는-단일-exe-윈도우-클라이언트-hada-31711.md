---
category: AI
collected_at: '2026-07-23T09:38:04+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31711
id: hada-31711
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
source: geeknews
tags:
- AI
- Other
- github.com/akon47
title: 'Show GN: NvChat – NVIDIA의 무료 LLM을 쓰는 단일 exe 윈도우 클라이언트'
url: https://github.com/akon47/NvChat
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
NVIDIA의 build.nvidia.com 은 여러 오픈 모델을 OpenAI 호환 API로 무료로 쓸 수 있게 해줍니다. 그런데 매번 웹 플레이그라운드로 들어가는 게 번거로워서, 클로드, ChatGPT 데스크톱 앱처럼 쓸 수 있는 윈도우 클라이언트를 직접 만들었습니다.

### 기능

- 사용 가능한 모델 목록을 API로 불러와 검색해서 선택 (100개 이상)
- 실시간 스트리밍. 응답이 끝난 뒤가 아니라 스트리밍 도중에도 마크다운을 렌더링합니다  
  (표, 구문 강조된 코드 블록 포함)
- 추론(reasoning) 과정 표시 (deepseek-r1 등 reasoning\_content / <think> 를 내보내는 모델)

### 사용에 필요한 것 / 알아둘 점

- build.nvidia.com 무료 API 키(nvapi-...)가 필요합니다. NVIDIA 계정으로 로그인 후 아무 모델 페이지의 'Get API Key'로 발급받아 설정에 넣으면 됩니다. (앱 자체에는 별도 가입이 없습니다)
- 무료 티어에는 NVIDIA 측 요청 한도가 있습니다.
- 코드 서명이 없어서 첫 실행 시 Windows SmartScreen 경고가 뜹니다. 추가 정보 → 실행.
- Windows x64 전용입니다.

무료, MIT 라이선스입니다. 소스와 exe 다운로드: <https://github.com/akon47/NvChat>

## 원문
- [원문](https://github.com/akon47/NvChat)
- [GeekNews 토론](https://news.hada.io/topic?id=31711)

## My Note
<!-- 한 줄 코멘트 남기기 -->

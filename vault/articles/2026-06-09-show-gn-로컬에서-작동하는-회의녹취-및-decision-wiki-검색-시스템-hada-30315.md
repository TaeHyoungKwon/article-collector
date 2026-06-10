---
category: AI
collected_at: '2026-06-09T11:59:41+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30315
id: hada-30315
matched_keywords:
- AI
- LLM
read: false
recommend_score: -994.901
recommended_on: '2026-06-09'
source: geeknews
tags:
- AI
- Other
- github.com/notadev-iamaura
title: 'Show GN: 로컬에서 작동하는 회의녹취 및 Decision Wiki 검색 시스템'
url: https://github.com/notadev-iamaura/meeting-transcriber
---

## TL;DR
- 이 글은 로컬에서 회의 녹취 및 결정사항을 정리할 수 있는 오픈소스 도구를 소개한다.
- 이 도구는 외부 AI 사용이 어려운 환경에서도 회의록 및 액션아이템을 효과적으로 관리할 수 있도록 설계되었다.
- 특히 회의가 많은 업무 환경에서 효율성을 높이는 데 기여할 수 있는 점이 중요하다.

## GeekNews 요약
한국어 회의를 로컬에서 녹음하고, 전사·요약·Decision Wiki 정리하고 검색 (AI 챗)할 수 있는 오픈소스 도구를 만들어봤습니다.

저처럼 업무 환경상 외부AI나 회의 녹취/전사 서비스를 사용할 수 없는 분들에게 도움이 되지 않을까 합니다.  
하루에 회의가 10개 이상 있는 날은 회의에서 나온 회의록과 액션아이템만 체크해도 야근이 기다리고 있습니다.  
문제는 회의록을 남기는 것 자체보다, 나중에 다시 찾을 수 있는 형태로 남기는 것이었습니다.

그래서 단순한 회의 전사보다는, 회의에서 나온 결정사항과 액션아이템을 원문 근거와 함께 쌓아가는 로컬 Decision Wiki를 목표로 만들고 있습니다.

- M4 16GB 수준에서도 작동할 수 있도록....

현재는 이런 흐름을 지향합니다.

- Apple Silicon Mac에서 로컬 실행
- 한국어 회의 녹음/전사
- 화자 분리
- 로컬 LLM 기반 교정/요약 (Gemma E4B)
- ChromaDB + SQLite FTS5 기반 회의 검색
- 결정사항과 액션아이템을 Markdown Wiki로 정리
- Wiki 항목에서 원문 timestamp 근거 확인
- 회의 원문과 Wiki를 기반으로 검색/채팅

모든 처리는 로컬에서 이루어지는 방향으로 설계했습니다. 회의 데이터를 외부 API로 보내기 어렵거나, 조직 내부 논의 내용을 외부 서비스에 올릴 수 없는 환경을 우선 고려했습니다.

아직 초기 베타이고, Apple Silicon Mac 전용입니다. (다른 환경은 테스트가 어렵다보니...)

필요한 모델이 많아서 설치 과정도 완전히 가볍지는 않습니다.  
pyannote 화자 분리 모델을 쓰려면 HuggingFace gated model 동의와 토큰 설정이 필요하고, 로컬 모델을 쓰기 때문에 하드웨어 조건도 있습니다.

그래도 저처럼 회의가 많고, 매번 의사결정 사항을 정리하는 데 시간이 많이 들어가며, 외부 AI 연결이 어려운 환경에서 일하는 분들에게는 쓸모가 있을 수 있다고 생각해 공개했습니다.

피드백이나 비슷한 문제를 겪은 경험을 들려주시면 감사하겠습니다.

## 원문
- [원문](https://github.com/notadev-iamaura/meeting-transcriber)
- [GeekNews 토론](https://news.hada.io/topic?id=30315)

## My Note
<!-- 한 줄 코멘트 남기기 -->

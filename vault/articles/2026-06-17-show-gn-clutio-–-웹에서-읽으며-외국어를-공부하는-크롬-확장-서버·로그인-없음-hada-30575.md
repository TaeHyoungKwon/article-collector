---
category: AI
collected_at: '2026-06-17T17:12:48+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30575
id: hada-30575
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
recommended_on: '2026-06-17'
source: geeknews
tags:
- AI
- Other
- clutio.com
title: 'Show GN: Clutio – 웹에서 읽으며 외국어를 공부하는 크롬 확장 (서버·로그인 없음)'
url: https://www.clutio.com/
---

## TL;DR
- 이 글은 Clutio라는 크롬 확장을 통해 웹에서 외국어를 공부하는 방법을 다룹니다.
- 사용자가 클릭한 단어의 문맥에 맞는 뜻을 LLM이 제공하고, 이를 단어장 및 빈칸 퀴즈로 활용할 수 있습니다.
- 이 확장은 로그인이나 서버 의존 없이 개인 브라우저에 데이터가 저장되어 사용자 프라이버시를 보호합니다.

## GeekNews 요약
영문 뉴스·논문·문서를 읽다가 모르는 단어가 나오면 번역기 탭을 왔다 갔다 하게 되고,  
사전 뜻은 정작 그 문장 문맥엔 안 맞는 게 불편해서 만들었습니다.

- 아무 페이지에서 단어를 클릭하면 LLM이 '그 문장 문맥' 기준으로 뜻을 줍니다  
  (뉴스의 "lead"와 화학 문서의 "lead"가 다르게 나옴).
- 클릭한 단어 + 그 문장을 자동으로 단어장에 저장하고, 모인 걸로 빈칸 퀴즈를 만들어  
  '읽기'가 곧 복습이 되게 했습니다.

설계상 결정:

- 백엔드·로그인 없음. 단어장·퀴즈는 브라우저(IndexedDB)에만 저장되고 서버로 안 보냅니다.
- 번역 요청은 브라우저에서 Groq 무료 티어로 직접 호출(하루 약 14,400회). 단어+문장이  
  Groq로는 가지만, 제 서버를 거치는 건 아무것도 없습니다. (그래서 무료로 운영 가능)
- MV3, content script + IndexedDB. 7개 언어 지원.

한계도 솔직히: 기기 간 동기화 없음, 무료 쿼터 의존. 문맥 번역 품질·프라이버시 모델에  
대한 피드백 환영합니다.

## 원문
- [원문](https://www.clutio.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=30575)

## My Note
<!-- 한 줄 코멘트 남기기 -->

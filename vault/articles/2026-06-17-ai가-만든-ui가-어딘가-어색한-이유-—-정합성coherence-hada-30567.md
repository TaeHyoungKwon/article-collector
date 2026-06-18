---
category: AI
collected_at: '2026-06-17T10:29:07+09:00'
geeknews_comments: 5
geeknews_score: 13
geeknews_url: https://news.hada.io/topic?id=30567
id: hada-30567
matched_keywords:
- AI
read: false
recommend_score: -994.823
recommended_on: '2026-06-17'
source: geeknews
tags:
- AI
- Other
- dev.to
title: AI가 만든 UI가 어딘가 어색한 이유 — 정합성(coherence)
url: https://dev.to/kiwibreaksme/aiga-mandeun-uiga-eodinga-eosaeghan-iyu-geurigo-geugeol-gocineun-han-gaji-weoncig-5e4p
---

## TL;DR
- 이 글은 AI가 생성한 UI에서 정합성이 결여된 이유와 해결 방안을 다룹니다.
- AI가 만든 UI에서 합치면 "생성된 티"가 나는 주된 원인은 각 요소 간의 불일치, 즉 정합성의 부재입니다.
- 정합성을 높이기 위한 구체적인 방법이 제시되어 있어, 실무에서 AI를 활용한 디자인 개선에 유용한 시사점을 제공합니다.

## GeekNews 요약
AI한테 UI 시키면 컴포넌트는 멀쩡한데 합치면 "생성된 티"가 나죠.  
원인은 못생긴 부품이 아니라 부품들이 서로 안 맞는 것 — 정합성의 부재입니다.  
해법은 의외로 단순합니다 — 축마다(모서리·강조색·간격·그림자) 값을 하나만 정하고, 전부 거기 맞추는 거죠.  
Refactoring UI·Material 3·Apple HIG·WCAG 근거 + 복붙 CSS로 정리했습니다.  
직접 보는 데모: <https://styleseed-demo.vercel.app/how-it-thinks>  
오픈소스(MIT): <https://github.com/bitjaru/styleseed>

## 원문
- [원문](https://dev.to/kiwibreaksme/aiga-mandeun-uiga-eodinga-eosaeghan-iyu-geurigo-geugeol-gocineun-han-gaji-weoncig-5e4p)
- [GeekNews 토론](https://news.hada.io/topic?id=30567)

## My Note
<!-- 한 줄 코멘트 남기기 -->

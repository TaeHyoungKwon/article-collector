---
category: Other
collected_at: '2026-06-10T12:19:00+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30350
id: hada-30350
matched_keywords: []
read: false
recommend_score: 1.386
source: geeknews
tags:
- Other
- github.com/greekr4
title: 'Show GN: Playwright 봇 탐지를 우회하는 스킬'
url: https://github.com/greekr4/playwright-bot-bypass
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Playwright로 사이트에 접속하면 봇탐지에 바로 막히는 경우가 많습니다. 인터넷에 떠도는 "스텔스" 스니펫들을 붙여봤더니, 어떤 건 오히려 더 잘 걸리더군요. 그래서 8개 탐지기로 직접 측정해보고, 실제로 통과하는 조합만 골라 스킬로 만들었습니다.

설치 / 사용

- 설치: npx skills add greekr4/playwright-bot-bypass
- 사용: playwright-bot-bypass 호출

좀 의외였던 점

- 흔히 쓰는 navigator 위조(가짜 플러그인·캔버스 노이즈·webdriver 삭제 등)는 진짜 크롬과 미묘하게 안 맞아서 오히려 탐지 신호가 됩니다. 하나는 실제 크롬에서 크래시까지 났습니다
- 그래서 위조는 전부 빼고, 진짜 크롬(headed)에 맡긴 뒤 Playwright 흔적 딱 2개만 제거했습니다 (\_\_pwInitScripts 제거 + rebrowser의 CDP 누수 차단)
- 결론은 "덜 꾸밀수록 더 안 걸린다" 였습니다

피드백 환영합니다 — 특히 "이 탐지기는 못 뚫더라" 같은 제보 주시면 반영하겠습니다.

## 원문
- [원문](https://github.com/greekr4/playwright-bot-bypass)
- [GeekNews 토론](https://news.hada.io/topic?id=30350)

## My Note
<!-- 한 줄 코멘트 남기기 -->

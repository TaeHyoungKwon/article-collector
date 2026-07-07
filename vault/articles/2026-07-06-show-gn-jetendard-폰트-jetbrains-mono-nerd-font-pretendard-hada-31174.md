---
category: AI
collected_at: '2026-07-06T17:36:26+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31174
id: hada-31174
matched_keywords:
- AI
read: false
recommend_score: 3.609
recommended_on: '2026-07-07'
source: geeknews
tags:
- AI
- Other
- github.com/kuskhan
title: 'Show GN: Jetendard 폰트 (JetBrains Mono Nerd Font + Pretendard)'
url: https://github.com/kuskhan/jetendard
---

## TL;DR
- 이 글은 Jetendard 폰트의 설계 배경과 특징을 설명한다.
- Jetendard 폰트는 한글의 가독성을 높이기 위해 스케일을 조정하여 불필요한 자간 공백을 줄이고, 코딩 환경에서의 시각적 편안함을 제공한다.
- 이는 코딩 시 한글의 가독성을 향상시키며, 개발자들이 보다 효율적으로 작업할 수 있게 돕는다.

## GeekNews 요약
[여밀 폰트](https://news.hada.io/topic?id=31137) 의 소스코드를 거의 그대로 사용했습니다. 여밀 폰트와 다른 점은 [Geist mono font](https://github.com/vercel/geist-font) 대신에 [JetBrains Mono Nerd Font Mono](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/JetBrainsMono/Ligatures)를 사용했습니다.

이 폰트를 만들게 된 이유는

1. 대부분의 코딩용 고정폭 폰트에 한글 폰트가 포함되어 있지 않아 IDE 나 터미널에서 fallback 문자로 대체되면서 Unicode box-drawing 문자가 미묘하게 밀리면서 보기 흉해지는 현상이 생김.
2. 일반적으로 코딩용 고정폭 폰트에 한글 폰트를 포함하면 영문 2자가 한글 1자 보다 현저하게 크기 때문에 한글 폰트 주변에 불필요한 공백이 생기면서 한글 띄어쓰기 공백과 시각적으로 혼동되어 한글을 읽을 때 피로도가 증가함.

1번을 만족하고자 하면 2번의 문제가 생기고 2번을 만족하고자 하면 1번의 문제가 생기는 상충되는 면이 있어 모두 어느 정도 만족하고자 만들게 되었습니다.

한글 폰트의 스케일을 조금 더 키워 한글의 불필요한 자간 공백을 최대한 줄이는 방법을 선택했습니다. 어차피 공백으로 버리게 되는 공간에 글자를 좀 더 꽉 채워넣는 것입니다. 한글 글자가 좀 커보이는 현상은 있지만, 띄어쓰기가 좀 더 명확히 구분되어 한글 읽기에 편하고 글자를 키웠기에 한글 폰트 자체도 더 선명하게 보입니다.

## 원문
- [원문](https://github.com/kuskhan/jetendard)
- [GeekNews 토론](https://news.hada.io/topic?id=31174)

## My Note
<!-- 한 줄 코멘트 남기기 -->

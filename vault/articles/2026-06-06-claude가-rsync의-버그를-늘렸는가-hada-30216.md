---
category: Other
collected_at: '2026-06-06T09:13:33+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30216
id: hada-30216
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- alexispurslane.github.io
title: Claude가 rsync의 버그를 늘렸는가?
url: https://alexispurslane.github.io/rsync-analysis/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Claude 보조 릴리스**는 rsync v3.4.2와 v3.4.3 두 건뿐이며, 심각도 가중 버그/10커밋 기준으로 과거 릴리스보다 유난히 버그가 많다는 증거가 없음
- **sev/10c**는 버그 심각도 점수를 0~1로 정규화해 릴리스별로 합산하고 커밋 수로 나눈 뒤 10커밋당 값으로 환산하는 핵심 지표임
- v3.4.2는 50커밋·9개 Claude 커밋·버그 0개·0.00 sev/10c이고, v3.4.3은 34커밋·28개 Claude 커밋·버그 17개·3.29 sev/10c로 IQR 양쪽을 끼며 어느 쪽도 **이상치**가 아님
- **정확 순열 검정** p값은 46%, Fisher의 정확 검정 p값은 74%, 오즈비는 1.06으로, Claude 릴리스가 무작위 2개 릴리스보다 나쁘거나 중앙값 초과 가능성이 높다는 신호가 거의 없음
- v3.4.1은 Claude 도입 전 릴리스인데도 59버그·9커밋·39.39 sev/10c로 전체 데이터의 최악값이었으며, rsync 논란의 핵심은 **역사적 분포** 없이 단일 회귀를 Claude와 연결한 데 있음

---

## 원문
- [원문](https://alexispurslane.github.io/rsync-analysis/)
- [GeekNews 토론](https://news.hada.io/topic?id=30216)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-09T09:46:26+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31252
id: hada-31252
matched_keywords:
- AI
read: false
recommend_score: 3.307
source: geeknews
tags:
- AI
- Other
- tris.sherliker.net
title: Uniqlo 티셔츠의 난독화된 bash 스크립트 해독하기
url: https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Uniqlo 매장에서 팔린 Akamai 디자인 티셔츠에는 `base64 --decode` 결과를 `eval`로 실행하는 **난독화된 bash 코드**가 인쇄돼 있었지만, 실제로는 `Peace for All` 캠페인용 이스터에그였음
- Base64로 인코딩된 Here string을 풀면 터미널에서 `♥PEACE♥FOR♥ALL♥` 문구를 **사인파 애니메이션**으로 반복 출력하는 스크립트가 나옴
- Base64에는 오류 정정이 없어 전사가 까다로웠고, 문자열 패딩과 따옴표·중괄호가 맞는지 확인한 뒤 Android OCR, Tesseract, Claude 결과를 비교해 정리함
- 디코딩된 스크립트는 `tput`, `bc`, 256색 ANSI 이스케이프를 조합해 터미널 크기별 문자 위치와 색상을 계산하고, `CTRL+C` 종료 시 커서를 복구함
- Akamai는 뒷면의 실제 코드를 Linux와 연결해 설명했으며, 글꼴은 초기 추정인 Consolas가 아니라 **Roboto Mono**로 정정됨

---

## 원문
- [원문](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/)
- [GeekNews 토론](https://news.hada.io/topic?id=31252)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-05-13T10:03:34+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29450
id: hada-29450
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/davmlaw
title: They Live Adblocker - 영화 They Live(1988)에서 영감을 받은 광고 차단기
url: https://github.com/davmlaw/they_live_adblocker
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- They Live Adblocker는 [uBlock Origin Lite](https://github.com/uBlockOrigin/uBOL-home)의 포크로, 꾸미기 필터로 차단된 광고를 숨기는 대신 *They Live*의 구호가 적힌 **흰색 타일**로 바꿔줌
- 광고마다 **OBEY**, **CONSUME**, **WATCH TV**, **SLEEP**, **SUBMIT**, **CONFORM**, **STAY ASLEEP**, **BUY**, **WORK**, **NO INDEPENDENT THOUGHT**, **DO NOT QUESTION AUTHORITY** 중 하나가 무작위로 표시됨
- 아이디어는 2015년에 작성된 블로그 글 [*They Live adblock mode*](https://proceduralgraphics.blogspot.com/2015/04/they-live-adblock-mode.html)에서 출발했음
- 설치는 [Releases page](https://github.com/davmlaw/they_live_adblocker/releases)에서 **`uBOLite_theylive.chromium.zip`** 을 내려받아 압축을 풀고, Chromium / Chrome / Brave / Edge에서 `Load unpacked`로 확장 프로그램을 불러오는 방식임
- 기본 uBO Lite의 **Basic** 필터링 모드는 네트워크 계층에서 광고를 막기 때문에 DOM 요소가 생기지 않아 OBEY 타일로 바뀌지 않고 빈 공간만 남음
- OBEY 타일을 보려면 uBO Lite 대시보드에서 해당 사이트의 필터링 모드를 **Optimal** 또는 **Complete**로 설정한 뒤 새로고침해야 함
- 소스 빌드는 **Node 22**가 필요하며, `tools/make-mv3.sh chromium` 명령으로 Chromium용 패키지를 만들 수 있고 `firefox`, `edge`, `safari` 대상도 지정 가능함
- 동작 방식은 uBO Lite의 꾸미기 필터가 원래 주입하던 `display: none !important` CSS 대신, `data-ubol-they-live` 속성의 문구를 `::after` 오버레이로 보여주는 **흰색 박스 마스크**를 적용하는 구조임
- 늦게 로드되는 광고까지 처리하기 위해 DOM을 순회하고 **MutationObserver**로 새로 추가된 요소를 감지해, 매칭된 광고 요소에 무작위 구호를 태깅함
- 수정된 파일은 [`davmlaw/uBlock`](https://github.com/davmlaw/uBlock/tree/they-live) 서브모듈에 있으며, `they-live.js`가 구호 목록·CSS 생성·DOM 태깅을 담당하고 관련 주입 지점과 스크립트 등록 코드가 패치됨
- 개인 취미용 포크이며 공식 uBlock Origin 제품이 아니므로 관련 이슈를 uBO 쪽에 제기하지 말아야 함
- 숨겨졌던 요소를 다시 보이게 만들기 때문에 사이트 CSS가 광고 슬롯 축소를 전제로 한 경우 레이아웃이 밀릴 수 있고, 사용자 정의 꾸미기 필터와 네트워크 차단 광고는 OBEY 처리되지 않음
- 라이선스는 upstream uBlock Origin / uBO Lite와 같은 **GPL-3.0**임

## 원문
- [원문](https://github.com/davmlaw/they_live_adblocker)
- [GeekNews 토론](https://news.hada.io/topic?id=29450)

## My Note
<!-- 한 줄 코멘트 남기기 -->

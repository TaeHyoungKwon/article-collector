---
category: AI
collected_at: '2026-08-03T15:54:17+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32091
id: hada-32091
matched_keywords:
- AI
read: false
recommend_score: -996.901
recommended_on: '2026-08-04'
source: geeknews
tags:
- AI
- Other
- github.com/hsol
title: 'Show GN: 맥 파일명 자소분리를 자동으로 막아주는 메뉴바 앱을 만들었습니다 (Python · rumps · watchdog ·
  Deve...'
url: https://github.com/hsol/jaso
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
맥에서 만든 파일·폴더 이름의 한글이 윈도우에서 깨지는 자소분리를 자동으로 막아주는 메뉴바 앱입니다. 2024년에 개인용으로 만들어두고 패키징에서 막혀 묵혀뒀다가, 이번에 서명·공증 붙인 DMG로 배포했습니다.

#### 문제

맥(APFS/HFS+)은 파일명 한글을 NFD로 저장합니다. '각'을 'ㄱ + ㅏ + ㄱ'으로 쪼개서 씁니다. 윈도우와 대부분의 소프트웨어는 NFC를 씁니다. 그래서 맥에서 저장한 파일을 구글 드라이브·원드라이브로 공유하면 윈도우 쪽 화면에는 이렇게 보입니다.

ㅇㅣㄹㅓㅎㄱㅔㄷㅗㅣㅂㄴㅣㄷㅏ.txt

10년 넘게 그대로라 맥과 윈도우가 섞인 팀이면 계속 마주칩니다.

#### 기존 방식과 다른 점

반디네이머로 일괄 변환하거나 convmv -r -f utf-8 -t utf-8 --nfc . 를 돌리는 방법이 이미 있습니다. 문제는 한 번 고쳐도 끝이 아니라는 것입니다. 맥에서 파일을 하나 더 만들거나 이름만 바꿔도 그 파일은 다시 NFD가 됩니다. 변환이 일회성 이벤트라서 그렇습니다.

자소는 폴더를 등록해두면 그 안에서 생기거나 이름이 바뀌는 파일을 감시해 NFC로 되돌립니다. 상태로 유지하는 쪽이라 변환을 실행한다는 행위 자체가 없어집니다.

#### 기능

- 감시 폴더 다중 등록·해제. 등록 상태가 영속되어 앱을 다시 켜면 이어서 감시합니다
- 로그인 시 자동실행. ~/Library/LaunchAgents/tech.proofer.jaso.plist 를 만들거나 지우는 방식입니다
- 한번에 변환. 등록된 폴더를 모두 훑어 이미 깨져 있는 파일을 일괄 교정하고 폴더별 건수를 알려줍니다

#### 스택

Python 3.11, rumps(메뉴바 UI), watchdog(macOS에서는 FSEvents), PyObjC/AppKit, py2app 번들링입니다.

#### 배포

- 다운로드: <https://github.com/hsol/jaso/releases/latest>
- Apple Silicon(M1 이상) 전용, macOS 11 이상입니다. 인텔 맥에서는 실행되지 않습니다

#### 밝힐 것

- 무료이고 오픈소스(MIT)입니다.
- 실행 시 GA4로 익명 사용 통계를 보냅니다. 임의로 생성한 client\_id만 쓰고 파일명이나 경로는 보내지 않습니다

2024년에 로직까지 만들어놓고 패키징에서 막혀서, 인프런에 macOS 개발자를 구한다는 글까지 올렸는데 지원이 없었는데, 이번엔 AI 도구 붙여서 패키징·서명·공증까지 혼자 끝냈습니다. 이슈나 PR 환영합니다.

#### 개발자 정보

임한솔 / [홈페이지 방문](https://hsol.info)

## 원문
- [원문](https://github.com/hsol/jaso)
- [GeekNews 토론](https://news.hada.io/topic?id=32091)

## My Note
<!-- 한 줄 코멘트 남기기 -->

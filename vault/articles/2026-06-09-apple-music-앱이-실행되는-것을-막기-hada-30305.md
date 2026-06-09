---
category: Other
collected_at: '2026-06-09T10:09:47+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30305
id: hada-30305
matched_keywords: []
read: false
recommend_score: 1.307
source: geeknews
tags:
- Other
- lowtechguys.com
title: Apple Music 앱이 실행되는 것을 막기
url: https://lowtechguys.com/musicdecoy/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Music Decoy는 실행 중인 프로세스로 존재해, 실수로 **▶ Play**를 눌렀을 때 시스템 Music 앱이 열리지 않게 하는 앱
- 백그라운드에서 **전혀 작업하지 않고**, Music 앱과 같은 번들 식별자를 사용해 시스템이 Music 앱을 이미 실행 중으로 인식하게 만드는 방식
- v1.1부터 **mediaAppPath** 설정으로 ▶ Play 입력 시 Spotify 같은 다른 앱을 실행하도록 구성 가능
- Music 앱 자동 실행은 키보드 ▶ Play 입력, 블루투스 헤드셋 연결 후 재생 명령, 통화 종료 뒤 헤드셋이 통화 모드에서 음악 모드로 전환될 때 발생
- `rcd`는 재생 이벤트 때 현재 오디오 재생 앱이 있으면 해당 앱에 명령을 보내고, 없으면 시스템 **Music 앱**을 실행하며, 데몬 비활성화는 키보드 미디어 재생 제어까지 끄는 결과

---

## 원문
- [원문](https://lowtechguys.com/musicdecoy/)
- [GeekNews 토론](https://news.hada.io/topic?id=30305)

## My Note
<!-- 한 줄 코멘트 남기기 -->

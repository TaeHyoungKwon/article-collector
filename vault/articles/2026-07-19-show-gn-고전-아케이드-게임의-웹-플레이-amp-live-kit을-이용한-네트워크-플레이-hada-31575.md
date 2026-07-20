---
category: AI
collected_at: '2026-07-19T11:02:34+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31575
id: hada-31575
matched_keywords:
- backend
- AI
read: false
recommend_score: -995.307
recommended_on: '2026-07-20'
source: geeknews
tags:
- AI
- Other
- playarcade.to
title: 'Show GN: 고전 아케이드 게임의 웹 플레이 &amp;  Live kit을 이용한 네트워크 플레이'
url: https://playarcade.to
---

## TL;DR
- 이 글은 고전 아케이드 게임을 웹 기반에서 네트워크 플레이로 즐길 수 있는 플랫폼 개발에 대해 설명한다.
- 사용자가 mame rom을 업로드하고 관리자 승인을 통해 네트워크 게임을 지원하며, 화면 전송 방식으로 동기화 문제를 해결했다.
- 이는 고전 게임을 현대적 기술로 재현하여 사용자 경험을 확장하며, 네트워크 플레이의 가능성을 제시한다.

## GeekNews 요약
고전 mame게임을 웹으로 즐길 수 있는 사이트를 만들어 보았습니다.  
단순하게 웹으로 즐길 수 있는 사이트는 많이 있는것 같은데, 네트워크 플레이를 웹상에서 원활하게 지원하는 사이트는 없는것 같아서  
네트워크 플레이에 중점을 두고 만들어 봤습니다.

일단, 사용자가 mame rom을 업로드하면, 관리자에서, 해당 롬의 문제가 있는지 검사 후 승인하면 사용자에게 노출됩니다.  
1P, 2P를 지원하는 게임이라면, 게임의 종류와 상관없이 네트워크 플레이를 가능하게 만들어 봤습니다.

Backend : FastAPI, Radis, postgresql, wss, likvekit  
Frontend : react + vite, tailwindCss

초기에는 네트워크 플레이시에 각기 에뮬레이터를 웹에 띄우고, 사용자의 키 입력만을 전달하는 식으로 작업을 진행하였으나, 동기화 부분에서 심각한 문제가 발생했습니다. 키만 입력이 서로 전달이 되고, 캐릭터 설정이라던지. 에뮬레이터의 로딩 시간 차이 문제라던지 도저히 동기화 해서 게임 진행이 되지 않더군요. 그래서 생각한게, 네트워크 게임을 진행하면, 화면을 통채로 참여자의 브라우저에 전송시켜 버리는 방법을 생각했습니다. livekit을 생각했고, 이 상태에서, 키 입력만 웹 소켓을 통해서 서로 주고 받도록 했습니다.

그제서야 서로 동기화가 완벽하게 해결되어서 슈팅, 파이팅 게임이든지 간에 아무런 문제 없이 네트워크 게임 진행이 가능하게 되었습니다.  
문제는 네트워크 트래픽이지만요.

가볍게 즐겨 볼 수 있도록 게임 진행 이외에는 다른 기능이 없게 만들었습니다.  
한번 살펴보시고, 개선점을 알려 주시면 감사하겠습니다.

## 원문
- [원문](https://playarcade.to)
- [GeekNews 토론](https://news.hada.io/topic?id=31575)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-29T23:53:56+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31954
id: hada-31954
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-08-23'
source: geeknews
tags:
- AI
- Other
- tailscale.com
title: 탈옥한 Kindle에서 활용하는 더 많은 Tailscale 기능
url: https://tailscale.com/blog/jailbroken-kindle-proxy-tun-modes
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 탈옥한 Kindle용 Tailscale에 기본 **Tailscale SSH**, 앱별 프록시, 일부 기기를 위한 TUN 모드가 추가됨
- 일반적인 Kindle에서는 **사용자 공간 모드**의 한계로 KOReader가 `100.x.y.z` 같은 tailnet 주소에 직접 연결할 수 없었음
- 새 프록시 모드는 로컬 포트의 **SOCKS5·HTTP CONNECT** 요청을 `tailscaled`가 받아 Calibre, Wallabag 등 다른 tailnet 노드로 전달함
- 별도 **KOReader 플러그인**은 Kindle뿐 아니라 Kobo와 PocketBook에서도 콘텐츠 서버 접근에 필요한 프록시 인터페이스를 자동 생성함
- 비공식 탈옥 환경의 커뮤니티 코드인 만큼 **기기별 호환성 차이**가 있으며 직접 설치하고 설정해야 함

---

## 원문
- [원문](https://tailscale.com/blog/jailbroken-kindle-proxy-tun-modes)
- [GeekNews 토론](https://news.hada.io/topic?id=31954)

## My Note
<!-- 한 줄 코멘트 남기기 -->

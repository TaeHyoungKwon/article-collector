---
category: Other
collected_at: '2026-07-26T08:30:12+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31813
id: hada-31813
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- kitsumed.github.io
title: Android가 기기 내 ADB를 곧 제한할 수 있음
url: https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Google의 공식 발표가 아닌 진행 중인 **IssueTracker 기능 요청**에서 ADB 핵심 유지보수 담당자가 악용 방지를 위해 로컬 연결을 제한하고 `wlan0`에만 바인딩하는 방안을 거론함
- `wlan0`만 허용하면 루프백 주소 `127.0.0.1`을 이용하는 **기기 내 ADB**는 물론 VPN·Ethernet 기반 ADB와 여러 개발 환경까지 작동하지 않을 수 있음
- 논의는 Wireless ADB 인증을 완전히 우회한 **CVE-2026-0073**에서 시작됐으며, 원래 요청은 ADBD의 수신 인터페이스를 선택해 모든 네트워크에 노출되지 않도록 하자는 것임
- 일반적인 악성 앱은 ADBD를 직접 시작하거나 Wireless ADB 페어링·TCP/IP 승인을 단독으로 마칠 수 없어, 사용자의 **수동 조작** 없이는 ADB 권한을 얻기 어려움
- 루프백 연결을 영구 차단하면 Shizuku와 libadb-android 기반 도구가 영향을 받으므로, 기본 차단을 재부팅 후에도 해제할 수 있는 **사용자 선택 설정**이 필요함

---

## 원문
- [원문](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/)
- [GeekNews 토론](https://news.hada.io/topic?id=31813)

## My Note
<!-- 한 줄 코멘트 남기기 -->

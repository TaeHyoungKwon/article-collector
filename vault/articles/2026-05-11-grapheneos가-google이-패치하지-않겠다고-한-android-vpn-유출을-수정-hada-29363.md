---
category: Other
collected_at: '2026-05-11T00:33:51+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29363
id: hada-29363
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- cyberinsider.com
title: GrapheneOS가 Google이 패치하지 않겠다고 한 Android VPN 유출을 수정
url: https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **GrapheneOS**가 Android의 “Always-On VPN”과 “Block connections without VPN”이 켜져 있어도 실제 IP 주소가 유출될 수 있는 VPN 우회 취약점을 새 업데이트에서 수정함
- 취약점은 Android 16 네트워킹 스택의 **QUIC 연결 종료** 기능에서 비롯됐으며, 일반 앱이 표준 권한만으로 UDP 페이로드를 system\_server에 등록할 수 있었음
- 앱의 UDP 소켓이 파괴되면 권한 있는 **system\_server**가 저장된 페이로드를 VPN 터널이 아닌 물리 네트워크 인터페이스로 직접 보내 VPN 잠금 보호를 우회함
- Google은 해당 문제를 “**Won’t Fix (Infeasible)**” 및 “NSBC”로 분류했고, Android 보안 권고 기준을 충족하지 않는다고 판단해 기존 입장을 유지함
- GrapheneOS는 release 2026050400에서 “registerQuicConnectionClosePayload optimization”을 비활성화했으며, 2026년 5월 Android 보안 패치, hardened\_malloc 개선, Linux 커널 업데이트, libpng CVE-2026-33636 백포트 수정도 포함함

---

## 원문
- [원문](https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/)
- [GeekNews 토론](https://news.hada.io/topic?id=29363)

## My Note
<!-- 한 줄 코멘트 남기기 -->

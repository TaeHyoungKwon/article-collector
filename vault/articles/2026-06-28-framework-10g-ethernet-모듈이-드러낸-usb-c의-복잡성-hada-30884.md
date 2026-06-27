---
category: AI
collected_at: '2026-06-28T01:36:04+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30884
id: hada-30884
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- jeffgeerling.com
title: Framework 10G Ethernet 모듈이 드러낸 USB-C의 복잡성
url: https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- WisdPi의 **10G Ethernet Expansion Card**는 Framework 확장 슬롯에 꽂는 10GbE 모듈이지만, 실제 성능은 USB-C 포트의 세부 규격과 드라이버에 크게 좌우됨
- Realtek **RTL8159** 컨트롤러가 10Gbps에 가까운 속도를 내려면 USB 3.2 Gen 2x2, 즉 20Gbps 연결이 필요해 USB4 일부 구성과 USB 3.2 Gen 2x1에서는 병목이 생김
- Framework 13 AMD Ryzen AI 5 340에서는 Windows 11도 기대 속도에 못 미쳤고 Linux는 더 낮았으며, Framework 12도 기본 드라이버에서는 `iperf3`가 약 **7Gbps**에 그침
- Windows에서 Realtek 드라이버를 설치하자 Framework 12는 **9.4Gbps 이상**을 기록했지만, 양방향 전송과 발열에서는 여전히 제약이 남음
- 대부분의 사용자는 약 $40의 2.5Gbps **Ethernet Expansion Card**가 더 현실적이며, 외장 USB-C 동글 없이 더 빠른 유선망이 필요할 때만 $99 WisdPi 10G Card를 고려할 만함

---

## 원문
- [원문](https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/)
- [GeekNews 토론](https://news.hada.io/topic?id=30884)

## My Note
<!-- 한 줄 코멘트 남기기 -->

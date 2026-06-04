---
category: AI
collected_at: '2026-06-04T09:36:33+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30159
id: hada-30159
matched_keywords:
- AI
read: false
recommend_score: 3.307
source: geeknews
tags:
- AI
- Other
- blog.nns.ee
title: 'Pwnd Blaster: 스피커를 전혀 만지지 않고 스피커로 PC 해킹하기'
url: https://blog.nns.ee/2026/06/03/katana-badusb/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Creative Sound Blaster Katana V2X**는 Bluetooth 범위 약 15m 안의 공격자가 페어링이나 물리 접촉 없이 CTP 명령과 펌웨어 업데이트를 실행해 감시 장치나 원격 Rubber Ducky처럼 바꿀 수 있음
- USB의 **CTP**는 정적 키 기반 challenge-response 인증을 요구하지만, Bluetooth 경로는 GATT characteristic을 통해 같은 CTP 명령을 인증 없이 받아 정보 읽기와 설정 변경을 허용함
- 펌웨어 컨테이너는 `FBOOT`, `FMAIN`, `CHK2`로 구성되며, **서명 검증 없이** SHA-256 체크섬인 `CHK2`만 맞으면 패치된 펌웨어를 수락함
- PoC는 BLE로 약 10분 동안 커스텀 펌웨어를 업로드한 뒤 재부팅된 스피커가 USB **HID 키보드**처럼 `echo pwned`를 입력하고 실행하게 만들었음
- **Creative**는 SingCERT를 통한 연락 뒤 “사이버보안 위험을 제시하지 않는다”며 취약점으로 보지 않았고, 최신 펌웨어는 취약하며 CTP-over-Bluetooth를 막는 비공식 패치만 제공됨

---

## 원문
- [원문](https://blog.nns.ee/2026/06/03/katana-badusb/)
- [GeekNews 토론](https://news.hada.io/topic?id=30159)

## My Note
<!-- 한 줄 코멘트 남기기 -->

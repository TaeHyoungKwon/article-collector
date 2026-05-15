---
category: Other
collected_at: '2026-05-15T10:28:01+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29530
id: hada-29530
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- tomshardware.com
title: Microsoft BitLocker – YellowKey 제로데이 익스플로잇
url: https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Chaotic Eclipse의 **YellowKey**는 USB 파일과 Windows 복구 환경만으로 BitLocker 잠금 드라이브 접근을 가능하게 함
- Tom's Hardware 테스트에서 `System Volume Information`에 `FsTx` 파일을 복사하고 **Shift+Restart** 후 `Control` 키를 누르는 절차가 동작함
- 재부팅 뒤 질문이나 메뉴 없이 **상승 권한 명령줄**로 진입했고, BitLocker로 잠긴 드라이브에 키 입력 없이 전체 접근 가능했음
- Alice 드라이브를 Bob 기기로 옮겨 여는 방식은 어려워 보이나, 기기 자체를 훔치면 대상 **TPM**을 그대로 이용할 수 있어 위험이 커짐
- SecurityOnline에 따르면 YellowKey는 **Windows Server 2022·2025**에서도 동작하지만 Windows 10에서는 동작하지 않음

---

## 원문
- [원문](https://www.tomshardware.com/tech-industry/cyber-security/microsoft-bitlocker-protected-drives-can-now-be-opened-with-just-some-files-on-a-usb-stick-yellowkey-zero-day-exploit-demonstrates-an-apparent-backdoor)
- [GeekNews 토론](https://news.hada.io/topic?id=29530)

## My Note
<!-- 한 줄 코멘트 남기기 -->

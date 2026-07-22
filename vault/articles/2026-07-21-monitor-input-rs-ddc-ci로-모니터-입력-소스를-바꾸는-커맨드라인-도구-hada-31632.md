---
category: Backend
collected_at: '2026-07-21T09:31:02+09:00'
geeknews_comments: 6
geeknews_score: 10
geeknews_url: https://news.hada.io/topic?id=31632
id: hada-31632
matched_keywords:
- backend
read: false
recommend_score: -995.018
recommended_on: '2026-07-21'
source: geeknews
tags:
- Backend
- Other
- github.com/kojiishi
title: monitor-input-rs - DDC/CI로 모니터 입력 소스를 바꾸는 커맨드라인 도구
url: https://github.com/kojiishi/monitor-input-rs
---

## TL;DR
- monitor-input-rs는 DDC/CI 프로토콜을 통해 모니터의 입력 소스를 커맨드라인에서 쉽게 전환할 수 있는 도구이다.
- 사용자는 특정 모니터를 지정하고 입력 소스를 토글하는 다양한 기능을 지원받아 다중 모니터 환경에서 유연하게 설정을 관리할 수 있다.
- 이는 윈도우, 맥, 리눅스 사용자들이 더 효율적으로 작업할 수 있도록 도와주며, 특히 다중모니터 환경에서 유용한 솔루션이 된다.

## GeekNews 요약
- **DDC/CI** 프로토콜로 모니터의 입력 소스(DisplayPort, HDMI, USB-C 등)를 커맨드라인에서 전환하는 도구로, **윈/맥/리눅스** 모두 지원
- 이름/인덱스 뒤에 `=입력소스` 를 붙여 입력 소스를 직접 지정가능
  - `monitor-input Dell=dp1` → "Dell" 포함 모니터 전부를 DisplayPort1로 설정
  - `monitor-input 0=usbc1` → 첫번째 모니터를 USB-C1으로 설정
- 인자 없이 실행하면 연결된 모든 모니터 목록을 출력하며, 각 항목에 이름/현재 **Input Source**/**Backend** 필드 표시
- 이름 일부 또는 **인덱스(숫자)** 로 특정 모니터를 검색/조회 가능
  - `monitor-input Dell` 은 이름에 "Dell" 포함 모니터 전체 나열, `monitor-input 2` 는 인덱스 2번 모니터 조회
- 입력 소스에 숫자를 넣어 비표준 **벤더 특정(vendor-specific)** 입력 소스에도 대응
  - `monitor-input U2723=15 P3223=17`
- 쉼표(`,`)로 두 개 이상의 소스를 등록해 현재 상태에 따라 순차 전환하는 **토글/사이클 기능** 지원
  - `P3223=hdmi1,usbc2` → HDMI1과 USBC2 사이 토글, `hdmi1,usbc2,dp1` 처럼 3개 이상 순환도 가능
- 다중모니터 토글 기능: 여러 모니터를 동시에 전환할 때 **첫 번째 모니터의 현재 입력 소스**를 기준으로 나머지를 맞춰 입력 소스 일관성 유지
  - `monitor-input U2723=dp1,usbc2 P3223=hdmi1,usbc2` 에서 첫 모니터 `U2723`의 입력 소스가 `DisplayPort1`이면 `UsbC2`로 변경
  - 첫 모니터가 목록의 두 번째 소스로 바뀌면, 이후 모니터들도 각자 목록의 **두 번째 소스**로 변경됨 (예: `P3223`은 `UsbC2`)
- Windows에서는 `-F winapp` 옵션으로 콘솔 창이 뜨지 않는 **서브시스템 버전(monitor-inputw.exe)** 제공, 오류는 토스트 알림으로 표시
- 커맨드라인 실행 외에 **라이브러리(as library)** 형태로도 노출되어 다른 Rust 코드에서 직접 호출 가능

## 원문
- [원문](https://github.com/kojiishi/monitor-input-rs)
- [GeekNews 토론](https://news.hada.io/topic?id=31632)

## My Note
<!-- 한 줄 코멘트 남기기 -->

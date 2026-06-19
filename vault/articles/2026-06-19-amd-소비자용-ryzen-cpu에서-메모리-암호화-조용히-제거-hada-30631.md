---
category: Other
collected_at: '2026-06-19T10:01:15+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30631
id: hada-30631
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- tomshardware.com
title: AMD, 소비자용 Ryzen CPU에서 메모리 암호화 조용히 제거
url: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 소비자용 Ryzen CPU에서 **Transparent Secure Memory Encryption(TSME)** 지원이 새 AGESA 펌웨어 이후 사라져, 사용자가 메모리 암호화 보호 상태 변화를 알아차리기 어려운 상황임
- TSME는 OS 개입 없이 전체 RAM을 암호화해 **cold-boot exploit**, DRAM 인터페이스 스누핑, 메모리 모듈 제거 같은 물리적 공격을 막는 기능임
- Ben Kilpatrick의 GitHub 조사와 MSI 제어 테스트에서는 소비자용 Ryzen 칩이 구형 펌웨어에서 TSME를 활성화했지만, **AGESA 1.2.7.0**에서는 “not supported”로 표시됨
- AMD는 TSME가 “AMD PRO Technologies의 일부로 PRO CPU에만 적용되는 보안 기능”이라고 답했으며, AMD 엔지니어는 추가 질문에 **더 공유할 정보가 없다**고 답함
- 물리적 접근 공격을 우려하는 사용자는 AMD가 지원 범위를 명확히 하거나 복원하지 않는 한 **Ryzen Pro 또는 EPYC** 시스템을 선택해야 함

---

## 원문
- [원문](https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change)
- [GeekNews 토론](https://news.hada.io/topic?id=30631)

## My Note
<!-- 한 줄 코멘트 남기기 -->

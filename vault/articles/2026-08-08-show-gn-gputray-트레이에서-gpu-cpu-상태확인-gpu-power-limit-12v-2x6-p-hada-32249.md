---
category: Other
collected_at: '2026-08-08T07:26:08+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32249
id: hada-32249
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/kirinonakar
title: 'Show GN: GpuTray - 트레이에서 GPU/CPU 상태확인, GPU power limit, 12V-2x6 pin monitoring'
url: https://github.com/kirinonakar/GPUtray
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
GPU 상태를 확인할 때마다 HWiNFO나 Afterburner 같은 프로그램을 열어두는 게 번거로워서 만든 가벼운 Windows 시스템 트레이 모니터링 도구입니다.

트레이의 16x16 아이콘 자체가 실시간 그래프로 동작하며 CPU, RAM, GPU, VRAM, GPU 온도, 12V-2x6 핀 전류 중 최대 5개 항목을 동시에 표시할 수 있습니다.

#### 주요 기능

- CPU / RAM / GPU / VRAM / GPU 온도를 시스템 트레이에서 실시간 그래프로 표시
- 사용률에 따라 Green / Yellow / Red로 색상 변경
- 우클릭하면 상세 그래프 대시보드 표시
- 모니터링 데이터를 CSV로 실시간 저장
- NVIDIA GPU는 NVML을 이용해 온도 및 전력 관련 정보 확인
- GPU Power Limit을 BIOS 기본 TDP의 70~100% 범위에서 조절
- 설정한 Power Limit을 Windows 로그인 시 자동 적용 가능

#### ASUS ROG Astral 전용 기능

ASUS ROG Astral의 12V-2x6 전원 커넥터 상태도 확인할 수 있도록 기능을 추가했습니다.

카드에 탑재된 IT8915FN 센서를 NVAPI I2C를 통해 읽어 6개 핀의 전류를 각각 모니터링합니다.

특정 핀이 0A가 되거나 9.2A를 초과하면 경고를 표시할 수 있고, 사용자가 확인하면 GPU를 50% 이상 사용 중인 프로세스를 종료하는 보호 기능도 선택적으로 사용할 수 있습니다.

#### 구현

C++17 + Win32 API 기반으로 만들었고 GDI+, PDH, DXGI, NVML 등을 사용합니다.

Windows 10/11에서 사용할 수 있으며 MIT License로 공개했습니다.

사용해 보시고 피드백 남겨주시면 정말 감사하겠습니다!

GitHub 레포지토리 (다운로드 및 소스코드): <https://github.com/kirinonakar/GPUtray>

개인 홈페이지 (다른 개발 앱들도 구경해 보세요!): <https://kirinonakar.github.io/>

## 원문
- [원문](https://github.com/kirinonakar/GPUtray)
- [GeekNews 토론](https://news.hada.io/topic?id=32249)

## My Note
<!-- 한 줄 코멘트 남기기 -->

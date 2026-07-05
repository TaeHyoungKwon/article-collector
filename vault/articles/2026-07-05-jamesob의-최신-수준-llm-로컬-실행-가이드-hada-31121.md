---
category: AI
collected_at: '2026-07-05T00:40:46+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31121
id: hada-31121
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-07-05'
source: geeknews
tags:
- AI
- Other
- github.com/jamesob
title: Jamesob의 최신 수준 LLM 로컬 실행 가이드
url: https://github.com/jamesob/local-llm
---

## TL;DR
- 이 글은 Jamesob의 로컬 실행을 위한 최신 수준 LLM과 음성-텍스트 변환 구성 방법을 설명한다.
- 약 40,000달러의 예산으로 4× RTX PRO 6000을 사용해 P2P 성능 향상을 통해 Gen4 라인레이트에 도달할 수 있다.
- 이를 통해 독자는 고성능 AI 모델 실행을 위한 하드웨어 최적화와 구체적인 사양 설정 방법을 배울 수 있다.

## GeekNews 요약
- 로컬에서 **최신 수준 LLM**과 음성-텍스트 변환을 돌리기 위한 하드웨어 구성, PCIe 스위치 설정, Docker 실행 구성을 한 저장소에 정리함
- 약 **$2k** 예산은 2× RTX 3090으로 48GB VRAM을 확보해 Qwen3.6-27B와 `whisper-large-v3` 기반 로컬 STT를 실행하는 구성을 목표로 함
- 약 **$40k** 예산은 4× RTX PRO 6000 Blackwell Workstation으로 384GB VRAM을 확보해 Claude Opus에 꽤 가까운 모델 지능을 얻는 구성을 전제로 함
- 실제 4× RTX 6000 Pro 시스템은 중고 EPYC/DDR4 기반 본체와 **c-payne PCIe Gen4 스위치**를 조합해 GPU 간 P2P 통신을 CPU 루트 컴플렉스 대신 스위치 패브릭 안에서 처리함
- BIOS, GRUB, ACS, 전력 제한 설정까지 맞춘 결과 P2P는 **27.5GB/s 단방향**, 50.4GB/s 양방향, 0.37–0.45µs 지연으로 Gen4 라인레이트에 도달함

---

## 원문
- [원문](https://github.com/jamesob/local-llm)
- [GeekNews 토론](https://news.hada.io/topic?id=31121)

## My Note
<!-- 한 줄 코멘트 남기기 -->

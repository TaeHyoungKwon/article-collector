---
category: Other
collected_at: '2026-07-10T09:32:01+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31283
id: hada-31283
matched_keywords: []
read: false
recommend_score: 1.609
source: geeknews
tags:
- Other
- github.com/5uck1ess
title: tts-bench - 로컬에서 TTS 모델 비교를 위한 벤치마크
url: https://github.com/5uck1ess/tts-bench
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **로컬 TTS 모델 55종**을 어떤 하드웨어에서든 세 가지 관점으로 비교하는 오픈소스 벤치마크
- **Speed(속도)/Listen(청취)/Scores(객관 지표)** 세 렌즈로 구성, CPU/CUDA/Apple Silicon에서 측정
  - Speed는 콜드/웜 **TTFA**(첫 오디오까지 시간), **RTF**(실시간 대비 배속), 메모리를 측정
  - Listen은 모든 모델·프롬프트를 기본 음성 + 복제로 인라인 재생, 귀로 직접 모델 선택
  - Scores는 **UTMOS**(자연스러움)·**WER**(명료도)·**SIM**(복제 충실도)를 seed-tts-eval 방식으로 채점
- 설치 없이 모든 모델을 들어볼 수 있는 **Demos 사이트** 제공, 프롬프트별/모델별 탐색 가능
- 55종 중 **41종이 참조 클립으로 음성 복제(voice cloning)** 가능, 참조 형식 3종 지원(wav 단독 / wav + 전사 / HF 게이트 wav)
- 한국어는 전체 55종이 모두 지원하는 것은 아니지만, **Supertonic, VoxCPM, OmniVoice** 등 다국어/한국어 지원 모델이 포함
  - 다만 기본 벤치 프롬프트는 영어/프랑스어 중심이라, 한국어 품질을 보려면 별도 한국어 문장으로 Listen/compare를 돌려 귀로 확인하는 편이 나음
  - 테스트 결과 위 Supertonic, VoxCPM, OmniVoice 는 들을만한 품질을 보여줌
- **복제 A/B 투표 상위** — OmniVoice(음색 일치 최상위, 단 단어 뭉갬/누락 가능), Echo-TTS(공동 1위급, 44.1kHz), IndexTTS-2(3위, 억양 유지)
- 벤치 코드는 MIT 라이선스, 각 TTS 모델은 개별 라이선스 적용

## 원문
- [원문](https://github.com/5uck1ess/tts-bench)
- [GeekNews 토론](https://news.hada.io/topic?id=31283)

## My Note
<!-- 한 줄 코멘트 남기기 -->

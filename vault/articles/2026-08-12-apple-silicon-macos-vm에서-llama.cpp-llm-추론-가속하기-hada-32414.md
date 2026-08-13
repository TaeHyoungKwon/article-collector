---
category: AI
collected_at: '2026-08-12T05:33:11+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32414
id: hada-32414
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-08-12'
source: geeknews
tags:
- AI
- Other
- github.com/trycua
title: Apple Silicon macOS VM에서 llama.cpp LLM 추론 가속하기
url: https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Apple `Virtualization.framework`의 가상 GPU가 보수적인 Metal 기능을 보고해 llama.cpp가 느린 커널을 선택하던 문제를, 게스트 프로세스 한정 **호환성 계층**으로 우회해 최대 16.36배 가속함
- 호환성 계층은 `supportsFamily:` 응답을 **Apple family 9**까지 허용하고 최대 threadgroup 메모리를 32KB에서 64KB로 높여 SIMD-group reduction·matrix와 bfloat16 경로를 활성화함
- M1 Ultra에서 TinyLlama 1.1B는 프롬프트 처리와 토큰 생성이 각각 **11.08배·16.36배** 빨라졌고, Gemma 4 12B는 7.20배·14.54배, Muse Glimmer 30B는 7.55배·8.87배 향상됨
- 물리 GPU 할당이나 VFIO passthrough가 아니라 기존 Apple 가상 GPU 경로의 기능 응답만 바꾸는 방식이며, **MLX-LM은 기본 VM에서도 빨라** 성능 차이가 거의 없었음
- 사설 Metal 구현에 의존하는 **실험적 연구 릴리스**로, M1 Ultra와 지정된 Tahoe 환경만 검증됐으며 Apple Silicon 세대·macOS 버전·Metal API별 추가 검증이 필요함

---

## 원문
- [원문](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md)
- [GeekNews 토론](https://news.hada.io/topic?id=32414)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-08-13T12:00:03+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32456
id: hada-32456
matched_keywords:
- AI
- LLM
read: false
recommend_score: 5.099
source: geeknews
tags:
- AI
- Other
- unsloth.ai
title: Unsloth, Qwen3.8 2.4T를 397GB로 줄여 로컬 실행 지원
url: https://unsloth.ai/docs/models/qwen3.8
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Unsloth가 **Qwen3.8-2.4T-A95B의 GGUF 양자화 모델과 로컬 실행 가이드**를 공개
- BF16 원본은 **4.89TB**지만 Dynamic 1-bit 버전은 **397GB**까지 축소해 약 91% 크기를 줄임
- 1-bit부터 8-bit/BF16까지 다양한 버전을 제공하며 2-bit 약 657GB, 3-bit 956GB, 4-bit 1.31TB 수준
- 모든 레이어를 똑같이 줄이지 않고 중요한 레이어는 더 높은 정밀도를 유지하는 **Unsloth Dynamic 양자화**를 적용
- 2.4T 전체 파라미터 중 토큰당 95B를 활성화하는 MoE 모델로, 양자화해도 일반 PC보다는 **수백 GB 메모리를 갖춘 고사양 워크스테이션** 대상
- Unsloth Desktop에서 Mac/Windows/Linux로 실행할 수 있으며 RAM 오프로딩과 멀티 GPU 구성도 지원
- **llama.cpp/Ollama/LM Studio/vLLM/SGLang** 등을 통한 실행과 자체 API 서빙도 가능
- 로컬 API로 띄운 뒤 Pi/OpenClaw/Hermes 같은 에이전트 도구의 모델 백엔드로 연결하는 방법도 안내
- 즉 Qwen3.8 Max급 모델을 작은 PC에서 돌린다는 의미보다는, **데이터센터급 모델의 자체 실행 범위를 워크스테이션까지 넓힌 것**에 가까움
- Qwen 개발팀에 따르면 [**Qwen3.8-27B**를 이번 주 공개할 예정](https://x.com/QwenDevs/status/2087154835741364507)이라고 하니, 개인용은 이 **27B 버전이 훨씬 현실적인 선택지**가 될 것

## 원문
- [원문](https://unsloth.ai/docs/models/qwen3.8)
- [GeekNews 토론](https://news.hada.io/topic?id=32456)

## My Note
<!-- 한 줄 코멘트 남기기 -->

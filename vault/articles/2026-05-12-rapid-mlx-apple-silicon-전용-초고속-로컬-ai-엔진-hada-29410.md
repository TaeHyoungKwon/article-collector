---
category: AI
collected_at: '2026-05-12T09:46:02+09:00'
geeknews_comments: 3
geeknews_score: 12
geeknews_url: https://news.hada.io/topic?id=29410
id: hada-29410
matched_keywords:
- AI
- LLM
- Claude Code
read: false
recommend_score: 8.981
source: geeknews
tags:
- AI
- Other
- github.com/raullenchai
title: Rapid-MLX - Apple Silicon 전용 초고속 로컬 AI 엔진
url: https://github.com/raullenchai/Rapid-MLX
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 애플 실리콘 맥에서 **로컬 AI 모델을 구동**하는 추론 엔진으로, Apple의 **MLX 프레임워크** 기반 네이티브 Metal 컴퓨트 커널 활용
- Ollama 대비 최대 **4.2배 빠른 추론 속도** - Phi-4 Mini 14B 기준 180 tok/s(Ollama 56 tok/s 대비 3.2배), Qwen3.5-9B 기준 108 tok/s(Ollama 41 tok/s 대비 2.6배)
- 캐시된 상태에서 **TTFT 0.08초**(Kimi-Linear-48B 기준), 대부분 모델에서 0.1~0.3초 수준
- **17개 도구 호출 파서** 내장 및 모델명 기반 자동 감지 — 4bit 양자화 모델이 깨진 도구 호출을 텍스트로 출력해도 자동으로 구조화된 형식으로 복구
- 16GB MacBook Air(Qwen3.5-4B, 160 tok/s)부터 256GB Mac Studio Ultra(DeepSeek V4 Flash 158B, 31 tok/s, 1M 컨텍스트)까지 **RAM별 최적 모델 매핑** 제공
  - **16GB** MacBook Air/Pro: Qwen3.5-4B 4bit → 2.4GB RAM 사용, 160 tok/s, 채팅·코딩·도구 호출 가능
  - **24GB** MacBook Pro: Qwen3.5-9B 4bit → 5.1GB, 108 tok/s, 범용 모델
  - **32GB** Mac Mini/Studio: Qwen3.5-27B 4bit(15.3GB, 39 tok/s), Nemotron-Nano 30B 4bit(18GB, **141 tok/s**, 100% 도구 호출), Qwen3.6-35B-A3B 4bit(20GB, 95 tok/s, **256 MoE expert, 262K 컨텍스트**)
  - **48~64GB**: Qwen3.5-35B-A3B 8bit → 37GB, 83 tok/s, **스마트+빠름의 최적 균형**
  - **96GB+**: Qwen3.5-122B mxfp4 → 65GB, 57 tok/s, 프론티어급 지능
  - **128GB+**: DeepSeek V4 Flash 158B-A13B 2-bit DQ → 91GB, 56 tok/s, day-0 프론티어 MoE
  - **192~256GB**: Qwen3.5-122B 8bit(130GB, 44 tok/s) 또는 DeepSeek V4 Flash 8-bit(136GB, 31 tok/s, **1M 컨텍스트**)
  - 4bit는 메모리 절약(대부분 권장), 8bit는 고품질 추론, mxfp4는 고품질 4bit 포맷
- chain-of-thought 모델의 추론 과정을 별도 `reasoning_content` 필드로 분리하는 **추론 분리** 기능 - Qwen3, DeepSeek-R1, MiniMax, GPT-OSS 포맷 지원
- 표준 트랜스포머용 **KV 캐시 트리밍**과 Qwen3.5 하이브리드 아키텍처용 **DeltaNet 상태 스냅샷**(~0.1ms 복원)으로 멀티턴 대화 TTFT 2~5배 개선, 별도 플래그 없이 항상 활성화
- 로컬 프리필이 느린 대규모 컨텍스트 요청을 GPT-5, Claude 등 클라우드 LLM으로 자동 전환하는 **스마트 클라우드 라우팅** 지원
- **OpenAI API 드롭인 대체** — Cursor, Claude Code, Aider, LangChain, PydanticAI, smolagents, Hermes Agent, Open WebUI 등 OpenAI 호환 앱이면 `localhost:8000/v1`로 즉시 연동
- Vision(Gemma 4, Qwen-VL), Audio(TTS/STT), Embeddings, Gradio Chat UI, 스키마 제약 JSON 생성 등 **멀티모달 및 옵션 확장** 지원
- TurboQuant V-cache(86% 메모리 절감), KV 캐시 양자화, 프리필 청킹, tool logits bias 등 **다양한 최적화 기법** 내장
- 모델+에이전트 하네스 호환성을 측정하는 **MHI(Model-Harness Index)** 제공 — Qwopus 27B가 MHI 92로 최고 점수
- Speculative Decode(1.5~2.3배), EAGLE-3(3~6.5배), ReDrafter(1.4~1.5배) 등 **추가 가속 기법**이 로드맵에 포함
- Apache 2.0 라이선스

## 원문
- [원문](https://github.com/raullenchai/Rapid-MLX)
- [GeekNews 토론](https://news.hada.io/topic?id=29410)

## My Note
<!-- 한 줄 코멘트 남기기 -->

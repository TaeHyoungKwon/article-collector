---
category: AI
collected_at: '2026-07-27T10:07:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=31856
id: hada-31856
matched_keywords:
- backend
- AI
- LLM
read: false
recommend_score: 7.386
recommended_on: '2026-07-28'
source: geeknews
tags:
- AI
- Other
- netflixtechblog.com
title: Netflix의 사내 LLM 서빙 플랫폼
url: https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c
---

## TL;DR
- 넷플릭스는 LLM을 기존 ML 인프라에서 통합하여 운영하는 서빙 플랫폼을 개발했다.
- 선택된 vLLM은 사용자 정의 모델 지원과 디버깅 용이성을 제공하며, 안정적인 배포를 위한 여러 전략을 적용했다.
- 이 접근 방식은 넷플릭스의 ML 시스템의 유연성을 높이고, 기술적 간극을 보완하여 효율적인 모델 운영을 가능하게 한다.

## GeekNews 요약
- 넷플릭스는 LLM을 별도 사일로로 분리하지 않고 기존 ML 인프라에서 함께 운영하며, **vLLM과 Triton**을 통합 서빙 체계에 연결함
- 기본 엔진으로 선택한 **vLLM**은 사용자 정의 모델 지원, 디버깅 용이성, 확장 훅, 연구 환경과의 친숙성을 갖췄으며, Triton의 vLLM backend로 모델과 프런트엔드의 결합도 줄임
- 기존 gRPC와 OpenAI 호환 API를 함께 제공하지만 `response_format` 누락, Triton·vLLM 버전 불일치, 비표준 모델 처리처럼 **프로덕션에서 드러난 간극**을 직접 보완해야 했음
- 안정적인 배포에는 비용이 낮은 **Red-Black 전략**을 우선 적용하고, 호환되지 않는 I/O 변경이 불가피할 때만 여러 버전을 동시에 유지하는 Versioned 전략을 사용함
- 요청별 제약을 디코딩 루프에서 강제하는 로짓 프로세서를 vLLM V1의 배치 처리와 멀티스레드 C++로 재구현했으며, 앞으로 GPU 융합 커널·비동기 스케줄링·저정밀 모델로 확장할 계획임

---

## 원문
- [원문](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c)
- [GeekNews 토론](https://news.hada.io/topic?id=31856)

## My Note
<!-- 한 줄 코멘트 남기기 -->

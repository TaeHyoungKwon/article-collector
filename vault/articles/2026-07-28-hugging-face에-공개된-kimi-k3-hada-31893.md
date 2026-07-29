---
category: AI
collected_at: '2026-07-28T09:55:02+09:00'
geeknews_comments: 2
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31893
id: hada-31893
matched_keywords:
- AI
- LLM
read: false
recommend_score: -994.977
recommended_on: '2026-07-29'
source: geeknews
tags:
- AI
- Other
- huggingface.co
title: Hugging Face에 공개된 Kimi-K3
url: https://huggingface.co/moonshotai/Kimi-K3
---

## TL;DR
- Kimi-K3는 2.8조 개의 매개변수를 가진 오픈 가중치 멀티모달 AI 모델이다.
- 이 모델은 Kimi K2보다 2.5배 높은 스케일링 효율을 제공하며, 다양한 작업을 지원한다.
- Kimi-K3의 공개와 최신 기술은 AI 모델 개발에 있어 효율성과 성능 개선의 새로운 기준을 설정할 수 있다.

## GeekNews 요약
- **Kimi K3**는 2.8조 개 매개변수와 104만 8,576토큰 컨텍스트를 갖춘 오픈 가중치 네이티브 멀티모달 에이전트 모델로, 장시간 코딩·지식 작업·추론을 지원함
- **Kimi Delta Attention(KDA)**, Attention Residuals, Stable LatentMoE를 결합해 896개 전문가 중 토큰마다 16개를 활성화하며, Kimi K2보다 전체 스케일링 효율이 약 2.5배 높음
- 공개 평가에서 GPQA Diamond 93.5, Terminal-Bench 2.1 88.3, BrowseComp 91.2, OmniDocBench 91.1을 기록했지만, 모델별 하네스·추론 설정·하드웨어 차이를 함께 고려해야 함
- **MXFP4 가중치·MXFP8 활성값**으로 양자화 인식 학습됐으며 Transformers, vLLM, SGLang, Docker와 OpenAI·Anthropic 호환 API로 실행할 수 있음
- 다중 턴과 도구 호출에서는 API가 반환한 `reasoning_content`와 `tool_calls`를 포함한 전체 assistant 메시지를 그대로 다시 전달해야 하며, 코드와 가중치는 **Kimi K3 License**로 공개됨

---

## 원문
- [원문](https://huggingface.co/moonshotai/Kimi-K3)
- [GeekNews 토론](https://news.hada.io/topic?id=31893)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-13T17:54:48+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30454
id: hada-30454
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 8.901
recommended_on: '2026-06-13'
source: geeknews
tags:
- AI
- Other
- marktechpost.com
title: Moonshot AI가 Kimi K2.7-Code를 출시했습니다.
url: https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/
---

## TL;DR
- 문샷 AI는 코딩 성능을 향상시킨 에이전트 중심의 모델 '키미 K2.7-Code'를 출시했다.
- K2.7-Code는 1조 개의 매개변수를 가진 혼합 전문가 모델로, 이전 모델보다 코딩 성능을 대폭 개선하고 참조 토큰 사용량을 30% 줄였다.
- 이 모델의 출시는 소프트웨어 엔지니어링 작업에 대한 효율성을 높이고, 서버급 배포를 통해 실용적인 응용을 가능하게 한다.

## GeekNews 요약
> 문샷 AI가 이전 모델 대비 코딩 성능을 대폭 향상시키고 추론 토큰 소모량을 30% 줄인 에이전트 중심의 오픈 가중치 코딩 모델 '키미 K2.7-Code'를 출시했습니다.

---

#### 전문 번역

이번 주, 문샷 AI(Moonshot AI)가 키미 K2.7-Code(Kimi K2.7-Code)를 출시했습니다. 이는 코딩에 특화된 에이전트 중심의 모델입니다. 모델 가중치는 수정된 MIT 라이선스에 따라 허깅페이스(Hugging Face)에 배포됩니다. 또한 키미 API와 키미 코드를 통해서도 사용할 수 있습니다. K2.7-Code는 일반적인 대화가 아닌 장기적인 소프트웨어 엔지니어링 작업을 목표로 합니다. 이 모델은 여러 단계에 걸쳐 계획을 수립하고, 코드를 수정하며, 도구를 실행하고, 디버깅을 수행합니다. 문샷 AI는 이 모델을 구독형 코딩 플랫폼과 결합하여 제공합니다.

##### 키미 K2.7-Code 스펙

K2.7-Code는 혼합 전문가(MoE, Mixture-of-Experts) 모델입니다. 총 1조(1T) 개의 매개변수(파라미터)를 보유하고 있으며, 토큰당 320억(32B) 개의 매개변수가 활성화됩니다. 이 구조는 총 384개의 전문가 중 토큰당 8개의 전문가가 선택되고 1개의 전문가가 공유되는 방식을 사용합니다. Dense 레이어 1개를 포함하여 총 61개의 레이어로 구성되어 있습니다.

어텐션 메커니즘에는 MLA가 사용되었으며, 피드포워드 경로에는 SwiGLU가 적용되었습니다. MoonViT 비전 인코더는 이미지 및 비디오 입력을 위해 4억(400M) 개의 매개변수를 추가합니다. 이 모델은 네이티브 INT4 양자화가 적용된 상태로 제공됩니다. 컨텍스트 창은 256K 토큰(262,144)입니다. 두 가지 제약 사항이 있습니다. 생각 모드(Thinking mode)는 필수 사항이며, 이를 비활성화하면 API 오류가 반환됩니다. 샘플링 매개변수는 온도(temperature) 1.0, top\_p 0.95, n 1, 페널티 0.0으로 고정되어 있습니다. 기본 최대 출력은 32,768 토큰입니다. vLLM, SGLang, KTransformers를 사용하여 자체 호스팅할 수 있습니다. 허깅페이스 리포지토리의 크기는 디스크 기준 약 595GB로 매우 큽니다. 이는 노트북용 모델이 아닌 서버급 배포를 겨냥한 타겟입니다.

##### 벤치마크 점수

문샷 팀은 6가지 벤치마크 결과를 발표했습니다. 이들은 K2.7-Code를 K2.6, GPT-5.5, 클로드 오푸스 4.8(Claude Opus 4.8)과 비교했습니다. K2.7-Code는 모든 항목에서 K2.6을 능가했습니다. 코딩 부문에서 가장 큰 상승을 보인 것은 Kimi Code Bench v2로, 기존 50.9%에서 62.0%로 상승했습니다.

K2.7-Code는 MCP Mark Verified 벤치마크에서 81.1%를 기록하며 오푸스 4.8의 76.4%를 제쳤습니다. 또한 MLS Bench Lite에서는 GPT-5.5에 근접한 수치를 기록했습니다. K2.7-Code는 Kimi Code CLI에서 실행되었으며, GPT-5.5는 Codex xhigh, 오푸스 4.8은 Claude Code xhigh 환경에서 테스트되었습니다.

## 원문
- [원문](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/)
- [GeekNews 토론](https://news.hada.io/topic?id=30454)

## My Note
<!-- 한 줄 코멘트 남기기 -->

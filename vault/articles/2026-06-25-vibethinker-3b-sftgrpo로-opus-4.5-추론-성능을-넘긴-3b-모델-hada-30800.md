---
category: AI
collected_at: '2026-06-25T05:41:04+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30800
id: hada-30800
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.901
recommended_on: '2026-06-24'
source: geeknews
tags:
- AI
- Other
- arxiv.org
title: 'VibeThinker-3B: SFT+GRPO로 Opus 4.5 추론 성능을 넘긴 3B 모델'
url: https://arxiv.org/abs/2606.16140
---

## TL;DR
- VibeThinker-3B는 3B 파라미터로 높은 추론 성능을 달성하기 위한 연구를 다룬다.
- 이 모델은 다양한 학습 기법을 결합하여 DeepSeek V3.2 등 주요 모델과 유사한 성능을 보인다.
- 연구 결과는 소형 모델이 높은 효율성을 유지하면서도 강력한 추론 능력을 갖출 수 있음을 시사한다.

## GeekNews 요약
- **VibeThinker-3B**는 3B 파라미터만으로 검증 가능한 추론을 어디까지 압축할 수 있는지 실험한 소형 밀집 모델임
- 학습 파이프라인은 **Spectrum-to-Signal** 사후학습을 바탕으로 커리큘럼 지도 미세조정, 다중 도메인 강화학습, 오프라인 자기증류를 결합함
- AIME26은 94.3점, **CLR** 적용 시 97.1점을 기록했고 LiveCodeBench v6 Pass@1 80.2, 최근 미공개 LeetCode 콘테스트 수락률 96.1%도 보고됨
- DeepSeek V3.2, GLM-5, Gemini 3 Pro 같은 훨씬 큰 플래그십 모델과 비슷하거나 더 높은 성능대에 들어가면서도, IFEval 93.4점으로 **엄격한 지시 제어성**을 유지함
- **Parametric Compression-Coverage Hypothesis**는 검증 가능한 추론은 작은 reasoning core에 압축될 수 있지만, 개방형 지식과 범용 역량에는 더 넓은 파라미터 커버리지가 필요하다고 봄

---

## 원문
- [원문](https://arxiv.org/abs/2606.16140)
- [GeekNews 토론](https://news.hada.io/topic?id=30800)

## My Note
<!-- 한 줄 코멘트 남기기 -->

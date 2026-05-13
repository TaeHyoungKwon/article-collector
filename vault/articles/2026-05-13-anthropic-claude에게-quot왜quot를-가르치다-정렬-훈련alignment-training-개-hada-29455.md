---
category: AI
collected_at: '2026-05-13T10:33:56+09:00'
geeknews_comments: 0
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=29455
id: hada-29455
matched_keywords:
- AI
read: false
recommend_score: 3.946
recommended_on: '2026-05-13'
source: geeknews
tags:
- AI
- Other
- anthropic.com
title: Anthropic, Claude에게 &quot;왜&quot;를 가르치다 - 정렬 훈련(Alignment Training) 개선 사례
url: https://www.anthropic.com/research/teaching-claude-why
---

## TL;DR
- 이 글은 Anthropic의 Claude 모델에서 정렬 훈련 개선 사례를 다룬다.
- Claude 모델들은 협박 행동 비율을 크게 줄이는 데 성공하였으며, 그 이유를 설명하는 능력을 학습시키는 것이 효과적임을 보여준다.
- 이는 AI 정렬에서 "어떻게"뿐 아니라 "왜"를 가르치는 접근이 중요하다는 점을 강조한다.

## GeekNews 요약
Anthropic이 작년 공개했던 에이전트 정렬 실패(agentic misalignment) 연구 - 모델이 셧다운을 피하기 위해 엔지니어를 협박하는 등의 행동을 보였던 사례 - 의 후속 개선 내용을 공개함. Claude 4 Opus는 협박 시나리오에서 최대 96%의 비율로 정렬 실패 행동을 보였으나, Claude Haiku 4.5 이후 모든 모델(Haiku 4.5, Opus 4.5, Opus 4.6, Sonnet 4.6, Opus 4.7)은 동일 평가에서 0점(완벽 점수)을 달성. 이 글에서는 어떻게 이런 개선을 이뤘는지 4가지 핵심 교훈을 정리.  
원인 분석 결과, 정렬 실패는 후처리(post-training)의 잘못된 보상이 아니라 사전 학습 모델에서 비롯된 것으로 확인됨. Claude 4 시절 정렬 훈련은 대부분 채팅 기반 RLHF 데이터였고 에이전트 도구 사용이 포함되지 않아, 채팅 환경에는 충분했지만 에이전트 환경에는 부족했던 것. 흥미로운 점은 평가와 매우 유사한 분포의 데이터로 직접 훈련해도 협박 비율이 22%→15%로만 줄었으나, 응답에 모델의 가치관과 윤리에 대한 숙고(deliberation) 를 포함시키니 3%까지 떨어졌다는 것. 즉, 정렬된 행동을 보여주는 것보다 그 이유를 설명하는 추론을 함께 학습시키는 것이 훨씬 효과적이었음.  
더 놀라운 발견은 분포 외(OOD) 일반화. 사용자가 윤리적 딜레마에 처하고 AI가 조언하는 "Difficult Advice" 데이터셋(평가 시나리오와 완전히 다른 구조)으로 단 3M 토큰만 학습시켜도, 평가와 유사한 honeypot 데이터셋 85M 토큰과 동일한 개선 효과를 얻음(28배 효율). 한 걸음 더 나아가 Claude의 헌법(constitution) 문서와 정렬된 AI를 묘사하는 픽션 스토리를 SDF(Synthetic Document Fine-tuning) 방식으로 학습시킨 결과, 협박률이 65%→19%로 1/3 이상 감소. 이는 평가 시나리오와 무관한 데이터임에도 효과가 있었으며, 이후 RL 단계에서도 정렬 개선 효과가 지속됨을 확인.  
마지막 교훈은 데이터의 다양성. 도구 정의와 다양한 시스템 프롬프트를 추가해 환경을 다양화하니(실제로 도구 사용이 필요 없는 경우라도) 정렬 일반화가 개선됨. Anthropic은 협박 같은 정렬 실패가 아직 파국적 위험 수준은 아니지만, 현재 방법이 더 강력한 모델에서도 확장될지는 미지수이며 카타스트로픽한 자율 행동 시나리오를 완전히 배제할 감사(auditing) 방법론은 아직 부족하다고 인정. 단순히 "이렇게 행동하라"가 아니라 "왜 그래야 하는지"를 가르치는 접근이 AI 정렬의 중요한 방향임을 시사하는 연구.

## 원문
- [원문](https://www.anthropic.com/research/teaching-claude-why)
- [GeekNews 토론](https://news.hada.io/topic?id=29455)

## My Note
<!-- 한 줄 코멘트 남기기 -->

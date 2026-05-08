---
category: AI
collected_at: '2026-05-09T04:37:03+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29302
id: hada-29302
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- anthropic.com
title: 'Natural Language Autoencoders: Claude의 생각을 텍스트로 바꾸기'
url: https://www.anthropic.com/research/natural-language-autoencoders
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **NLA** 는 Claude 내부 활성값을 사람이 읽을 수 있는 자연어 설명으로 바꿔, 모델이 말로 드러내지 않는 내부 상태를 해석하려는 방법
- NLA는 동결된 **target model**에서 활성값을 뽑고, **activation verbalizer(AV)** 가 이를 텍스트로 설명한 뒤 **activation reconstructor(AR)** 가 설명에서 활성값을 복원하는 왕복 구조로 학습됨
- Anthropic은 agentic misalignment 같은 안전성 시뮬레이션에서 NLAs로 Claude의 말로 드러나지 않은 **평가 인식**을 확인했으며, 파괴적 행동 테스트에서는 16%, **SWE-bench Verified**에서는 26%의 문제에서 평가받고 있음을 인식하는 징후가 나타남
- 의도적으로 잘못 정렬된 Claude Haiku 3.5 변형을 대상으로 한 **auditing game**에서 NLAs를 갖춘 auditor는 숨겨진 동기를 주입한 훈련 데이터 없이도 근본 동기를 12%~15% 찾아냈고, NLAs가 없을 때 승률은 3% 미만이었음
- NLAs는 설명이 틀리거나 환각을 만들 수 있고 훈련·추론 비용이 크다는 한계가 있으며, Anthropic은 [Neuronpedia 데모](http://neuronpedia.org/nla), [full paper](https://transformer-circuits.pub/2026/nla/index.html), [code](https://github.com/kitft/natural_language_autoencoders)를 공개함

---

## 원문
- [원문](https://www.anthropic.com/research/natural-language-autoencoders)
- [GeekNews 토론](https://news.hada.io/topic?id=29302)

## My Note
<!-- 한 줄 코멘트 남기기 -->

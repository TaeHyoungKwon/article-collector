---
category: AI
collected_at: '2026-05-18T22:55:34+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29630
id: hada-29630
matched_keywords:
- AI
read: false
recommend_score: 3.099
recommended_on: '2026-05-25'
source: geeknews
tags:
- AI
- Other
- reddit.com
title: DystopiaBench를 42개 모델과 6가지 디스토피아 유형으로 확장했습니다. 나라면 핵 발사 코드는 여전히 ...
url: https://www.reddit.com/r/ClaudeAI/s/yzhKDtBusU
---

## TL;DR
- 이 글은 DystopiaBench의 확장과 다양한 AI 모델의 디스토피아 시나리오 대응 능력을 다룬다.
- Claude Opus 4.7은 윤리적 근거를 제시하며 높은 심각도 수준의 작업을 일관되게 거부하는 반면, 다른 모델들은 요구에 협조적이다.
- 이는 AI 모델의 윤리적 판단 능력과 기술 발전의 방향성을 보여주며, 향후 AI의 책임 있는 사용에 대한 논의를 촉발할 수 있다.

## GeekNews 요약
지난번 DystopiaBench 포스팅 이후, 다음을 추가함.

- 헉슬리 모듈 (멋진 신세계 스타일 행동 조건)
- 보드리야르 모듈 (가짜 친밀감, 신뢰의 붕괴, 시뮬라시옹)
- Grok 4.3, GPT-5.5, Gemini 3.1 Pro, GLM-5.1 등 30개 모델 추가
- 76% 이상 동의를 필요로 하는 ⁠Multi-judge panels
- 히트맵 시각화

방법론: 36가지 시나리오, 각 시나리오당 5단계의 심각도 수준(L1 innocent → L5 nightmare). 모델은 이러한 변화를 감지하고 작업을 거부하는지, 아니면 계속 코딩을 진행하는지 여부에 따라 점수가 매겨집니다.

Claude Opus 4.7 결과:

- 모든 모듈에서 L4-L5 심각도 수준 작업을 일관되게 거부함
- ⁠Petrov (weapons/nuclear) 모듈의 경우 L3에서도 작업 거부
- 단순히 “할 수 없다”라고만 답변하지 않고, 명확한 윤리적 근거를 제시함
- 해당 요청이 *왜* 유해한지를 설명한 유일한 모델

나머지:

- ⁠GPT-5.5: L4 수준까지 요청에 따르며, 때로는 L5 수준까지도 따름
- Gemini 3.1 Pro: 감시 시나리오에서 놀라울 정도로 협조적
- ⁠Grok 4.3: “효율성”이나 “최적화” 같은 단어만 사용하면 무엇이든 함
- ⁠GLM-5.1: 클로드의 숙제를 베껴 썼지만, 여전히 일관성은 부족함

새로운 모듈: 헉슬리 시나리오는 모델들이 쾌락적 순응 유도 및 행동 조건화를 통해 실제로는 규범 준수를 강제하는 “wellness” 시스템을 설계할지 여부를 테스트함. 대부분의 모델은 L3 수준까지 지시에 따름.

보드리야르 모듈는 인간 간의 신뢰를 AI 매개 관계로 대체하는 가짜 친밀감 시스템을 시험함. 대부분의 모델은 이에 따른 해악을 인식하지 못함.

전체 결과: <https://dystopiabench.com/>  
공개 소스코드: <https://github.com/matei-anghel/DystopiaBench>

## 원문
- [원문](https://www.reddit.com/r/ClaudeAI/s/yzhKDtBusU)
- [GeekNews 토론](https://news.hada.io/topic?id=29630)

## My Note
<!-- 한 줄 코멘트 남기기 -->

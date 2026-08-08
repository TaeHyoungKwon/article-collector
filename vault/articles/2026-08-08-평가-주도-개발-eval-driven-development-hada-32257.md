---
category: AI
collected_at: '2026-08-08T10:03:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32257
id: hada-32257
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
recommended_on: '2026-08-08'
source: geeknews
tags:
- AI
- Other
- medium.com
title: 평가 주도 개발 (Eval-driven development)
url: https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Airbnb는 비결정적 출력과 주관적 정답, 검색·추론·도구 호출의 연쇄 실패를 다루기 위해 평가를 사후 검증이 아닌 **핵심 엔지니어링 규율**로 취급함
- **평가 주도 개발(EDD)** 은 실제 오류를 발견해 평가 기준으로 만들고 지속적으로 검사하며, 출시 목표와 게이트를 먼저 정하고 최종 인간 의사결정자를 둠
- 결정론적 검사, **LLM 심판(LLM-as-a-Judge)**, 인간 평가를 계층적으로 사용하며, 가상 심판은 나쁜 사례를 포함한 50~100개 골든 데이터셋에서 인간과 80% 후반~90%대 일치하도록 보정해야 함
- 에이전트 시스템은 최종 답변만으로 평가할 수 없으므로 **실행 추적과 스팬**을 재구성해 하위 에이전트 호출 시점, 도구 선택, 매개변수와 중간 상태까지 검사해야 함
- 프로덕션에서도 비식별화된 실사용 트래픽을 지속적으로 표본 추출하고 새 실패 유형을 평가에 반영해야 하며, 좋은 모델보다 **명확한 제품 기준과 팀 협업**이 성공을 좌우함

---

## 원문
- [원문](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788)
- [GeekNews 토론](https://news.hada.io/topic?id=32257)

## My Note
<!-- 한 줄 코멘트 남기기 -->

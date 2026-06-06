---
category: AI
collected_at: '2026-06-05T09:02:38+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30186
id: hada-30186
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -995.099
recommended_on: '2026-06-05'
source: geeknews
tags:
- AI
- Other
- anthropic.com
title: Anthropic은 제품 전반에서 Claude를 어떻게 봉쇄할까
url: https://www.anthropic.com/engineering/how-we-contain-claude
---

## TL;DR
- 이 글은 Anthropic이 Claude의 잠재적 피해를 봉쇄하기 위한 아키텍처 구축 방안을 다룬다.
- 에이전트의 능력과 접근성을 확대함에 따라 위험이 증가하므로 containment 방식의 중요성이 강조된다.
- 모델 계층보다 환경 계층에서 봉쇄를 설계해야 한다는 교훈은 안전성을 높이는 데 중요한 시사점을 제공한다.

## GeekNews 요약
- 에이전트의 능력과 접근권한이 커질수록 **잠재적 피해 반경** 도 함께 확대되며, 클로드 웹/Claude Code/Cowork 각각에 맞춘 봉쇄 아키텍처 구축 경험을 정리
- 위험은 **실패 가능성**과 **피해 규모** 두 요소로 구성되며, 안전장치와 모델 학습으로 첫 번째는 낮아졌지만 두 번째는 능력·접근 확대에 따라 계속 증가
- 행동을 감독하는 **human-in-the-loop** 방식은 승인 피로 탓에 한계가 있어, 에이전트가 *할 수 있는 범위* 자체를 제한하는 **containment(봉쇄)** 에 가장 큰 공을 들임
- claude.ai의 **임시 컨테이너**, Claude Code의 **사람 개입 샌드박스**, Cowork의 **로컬 VM** 세 가지 격리 패턴을 사용자별 특성에 맞춰 적용
- 가장 큰 교훈은 **모델 계층보다 환경 계층에서 먼저 봉쇄를 설계**해야 하며, 직접 만든 커스텀 구성 요소가 가장 취약한 지점이라는 점

---

## 원문
- [원문](https://www.anthropic.com/engineering/how-we-contain-claude)
- [GeekNews 토론](https://news.hada.io/topic?id=30186)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-07-28T22:37:04+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31913
id: hada-31913
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/humanlayer
title: SlopCodeBench로 본 Opus 5의 장기 코딩 성능
url: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 요구사항이 단계적으로 추가되는 **장기 코딩 벤치마크**에서 Opus 5는 17개 체크포인트 중 4개만 엄격 통과해, 지속적인 개입 없이 코드베이스를 발전시키기에는 아직 신뢰하기 어려운 수준임
- SlopCodeBench는 체크포인트마다 새 요구사항을 공개하고 이전 회귀 테스트까지 모두 통과해야 성공으로 인정해, 일회성 문제 해결보다 **장기 유지보수 능력**을 측정함
- Opus 5의 엄격 통과율은 **24%** 로 Opus 4.8과 Sonnet 5의 6%보다 높았지만, 세 모델 모두 쉬움·중간·어려움 문제에서 마지막 체크포인트까지 결함 없이 도달하지 못함
- Opus 5는 Opus 4.8보다 함수·호출 가능 단위를 5배, 프로덕션 코드를 약 1.8배 많이 작성했으며, 모든 모델에서 진행할수록 **복잡도·장황함·코드 냄새**가 증가함
- 단일 코드 품질 지표보다 **누적 명세 전체의 통과율**이 유지보수성을 현실적으로 보여주며, 잘 격리된 반복 개발 벤치마크에서 80% 이상을 기록해야 무인 실행에 대한 신뢰가 크게 높아질 수 있음

---

## 원문
- [원문](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md)
- [GeekNews 토론](https://news.hada.io/topic?id=31913)

## My Note
<!-- 한 줄 코멘트 남기기 -->

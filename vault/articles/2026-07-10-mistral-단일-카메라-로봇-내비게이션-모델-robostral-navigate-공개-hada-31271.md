---
category: AI
collected_at: '2026-07-10T00:34:14+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31271
id: hada-31271
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-09-01'
source: geeknews
tags:
- AI
- Other
- mistral.ai
title: Mistral, 단일 카메라 로봇 내비게이션 모델 Robostral Navigate 공개
url: https://mistral.ai/news/robostral-navigate/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 로봇이 **RGB 카메라 하나**와 자연어 지시만으로 복잡한 환경을 이동하도록 만든 Mistral의 첫 **8B embodied navigation 모델**임
- R2R-CE validation unseen에서 **76.6% 성공률**을 기록해 단일 카메라 방식뿐 아니라 depth·다중 카메라 기반 최고 시스템보다도 높은 성능을 냄
- 현재 화면의 목표 **이미지 좌표**와 도착 시 방향을 예측하는 pointing 방식을 쓰며, 시야 밖 목표는 로봇 로컬 좌표계의 변위 명령으로 대체함
- 기존 오픈소스 VLM에 의존하지 않고 사내에서 구축했으며, 시뮬레이션으로 만든 약 **40만 개 trajectory**와 6,000개 scene으로 학습함
- prefix-caching으로 학습 토큰을 22배 줄이고, 이후 **CISPO 온라인 강화학습**으로 성공률을 3.2% 더 끌어올림

---

## 원문
- [원문](https://mistral.ai/news/robostral-navigate/)
- [GeekNews 토론](https://news.hada.io/topic?id=31271)

## My Note
<!-- 한 줄 코멘트 남기기 -->

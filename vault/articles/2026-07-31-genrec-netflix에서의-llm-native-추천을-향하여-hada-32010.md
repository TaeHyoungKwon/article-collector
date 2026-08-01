---
category: AI
collected_at: '2026-07-31T12:45:15+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32010
id: hada-32010
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.307
recommended_on: '2026-08-01'
source: geeknews
tags:
- AI
- Other
- netflixtechblog.com
title: 'GenRec: Netflix에서의 LLM-native 추천을 향하여'
url: https://netflixtechblog.com/genrec-towards-llm-native-recommendation-at-netflix-f20be6f643e3
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
• 생산 모델의 복잡성 해결: 넷플릭스의 기존 추천 시스템은 수천 개의 수작업 피처와 복잡한 아키텍처에 의존하여 새로운 유스케이스 추가 비용이 높았으나, 대형 언어 모델(LLM) 기반의 GenRec이 이를 대체하기 위해 개발되었습니다.  
• GenRec의 핵심 파이프라인: GenRec은 사용자 이력, 아이템 메타데이터, 맥락을 자연어 프롬프트로 변환(Verbalization)하고, 넷플릭스 전용 데이터로 파인튜닝된 파운데이션 LLM과 카탈로그 인식 점수 산정 헤드(Scoring Head)를 결합하여 추천 순위를 생성합니다.  
• 2단계 학습 프레임워크: Phase 1에서는 오픈소스 LLM을 넷플릭스 코퍼퍼스로 적응시켜 콘텐츠와 행동 패턴을 학습하며, Phase 2에서는 랭킹 데이터와 보상 목표를 바탕으로 포스트 트레이닝을 수행합니다.  
• 컨텍스트 엔지니어링의 도입: 토큰 예산 제약을 해결하기 위해 고신호 상호작용은 유지하고 저신호 이벤트는 생략하거나 반복 행동을 압축하는 컨텍스트 엔지니어링을 적용하여 품질 저하 없이 토큰과 비용을 크게 절감했습니다.  
• 보상 가중 랭킹 목적 함수: 장기적 회원 만족도 프록시와 비즈니스 목표(콘텐츠 유형 및 출시 단계별 재조정)를 반영한 보상 가중 손실 함수를 사용하여 단순 클릭을 넘어선 최적화를 달성했습니다.  
• vLLM 기반 프리필 전용 추론: vLLM을 활용한 내부 LLM 서빙 스택에서 오토레그레시브 디코딩 대신 프리필 전용(prefill-only) 모드로 실행하여 후보군 전체의 점수를 단일 포워드 패스로 계산함으로써 서빙 비용을 최적화했습니다.  
• 온라인 A/B 테스트 성과: 약 10%의 트래픽을 대상으로 진행한 4주간의 대규모 A/B 테스트에서, GenRec은 기존 프로덕션 순위 모델 대비 훨씬 적은 Phase-2 라벨드 데이터와 입력 신호만을 사용하고도 단기 및 장기 온라인 지표에서 통계적으로 유의미한 개선을 기록했습니다.

## 원문
- [원문](https://netflixtechblog.com/genrec-towards-llm-native-recommendation-at-netflix-f20be6f643e3)
- [GeekNews 토론](https://news.hada.io/topic?id=32010)

## My Note
<!-- 한 줄 코멘트 남기기 -->

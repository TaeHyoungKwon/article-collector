---
category: AI
collected_at: '2026-06-25T10:46:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30813
id: hada-30813
matched_keywords:
- AI
- LLM
read: false
recommend_score: -994.901
recommended_on: '2026-06-25'
source: geeknews
tags:
- AI
- Other
- llm-router.cafe24.com
title: Cafe24, LLM Router 공개
url: https://llm-router.cafe24.com/
---

## TL;DR
- 이 글은 Cafe24에서 공개한 통합 LLM 인프라인 LLM Router에 대해 다루고 있다.
- LLM Router는 100개 이상의 모델을 단일 API로 호출하고, 비용 최적화를 위한 다양한 기능을 제공한다.
- 이 기술은 개발자들이 API 통합 작업을 단순화하고 비용 관리를 개선할 수 있는 이점을 제공한다.

## GeekNews 요약
- Claude, Gemini, Qwen, Llama, DeepSeek 등 **100개 이상 모델**을 **단일 엔드포인트**로 호출하는 통합 LLM 인프라
- **OpenAI 호환 단일 API**를 제공해, Provider마다 다른 API 명세·재시도 로직·스트리밍 포맷을 따로 학습/유지할 필요 없음
- **Auto Router**가 프롬프트를 분석해 코딩/추론/번역/창작 유형을 판별하고 최적 비용의 모델 자동 선택
  - 예: "React 무한 스크롤 코드 만들어줘" → 코딩 감지 → claude-sonnet-4-6
- **Auto Fallback**으로 장애·타임아웃 시 사전 정의된 대체 경로로 즉시 전환, 실패한 호출은 과금 제외(ZCI)
  - 예: qwen3-72b → llama-3.3-70b → deepseek-v3
- **Provider Routing**으로 비용·속도·처리량 기준에 맞춰 프로바이더 우선순위 설정 가능
- **BYOK**(Bring Your Own Key) 모드로 보유 중인 OpenAI/Anthropic/Google 키를 그대로 등록해 비용 직접 통제 가능
- **Semantic Cache**로 유사 질문은 LLM 호출 자체를 스킵해 토큰 비용 절감, 응답은 ms 단위 반환
- **Preset** 기능으로 Primary 모델·System Prompt·Sampling·다단계 Fallback 체인을 묶어 저장, 호출은 한 줄이고 조정은 콘솔에서 처리해 코드 재배포 ZERO
- **Privacy & 거버넌스**로 로그·모델 전달 데이터의 민감 정보(PII) 자동 마스킹 지원
- **Realtime Dashboard**에서 요청·비용·토큰 추이, 모델별 비용 비중, 성공/실패 비율, 요청 단위 상세 로그 확인
- **Playground**에서 코드 없이 모델별 응답 품질·속도·비용 즉시 비교
- 약정·구독 없는 **크레딧 종량제**, 월 기본요금 0원, 가입 즉시 무료 크레딧 제공, 원화 기반 과금 및 세금계산서 발행 지원

## 원문
- [원문](https://llm-router.cafe24.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=30813)

## My Note
<!-- 한 줄 코멘트 남기기 -->

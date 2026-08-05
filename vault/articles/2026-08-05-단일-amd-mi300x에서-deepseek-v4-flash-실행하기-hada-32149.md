---
category: AI
collected_at: '2026-08-05T03:31:57+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32149
id: hada-32149
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.901
recommended_on: '2026-08-05'
source: geeknews
tags:
- AI
- Other
- github.com/ryanzhou
title: 단일 AMD MI300X에서 DeepSeek V4 Flash 실행하기
url: https://github.com/ryanzhou/deepseek-v4-flash-mi300x
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 304B 매개변수의 **DeepSeek-V4-Flash-0731**을 추가 가중치 양자화나 오프로딩 없이 단일 AMD MI300X에서 프로덕션 운영하기 위한 구성과 패치를 제공함
- MI300X의 **192GB HBM3**에 156.67GiB 가중치와 20GB GPU KV 캐시를 배치하고, 퇴거된 프리픽스 캐시는 96GiB CPU 계층에 저장함
- 고정된 vLLM ROCm·AITER 스택에서 단일 스트림 디코드 중앙값 **168.6 tok/s**, 8개 스트림 합계 542 tok/s, 64개 버스트 합계 830 tok/s를 기록했으며 256K 컨텍스트를 검증함
- MI300X의 FNUZ FP8 형식, 고동시성 MoE 라우팅, 인과적 추측 검증, CPU-KV 동기화, 누락된 `gfx942` 커널 튜닝을 **읽기 전용 오버레이**와 AITER 튜닝 테이블로 보완함
- 성능 수치는 고정된 이미지와 프롬프트에 대한 검증 기준이며, HBM 사용량이 205.8GB 중 약 204.5GB에 달하므로 KV 풀 확대보다 메모리 여유·콜드 및 캐시 경로의 정확성 검증이 중요함

---

## 원문
- [원문](https://github.com/ryanzhou/deepseek-v4-flash-mi300x)
- [GeekNews 토론](https://news.hada.io/topic?id=32149)

## My Note
<!-- 한 줄 코멘트 남기기 -->

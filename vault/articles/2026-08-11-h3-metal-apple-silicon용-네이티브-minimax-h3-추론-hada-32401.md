---
category: Other
collected_at: '2026-08-11T19:32:18+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32401
id: hada-32401
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/antirez
title: H3-metal - Apple Silicon용 네이티브 MiniMax-H3 추론
url: https://github.com/antirez/h3.c
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **h3-metal**은 Apple Silicon에서 MiniMax-H3의 프롬프트·이미지·영상·오디오 기반 생성 기능을 네이티브로 실행하며, 현재 M3 Max와 M5 Max의 Metal 성능 및 메모리 최적화에 집중함
- 대화형 세션은 BF16 프롬프트 조건, DiT, 영상 디코더를 메모리에 유지하며 **첫/마지막 프레임 조건**과 순서가 보존되는 Ref2VA 참조를 지원함
- 속도와 품질은 디노이징 횟수, DiT 블록 수, 전체 디노이저 또는 코어 재사용, **토큰 축소**, 내부 렌더링 해상도를 독립적으로 조절해 선택함
- M5 Max의 512×512·22프레임 테스트에서 4회 디노이징은 약 **3.5초**가 걸렸고, 토큰 축소는 검증된 `45 layers + reuse 2` 구성을 16.69초에서 12.60초로 줄였으나 구도나 세부 표현이 달라질 수 있음
- M5에서는 int8 MLP·QKV·attention 출력과 TensorOps 경로를 사용하고, 모델 단계를 나눠 적재해 **33B Transformer**, Qwen 인코더, 디코더가 통합 메모리에 동시에 존재하지 않도록 함

---

## 원문
- [원문](https://github.com/antirez/h3.c)
- [GeekNews 토론](https://news.hada.io/topic?id=32401)

## My Note
<!-- 한 줄 코멘트 남기기 -->

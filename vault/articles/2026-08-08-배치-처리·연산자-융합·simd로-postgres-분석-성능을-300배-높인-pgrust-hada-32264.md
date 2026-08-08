---
category: Other
collected_at: '2026-08-08T20:09:22+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32264
id: hada-32264
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- malisper.me
title: 배치 처리·연산자 융합·SIMD로 Postgres 분석 성능을 300배 높인 pgrust
url: https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- pgrust 0.2는 쿼리 엔진을 중심으로 성능을 개선해 이전 버전보다 **10배**, OLTP에서 Postgres보다 30%, ClickBench에서 **300배** 빠르며 ClickHouse도 앞섬
- Postgres의 행 단위 **Volcano 실행 모델**은 각 행마다 런타임에 결정되는 `next()`를 호출해 함수 호출 비용이 크고 CPU 파이프라이닝 같은 최적화를 활용하기 어려움
- 5억 개의 `float8` 값을 더하는 축소 실험에서 1.3초가 걸린 행 단위 실행을 **배치 처리로 480ms**, 연산자 융합으로 358ms, SIMD로 135ms까지 단축함
- 스택 버퍼를 사용하는 배치는 할당과 호출 횟수를 줄이고, **연산자 융합**은 스캔과 집계를 합쳐 복사를 없애며, SIMD는 여러 값을 동시에 처리함
- 모든 쿼리 조합에 최적화된 융합 코드를 미리 준비할 수 없어 **JIT 컴파일**이 필요하며, 부동소수점 SIMD는 덧셈 순서가 달라져 결과에 미세한 차이가 생길 수 있음

---

## 원문
- [원문](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/)
- [GeekNews 토론](https://news.hada.io/topic?id=32264)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-07-28T09:58:03+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31895
id: hada-31895
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- nikolays.github.io
title: PGSimCity - PostgreSQL의 작동 방식을 탐험 가능한 3D 도시로 시각화
url: https://nikolays.github.io/PGSimCity/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- PostgreSQL의 연결/백엔드/공유 메모리/WAL/스토리지/체크포인트/autovacuum/복제를 **건물과 구역으로 표현한 3D 교육용 시뮬레이션**으로, 각 건물과 애니메이션이 실제 데이터베이스 메커니즘에 대응함
- `shared_buffers`의 clock-sweep 교체, WAL 기록과 플러시, 체크포인트 페이싱, xmin 지평선과 테이블 팽창 등 **내부 동작을 느린 시간 척도로 관찰**할 수 있도록 수치와 규모를 축소함
- 실제 PostgreSQL 코드를 실행하는 에뮬레이터가 아니라 손으로 작성한 모델이며, PostgreSQL 문서와 소스를 기준으로 세 차례 전문 검토와 별도 시각적 감사를 거치고 **210개 테스트**로 주요 계산과 제한값을 고정함
- 버퍼 부족, 장기 실행 트랜잭션, 체크포인트 폭주, `synchronous_commit=off`, 느린 복제 재생 같은 시나리오를 실행해 **운영 설정이 지연/팽창/내구성/복제 지연에 미치는 변화**를 직접 살펴볼 수 있음
- three.js/TypeScript/Vite로 만든 정적 WebGL2 애플리케이션이며, 향후 실제 WebAssembly PostgreSQL의 쿼리 실행 결과와 계획을 현재의 내부 모델에 연결하는 **하이브리드 구조**도 가능한 방향으로 검토함

---

## 원문
- [원문](https://nikolays.github.io/PGSimCity/)
- [GeekNews 토론](https://news.hada.io/topic?id=31895)

## My Note
<!-- 한 줄 코멘트 남기기 -->

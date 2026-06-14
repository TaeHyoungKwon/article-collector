---
category: AI
collected_at: '2026-06-14T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30469
id: hada-30469
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.693
source: geeknews
tags:
- AI
- Other
- github.com/murrdb
title: murrdb/murr - ML/AI 워크로드용 서브 밀리초 캐시
url: https://github.com/murrdb/murr
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- AI 추론 워크로드를 겨냥한 **RocksDB 기반 NVMe/S3 캐시**로 Redis를 대체 가능
  - 배치 처리 방식의 **low-latency 제로 카피 읽기 및 쓰기**에 최적화
- 배치 데이터 파이프라인과 추론 앱 사이에 위치하는 데이터 서빙 계층으로 **Parquet 입력**, **Arrow-Flight 출력**
- 핫 데이터는 메모리, 콜드 데이터는 디스크에 두고 S3 기반 복제를 적용한 **계층형 저장(tiered storage)**
- **배치 입력·배치 출력** 방식으로 컬럼형 저장 위에서 행 단위 오버헤드 없이 동작, 1GB Parquet/Arrow 파일을 Ingestion API에 그대로 투입 가능
- **제로카피 와이어 프로토콜**로 API 응답에서 np.ndarray/pd.DataFrame/pt.Tensor를 변환 없이 구성 가능
- **무상태(stateless)** 설계로 모든 상태를 S3에 보존, 블록 스토리지에서 자체 부트스트랩하므로 노드 퇴출 시에도 복구 가능
- **First-class Python 지원**으로 Numpy/Pandas/Polars/Pytorch 배열과 제로카피 매핑, **Sparse columns**는 데이터 없는 컬럼이 0바이트 차지
- Murr가 적합한 경우
  - 데이터가 무겁고 표 형태(tabular)인 경우, S3 위의 대용량 **Parquet 덤프** 등
  - 읽기가 배치로 이뤄지는 경우: 1000개 문서에 걸쳐 100개 컬럼을 가져오는 작업 같은 것
  - 비용을 중시하는 상황에는 디스크/S3 오프로딩이 메모리 큰 Redis 보다 운영상 더 단순하고 저렴
- 경쟁 기술 대비 강점
  - **Redis** 대비: S3기반 영속성 제공, 콜드 데이터를 로컬 NVMe로 오프로딩 가능
  - 임베디드 **RocksDB** 대비: 생산자-추론 노드 간 데이터 동기화 직접 구축 불필요, 처음부터 분산 설계됨
  - **DynamoDB** 대비: 쿼리당이 아닌 CPU/RAM만 과금되어 약 **10배 저렴**
- 벤치마크상 packed-blob 읽기에서 Redis 대비 약 **3배**, Feast 스타일 HSET에서 약 **12배** 빠르며 HSET 대비 약 3배 적은 RAM 사용
- **범용 DB가 아니므로** OLTP는 Postgres, 분석은 Clickhouse/BigQuery/Snowflake, 범용 캐싱은 Redis 권장
- Apache 2.0 라이선스

## 원문
- [원문](https://github.com/murrdb/murr)
- [GeekNews 토론](https://news.hada.io/topic?id=30469)

## My Note
<!-- 한 줄 코멘트 남기기 -->

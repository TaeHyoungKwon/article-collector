---
category: Other
collected_at: '2026-05-15T23:41:23+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29540
id: hada-29540
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- velog.io
title: 무작위 접근(Random access) 워크로드에 적합한 ZFS 튜닝 방법
url: https://velog.io/@skynet/%EB%AC%B4%EC%9E%91%EC%9C%84-%EC%A0%91%EA%B7%BCRandom-access-%EC%9B%8C%ED%81%AC%EB%A1%9C%EB%93%9C%EC%97%90-%EC%A0%81%ED%95%A9%ED%95%9C-ZFS-%ED%8A%9C%EB%8B%9D-%EB%B0%A9%EB%B2%95
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- ZFS 기본 파라미터는 순차 접근과 무작위 접근 사이의 절충안으로 설정됨
  - 워크로드 특성을 명확히 안다면 더 공격적인 튜닝 가능
- 순차 접근 vs 무작위 접근 차이 설명
  - HDD는 헤드 이동 때문에 무작위 접근 성능이 순차 접근 대비 수십~수백배 느려질 수 있음
  - SSD도 무작위 접근이 훨씬 빨라졌지만 순차 접근이 여전히 더 효율적임
  - 큰 파일을 순서대로 읽는 워크로드는 순차 접근 성향이 강함
  - 작은 파일 여러 개를 자주 읽는 워크로드는 무작위 접근 성향이 강해지기 쉬움
- 워크로드 분석 방법 소개
  - 코드/구조 기반 논리적 추론
  - 처리량(bps)+초당 IO 수(iops) 기반 평균 IO 크기 계산
  - zpool iostat -r 기반 IO 크기 분포 분석
- zpool iostat -r 해석
  - ind: 개별 논리 요청 크기
  - agg: 실제 병합되어 수행된 IO 크기
  - agg가 ind보다 크면 인접 IO 병합이 잘 일어나고 있다는 뜻
- 예제 워크로드 분석 결과
  - 동기 읽기 비중 약 76%
  - 32KiB 이하 읽기가 99% 이상
  - 비동기 쓰기 역시 작은 IO 비중 높음
  - 전체적으로 무작위 접근 성향이 매우 강한 워크로드
- zfs\_prefetch\_disable
  - ZFS는 순차 접근 패턴 감지 시 인접 블록을 미리 ARC에 적재함
  - 무작위 접근 워크로드에서는 사전 읽기 적중률이 낮아 불필요한 IO만 늘어날 수 있음
  - arc\_summary 기반으로 사전 읽기 효율 측정 가능
  - 적중률이 낮다면 zfs\_prefetch\_disable 검토 가능
- recordsize
  - 기본값은 128K
  - 예제 워크로드에서는 대부분의 IO가 32KiB 이하이므로 더 작은 recordsize 검토 가능
- 최적값 선정
  - 벤치마크 기반으로 결정하는 것이 중요
  - MySQL/Postgres 같은 DB는 이미 검증된 튜닝 사례가 많음
  - 일반적으로 DB 페이지 크기와 유사한 recordsize를 사용하는 경우가 많음

## 원문
- [원문](https://velog.io/@skynet/%EB%AC%B4%EC%9E%91%EC%9C%84-%EC%A0%91%EA%B7%BCRandom-access-%EC%9B%8C%ED%81%AC%EB%A1%9C%EB%93%9C%EC%97%90-%EC%A0%81%ED%95%A9%ED%95%9C-ZFS-%ED%8A%9C%EB%8B%9D-%EB%B0%A9%EB%B2%95)
- [GeekNews 토론](https://news.hada.io/topic?id=29540)

## My Note
<!-- 한 줄 코멘트 남기기 -->

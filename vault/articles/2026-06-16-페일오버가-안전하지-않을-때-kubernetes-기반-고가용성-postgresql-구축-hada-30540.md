---
category: AI
collected_at: '2026-06-16T21:26:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30540
id: hada-30540
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- datadoghq.com
title: '페일오버가 안전하지 않을 때: Kubernetes 기반 고가용성 PostgreSQL 구축'
url: https://www.datadoghq.com/blog/engineering/postgresql-ha-kubernetes/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- k8s 기반 PostgreSQL 클러스터에서 네트워크 장애 시 **복제 지연(replication lag)** 이 누적되며 안전한 페일오버가 불가능해지는 구조적 약점을 해결한 방법
- 기존 구조는 **가용성(availability)** 을 **내구성(durability)** 보다 우선시해, 프라이머리가 쓰기를 계속 받는 동안 복제본이 뒤처지면서 데이터 손실 없이 승격할 후보가 사라짐
- 해결책으로 페일오버 후보에 **동기식 복제(synchronous replication)** 를 적용하고, 오픈소스 고가용성 관리자 **Patroni**로 조율
- 리더 풀 스탠바이만 동기식 복제에 참여하고 읽기 복제본은 비동기를 유지하는 **하이브리드 복제 모델**로, 내구성과 지연 시간 사이 균형 확보
- `remote_apply` 모드 적용 시 쓰기 지연 53% 증가 등 성능 비용에도, **5가지 장애 시나리오 검증**을 통해 안전한 자동 페일오버 달성

---

## 원문
- [원문](https://www.datadoghq.com/blog/engineering/postgresql-ha-kubernetes/)
- [GeekNews 토론](https://news.hada.io/topic?id=30540)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-05-23T09:24:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29779
id: hada-29779
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- slack.engineering
title: 'SSH에서 REST로: 보안 중심의 Slack EMR 데이터 파이프라인 현대화'
url: https://slack.engineering/from-ssh-to-rest-a-security-driven-modernization-of-slacks-emr-data-pipelines/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Slack 데이터 플랫폼에는 **700개 이상의 SSH 기반 Operator**가 일일 검색 인덱싱, 분석 작업 등 핵심 데이터 파이프라인을 운영, 모든 작업이 프로덕션 AWS EMR 클러스터에 **직접 SSH 접속**을 요구해 광범위한 보안 위협 표면 형성
- 이 SSH 의존성은 보안 위험뿐 아니라 **Spark on Kubernetes, EMR on EKS 전환, Whitecastle 이니셔티브 완료** 등 인프라 현대화를 가로막는 핵심 장애물로 작용
- 해결책으로 **YARN Distributed Shell**을 활용해 임의의 셸 명령까지 YARN 컨테이너에서 실행 가능하게 만들고, Slack 자체 REST 게이트웨이 **Quarry**를 통해 모든 잡 제출을 통합
- **8개 데이터 리전에 걸쳐 무중단(zero downtime)으로 700개 이상 잡을 마이그레이션**, 3분기 만에 100% SSH 제거 완료
- 결과적으로 **공격 표면 축소, 작업 신뢰성 향상, 가시성 개선**과 함께 **Whitecastle 완수 및 Spark on Kubernetes 등 차세대 인프라 기반** 확보

---

## 원문
- [원문](https://slack.engineering/from-ssh-to-rest-a-security-driven-modernization-of-slacks-emr-data-pipelines/)
- [GeekNews 토론](https://news.hada.io/topic?id=29779)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-08-10T09:45:01+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32323
id: hada-32323
matched_keywords:
- AI
- RAG
read: false
recommend_score: 5.099
recommended_on: '2026-08-10'
source: geeknews
tags:
- AI
- Other
- atlassian.com
title: 'StreamHub 확장: 하루 1,450억 이벤트 처리를 위해 Kinesis에서 Kafka로 전환'
url: https://www.atlassian.com/blog/how-we-build/scaling-streamhub-transitioning-from-kinesis-to-kafka-for-145-billion-daily-events
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Atlassian의 StreamHub는 하루 **220억 건에서 1,500억 건의 이벤트를 수집**하는 규모로 성장하면서, 200~300억 건 수준까지 잘 작동했던 Amazon Kinesis를 넘어 장기 보관 비용/소비자 확장성/멀티클라우드를 위해 AWS MSK 기반 Kafka로 전환함
- Kafka의 **Tiered Storage**로 실시간 데이터는 로컬 디스크에서 처리하고 오래된 데이터는 S3로 이동해 비싼 EBS 과잉 할당을 줄였으며, 대규모 과거 데이터 조회가 실시간 소비자의 IOPS를 잠식하는 문제도 분리함
- 하지만 하루 1,500억 건 규모에서는 **Managed Kafka도 무한히 확장되지 않았으며**, broker 네트워크/EBS 한계, S3 요청 폭증, tiered storage offload 지연, 스토리지 확장 cooldown, AZ 장애 시 control plane 의존성 등이 실제 장애 원인이 됨
- 장애를 겪은 뒤 평균 클러스터 사용률 대신 **가장 뜨거운 broker를 기준으로 용량을 계획**하고, 네트워크/로컬 디스크를 의도적으로 여유 있게 확보하며 rate limit, Kafka quota, quarantine으로 특정 워크로드가 전체 클러스터를 무너뜨리지 못하게 변경함
- 대형 클러스터를 여러 shard로 나누고 별도 **failover cluster와 규정 준수 가능한 companion region**을 마련해, 장애가 난 managed service의 control plane 자체에 의존하지 않고 복구할 수 있는 경로를 구축함

---

## 원문
- [원문](https://www.atlassian.com/blog/how-we-build/scaling-streamhub-transitioning-from-kinesis-to-kafka-for-145-billion-daily-events)
- [GeekNews 토론](https://news.hada.io/topic?id=32323)

## My Note
<!-- 한 줄 코멘트 남기기 -->

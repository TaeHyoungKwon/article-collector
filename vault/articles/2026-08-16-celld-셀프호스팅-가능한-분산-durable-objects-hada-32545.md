---
category: AI
collected_at: '2026-08-16T09:30:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32545
id: hada-32545
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.693
source: geeknews
tags:
- AI
- Other
- github.com/denoland
title: celld - 셀프호스팅 가능한 분산 Durable Objects
url: https://github.com/denoland/celld
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Deno가 공개한 오픈소스 런타임으로, **Cloudflare Workers와 Durable Objects 모델을 자신의 서버에서 실행**할 수 있게 함
- **Cloudflare용 코드를 비교적 적은 변경으로 셀프호스팅**하는 것이 목표: 기존 Wrangler 프로젝트의 Module Worker, `fetch`, Service Binding, Durable Object, Static Assets 등을 지원
- Durable Object 하나를 **이름을 가진 작은 서버 + 전용 SQLite DB**인 `cell`로 취급하며, 사용자/문서/채팅방/AI Agent 단위로 나눠 사용할 수 있음
  - 각 cell은 독립된 DB와 단일 writer를 가지므로 하나의 거대한 공유 DB에서 발생하는 **경합과 장애 범위를 구조적으로 분리**하고, 애플리케이션이 처음부터 자연스럽게 샤딩됨
  - 사용하지 않는 cell은 메모리에서 내려가 Object Storage에만 남기 때문에 **inactive 상태의 비용이 거의 없고**, 필요할 때 다시 활성화됨
- 데이터와 배포 상태를 **자신이 소유한 S3 호환 스토리지 또는 Google Cloud Storage**에 보관해 특정 Cloudflare 계정이나 관리형 데이터베이스에 의존하지 않음
- 별도의 Control Plane, Consensus 서버, 고정된 클러스터 membership이 없으며 **같은 버킷을 바라보는 노드를 실행하는 것만으로 fleet에 추가**할 수 있음
- HTTP뿐 아니라 Durable Object의 **Alarm, WebSocket, RPC**도 지원해 상태를 오래 유지하는 실시간 서비스나 Agent 같은 워크로드를 실행 가능
- Cloudflare가 Durable Objects 위에 구축한 **D1과 Workflows 지원도 계획 중**이라, 향후 Workers + D1 애플리케이션까지 셀프호스팅 범위를 넓힐 예정
- 반면 KV/R2/Workers AI/Vectorize/Hyperdrive 등 별도의 Cloudflare 관리형 서비스는 범위 밖이며, **Cloudflare 플랫폼 전체를 복제하는 프로젝트는 아님**
- 아직 **Alpha 단계**로 TLS/Ingress/사용자 인증 등 운영 환경의 일부 기능은 직접 구성해야 함
- 즉 Cloudflare Durable Objects의 **“상태를 가진 작은 서버를 수평으로 많이 만드는 프로그래밍 모델”은 유지하면서, 실행 머신과 데이터 저장소를 직접 소유할 수 있게 하는 것**이 celld의 가장 큰 특징

## 원문
- [원문](https://github.com/denoland/celld)
- [GeekNews 토론](https://news.hada.io/topic?id=32545)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-08T09:00:04+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30262
id: hada-30262
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- romaglushko.com
title: Kubernetes Gateway API
url: https://www.romaglushko.com/blog/k8s-gateway-api/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 2025년 11월 Kubernetes는 전체 클러스터의 40% 이상에서 사용되던 **NGINX Ingress Controller**의 2026년 3월 **deprecation**을 발표, 이 결정은 **Gateway API**를 Ingress API의 후속으로 자리매김하는 전환점이 됨
- Gateway API는 inbound 트래픽 관리에 필요한 폭넓은 기능을 다루며, Ingress API보다 **표현력**이 높고 팀 간 **관심사 분리**를 명확히 함
- Ingress API의 한계로는 좁은 API 범위, 경직된 확장성, **정책 강제 부재**, 모호한 소유권 경계, 안전한 cross-namespace 미지원 등이 있음
- Gateway API는 GatewayClass, Gateway, Listener, **Route** 등 분리된 리소스 모델과 ReferenceGrant, **Policy attachment** 같은 보안·확장 메커니즘을 제공
- NGINX Ingress Controller의 반복된 CVE는 구조적 결함에서 비롯되며, 장기적으로는 **Gateway API로의 마이그레이션**이 유일한 근본 해결책임

---

## 원문
- [원문](https://www.romaglushko.com/blog/k8s-gateway-api/)
- [GeekNews 토론](https://news.hada.io/topic?id=30262)

## My Note
<!-- 한 줄 코멘트 남기기 -->

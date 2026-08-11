---
category: Other
collected_at: '2026-08-11T20:01:35+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32402
id: hada-32402
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- blog.yossarian.net
title: GitHub Actions에 OIDC audience 제약이 필요한 이유
url: https://blog.yossarian.net/2026/08/10/github-actions-needs-oidc-audience-constraints
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- GitHub Actions의 `id-token: write`는 작업이 임의의 audience로 OIDC 토큰을 발급할 수 있게 해, 취약하거나 악성인 서드파티 코드가 **다른 서비스로 권한을 확장**할 수 있음
- OIDC의 **`aud` 클레임**은 토큰을 받아들일 서비스를 제한해, 특정 서비스용 토큰이 탈취돼도 다른 서비스에서 오용되지 않도록 방어함
- GitLab CI/CD는 audience를 작업 정의에 정적으로 선언하지만, GitHub Actions는 HTTP 요청의 `audience` 매개변수로 지정하므로 **런타임에 대상을 선택**할 수 있음
- GitHub는 `id-token: [pypi]`처럼 허용할 audience를 미리 선언하게 해, PyPI 배포 작업이 `sts.amazonaws.com`용 토큰을 발급받아 **AWS 접근에 악용되는 상황**을 막아야 함
- 동적 audience가 필요한 경우 기존 `id-token: write`를 덜 안전한 포괄 옵션으로 유지하되, 정적 제약을 지원하면 독립적인 OIDC 연동 서비스 사이의 공격 전환을 줄일 수 있음

---

## 원문
- [원문](https://blog.yossarian.net/2026/08/10/github-actions-needs-oidc-audience-constraints)
- [GeekNews 토론](https://news.hada.io/topic?id=32402)

## My Note
<!-- 한 줄 코멘트 남기기 -->

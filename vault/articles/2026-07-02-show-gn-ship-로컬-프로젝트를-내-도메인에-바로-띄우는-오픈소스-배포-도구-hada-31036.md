---
category: AI
collected_at: '2026-07-02T12:32:07+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31036
id: hada-31036
matched_keywords:
- AI
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- github.com/gronxb
title: 'Show GN: Ship - 로컬 프로젝트를 내 도메인에 바로 띄우는 오픈소스 배포 도구'
url: https://github.com/gronxb/ship
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Ship은 로컬에 있는 작은 웹 서비스를 내 도메인에 바로 띄우기 위해 만들고 있는 오픈소스 배포 도구입니다.

제가 원했던 흐름은 단순했습니다.

1. SSR 서버 프로젝트를 하나 스캐폴딩합니다.
2. Dockerfile을 둡니다.
3. `ship --service demo`를 실행합니다.
4. `demo.your-domain.com`에서 바로 확인합니다.

초기 접근은 Tailscale 네트워크 안에서만 열리게 해두고, 필요할 때마다 특정 서비스만 인터넷에 공개할 수 있는 구조로 만들고 있습니다.

그래서 평소에는 개인 홈서버/Mac mini 안의 내부 서비스처럼 쓰다가, 누군가에게 보여줘야 할 때만 인터넷망으로 전환할 수 있습니다.

대시보드에서는 배포된 서비스 목록, 내부/외부 공개 상태, 로그, 실행된 명령 등을 확인할 수 있습니다.

아직 초기 버전이라 Cloudflare 도메인과 Tailscale 설정이 필요합니다. README에 설치 과정과 예제 흐름을 정리해두었습니다.

홈서버나 Mac mini에서 작은 서비스를 자주 띄우는 분들이 보시기에 이런 흐름이 쓸만한지 피드백을 받아보고 싶습니다.

## 원문
- [원문](https://github.com/gronxb/ship)
- [GeekNews 토론](https://news.hada.io/topic?id=31036)

## My Note
<!-- 한 줄 코멘트 남기기 -->

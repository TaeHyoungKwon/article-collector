---
category: Other
collected_at: '2026-06-26T10:11:49+09:00'
geeknews_comments: 1
geeknews_score: 5
geeknews_url: https://news.hada.io/topic?id=30845
id: hada-30845
matched_keywords: []
read: false
recommend_score: 2.0
source: geeknews
tags:
- Other
- blog.cloudflare.com
title: 모든 고객을 위한 Cloudflare OAuth
url: https://blog.cloudflare.com/oauth-for-all/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Cloudflare는 고객이 직접 **self-managed OAuth** 앱을 만들 수 있게 해, Cloudflare API 접근을 표준 위임 승인 흐름으로 제공할 수 있게 함
- 예전에는 일부 수동 온보딩된 파트너만 타사 OAuth를 쓸 수 있었고, 자체 통합 개발자는 위임형 앱 흐름에 맞지 않는 **API 토큰**에 의존해야 했음
- 전체 공개를 위해 동의 화면, 철회, 앱 소유권 표시를 개선하고 OAuth 엔진 **Hydra**를 1.X에서 2.X로 단계적으로 업그레이드함
- 업그레이드 과정에서는 스키마 마이그레이션, 토큰 갱신 오류, 철회 이벤트 유실 위험, 403 증가가 발생했고, 동시 인덱스 생성·철회 재생 큐·데이터 복원으로 대응함
- 업그레이드 후 API P95는 185ms에서 101ms로 **45% 감소**했고 CPU 사용량도 1.07코어에서 0.67코어로 줄어, 공개 OAuth 운영 기반이 안정화됨

---

## 원문
- [원문](https://blog.cloudflare.com/oauth-for-all/)
- [GeekNews 토론](https://news.hada.io/topic?id=30845)

## My Note
<!-- 한 줄 코멘트 남기기 -->

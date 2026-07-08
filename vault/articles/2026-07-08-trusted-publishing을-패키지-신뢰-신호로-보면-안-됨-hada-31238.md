---
category: Other
collected_at: '2026-07-08T17:01:35+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31238
id: hada-31238
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- blog.yossarian.net
title: Trusted Publishing을 패키지 신뢰 신호로 보면 안 됨
url: https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Trusted Publishing**의 “신뢰”는 패키지를 사람이 믿어도 된다는 뜻이 아니라, CI/CD 같은 외부 **머신 신원**과 패키지 인덱스 사이의 업로드 인증 관계를 가리킴
- PyPI의 구현은 **OIDC 연합** 위에서 동작하며, 장기 API 토큰 대신 짧고 범위가 좁은 게시 자격 증명을 발급해 장기·과권한 자격 증명 노출을 줄임
- PyPI가 2023년에 공개한 뒤 npm, RubyGems, crates.io, NuGet 등으로 확산됐지만, 데이터 모델 복잡성, OIDC 제공자별 처리, CI/CD 침해 가능성은 남아 있음
- PyPI는 Trusted Publishing 상태를 프로젝트 페이지의 **초록 체크 표시**로 강조하지 않고, 파일 상세의 단순 Yes/No 메타데이터로만 보여 안전성 신호로 오해될 여지를 줄임
- Trusted Publishing과 PyPI attestations는 업로드 인증이나 머신 신원 기반 서명 여부만 말해주며, 별도로 그 신원을 신뢰하기 전에는 패키지 안전성이나 품질을 판단할 수 없음

---

## 원문
- [원문](https://blog.yossarian.net/2026/07/07/You-shouldnt-trust-trusted-publishing)
- [GeekNews 토론](https://news.hada.io/topic?id=31238)

## My Note
<!-- 한 줄 코멘트 남기기 -->

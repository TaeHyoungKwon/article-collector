---
category: Other
collected_at: '2026-06-02T14:23:20+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30110
id: hada-30110
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- relivio.dev
title: 'Show GN: Relivio: 배포 직후 15분을 STABLE/WATCH/RISK로 정리하는 도구'
url: https://relivio.dev/demo
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. 회사 다니면서 사이드프로젝트로 개발 도구를 만들고 있습니다. 배포 직후 15분의 판단을 정리하는 Relivio 를 공유합니다.

저한테 배포가 마음에 걸리는 건 배포 자체가 아니라 직후 15분이었습니다. CI 는 통과했고 대시보드도 대체로 정상인데, 에러가 조금 늘었을 때 이게 이번 배포 탓인지, 원래 가끔 있던 흔들림인지, 지금 되돌려야 하는지 바로 닫히지 않습니다.

Relivio 는 기존 모니터링을 대체하는 도구가 아닙니다. 모니터링은 평소 시스템 상태를 넓게 보는 데 강하고, Relivio 는 "이번 배포가 지금 괜찮은가" 하나만 닫는 좁은 레이어입니다.

하는 일은 단순합니다. 이미 있는 에러 로그, 스택트레이스, 예외 타입, 배포 정보를 받아 배포 단위로 하나의 verdict 를 만듭니다.

- STABLE / WATCH / RISK 세 단계 판단
- 영향받은 API 목록
- 다음 조치(next action) 한 줄

원칙 하나를 강하게 잡았습니다. 쓰는 쪽에서 새로 측정해 보내야 하는 데이터는 받지 않습니다. 이 선이 없으면 결국 작은 APM 을 다시 만드는 쪽으로 가기 때문입니다.

사람은 콘솔이나 Slack / Discord 알림으로 verdict 를 보고, 에이전트는 API 나 MCP 서버로 같은 verdict 를 읽습니다. 배포 직후의 판단 기록이 나중에 다른 에이전트나 미래의 나에게도 읽히게 하려는 구조입니다.

- 바로 써보기 (가입 없이): relivio.dev/demo
- Source / 데모 앱 repo: github.com/lazypl82/relivio-demo-fastapi
- TypeScript SDK: npm relivio
- Python SDK: PyPI relivio
- MCP 서버 포함
- 제품 소개: relivio.dev

아직 alpha 고 첫 사용자를 못 만들었습니다. 다음 점이 특히 궁금합니다.

1. 배포 직후 15분을 따로 다루는 레이어가 실제로 필요하다고 느끼시나요, 아니면 기존 스택으로 충분한가요?
2. STABLE / WATCH / RISK 3 단 구분이 실무에서 쓸 만한가요? (WATCH 가 가장 자신 없습니다)
3. 에이전트가 verdict 를 MCP 로 읽는 구조가 쓸모 있을까요?

## 원문
- [원문](https://relivio.dev/demo)
- [GeekNews 토론](https://news.hada.io/topic?id=30110)

## My Note
<!-- 한 줄 코멘트 남기기 -->

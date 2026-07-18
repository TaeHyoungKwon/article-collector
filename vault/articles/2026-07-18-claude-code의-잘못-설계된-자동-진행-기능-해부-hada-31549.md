---
category: Dev Tools
collected_at: '2026-07-18T18:13:52+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31549
id: hada-31549
matched_keywords:
- Claude Code
read: false
recommend_score: 2.901
source: geeknews
tags:
- Dev Tools
- Other
- olafalders.com
title: Claude Code의 잘못 설계된 자동 진행 기능 해부
url: https://www.olafalders.com/2026/07/17/claude-code-anatomy-of-a-misfeature/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code `2.1.198`은 `AskUserQuestion`에 60초간 답이 없으면 모델이 자체 판단으로 작업을 계속하는 **자동 진행 기능**을 기본 활성화했지만, 출시 당시 변경 로그와 문서에는 기록하지 않았음
- 권한 요청을 자동 승인하지는 않았으나, 이미 허용된 도구나 `--dangerously-skip-permissions` 환경에서는 “staging 또는 production” 같은 **의사결정 게이트**를 대신 통과할 수 있었고 일부 답변만 입력해도 나머지는 모델이 선택했음
- 문제 제기 약 이틀 뒤 나온 `2.1.200`은 기능을 삭제하지 않고 기본값만 껐으며, `/config`에서 `60s`, `5m`, `10m`, `never` 중 하나를 고르는 **옵트인 방식**으로 전환함
- 공개 저장소에는 실제 제품 소스나 도입·되돌림 커밋이 없지만, npm의 Bun 실행 파일에 포함된 JavaScript 번들을 비교해 `2.1.198`에서 AFK 문자열·스키마·분석 이벤트가 함께 추가됐음을 확인할 수 있음
- 기본 자동 업데이트와 불완전한 변경 기록이 결합하면 사용자 개입 없이 안전 가정이 달라질 수 있음. CLI를 고정하면서 플러그인은 갱신하려면 **`DISABLE_AUTOUPDATER=1`과 `FORCE_AUTOUPDATE_PLUGINS=1`** 을 함께 설정해야 함

---

## 원문
- [원문](https://www.olafalders.com/2026/07/17/claude-code-anatomy-of-a-misfeature/)
- [GeekNews 토론](https://news.hada.io/topic?id=31549)

## My Note
<!-- 한 줄 코멘트 남기기 -->

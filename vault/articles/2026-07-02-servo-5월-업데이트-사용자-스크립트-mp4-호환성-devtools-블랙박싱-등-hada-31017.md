---
category: Other
collected_at: '2026-07-02T04:04:54+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31017
id: hada-31017
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- servo.org
title: 'Servo 5월 업데이트: 사용자 스크립트, mp4 호환성, DevTools 블랙박싱 등'
url: https://servo.org/blog/2026/06/30/may-in-servo/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Servo 0.3.0**은 5월 병합분 391개 커밋을 담아 웹 플랫폼, 임베딩 API, 성능, 안정성, 보안 수정을 한 번에 반영한 릴리스임
- 웹 플랫폼은 `font-variant-*`, fast start 없는 **mp4** `<video>` 재생, 폼 인코딩, DOM API 추가로 실제 사이트 호환성을 넓힘
- 보안 측면에서는 JS 런타임을 **SpiderMonkey 140.10.1**로 올려 메모리 안전성 버그를 수정했고, CVE-2026-7322·CVE-2026-7323·MFSA 2026-36과 연결됨
- 사용자와 개발자는 servoshell의 `--host-file=`, `--userscripts=` 옵션과 Firefox **DevTools Debugger**의 “Ignore source” 블랙박싱을 활용할 수 있음
- 임베더는 **Rust 1.88.0 이상** 요구와 SiteDataManager·Preferences·DiagnosticsLogging의 breaking change를 반영해야 하며, 성능 개선은 레이아웃 순회 축소와 스레드 풀 통합에 집중됨

---

## 원문
- [원문](https://servo.org/blog/2026/06/30/may-in-servo/)
- [GeekNews 토론](https://news.hada.io/topic?id=31017)

## My Note
<!-- 한 줄 코멘트 남기기 -->

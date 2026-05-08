---
category: AI
collected_at: '2026-05-08T11:03:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29288
id: hada-29288
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- hacks.mozilla.org
title: Claude Mythos Preview로 Firefox를 강화한 비하인드 스토리
url: https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Mozilla는 모델 성능 향상과 **하네스(harness)** 개선으로 AI 생성 보안 보고서의 신호를 높이고 잡음을 줄여, Firefox에서 실제 보안 버그를 대규모로 찾는 파이프라인을 구축함
- Firefox [150 release](https://www.firefox.com/en-US/firefox/150.0/releasenotes/)에서는 **Claude Mythos Preview**가 식별한 271개 버그가 수정됐고, [149.0.2](https://www.firefox.com/en-US/firefox/149.0.2/releasenotes/), [150.0.1](https://www.firefox.com/en-US/firefox/150.0.1/releasenotes/), [150.0.2](https://www.firefox.com/en-US/firefox/150.0.2/releasenotes/)에도 관련 수정이 포함됨
- 공개된 대표 버그에는 JIT의 WebAssembly GC 구조체 초기화 제거로 인한 가짜 객체 원시 기능, IPC 경합 조건을 통한 부모 프로세스 UAF, NaN 역직렬화 문제, XSLT의 20년 된 rehash 버그, `rowspan=0`을 이용한 16비트 레이아웃 bitfield overflow 등이 들어감
- 공개된 버그 상당수는 **샌드박스 탈출**이며, 손상된 콘텐츠 프로세스가 권한 있는 부모 프로세스로 권한을 올리는 상황을 전제로 해 퍼징만으로 찾기 어려운 공격 표면을 AI 분석이 더 포괄적으로 다룸
- Mozilla는 기존 퍼징 인프라 위에 agentic 하네스를 얹어 재현되지 않는 추측을 버리고 테스트케이스로 가설을 검증했으며, 앞으로 패치가 tree에 들어올 때 스캔하도록 **지속적 통합**에 통합할 계획임

---

## 원문
- [원문](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)
- [GeekNews 토론](https://news.hada.io/topic?id=29288)

## My Note
<!-- 한 줄 코멘트 남기기 -->

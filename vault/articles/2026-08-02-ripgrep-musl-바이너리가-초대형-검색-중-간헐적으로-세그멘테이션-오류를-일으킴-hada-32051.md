---
category: AI
collected_at: '2026-08-02T10:36:14+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32051
id: hada-32051
matched_keywords:
- AI
- Codex
read: false
recommend_score: 4.901
recommended_on: '2026-08-03'
source: geeknews
tags:
- AI
- Other
- github.com/BurntSushi
title: Ripgrep musl 바이너리가 초대형 검색 중 간헐적으로 세그멘테이션 오류를 일으킴
url: https://github.com/BurntSushi/ripgrep/issues/3494
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Ripgrep 15.2.0의 **x86\_64-unknown-linux-musl** 바이너리가 대규모 파일 트리를 높은 동시성으로 검색할 때 간헐적으로 `SIGSEGV`와 함께 종료됨
- 충돌은 `opendir`가 호출한 `calloc` 내부에서 발생하며, **musl mallocng**의 힙 메타데이터 무결성 검사 지점이 스택 추적의 최상단에 나타남
- 재현 환경은 약 **20GiB·180만 개 파일**로 구성된 트리이며, 존재하지 않는 문자열을 `rg`로 반복 검색함
- 24코어 시스템에서 검색 트리가 커널 블록 캐시에 들어갈 만큼 RAM을 확보하면 일반적으로 **약 1분** 안에 문제가 발생함
- OpenAI Codex에 포함된 `rg`뿐 아니라 공식 릴리스와 바이트 단위로 동일한 바이너리에서도 독립적으로 재현돼 **Codex 의존성과 무관한 문제**로 확인됨

---

## 원문
- [원문](https://github.com/BurntSushi/ripgrep/issues/3494)
- [GeekNews 토론](https://news.hada.io/topic?id=32051)

## My Note
<!-- 한 줄 코멘트 남기기 -->

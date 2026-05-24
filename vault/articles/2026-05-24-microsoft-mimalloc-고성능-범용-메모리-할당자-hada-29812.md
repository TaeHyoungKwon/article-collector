---
category: AI
collected_at: '2026-05-24T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 11
geeknews_url: https://news.hada.io/topic?id=29812
id: hada-29812
matched_keywords:
- AI
read: false
recommend_score: 4.485
source: geeknews
tags:
- AI
- Other
- github.com/microsoft
title: microsoft/mimalloc - 고성능 범용 메모리 할당자
url: https://github.com/microsoft/mimalloc
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **malloc을 드롭인 교체 가능한 범용 할당자**로, 코드 수정 없이 기존 프로그램에 적용 가능
- **jemalloc, tcmalloc보다 빠르면서 메모리도 덜 씀** : tcmalloc 대비 13%, jemalloc 대비 2.5배 이상 빠름
  - 특정 벤치마크 1등이 아니라, **어떤 워크로드든 꾸준히 상위권**을 차지함
- **약 10k LOC의 단순한 자료구조**로 통합/이식이 쉬우며, 동시에 수천 대 규모 분산 서비스에서 운용 가능한 수준
- Windows, macOS, Linux, WASM, 다양한 BSD, Haiku, MUSL 등 다수 OS에 이식됨
- **멀티스레드에서 락 경합 걱정 제로**
  - 페이지마다 thread-local free 리스트와 concurrent free 리스트를 분리
  - 다른 스레드가 메모리 해제해도 **단일 CAS 한 번**이면 끝나며, 복잡한 동기화 코드 필요 없음
- C로 작성. MIT 라이선스

## 원문
- [원문](https://github.com/microsoft/mimalloc)
- [GeekNews 토론](https://news.hada.io/topic?id=29812)

## My Note
<!-- 한 줄 코멘트 남기기 -->

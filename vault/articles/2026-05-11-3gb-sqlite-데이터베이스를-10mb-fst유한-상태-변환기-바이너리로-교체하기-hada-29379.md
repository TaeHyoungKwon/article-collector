---
category: Other
collected_at: '2026-05-11T15:02:24+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29379
id: hada-29379
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- til.andrew-quinn.me
title: 3GB SQLite 데이터베이스를 10MB FST(유한 상태 변환기) 바이너리로 교체하기
url: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Taskusanakirja**는 입력 중 접두사 검색을 제공하는 핀란드어-영어 사전임
- 핀란드어 굴절형 확장으로 항목이 **4천만~6천만 개**까지 늘어 트라이가 한계에 닿음
- 임시 **SQLite FTS** 해법은 빨랐지만 최초 3GB 다운로드가 필요했음
- Rust 기반 **FST**가 SQLite 데이터를 약 10MB 바이너리로 줄여 300배 절감함
- FST는 접두사와 **접미사**를 함께 공유해 반복 굴절 패턴에 잘 맞음

---

## 원문
- [원문](https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/)
- [GeekNews 토론](https://news.hada.io/topic?id=29379)

## My Note
<!-- 한 줄 코멘트 남기기 -->

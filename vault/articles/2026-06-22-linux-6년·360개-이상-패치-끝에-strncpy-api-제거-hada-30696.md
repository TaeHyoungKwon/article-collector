---
category: Other
collected_at: '2026-06-22T03:33:59+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30696
id: hada-30696
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- phoronix.com/news
title: Linux, 6년·360개 이상 패치 끝에 strncpy API 제거
url: https://www.phoronix.com/news/Linux-7.2-Drops-strncpy
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Linux 7.2에서 커널 내부의 **strncpy API** 사용처가 사라지며, 오래전부터 폐기 예정이던 문자열 복사 인터페이스가 최종 제거됨
- strncpy()는 지정한 바이트 수만큼 복사하지만 **NUL 종료** 동작이 직관적이지 않아, 커널에서 수년간 버그의 원인으로 남아 있었음
- 목적지 버퍼를 불필요하게 0으로 채우는 특성은 **성능 문제**까지 만들었고, 이를 걷어내는 데 약 6년과 362개 커밋이 필요했음
- 금요일 머지에서 API 본체뿐 아니라 마지막 **per-CPU 아키텍처별 구현**도 함께 제거됨
- 커널 코드는 이제 용도에 따라 strscpy(), strscpy\_pad(), strtomem\_pad(), memcpy\_and\_pad(), memcpy() 같은 대체 함수를 골라야 함

---

## 원문
- [원문](https://www.phoronix.com/news/Linux-7.2-Drops-strncpy)
- [GeekNews 토론](https://news.hada.io/topic?id=30696)

## My Note
<!-- 한 줄 코멘트 남기기 -->

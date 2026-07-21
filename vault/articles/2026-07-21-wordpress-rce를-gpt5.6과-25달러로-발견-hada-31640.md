---
category: Other
collected_at: '2026-07-21T10:12:37+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31640
id: hada-31640
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- slcyber.io
title: WordPress RCE를 GPT5.6과 25달러로 발견
url: https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- GPT5.6 Sol Ultra가 최신 안정판 WordPress를 분석해 **인증 전 SQL 주입**부터 관리자 계정 생성과 원격 코드 실행(RCE)까지 이어지는 공격 체인을 10여 시간 만에 완성함
- 출발점은 WordPress 5.6부터 제공된 **Batch API의 배열 인덱스 불일치**로, 재귀 Batch 요청을 결합해 GET 제한과 매개변수 검증을 우회함
- 검증되지 않은 `author_exclude` 문자열로 UNION 주입을 일으킨 뒤, 조작한 게시물을 메모리 캐시에 넣고 **oEmbed 캐시·changeset·순환 참조·훅**을 연쇄적으로 악용함
- `customize_changeset`의 `user_id: 1`로 관리자 권한을 일시 획득하고 `parse_request` 훅으로 Batch 요청을 재실행해 새 관리자를 만든 뒤, 백도어 플러그인 ZIP을 업로드해 코드 실행에 도달함
- 월 200달러 구독의 주간 사용량 50%를 비례 계산한 비용은 약 **25달러**였으며, 사람의 역할은 제품과 공격 표면 선정, 프롬프트 조정 같은 상위 수준의 연구 지휘로 이동할 가능성이 커짐

---

## 원문
- [원문](https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/)
- [GeekNews 토론](https://news.hada.io/topic?id=31640)

## My Note
<!-- 한 줄 코멘트 남기기 -->

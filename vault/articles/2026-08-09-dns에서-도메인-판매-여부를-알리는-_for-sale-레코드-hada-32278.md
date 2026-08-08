---
category: Other
collected_at: '2026-08-09T06:37:10+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32278
id: hada-32278
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- specification.website
title: DNS에서 도메인 판매 여부를 알리는 _for-sale 레코드
url: https://specification.website/spec/foundations/for-sale-dns/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- RFC 10023은 운영 중인 도메인도 `_for-sale` **TXT 레코드**로 구매 가능 상태임을 브로커와 자동화 서비스에 알리는 규약을 정의함
- 도메인 파킹과 달리 기존 **웹·메일 서비스**를 그대로 유지할 수 있으며, 판매 신호도 브라우저에 노출되지 않음
- 레코드는 필수 버전 `v=FORSALE1;`과 최대 1개의 `tag=value` 쌍으로 구성되며, 설명·연락처 URI·희망 가격·독점 코드를 전달할 수 있음
- 레코드마다 태그 하나와 255옥텟 이하의 문자열 하나만 사용하고, **TTL은 3,600초 이하**로 설정하며 판매 의사가 사라지면 삭제해야 함
- 공개된 가격은 판매 약속이 아니며 텍스트와 URI가 조작될 수 있으므로, 처리기는 내용을 정제하고 사용자 확인 없이 링크로 자동 이동해서는 안 됨

---

## 원문
- [원문](https://specification.website/spec/foundations/for-sale-dns/)
- [GeekNews 토론](https://news.hada.io/topic?id=32278)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-05-10T02:38:30+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29330
id: hada-29330
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- news.ycombinator.com
title: 'Ask HN: 실제 UUID v4 충돌을 겪었습니다...'
url: https://news.ycombinator.com/item?id=48060054
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 데이터베이스가 오늘 **중복 UUID v4**를 감지했고, 기존 값은 2025년에 추가된 레코드의 `b6133fd6-70fe-4fe3-bed6-8ca8fc9386cd`와 완전히 같았음
- 사용 중인 패키지는 npm의 **uuid**이며, `import { v4 as uuidv4 } from "uuid";` 뒤 `const document_id = uuidv4();`로 생성해 데이터베이스에 넣는 방식이라고 함
- 데이터베이스에는 약 **15,000개 레코드**만 있어 통계적으로 불가능해 보이는데, 같은 일을 겪은 사람이 있는지 묻고 있음

## 원문
- [원문](https://news.ycombinator.com/item?id=48060054)
- [GeekNews 토론](https://news.hada.io/topic?id=29330)

## My Note
<!-- 한 줄 코멘트 남기기 -->

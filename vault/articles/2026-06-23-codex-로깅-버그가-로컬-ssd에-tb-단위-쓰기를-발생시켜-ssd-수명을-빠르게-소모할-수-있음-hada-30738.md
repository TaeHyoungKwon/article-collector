---
category: AI
collected_at: '2026-06-23T09:04:34+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30738
id: hada-30738
matched_keywords:
- AI
- Codex
read: false
recommend_score: 4.901
source: geeknews
tags:
- AI
- Other
- github.com/openai
title: Codex 로깅 버그가 로컬 SSD에 TB 단위 쓰기를 발생시켜 SSD 수명을 빠르게 소모할 수 있음
url: https://github.com/openai/codex/issues/28224
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Codex가 로컬 **SQLite 피드백 로그 DB**에 지속적으로 대량 데이터를 기록하며, 한 사용자 환경에서 21일 가동 후 메인 SSD에 약 **37TB**가 기록됨
- 이를 환산하면 연간 약 **640TB**, 1TB SSD 기준 연 약 640회 전체 쓰기에 해당하며, 일부 컨슈머 SSD의 보증 수명(약 600 TBW)을 1년 이내에 소진할 수 있음
- 보존 행은 약 50만 개에 불과하지만 AUTOINCREMENT 카운터는 **55억 ID**를 넘겨, 보존 행과 누적 삽입 ID 사이에 약 **1만 배 격차**가 존재
- 원인은 SQLite 피드백 로그 싱크가 **글로벌 TRACE 기본값**(`Targets::new().with_default(Level::TRACE)`)으로 설정되어, 의존성 내부 로그와 대용량 raw 프로토콜 페이로드까지 모두 영구 기록하기 때문
- 2026년 6월 22일 두 개의 **PR이 병합**되어 약 85%의 로그를 차단함에 따라 이슈가 종료됨

---

## 원문
- [원문](https://github.com/openai/codex/issues/28224)
- [GeekNews 토론](https://news.hada.io/topic?id=30738)

## My Note
<!-- 한 줄 코멘트 남기기 -->

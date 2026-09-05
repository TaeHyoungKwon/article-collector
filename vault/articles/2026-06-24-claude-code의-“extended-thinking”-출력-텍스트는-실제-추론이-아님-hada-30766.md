---
category: Dev Tools
collected_at: '2026-06-24T02:35:11+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30766
id: hada-30766
matched_keywords:
- Claude Code
read: false
recommend_score: 2.901
recommended_on: '2026-09-05'
source: geeknews
tags:
- Dev Tools
- Other
- patrickmccanna.net
title: Claude Code의 “Extended Thinking” 출력 텍스트는 실제 추론이 아님
url: https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code는 세션을 디스크에 기록하지만, 로컬 로그의 **thinking block**에는 실제 추론 텍스트 대신 600자 길이의 `signature`만 남아 있었음
- Claude의 추론은 **signature로 암호화**되며, 키는 Anthropic이 보유하고 사용자 기기에는 전달되지 않음
- API가 돌려주는 값은 실제 추론 원문이 아니라 **추론 요약**이고, 전체 thinking output을 얻으려면 enterprise agreement가 필요함
- `ctrl+o`로 보는 **extended-thinking** 출력도 Fable/Opus의 사고 과정 요약일 뿐, 세션에서 모델 행동을 직접 구동한 추론 자체는 아님
- Claude Code 세션을 감사 추적으로 쓰려면 로컬 파일, 입력·출력, 동작 로그만으로는 에이전트의 실제 논리를 재현할 수 없다는 점을 전제로 해야 함

---

## 원문
- [원문](https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/)
- [GeekNews 토론](https://news.hada.io/topic?id=30766)

## My Note
<!-- 한 줄 코멘트 남기기 -->

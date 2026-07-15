---
category: Dev Tools
collected_at: '2026-07-15T10:02:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31448
id: hada-31448
matched_keywords:
- Claude Code
read: false
recommend_score: 2.901
source: geeknews
tags:
- Dev Tools
- Other
- jola.dev
title: Claude가 ‘load-bearing’을 말하지 않게 만드는 방법
url: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code가 “honest take”, “load-bearing seam” 같은 문구를 반복한다면 **MessageDisplay 훅**으로 화면에 표시되기 전 다른 표현으로 치환할 수 있음
- Python 스크립트가 표준 입력의 JSON에서 `delta`를 읽어 **대소문자를 구분하지 않고 치환**한 뒤, 변경된 `displayContent`를 JSON으로 반환함
- 예제에서는 `seam`을 `whatchamacallit`, `you're absolutely right`를 `I'm a complete clown`, `honest take`를 `spicy doodad`, `load-bearing`을 `cooked`로 바꿈
- 스크립트를 `~/.claude/hooks/wordswap.sh`에 저장해 **실행 권한**을 부여하고, `~/.claude/settings.json`의 `hooks.MessageDisplay`에 명령 훅으로 등록해야 함
- 훅은 **Claude Code 시작 시 로드**되므로 새 세션을 열어야 적용되며, 치환 목록은 원하는 어휘로 자유롭게 바꿀 수 있음

---

## 원문
- [원문](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing)
- [GeekNews 토론](https://news.hada.io/topic?id=31448)

## My Note
<!-- 한 줄 코멘트 남기기 -->

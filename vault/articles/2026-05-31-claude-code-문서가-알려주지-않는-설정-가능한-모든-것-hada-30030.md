---
category: Dev Tools
collected_at: '2026-05-31T08:42:31+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30030
id: hada-30030
matched_keywords:
- Claude Code
read: false
recommend_score: 2.901
source: geeknews
tags:
- Dev Tools
- Other
- buildingbetter.tech
title: Claude Code - 문서가 알려주지 않는 설정 가능한 모든 것
url: https://buildingbetter.tech/p/i-read-the-claude-code-source-code
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Claude Code 2.1.87**에는 문서화되지 않은 설정이 많고, 개인·프로젝트별 `.claude/` 파일로 Hooks, Skills, Agents를 나눠 적용 가능함
- Hook은 stdin JSON과 exit code뿐 아니라 stdout의 **이벤트별 JSON 필드**로 명령 수정, 권한 결정, 컨텍스트 주입, 파일 감시까지 수행함
- 문서에 없는 Hook 필드 **`once`**, `async`, `asyncRewake`로 1회 실행, 백그라운드 감사 로그, 비동기 보안 차단 흐름을 만들 수 있음
- Skills와 Agents는 **숨겨진 frontmatter**로 모델·effort·스코프 Hook·Agent 위임·지속 메모리·CLAUDE.md 생략·MCP 의존성을 제어함
- Auto Mode, 자동 메모리, Dream, Magic Docs, 권한 glob, `context: fork`는 Claude Code를 **학습형 개발 환경**에 가깝게 구성해 줌

---

## 원문
- [원문](https://buildingbetter.tech/p/i-read-the-claude-code-source-code)
- [GeekNews 토론](https://news.hada.io/topic?id=30030)

## My Note
<!-- 한 줄 코멘트 남기기 -->

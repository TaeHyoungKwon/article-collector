---
category: Dev Tools
collected_at: '2026-08-16T03:38:34+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32534
id: hada-32534
matched_keywords:
- Claude Code
read: false
recommend_score: 2.901
recommended_on: '2026-08-17'
source: geeknews
tags:
- Dev Tools
- Other
- claude.com
title: Claude Code 세션의 가치를 극대화하는 방법
url: https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code는 같은 작업도 **컨텍스트 크기와 유지 턴 수**, 병렬 컨텍스트 수에 따라 토큰 사용량이 달라지므로 필요한 정보만 세션에 남겨야 함
- 비용은 모델, 입출력 유형, 프롬프트 캐시에 좌우되며 **출력은 입력보다 약 5배 비싸고**, 캐시 읽기는 일반 입력 가격의 0.1배임
- 대화 중간에 `/model`, `/effort`, Fast mode를 바꾸면 **프롬프트 캐시가 깨질 수 있으므로** 세션 시작이나 `/clear` 직후 설정하는 편이 저렴함
- 파일은 **@-mention으로 첨부**하고, 테스트·빌드처럼 출력이 많은 명령은 quiet 옵션을 적용하거나 서브에이전트에서 실행해 불필요한 컨텍스트 누적을 줄일 수 있음
- 새 작업 전에는 `/clear`, 같은 작업의 단계가 끝난 뒤에는 `/compact`를 사용하고, **1시간 캐시 만료** 전에 오래 자리를 비울 예정이라면 미리 압축하는 편이 유리함

---

## 원문
- [원문](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions)
- [GeekNews 토론](https://news.hada.io/topic?id=32534)

## My Note
<!-- 한 줄 코멘트 남기기 -->

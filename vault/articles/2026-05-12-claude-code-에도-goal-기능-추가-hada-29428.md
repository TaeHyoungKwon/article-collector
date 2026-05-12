---
category: Dev Tools
collected_at: '2026-05-12T17:34:38+09:00'
geeknews_comments: 2
geeknews_score: 7
geeknews_url: https://news.hada.io/topic?id=29428
id: hada-29428
matched_keywords:
- Claude Code
- Codex
read: false
recommend_score: 6.409
source: geeknews
tags:
- Dev Tools
- Other
- code.claude.com
title: Claude Code 에도 /goal 기능 추가
url: https://code.claude.com/docs/ko/goal
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code에 목표 기반 자동 반복 실행 기능인 /goal 추가
- 목표가 완료될 때까지 Claude가 여러 턴을 자동으로 이어서 실행
- 각 턴 종료 후 fast model이 목표 달성 여부를 평가
- 미완료 시 다음 턴 자동 시작, 완료 시 goal 자동 제거
- 평가자는 파일/명령을 직접 확인하지 않고 대화 기록 기준으로 판단
- 세션당 goal은 1개만 활성화 가능
- --resume, --continue 시 활성 goal도 복원
- Claude 문서에서는 session-scoped Stop hook 래퍼로 설명
- Codex CLI의 /goal과 유사하지만 구현 설명은 다름
- Codex는 goal continuation / budget limit 프롬프트 템플릿 중심
- Claude는 Stop hook, /loop, auto mode 체계 안에서 goal을 설명
- auto mode는 도구 승인 자동화, /goal은 턴 반복 자동화에 가까움
- 두 도구 모두 채팅형 보조자에서 목표 기반 자율 작업자로 수렴 중

## 원문
- [원문](https://code.claude.com/docs/ko/goal)
- [GeekNews 토론](https://news.hada.io/topic?id=29428)

## My Note
<!-- 한 줄 코멘트 남기기 -->

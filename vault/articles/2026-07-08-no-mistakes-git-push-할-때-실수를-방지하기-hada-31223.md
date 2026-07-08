---
category: AI
collected_at: '2026-07-08T09:31:02+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31223
id: hada-31223
matched_keywords:
- AI
- Codex
read: false
recommend_score: 4.901
source: geeknews
tags:
- AI
- Other
- github.com/kunchenguid
title: no-mistakes - git push 할 때 실수를 방지하기
url: https://github.com/kunchenguid/no-mistakes
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 실제 remote 앞에 **로컬 git 프록시**를 둬서, `origin` 대신 `no-mistakes`로 push하면 검증을 거쳐 **깔끔한 PR**을 자동 생성
- push 시 **일회용 worktree**를 띄워 **AI 기반 검증 파이프라인**을 `review → test → docs → lint → push → PR → CI` 순서로 실행하고, 모든 검사 통과 후에만 설정된 push 대상으로 브랜치 전달
- 검증이 **격리된 worktree**에서 실행되는 **논블로킹** 구조라 진행 중인 작업을 방해하지 않음
- **Agent 비종속적**: `claude`, `codex`, `opencode`, `pi`, `copilot` 등을 지원하며 순서 지정 폴백 제공
- **Agent 네이티브**: `/no-mistakes`로 코딩 에이전트의 작업이나 이미 커밋된 작업을 **검증 파이프라인에 태울 수 있음**
- 각 단계는 통과하거나, 사용자가 처리해야 할 **finding**과 함께 중단됨. 안전한 기계적 수정은 자동 적용되고, 의도가 걸린 항목만 **approve / fix / skip**으로 사용자에게 에스컬레이션
- 모든 검사가 green이 되기 전까지는 어떤 것도 push 대상에 도달하지 않음
- 세 가지 실행 방식 지원
  - `git push no-mistakes` — 커밋된 브랜치를 게이트 remote로 push하는 명시적 Git 경로
  - `no-mistakes` — TUI, 변경 후 실행 시(커밋 불필요) 브랜치 생성·커밋·push를 마법사가 안내, `-y`로 자동 수행
  - `/no-mistakes` — 에이전트 skill, 내부적으로는 비대화형 [TOON(Token-Oriented Object Notation)](https://news.hada.io/topic?id=24458) 인터페이스로 `no-mistakes axi` 구동
- 모든 검사 통과 시 게이트가 브랜치를 전달하고 PR을 열어주므로, 수동 `git push origin` 이나 직접 PR 본문을 작성할 필요 없음
- MIT 라이선스

## 원문
- [원문](https://github.com/kunchenguid/no-mistakes)
- [GeekNews 토론](https://news.hada.io/topic?id=31223)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-08T15:33:17+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30282
id: hada-30282
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 8.901
recommended_on: '2026-06-08'
source: geeknews
tags:
- AI
- Other
- github.com/devenjarvis
title: 'Show HN: Lathe – LLM으로 새 도메인을 건너뛰지 않고 학습하기'
url: https://github.com/devenjarvis/lathe
---

## TL;DR
- Lathe는 LLM을 활용하여 사용자가 실습형 기술 튜토리얼을 로컬 UI에서 직접 학습할 수 있도록 돕는 도구이다.
- 이 도구는 튜토리얼 생성, 검증, 확장을 지원하며, 여러 LLM 세션에서 튜토리얼 제작이 가능하다.
- Lathe는 개인 학습에 초점을 맞추고 있으며, 사용자 맞춤형 튜토리얼을 통한 효과적인 자기 학습 방법을 제공한다.

## GeekNews 요약
- Lathe는 LLM이 대신 생각하게 하기보다 가르치도록 쓰는 실험으로, 프롬프트에서 **실습형 기술 튜토리얼**을 생성하고 사용자가 로컬 UI에서 직접 손으로 따라가며 학습하게 함
- 단일 파트 또는 여러 파트의 튜토리얼 생성을 지원하며, 질문하기, 튜토리얼 검증, 새 파트 확장, 검색 태그 추가를 위한 **LLM skills**를 제공함
- Claude Code, Cursor, Codex의 대화형 LLM 세션에서 튜토리얼을 생성할 수 있고, Go로 만든 `lathe` CLI가 튜토리얼 저장, 관리, 렌더링, 영속 상태를 담당함
- CLI 자체는 LLM을 호출하지 않으며, 웹 버튼과 `lathe verify`·`lathe extend` 명령은 LLM 세션에 붙여 넣을 **skill command**를 제공하는 방식임
- 로컬 웹 UI는 `lathe serve`로 실행하며 기본 포트는 `4242`; 튜토리얼 목록에서 제목, 주제, 태그, 저장소, 도구 버전 검색과 최신순·오래된순·제목순 정렬, 상태·유형·태그·버전 필터를 지원함
- 읽기 UI는 오른쪽 사이드바의 목차 탐색, 본문 중간의 사이드 노트, 튜토리얼 끝의 독자용 연습 문제를 제공함
- 모든 튜토리얼은 사용한 출처, 모델, 튜토리얼 문체를 이끈 프롬프트를 기록하며, 출처 기록은 `metadata.json`의 `sources` 필드와 UI의 출처 패널로 확인 가능함
- 튜토리얼은 전역 경로 `~/.lathe/tutorials/`에 슬러그별 디렉터리로 저장되며, `metadata.json`과 `part-01.md` 같은 파트 파일 또는 `index.md`로 구성됨
- 설치는 단일 독립 실행 바이너리 `lathe`를 `$PATH`에 두는 방식이며, macOS용 Homebrew cask, `curl | sh` 설치 스크립트, Go 1.25+ 기반 `go install`, 소스 빌드를 지원함
- skills는 바이너리에 번들되어 있으며 `lathe skills install`로 Claude Code, Cursor, Codex용 위치에 설치 가능함
- 튜토리얼 문체는 **voice**로 제어되며 기본 `plainspoken`과 `companion`이 함께 제공되고, `/lathe-voice`로 사용자 정의 voice를 만들 수 있음
- voice는 문체만 바꾸며 정확성, 조사, 인용, 검증, 구조는 바꾸지 않음; 사용자 정의 voice는 실존 인물 사칭, 자격 조작, LLM 저작 부인을 거부하도록 설정됨
- 검증은 선택 사항이며 대화형 LLM 세션에서 `/lathe-verify <slug>`로 실행됨; 새 `mktemp -d` 스크래치 디렉터리에 파일을 만들고 명령과 `## Checkpoint` 블록을 실행한 뒤 결과를 기록함
- 검증 상태는 `unverified`, `verifying`, `verified`, `failed`, `skipped`, `extending` 중 하나이며, 필요한 도구가 없으면 실패가 아니라 `skipped`로 기록됨
- 검증은 일반 LLM 권한 모델 아래에서 실행되어 도구 호출을 보고 승인할 수 있으며, 스크래치 디렉터리는 빌드 산출물을 저장소 밖에 두기 위한 관례일 뿐 보안 경계가 아님
- Lathe는 LLM이므로 LLM이 실패하는 방식으로 실패할 수 있으며, 튜토리얼 생성에는 접근 가능한 가장 큰 “thinking” 모델 사용을 권장함
- 현재 자체 테스트 사용 사례는 macOS의 Claude Code이며, 그 밖의 구성은 동작할 수 있지만 검증되지 않았다고 명시함
- 개인 학습을 위한 개인 사용 외의 콘텐츠 작성 용도로 의도되지 않음

## 원문
- [원문](https://github.com/devenjarvis/lathe)
- [GeekNews 토론](https://news.hada.io/topic?id=30282)

## My Note
<!-- 한 줄 코멘트 남기기 -->

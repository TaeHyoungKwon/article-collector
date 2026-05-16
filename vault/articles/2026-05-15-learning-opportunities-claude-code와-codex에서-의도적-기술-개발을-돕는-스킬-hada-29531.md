---
category: AI
collected_at: '2026-05-15T10:29:29+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29531
id: hada-29531
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -992.693
recommended_on: '2026-05-15'
source: geeknews
tags:
- AI
- Other
- github.com/DrCatHicks
title: Learning Opportunities - Claude Code와 Codex에서 의도적 기술 개발을 돕는 스킬
url: https://github.com/DrCatHicks/learning-opportunities
---

## TL;DR
- Claude Code와 Codex에서 사용자의 전문성을 증진시키는 기술 개발을 지원하는 학습 기회를 다룬 글이다.
- Claude는 사용자에게 10~15분짜리 선택형 학습 연습을 제공하며, 이를 통해 에이전틱 코딩 방식에서 학습의 질을 향상시키도록 설계되었다.
- 이 스킬은 개발자들이 실제 프로젝트에서 더욱 효과적으로 학습하고 성장할 수 있도록 돕는 데 중요한 의미가 있다.

## GeekNews 요약
- **에이전틱 코딩**을 하면서 프로젝트만이 아니라 **사용자의 전문성**도 키우도록 돕는 Claude Code 및 Codex용 스킬
- 새 파일 생성, 스키마 변경, 리팩터링 같은 **아키텍처 작업**을 마친 뒤 **Claude가 10~15분짜리 선택형 학습 연습을 제안**함
- 연습은 **예측, 생성, 인출 연습, 간격 반복** 같은 학습과학 기법을 사용하며, 사용자의 실제 프로젝트 작업에서 반쯤 풀린 예제를 만들어 줌
- AI 코딩 도구가 생성 코드 수용, 유창성 착각, 장시간 몰아치기, 메타인지 부족, 자기 테스트 감소를 유발할 수 있다는 문제를 줄이도록 설계됨
- Claude는 “이 주제로 짧은 학습 연습을 해볼까요? 약 10~15분입니다”처럼 묻고, 사용자가 수락하면 **대화형 연습**을 진행함
- 핵심 설계 원칙은 Claude가 자기 질문에 답하지 않고 **사용자 입력을 기다리는 것**이며, 빠른 agentic coding과 다른 반성·탐색 모드를 만들도록 의도됨
- 연습 유형에는 예측→관찰→성찰, 생성→비교, 실행 경로 추적, 디버깅 예측, 새 개발자에게 설명하기, 이전 세션 내용 인출 점검이 포함됨
- 현재 제안된 억제 조건은 한 세션에서 이미 연습을 거절했거나, 한 세션에서 연습을 2번 완료했을 때 학습 기회를 다시 제안하지 않는 것임
- Codex에서는 `codex plugin marketplace add https://github.com/DrCatHicks/learning-opportunities.git`로 마켓플레이스에 추가할 수 있고, `learning-opportunities`, `learning-opportunities-auto`, `orient`가 포함됨
- Claude Code에서는 [Claude Code plugin marketplace](https://docs.claude.com/en/docs/claude-code/plugins)로 추가한 뒤 `/plugin install learning-opportunities@learning-opportunities`를 설치하고 재시작해 활성화함
- `learning-opportunities-auto`는 Linux와 macOS에서 git commit 뒤 Claude가 연습 제안을 고려하게 하는 선택형 훅이며, Windows도 [추가 설정](https://github.com/DrCatHicks/learning-opportunities-auto/README.md#windows-setup)으로 사용할 수 있음
- `orient` 스킬은 새 저장소를 배울 때 `orientation.md`를 만들고, 프로그램 이해와 코드베이스 탐색 연구에 기반한 추천 레슨을 제공함
- [Learning-Goal](https://github.com/DrCatHicks/learning-goal)과 함께 쓰기 좋으며, 해당 스킬은 MCII 기법으로 반구조화된 대화형 학습 목표 설정을 돕는다고 소개됨
- 팀 실험에는 [MEASURE-THIS.md](https://github.com/DrCatHicks/learning-opportunities/docs/MEASURE-THIS.md)를 함께 사용할 수 있고, 검증된 설문 문항, 결과 해석 가이드, 리더십 공유용 “team boast” 템플릿, Claude.md 통계 엄밀성 넛지를 제공함
- [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)로 라이선스됨

## 원문
- [원문](https://github.com/DrCatHicks/learning-opportunities)
- [GeekNews 토론](https://news.hada.io/topic?id=29531)

## My Note
<!-- 한 줄 코멘트 남기기 -->

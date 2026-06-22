---
category: AI
collected_at: '2026-06-21T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30677
id: hada-30677
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: -990.901
recommended_on: '2026-06-21'
source: geeknews
tags:
- AI
- Other
- github.com/alibaba
title: open-code-review — Alibaba의 AI 코드 리뷰 도구
url: https://github.com/alibaba/open-code-review
---

## TL;DR
- 알리바바의 AI 코드 리뷰 도구 **open-code-review**는 수백만 건의 코드 결함을 식별한 후 오픈소스로 공개되었다.
- 이 도구는 **라인 단위의 심층 리뷰**를 통해 정밀도를 높이고, 코드 리뷰 속도를 향상시키며, 에이전트와 엔지니어링 로직의 하이브리드 구조로 동작한다.
- 개발자들은 이 도구를 통해 코드 결함의 식별과 리뷰 과정을 효과적으로 개선할 수 있을 것으로 기대된다.

## GeekNews 요약
- 알리바바가 내부에서 사용하던 **AI 코드 리뷰 어시스턴트**로 **2년간 수만 명의 개발자**가 **수백만 건의 코드 결함**을 식별한 뒤 오픈소스로 공개
- Git diff를 읽고 변경 파일을 **도구 사용 에이전트를 통해 LLM에 전달**하고, **라인 단위 정밀도**의 구조화된 리뷰 코멘트 생성
  - 에이전트는 전체 파일 읽기, 코드베이스 검색, 컨텍스트를 위해 다른 변경 파일 까지 확인하며 표면적 diff가 아닌 **심층 리뷰** 수행
- 핵심은 **결정론적 엔지니어링 × 에이전트 하이브리드** : 반드시 **정확해야 하는 단계는 엔지니어링 로직**이, **동적 판단은 에이전트**가 맡는 구조
- 동일 모델 기준 범용 에이전트(Claude Code) 대비 **Precision·F1이 더 높고 토큰은 약 1/9** 수준만 소비하며 리뷰 속도도 빠름
  - 실제 결함을 빠짐없이 잡는 Recall은 더 낮은 대신, **보고하는 건 대부분 진짜 결함**이 되도록 정밀도를 우선한 의도적 트레이드오프
- **정밀 파일 선택**과 **스마트 파일 번들링**으로 큰 변경셋에서도 누락 없이 안정적으로 동작하며, 연관 파일을 격리된 서브 에이전트로 동시 리뷰
- 세분화된 규칙 매칭은 **템플릿 엔진 기반**이라 언어 기반 안내보다 안정적·예측 가능, 독립 모듈로 코멘트 위치·내용 정확도 동시 개선
- 4계층 우선순위 체인 : `--rule` > 프로젝트 설정 > 글로벌 설정 > 시스템 기본
  - 각 계층은 first-match-wins 방식으로 경로가 매칭되면 해당 규칙 적용 후 다음 계층으로 넘어가지 않음
- CLI, 코딩 에이전트 플러그인(Skill·Claude Code·Codex), CI/CD 파이프라인 통합 지원
- OpenAI·Anthropic 호환
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/alibaba/open-code-review)
- [GeekNews 토론](https://news.hada.io/topic?id=30677)

## My Note
<!-- 한 줄 코멘트 남기기 -->

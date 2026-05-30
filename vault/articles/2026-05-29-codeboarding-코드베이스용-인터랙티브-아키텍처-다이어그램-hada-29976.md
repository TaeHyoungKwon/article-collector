---
category: AI
collected_at: '2026-05-29T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29976
id: hada-29976
matched_keywords:
- AI
- LLM
read: false
recommend_score: -994.614
recommended_on: '2026-05-29'
source: geeknews
tags:
- AI
- Other
- github.com/CodeBoarding
title: CodeBoarding - 코드베이스용 인터랙티브 아키텍처 다이어그램
url: https://github.com/CodeBoarding/CodeBoarding
---

## TL;DR
- CodeBoarding은 코드베이스 아키텍처를 자동으로 시각화해주는 오픈소스 도구이다.
- 이 도구는 정적 분석과 LLM 추론을 통해 코드베이스의 다이어그램과 문서를 자동 생성하며, 결과물을 쉽게 저장하고 활용할 수 있다.
- 개발자는 CodeBoarding을 통해 AI와의 협업을 통해 코드 구조를 이해하고 기술 부채를 방지할 수 있는 기회를 가진다.

## GeekNews 요약
- 사람과 AI 에이전트가 함께 보는 코드베이스 지도를 자동으로 그려주는 오픈소스 도구
- **정적 분석과 LLM 추론을 결합**해 코드베이스의 고수준 아키텍처 다이어그램과 주요 컴포넌트 문서를 자동 생성
- 결과물은 `.codeboarding/` 디렉터리에 **Markdown 문서**와 **Mermaid 다이어그램** 형태로 저장되어 IDE, CI, PR, 문서에 그대로 임베드 가능
- **증분 업데이트**를 지원해 코드베이스 일부만 변경된 경우 해당 부분만 재분석해 대규모 레포지토리에서도 빠르게 동작
- 6개 핵심 컴포넌트로 구성
  - **Application Orchestrator & Repository Manager**: 분석 워크플로우 시작 및 컨텍스트 전달
  - **LLM Agent Core**: 전문화된 도구를 호출해 코드와 분석 데이터를 다룸
  - **Static Code Analyzer**: 코드 세그먼트의 정적 분석 수행
  - **Agent Tooling Interface**: 에이전트가 정적 분석 엔진에 질의하는 인터페이스
  - **Incremental Analysis Engine**: 변경된 코드만 정적 분석 요청 및 결과 캐싱
  - **Documentation & Diagram Generator**: 분석 결과를 문서와 다이어그램으로 변환
- 활용 시나리오
  - AI 에이전트가 코드를 작성하는 동안 **아키텍처 가시성 유지**
  - AI 생성 변경사항을 **시스템 컨텍스트와 함께 리뷰**하여 숨겨진 기술 부채 사전 차단
  - **레이어드 다이어그램과 컴포넌트 분해**로 대규모 레포지토리 빠른 이해
  - 로컬 워크플로우, IDE, PR, 문서에서 동일한 시각 모델 공유
- **8개 언어** 지원: Python, TypeScript, JavaScript, Java, Go, PHP, Rust, C#
- **여러 LLM 프로바이더 연동**: OpenAI, Anthropic, Google, Vercel AI Gateway, AWS Bedrock, Ollama, OpenRouter 등
- 세 가지 배포 형태로 제공
  - **CLI**: 로컬 분석, 자동화, CI 워크플로우용 (`pipx install codeboarding`)
  - **VS Code 익스텐션**: 에디터 내에서 시각적 아키텍처 확인
  - **GitHub Action**: CI에서 다이어그램을 항상 최신 상태로 유지
- 이미 **800개 이상의 유명 오픈소스 레포지토리**를 시각화한 샘플 디비 제공
  - 공개 Repo : [GeneratedOnBoardings](https://github.com/CodeBoarding/awesome-architecture-mds)
  - 호스팅된 탐색기에서 일부 확인 가능 [codeboarding.org/diagrams](https://codeboarding.org/diagrams)
- **비전**: 인간과 AI 에이전트가 모두 활용 가능한 **코드 이해의 오픈 스탠더드** 구축
- MIT 라이선스

## 원문
- [원문](https://github.com/CodeBoarding/CodeBoarding)
- [GeekNews 토론](https://news.hada.io/topic?id=29976)

## My Note
<!-- 한 줄 코멘트 남기기 -->

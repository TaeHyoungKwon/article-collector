---
category: AI
collected_at: '2026-05-27T15:54:15+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29920
id: hada-29920
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
recommended_on: '2026-05-27'
source: geeknews
tags:
- AI
- Other
- github.com/millionco
title: React Doctor — AI가 생성한 React 코드를 정적 분석으로 검증하는 진단 도구
url: https://github.com/millionco/react-doctor
---

## TL;DR
- 이 글은 AI가 생성한 React 코드의 품질을 검증하는 도구인 React Doctor에 대해 다루고 있다.
- React Doctor는 프로젝트를 스캔하여 다양한 항목에 대한 진단 결과를 0~100점으로 출력하며, AI 연동을 지원한다.
- AI 코드의 품질 검증이 중요해진 현시점에서, 이 도구는 개발자들에게 신뢰할 수 있는 코드 품질 관리 방법을 제공한다.

## GeekNews 요약
AI 코딩 에이전트가 쓴 React 코드가 정말 올바른지, 누가 검토하고 있을까요. React Doctor는 바로 이 물음에서 출발한 도구입니다. `npx react-doctor@latest` 한 줄로 프로젝트를 스캔하면 상태 관리·부수 효과·성능·보안·접근성·아키텍처 전반에 걸친 진단 결과가 0~100점 점수와 함께 터미널에 출력됩니다. Million.co에서 개발했으며, MIT 라이선스로 공개되어 있습니다.

**핵심 특징**

- **AI 에이전트 연동을 명시적으로 지원합니다.** `react-doctor install`을 실행하면 Claude Code, Cursor, Codex, OpenCode 등 주요 에이전트에 스킬을 자동으로 등록하고, git post-checkout/post-merge 훅도 설치합니다. 에이전트가 문제를 일으키고, 다른 에이전트가 바로 잡는 구조입니다.
- **oxlint 기반의 100개 이상 규칙을 내장합니다.** 자체 oxlint 플러그인(`oxlint-plugin-react-doctor`)에 규칙을 직접 구현해 별도 ESLint 런타임 없이도 빠른 분석이 가능합니다. Next.js, TanStack, React Native, Expo 등 프레임워크별 규칙 프리셋이 별도로 준비되어 있습니다.
- **React Compiler 규칙을 통합합니다.** `react-hooks-js/*` 계열 규칙을 통해 React Compiler가 활성화된 환경에서 수동 메모이제이션 코드가 남아 있는 경우 즉시 감지합니다.
- **GitHub Actions 네이티브 지원입니다.** Marketplace에 올라간 공식 액션을 추가하면 PR마다 인라인 어노테이션과 스티키 코멘트로 진단 결과를 남깁니다. `--diff` 모드를 쓰면 변경된 파일만 스캔해 CI 시간을 줄입니다.
- **Effect v4 기반 스트리밍 파이프라인입니다.** 스캔 엔진 내부는 Effect 라이브러리의 의존성 주입·태그드 에러·제너레이터 기반 제어 흐름으로 구성되어 있으며, 린팅과 데드코드 분석을 병렬로 실행합니다.
- **프로그래밍 방식 접근도 가능합니다.** `@react-doctor/api` 패키지의 `diagnose()` 함수를 통해 타입화된 진단 결과를 Node.js 코드에서 직접 받아 처리할 수 있습니다.
- **점수 공유 기능을 제공합니다.** 스캔 결과를 `react.doctor/share`에 게시해 팀이나 외부에 공유할 수 있습니다.

**차별점**

기존 ESLint 기반 React 플러그인들이 규칙 하나하나를 개발자가 선택하고 구성해야 하는 것과 달리, React Doctor는 설치 즉시 전체 범주 진단을 실행하는 '감사 도구'로 포지셔닝되어 있습니다. 특히 AI가 작성한 코드의 품질을 검증한다는 사용 시나리오를 전면에 내세운다는 점은 눈에 띄는 방향입니다.

v0.2.4의 Effect v4 마이그레이션, v0.2.7의 병렬 분석과 에이전트 감지, 그리고 현재 v0.2.8까지 짧은 릴리스 주기가 이어지고 있습니다. 아직 메이저 버전에 도달하지 않은 만큼 API가 바뀔 여지가 있지만, 개발 속도와 커버리지 확장 추세는 꾸준합니다. AI 코드 생성이 일상화된 환경에서 코드베이스 품질의 마지막 검문소 역할을 목표로 하는 도구로 주목할 만합니다.

## 원문
- [원문](https://github.com/millionco/react-doctor)
- [GeekNews 토론](https://news.hada.io/topic?id=29920)

## My Note
<!-- 한 줄 코멘트 남기기 -->

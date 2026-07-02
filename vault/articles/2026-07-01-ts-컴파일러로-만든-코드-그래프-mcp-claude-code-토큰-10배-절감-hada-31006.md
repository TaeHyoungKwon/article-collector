---
category: AI
collected_at: '2026-07-01T20:21:28+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31006
id: hada-31006
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -994.901
recommended_on: '2026-07-01'
source: geeknews
tags:
- AI
- Other
- dev.to
title: TS 컴파일러로 만든 코드 그래프 MCP, Claude Code 토큰 10배 절감
url: https://dev.to/samchon/i-made-ts-compiler-graph-mcp-10x-fewer-tokens-in-claude-code-1aea
---

## TL;DR
- 이 글은 TS 컴파일러 활용으로 코드 그래프를 생성하여 토큰 사용을 줄이는 방법을 설명한다.
- @ttsc/graph는 코드 의존성을 효율적으로 분석해 토큰을 약 10배 절감하며, 답변 품질은 유지된다.
- 이는 코드 분석 효율성을 높이는 동시에, 개발자의 작업 환경을 개선할 수 있는 가능성을 제공한다.

## GeekNews 요약
- 코딩 에이전트가 "이거 어떻게 동작해?" 같은 구조 질문에 답할 때, 보통 grep → 파일 열기 → import 추적을 수십 번 반복하며 토큰을 태움
- @ttsc/graph는 TypeScript 컴파일러가 이미 해석해둔 코드 그래프(무엇이 무엇을 호출/의존하는지)를 MCP로 에이전트에 넘겨, 파일을 헤집는 대신 그래프에서 바로 답하게 함
- 설계 핵심 두 가지
  - 인덱스만 반환 – 소스 본문은 절대 안 주고 이름·엣지·시그니처·file:line span만 → 응답 크기가 레포 규모와 무관, 토큰이 안 터짐
  - 강제 Chain-of-Thought – 단일 툴의 입력이 타입 스키마라, 에이전트가 question → draft → review를 채운 뒤에야 요청 가능. typia가 스키마+검증기로 컴파일해 "추론 건너뛰기"를 호출 경계에서 거부
- 결과: open question 기준 토큰 약 10배 절감, 답변 품질 동등 (8개 레포 × 4개 모델, 보수적 median)
- 왜 컴파일러인가: tree-sitter 같은 휴리스틱 파서는 tsconfig paths 별칭·모노레포 교차참조·심링크·re-export 체인을 못 풂. 실제 모듈 해석을 끝낸 컴파일러라야 정확 → 신뢰 가능 → 에이전트가 확신하고 멈춤
- 선구자 대비: codegraph / codebase-memory-mcp / serena도 같은 아이디어를 먼저 냈지만, open question에선 토큰이 안 줄거나 오히려 baseline보다 더 씀 (저자 벤치, zod 기준 세 도구 모두 +22~27%)
- 한계: TypeScript 전용(넓이 대신 깊이), TypeScript v7(Go 런타임, 현재 RC) 필요. 4줄 설치

## 원문
- [원문](https://dev.to/samchon/i-made-ts-compiler-graph-mcp-10x-fewer-tokens-in-claude-code-1aea)
- [GeekNews 토론](https://news.hada.io/topic?id=31006)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-15T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=31445
id: hada-31445
matched_keywords:
- AI
read: false
recommend_score: -996.614
recommended_on: '2026-07-16'
source: geeknews
tags:
- AI
- Other
- jetbrains.github.io
title: Hexana - JetBrains의 WebAssembly 및 바이너리 분석 도구
url: https://jetbrains.github.io/hexana/
---

## TL;DR
- 이 글은 JetBrains의 Hexana라는 WebAssembly 및 바이너리 분석 도구에 대해 설명하고 있다.
- Hexana는 Kotlin Multiplatform 코어를 공유하며 다양한 플랫폼에서 바이너리 분석과 디버깅 기능을 제공한다.
- 개발자들은 이 도구를 통해 WebAssembly 파일을 보다 효율적으로 처리하고 다양한 환경에서 활용할 수 있다.

## GeekNews 요약
- `.wasm` 파일의 구조 분석/편집/실행/디버깅을 지원하며 **JetBrains 플러그인**과 **VS Code 확장**으로 제공
- 두 제품이 하나의 **Kotlin Multiplatform 코어**를 공유하며 Core Wasm/Component Model/GC/SIMD/Threads 등을 지원함
- import/export/함수/타입/사용자 정의 섹션을 탐색하고 크기 프로파일링/미사용 코드/단형화(monomorphisation)를 분석
- **JetBrains 플러그인**은 편집 가능한 WAT/WIT와 WASM/ELF Structure 도구 창을 제공
  - GraalWasm/Chicory용 Java 코드 완성과 `WebAssembly.instantiate`의 JavaScript/TypeScript 타입 추론을 지원
  - Parquet/Arrow IPC/Protocol Buffers와 `.class`/`.jar`/`.war`/`.apk`/`.jit` 파일도 검사 가능
- **VS Code 확장**은 가상 스크롤 Hex 뷰어와 11개 구조 분석 탭을 제공하며 Cursor/VSCodium에서도 동작
  - Protocol Buffers descriptor set 뷰어와 스크립트 기반 사용자 정의 분석 탭을 제공
  - Component Model 파일의 의존성을 탐지하고 해결하며, MCP 서버는 필요할 때 별도로 다운로드해 실행함
- 두 제품 모두 MCP 서버와 Wasmtime/WAMR/GraalVM/wazero 실행을 지원함
- ELF/Mach-O/PE 분석과 중단점 디버깅은 현재 **실험적 기능**으로 제공
- JetBrains 플러그인은 **깊은 편집/코드 연동**에, VS Code 확장은 **가벼운 `.wasm` 검사**에 적합

## 원문
- [원문](https://jetbrains.github.io/hexana/)
- [GeekNews 토론](https://news.hada.io/topic?id=31445)

## My Note
<!-- 한 줄 코멘트 남기기 -->

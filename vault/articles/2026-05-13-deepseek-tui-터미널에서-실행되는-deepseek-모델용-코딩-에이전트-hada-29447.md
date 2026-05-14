---
category: AI
collected_at: '2026-05-13T09:46:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29447
id: hada-29447
matched_keywords:
- AI
- LLM
read: false
recommend_score: -994.901
recommended_on: '2026-05-13'
source: geeknews
tags:
- AI
- Other
- github.com/Hmbown
title: DeepSeek-TUI - 터미널에서 실행되는 DeepSeek 모델용 코딩 에이전트
url: https://github.com/Hmbown/DeepSeek-TUI
---

## TL;DR
- DeepSeek-TUI는 터미널 환경에서 DeepSeek V4 모델을 활용한 코딩 에이전트를 다룬다.
- 이 에이전트는 자동 모델 선택 및 다양한 운영 모드를 통해 효율적인 파일 관리와 코드 작성을 지원한다.
- 사용자는 복잡한 환경에서도 빠르고 편리한 개발 작업을 수행할 수 있어 생산성이 향상된다.

## GeekNews 요약
- DeepSeek V4 모델 기반 **터미널 코딩 에이전트**로, 파일 편집·셸 실행·Git 관리·웹 검색·서브 에이전트 조율을 키보드 중심 TUI에서 수행
- `--model auto`로 매 턴마다 **모델(deepseek-v4-pro/flash)과 사고 수준(off/high/max)을 자동 선택** — 경량 Flash 라우팅 호출로 판단 후 실제 모델에 전달
- **1M 토큰 컨텍스트 윈도우**, 스트리밍 추론 블록, **prefix-cache 인식 실시간 비용 추적** 내장
- Plan(읽기 전용 탐색)·Agent(승인 게이트 대화형)·YOLO(자동 승인) **세 가지 운영 모드** 제공
- **MCP 프로토콜** 연동으로 외부 도구 서버 확장 가능, Stdio·SSE·Streamable HTTP 세 가지 전송 지원
- 편집 후 rust-analyzer·pyright·gopls·clangd 등을 통한 **LSP 인라인 진단** 자동 반영
- 세션 저장/복원, 워크스페이스 롤백(side-git 스냅샷), **내구성 태스크 큐**(재시작 후에도 유지) 지원
- `deepseek serve --http`로 **HTTP/SSE 헤드리스 API 서버** 실행 가능, Zed 에디터와는 `--acp`로 Agent Client Protocol 연동
- **Skills 시스템**: GitHub에서 인스트럭션 팩 설치(`/skill install github:<owner>/<repo>`), 백엔드 서비스 불필요, 에이전트가 `load_skill`로 자동 선택
- NVIDIA NIM·Fireworks·OpenAI 호환·SGLang·vLLM·**Ollama** 등 다양한 외부 API 프로바이더 지원
- npm·Cargo·Homebrew·Docker·Scoop·소스 빌드 등 **다양한 설치 경로** 제공, Linux ARM64(Raspberry Pi, Graviton 등)도 v0.8.8부터 프리빌트 바이너리 지원
- MIT 라이선스

## 원문
- [원문](https://github.com/Hmbown/DeepSeek-TUI)
- [GeekNews 토론](https://news.hada.io/topic?id=29447)

## My Note
<!-- 한 줄 코멘트 남기기 -->

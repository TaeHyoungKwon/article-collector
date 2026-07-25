---
category: AI
collected_at: '2026-07-24T09:36:46+09:00'
geeknews_comments: 1
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=31744
id: hada-31744
matched_keywords:
- AI
- Codex
read: false
recommend_score: -993.846
recommended_on: '2026-07-25'
source: geeknews
tags:
- AI
- Other
- omp.sh
title: omp - Pi를 IDE 수준으로 확장한 터미널 AI 코딩 에이전트
url: https://omp.sh/
---

## TL;DR
- omp는 Pi를 기반으로 하는 IDE 수준의 터미널 AI 코딩 에이전트이다.
- LSP와 다양한 개발 기능을 통합해 에이전트가 IDE처럼 활용할 수 있도록 설계되었다.
- 개발자에게 효율적인 작업 환경을 제공하지만, 기존 Pi Extension과의 호환성 문제가 존재하므로 주의가 필요하다.

## GeekNews 요약
- [omp](https://omp.sh/)는 Mario Zechner의 오픈소스 코딩 에이전트 [Pi](https://github.com/badlogic/pi-mono)를 기반으로, IDE 수준의 개발 도구와 실전 기능을 기본 탑재한 터미널 코딩 에이전트
- 단순한 UI 변경판이 아니라 Pi의 에이전트 구조를 확장해 **LSP, 디버거(DAP), 서브에이전트, 코드 리뷰, 웹·PDF 읽기, 세션 공유, 메모리** 등을 통합
- LSP가 파일 수정 과정에 직접 연결되어 참조 검색, 심볼 이름 변경, 진단 확인 등을 에이전트가 IDE처럼 활용할 수 있음
- 파일 기반 Skills를 지원하며 OMP 전용 Skill뿐 아니라 Claude, Codex, OpenCode, GitHub 등의 기존 Skill 구조도 탐색 가능
- TUI의 완성도가 준수하고, 에이전트가 현재 파일을 읽는지, 검색·수정·검증 중인지, 서브에이전트가 동작 중인지 등을 화면에서 비교적 명확하게 보여줌
- 직접 사용해 본 결과, **AI가 지금 무엇을 하고 있는지 놓치지 않게 해주는 UI**가 특히 유용했음. 긴 작업에서도 멈춘 것인지 실행 중인지 판단하기 쉬웠음
- 다양한 모델 제공자를 지원하고 macOS·Linux·Windows에서 사용할 수 있으며, Bun·Homebrew·설치 스크립트와 사전 빌드 바이너리를 제공함

다만 Pi 확장 생태계와의 호환성은 아직 완전히 안정됐다고 보기 어려움. npm/source-link 방식으로 설치한 버전에서, [**CommonJS 의존성을 포함한 일부 기존 Pi Extension이 로드되지 않는 문제**](https://github.com/can1357/oh-my-pi/issues/6449)가 확인되었음. 사전 컴파일 바이너리는 영향을 받지 않지만 패키지 설치와 외부 Extension 조합에서는 주의가 필요함. 원인은 재로딩된 호환성 모듈이 기존 CommonJS 브리지를 덮어쓰는 문제로 확인됐으며, 현재 수정 PR이 열려 있지만 아직 병합 전임.

Pi의 간결함을 유지하면서도 별도 설정 없이 LSP와 여러 개발 기능을 활용하고, 에이전트의 진행 상황을 명확한 TUI로 확인하고 싶은 개발자에게 매력적인 선택지. 다만 기존 Pi Extension을 적극적으로 사용하는 경우에는 호환성 이슈와 릴리스 변경 사항을 확인하는 편이 좋음.

## 원문
- [원문](https://omp.sh/)
- [GeekNews 토론](https://news.hada.io/topic?id=31744)

## My Note
<!-- 한 줄 코멘트 남기기 -->

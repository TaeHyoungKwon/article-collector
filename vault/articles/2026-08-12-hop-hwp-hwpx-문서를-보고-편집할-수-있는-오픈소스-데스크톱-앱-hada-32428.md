---
category: AI
collected_at: '2026-08-12T15:32:44+09:00'
geeknews_comments: 0
geeknews_score: 5
geeknews_url: https://news.hada.io/topic?id=32428
id: hada-32428
matched_keywords:
- AI
- RAG
read: false
recommend_score: -994.208
recommended_on: '2026-08-12'
source: geeknews
tags:
- AI
- Other
- github.com/golbin
title: HOP - HWP/HWPX 문서를 보고 편집할 수 있는 오픈소스 데스크톱 앱
url: https://github.com/golbin/hop
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- HWP/HWPX 문서를 **macOS, Windows, Linux에서 열고 편집할 수 있는 오픈소스 데스크톱 앱**
- Rust 기반 HWP/HWPX 파서·에디터인 **rhwp**를 문서 엔진으로 사용하고, 그 위에 데스크톱 환경에 필요한 기능을 추가한 구조
- 현재 지원 기능
  - HWP/HWPX 문서 열기
  - HWP 저장 및 다른 이름으로 저장
  - PDF 내보내기
  - 인쇄
  - 파일 Drag & Drop
  - `.hwp`, `.hwpx` 파일 연결
  - 여러 창에서 문서 열기
- 데스크톱 앱은 **Tauri 2** 기반
  - Native 메뉴 및 파일 명령
  - Rust 기반 Document Session 관리
  - Atomic Save
  - Native SVG → PDF 변환
  - Single Instance 및 OS의 File Open Event 처리
  - 창별 Drag & Drop 등을 구현
- macOS는 Apple Silicon/Intel을 모두 지원하며 Homebrew로도 설치 가능
  - `brew install hop`
- Windows x64와 Linux의 `.deb`, `.rpm`, AppImage를 제공하며 Linux arm64와 Arch Linux AUR도 지원
- 아직 HWPX 저장은 지원하지 않으며 HWPX는 열기만 가능
- Autosave/Recovery도 아직 구현 중이며, Windows 빌드는 코드 서명이 되어 있지 않아 SmartScreen 경고가 표시될 수 있음
- 현재 최신 버전은 **v0.4.1**
- MIT License

## 원문
- [원문](https://github.com/golbin/hop)
- [GeekNews 토론](https://news.hada.io/topic?id=32428)

## My Note
<!-- 한 줄 코멘트 남기기 -->

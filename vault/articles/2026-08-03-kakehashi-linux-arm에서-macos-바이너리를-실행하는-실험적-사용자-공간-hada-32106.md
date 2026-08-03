---
category: Other
collected_at: '2026-08-03T23:31:41+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32106
id: hada-32106
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/wie-project
title: Kakehashi - Linux ARM에서 macOS 바이너리를 실행하는 실험적 사용자 공간
url: https://github.com/wie-project/kakehashi
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Kakehashi**는 Linux aarch64에서 Darwin Mach-O를 불러와 macOS ARM64 CLI 바이너리를 실행하는 사용자 공간 변환 계층으로, JIT나 명령어 에뮬레이션 없이 동작함
- 독립형 `libSystem`을 매핑하고 **BSD 시스템 호출**을 Linux로 변환하며, clang 프로브와 Darwin용 `7zz`, `curl`, 스레드 실행을 지원함
- 실제 실행은 **Linux aarch64**와 4KiB·16KiB 페이지 환경이 필요하지만, 바이너리 검사와 dry-load는 macOS를 포함한 모든 호스트에서 가능함
- 약 8천 파일·240MiB를 압축한 테스트에서 Darwin `7zz`는 네이티브 Linux 대비 약 **5.2배 느렸지만**, 파일 수가 적은 압축 중심 작업에서는 격차가 약 1.1~1.2배였음
- 목표는 macOS 전체 호환이 아니라 저렴한 Linux ARM CI에서 **Darwin CLI 도구**를 실행하는 것이며, GUI·코드 서명·공증·Xcode UI 테스트와 Apple 프레임워크 의존 작업은 지원 범위가 아님

---

## 원문
- [원문](https://github.com/wie-project/kakehashi)
- [GeekNews 토론](https://news.hada.io/topic?id=32106)

## My Note
<!-- 한 줄 코멘트 남기기 -->

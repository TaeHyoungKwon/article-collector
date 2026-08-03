---
category: AI
collected_at: '2026-08-03T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=32078
id: hada-32078
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 7.946
source: geeknews
tags:
- AI
- Other
- github.com/callstack
title: agent-device - AI 에이전트가 iOS/Android 기기를 제어하도록 돕는 CLI
url: https://github.com/callstack/agent-device
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **코딩 에이전트**가 실행 중인 앱을 직접 검사/조작/검증하고 결과를 근거로 저장하도록 지원
- iOS, Android, tvOS, Android TV, Amazon Vega OS TV, web, macOS, Linux 등 지원
- **토큰 효율적인 접근성 스냅샷**을 읽고 ref 또는 selector로 요소를 찾아 기기 동작 실행
- Vercel의 **agent-browser**에서 가져온 **inspect-act-verify** 프로세스를 모바일/TV/데스크톱 앱에 적용, 에이전트가 각 명령 결과를 읽고 다음 명령을 스스로 선택
- 에이전트들이 가능한 동작
  - **앱 상태 검사**: accessibility snapshot, ref, selector, React Native 컴포넌트 트리 확인
  - **화면 UI 조작**: 요소 탭/프레스, 필드 입력, 스크롤, 제스처, 대기, 상태 단언, 알림 처리
  - **실패 진단**: screenshot, video, log, trace, network 데이터, 성능 샘플, crash 상세, React profile 확보
  - **워크플로우 반복**: 정상 동작 단계를 **.ad 스크립트**로 저장해 로컬/CI에서 재현하거나 strict **Maestro YAML**로 내보내기
- 대상별 백엔드 사용: iOS/tvOS는 **XCTest**, Android는 ADB/snapshot helper, VVD는 Vega CLI/VDA, macOS는 로컬 helper, Linux는 **AT-SPI**
- native iOS/Android 앱 및 **React Native, Expo, Flutter** 로 개발된 앱도 지원
- Appium/Detox/Maestro 등은 테스트 스위트를 작성/유지하는 방식이지만, agent-device는 **런타임에 상태를 읽고 명령을 선택**하며 기존 도구를 보완하는 역할
- Cursor, Codex, Claude Code, Windsurf 등 에이전트 터미널에서 실행 가능
- MIT 라이선스

## 원문
- [원문](https://github.com/callstack/agent-device)
- [GeekNews 토론](https://news.hada.io/topic?id=32078)

## My Note
<!-- 한 줄 코멘트 남기기 -->

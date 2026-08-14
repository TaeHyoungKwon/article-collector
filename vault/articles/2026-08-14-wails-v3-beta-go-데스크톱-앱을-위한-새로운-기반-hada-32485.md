---
category: AI
collected_at: '2026-08-14T09:45:02+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=32485
id: hada-32485
matched_keywords:
- AI
read: false
recommend_score: 3.609
recommended_on: '2026-08-14'
source: geeknews
tags:
- AI
- Other
- v3.wails.io
title: Wails v3 Beta - Go 데스크톱 앱을 위한 새로운 기반
url: https://v3.wails.io/blog/wails-v3-beta/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 초기엔 **Go 백엔드 + HTML/CSS/JS·React·Vue 프론트엔드**로 맥/윈/리눅스용 단일 바이너리 앱을 만드는 가벼운 Electron 대체제였음
- 이후 v2를 거쳐 이번 **v3 Beta**에서는 단순 GUI 래퍼보다 복잡한 데스크톱 앱을 만들기 위한 애플리케이션 구조 자체를 크게 재설계
- `wails.Run(...)`과 암묵적인 컨텍스트 중심 구조를 버리고 **Application / Window / Service를 명시적인 객체와 수명주기**로 다루도록 변경
- 특히 **멀티윈도우를 기본 기능으로 지원**해 에디터/Inspector/Preferences/Tool Window처럼 여러 창을 사용하는 앱을 별도 우회 방식 없이 구현 가능
- 기존 binding 대신 **Go Service**를 도입해 백엔드 기능과 프론트엔드에 노출되는 API의 경계를 명확하게 만듦
- Go 소스를 정적 분석해 TypeScript 바인딩을 만들기 때문에 **주석과 실제 파라미터 이름까지 보존**하며, 런타임 reflection 기반 방식보다 프론트엔드 API가 풍부해짐
- Service가 Go API뿐 아니라 프론트엔드 asset/script까지 함께 제공할 수 있어, 향후 **설치형 플러그인 구조**를 만들 수 있는 기반도 추가됨
  - 범용 플러그인 시스템 자체는 아직 포함되지 않음
- 빌드 과정도 프레임워크 내부에 숨기지 않고 **Taskfile 기반으로 공개**해 직접 확인/확장/디버깅할 수 있게 바뀜
- 같은 Application/Service를 네이티브 창 없이 실행하는 **Server Build**도 지원해 데스크톱 UI와 백엔드 로직을 분리해 활용할 수 있음
- 맥/윈/리눅스의 amd64/arm64를 지원하고, Linux 기본 스택은 **GTK4 + WebKitGTK 6.0**으로 변경됨. iOS/Android도 실험적으로 지원
- v3는 2023년 1월 첫 Alpha 이후 3년 넘게 개발돼 이번에 Beta 단계에 진입함
- 단, 아직 **3.0 정식 릴리스가 아닌 Beta**이며 v2가 현재 안정 버전. 데스크톱 API는 안정화됐지만 운영 배포 전 충분한 테스트를 권장함
- v2→v3는 단순 버전 업이 아니라 Application/Window 수명주기, Service, v2 Runtime API, 프론트엔드 바인딩을 다시 옮겨야 하는 **실질적인 포팅 작업**으로 봐야 함

## 원문
- [원문](https://v3.wails.io/blog/wails-v3-beta/)
- [GeekNews 토론](https://news.hada.io/topic?id=32485)

## My Note
<!-- 한 줄 코멘트 남기기 -->

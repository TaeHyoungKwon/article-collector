---
category: AI
collected_at: '2026-06-08T13:53:02+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30280
id: hada-30280
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 5.307
source: geeknews
tags:
- AI
- Other
- github.com/seungmanchoi
title: 'Show GN: 1인 앱 개발을 위한 React Native + Expo 베이스 템플릿'
url: https://github.com/seungmanchoi/react-native-fsd-agent-template
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
1인 개발자가 React Native 앱을 빠르게 만들고 실제 스토어 배포까지 이어갈 수 있도록 만든 베이스 템플릿입니다.

React Native + Expo 기반에 Feature-Sliced Design(FSD) 구조를 적용했고, 앱 아이디어 발굴부터 기획, 디자인 시스템, 기능 구현, QA, 배포까지 이어지는 AI Agent Harness를 함께 넣었습니다.  
iOS, Android 배포 가능하고 앱 개발을 계속 하면서 이 프로젝트를 지속적으로 업데이트 하고 있습니다.

주요 특징은 다음과 같습니다.

- React Native 0.81 + Expo 54 기반
- TypeScript strict mode
- Expo Router, Zustand, TanStack Query, Axios, NativeWind 구성
- FSD 구조에 맞춘 features / entities / shared 레이어링
- Claude Code용 agent 9개와 skill 8개 포함
- “Make an app” 식의 명령으로 아이디어 → 기획 → 설계 → 구현 → QA 흐름을 자동화
- AdMob, Firebase Analytics, SecureStore 기반 토큰 저장, 인앱 리뷰 정책 모듈 포함
- EAS Build / Submit 기준의 스토어 배포 흐름 포함

단순 스타터보다는 “혼자서 앱을 많이 만들고 배포하는 사람”을 위한 템플릿에 가깝습니다.

예를 들어 새 앱을 만들 때 매번 반복되는 작업들, 즉 인증 구조, API 클라이언트, 상태 관리, 광고 동의 플로우, 분석 이벤트, 앱 리뷰 정책, 빌드 설정, FSD 모듈 구조 등을 처음부터 다시 붙이지 않도록 구성했습니다.

또 AI 에이전트가 코드를 아무 곳에나 생성하지 않도록 FSD 규칙, 작업 단계, QA 기준, typecheck/lint 기준을 템플릿 안에 함께 넣었습니다. 구현 후에는 qa-reviewer와 app-inspector가 코드 품질, UX, Safe Area, 접근성 등을 점검하는 흐름을 의도했습니다.

개인적으로는 “바이브 코딩으로 앱 하나 만들어보기”보다, “1인 개발자가 여러 앱을 반복적으로 기획하고 출시할 수 있는 생산 라인”에 초점을 맞춘 프로젝트입니다.

GitHub: <https://github.com/seungmanchoi/react-native-fsd-agent-template>

## 원문
- [원문](https://github.com/seungmanchoi/react-native-fsd-agent-template)
- [GeekNews 토론](https://news.hada.io/topic?id=30280)

## My Note
<!-- 한 줄 코멘트 남기기 -->

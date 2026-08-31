---
category: Dev Tools
collected_at: '2026-07-14T14:40:39+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31431
id: hada-31431
matched_keywords:
- Claude Code
read: false
recommend_score: 2.901
recommended_on: '2026-08-31'
source: geeknews
tags:
- Dev Tools
- Other
- scottwillsey.com
title: Xcode를 열지 않고 Mac·iOS 앱 빌드와 배포하기
url: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 초기 Apple 계정·인증서 설정을 마치면 **Xcode.app 내부 CLI 도구**만으로 Mac과 iOS 앱의 빌드, 서명, 배포를 자동화할 수 있음
- `project.yml`에서 **XcodeGen**으로 `.xcodeproj`를 재생성하고, `xcodebuild`, `notarytool`, `stapler`, `devicectl`로 프로젝트 생성부터 Mac 공증과 iPhone 설치까지 처리함
- Mac 배포는 `scripts/release.sh` 하나로 아카이브, **Developer ID 서명**, 공증, 티켓 스테이플링, Gatekeeper 검증, `/Applications` 설치를 순서대로 실행하며 실패 시 즉시 중단됨
- 빠른 컴파일과 테스트에는 `CODE_SIGNING_ALLOWED=NO`를 사용할 수 있지만, 이 **임시 서명 빌드**는 Gatekeeper를 통과하지 못하고 iCloud KVS와 App Group 권한도 실제 팀 ID에 결합되지 않음
- 서명 개인 키와 공증 암호는 **로그인 키체인**에 보관하고, `CLAUDE.md` 또는 `AGENTS.md`에 명령과 배포 규칙을 기록하면 Claude Code 같은 에이전트가 전체 워크플로를 반복 실행할 수 있음

---

## 원문
- [원문](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/)
- [GeekNews 토론](https://news.hada.io/topic?id=31431)

## My Note
<!-- 한 줄 코멘트 남기기 -->

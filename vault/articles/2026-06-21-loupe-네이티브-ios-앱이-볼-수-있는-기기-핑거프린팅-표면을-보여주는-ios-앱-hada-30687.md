---
category: AI
collected_at: '2026-06-21T20:33:39+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30687
id: hada-30687
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-06-21'
source: geeknews
tags:
- AI
- Other
- github.com/mysk-research
title: Loupe - 네이티브 iOS 앱이 볼 수 있는 기기 핑거프린팅 표면을 보여주는 iOS 앱
url: https://github.com/mysk-research/loupe
---

## TL;DR
- Loupe는 iOS와 iPadOS에서 기기의 핑거프린터 정보를 확인할 수 있는 오픈소스 앱이다.
- 이 앱은 사용자의 개인정보를 수집하지 않으면서도 기기가 노출하는 다양한 원시 값을 통해 핑거프린트를 형성할 수 있는 방법을 제공한다.
- 사용자와 개발자에게 앱과 웹사이트 간의 개인 인식 방법을 이해하는 데 중요한 통찰을 제공한다.

## GeekNews 요약
- **Loupe**는 공개 iOS API에서 실제 값을 읽어 원시 형태로 보여주는 iOS·iPadOS 앱이며, 서드파티 앱이 호출할 수 있는 API를 통해 기기가 노출하는 값을 직접 확인하게 함
- 이름, 이메일, 위치 없이도 여러 읽기 값이 함께 모여 앱과 웹사이트를 가로질러 사용자를 다시 인식하는 **핑거프린트**를 형성할 수 있음
- 읽기 값은 접근 비용에 따라 세 단계로 묶임
  - **Passive**: 프롬프트 없이 모든 앱에 보이는 locale, time zone, screen, battery 등
  - **Needs Permission**: contacts, photos, location, calendars처럼 iOS 프롬프트를 트리거하는 값
  - **Advanced**: `canOpenURL`을 통한 URL-scheme probing, 재설치 후에도 남는 Keychain persistence 같은 공개 API의 사이드채널 사용
- Loupe가 읽는 값은 명시적으로 내보내지 않는 한 기기를 떠나지 않으며, 집계나 해싱 없이 원시 값으로 표시되고 업로드·동기화·공유되지 않음
- 빌드에는 **Xcode 26 이상**이 필요하며, `code/Loupe.xcodeproj`를 열고 `Signing.local.xcconfig`에 `DEVELOPMENT_TEAM`과 bundle identifier를 채운 뒤 기기나 시뮬레이터에서 빌드·실행함
- Xcode의 buildable folders를 사용해 새 Swift 파일이 프로젝트 파일 수정 없이 자동으로 반영되며, macOS용으로도 빌드되지만 Mac 버전은 polished 상태가 되기 전 몇 가지 작업이 더 필요함
- Loupe는 무료 오픈소스이며, **source code**는 MIT License로 배포되지만 Loupe 이름·로고·앱 아이콘·이미지·아이콘·디자인 소스 파일은 MIT License 적용 대상이 아님

## 원문
- [원문](https://github.com/mysk-research/loupe)
- [GeekNews 토론](https://news.hada.io/topic?id=30687)

## My Note
<!-- 한 줄 코멘트 남기기 -->

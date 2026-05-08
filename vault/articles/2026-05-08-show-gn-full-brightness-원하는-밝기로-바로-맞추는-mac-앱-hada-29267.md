---
collected_at: '2026-05-08T03:03:27+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29267
id: hada-29267
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- github.com/baserize
title: 'Show GN: Full Brightness - 원하는 밝기로 바로 맞추는 Mac 앱'
url: https://github.com/baserize/full-brightness/blob/main/README.ko.md
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. Apple Developer Academy에서 교육을 받고 있는 김성현입니다.

오늘부터 일주일에 한 번, 일상 속 작은 불편을 앱으로 해결해 보고 직접 배포하는 챌린지를 시작했습니다.  
Full Brightness는 그 첫 번째 결과물입니다.

## 왜 만들었나요?

공용 데스크나 외부 모니터를 쓰다 보면, 모니터 밝기가 매번 다른 상태로 남아 있는 경우가 있습니다.

저는 보통 밝기를 최대로 두고 쓰는 편인데, Apple Developer Academy에서 자리를 옮길 때마다 데스크 모니터 밝기를 다시 맞추는 일이 반복됐습니다. 큰 문제는 아니지만, 매번 신경 쓰기에는 은근히 귀찮은 일이었습니다.

그래서 Mac에서 제어 가능한 디스플레이를 감지하고, 내가 정한 “Full” 밝기 기준으로 바로 맞춰 주는 작은 macOS 앱을 만들었습니다.

## 무엇을 할 수 있나요?

Full Brightness는 여러 대의 모니터를 쓰는 사람만을 위한 앱은 아닙니다.

MacBook 내장 디스플레이 하나만 쓰더라도, 내가 자주 쓰는 특정 밝기 값에 빠르게 도달하고 싶을 때 사용할 수 있습니다.

주요 기능은 다음과 같습니다.

- 원하는 Full 밝기 기준 설정
- 연결된 디스플레이를 한 번에 해당 밝기로 설정
- 새 디스플레이 연결 시 자동으로 Full 밝기 적용
- macOS 제어 센터 컨트롤 지원
- 사용자 지정 단축키 지원
- 메뉴 막대에서 빠르게 실행
- 해상도, HiDPI, 지원 여부 표시
- 영어/한국어 UI 지원

## 설치 방법

기본 설치 방법은 GitHub Release의 DMG입니다.

<https://github.com/baserize/full-brightness/releases/latest>

Homebrew로도 설치할 수 있습니다.

```
brew tap baserize/full-brightness https://github.com/baserize/full-brightness  
brew install --cask full-brightness
```

## 지원되는 디스플레이

현재는 macOS가 밝기 제어 경로를 제공하는 디스플레이를 대상으로 동작합니다.

예를 들면 Apple 내장 디스플레이나, macOS에서 밝기 제어가 가능한 일부 외부 디스플레이는 동작할 수 있습니다. 반대로 일부 모니터, 독, KVM, 어댑터, DisplayLink 계열 환경에서는 밝기 제어가 지원되지 않을 수 있습니다.

지원되지 않는 디스플레이도 목록에는 표시하고, 왜 제어되지 않는지 확인할 수 있도록 상태를 보여 줍니다.

## App Store에 올리지 않은 이유

이 앱은 현재 App Store 배포를 목표로 하지 않습니다.

Apple 내장 디스플레이처럼 macOS 기본 밝기 조절과 더 가깝게 동작하려면 공개 API만으로는 한계가 있었습니다. 그래서 직접 배포 버전에서는 private `DisplayServices` 경로를 사용합니다.

사용자가 직접 설치해 쓰는 방식으로는 동작하지만, App Store 심사 기준에는 맞지 않을 수 있어 GitHub Release와 Homebrew를 통한 직접 배포 방식으로 제공하고 있습니다.

## 챌린지에 대해

이번 앱은 “일상 속 작은 불편을 직접 해결해 보고 배포해 보자”는 챌린지의 첫 번째 결과물입니다.

거창한 프로젝트가 아니어도, 나나 주변 사람이 느끼는 불편을 하나씩 돌아보고, 간단한 솔루션을 만들어 실제로 배포해 보는 활동을 해 보려고 합니다.

강제성 있는 챌린지는 아니고, 일주일에 한 번 정도 작은 앱이나 도구를 만들어 보는 식입니다.  
비슷한 시도를 해 보고 싶은 분이 있다면 함께해도 좋겠습니다.

가볍게 써 보시고 피드백 주시면 감사하겠습니다.

## 원문
- [원문](https://github.com/baserize/full-brightness/blob/main/README.ko.md)
- [GeekNews 토론](https://news.hada.io/topic?id=29267)

## My Note
<!-- 한 줄 코멘트 남기기 -->

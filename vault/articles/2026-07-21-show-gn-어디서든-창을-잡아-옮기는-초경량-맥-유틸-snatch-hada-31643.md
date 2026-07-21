---
category: Other
collected_at: '2026-07-21T10:24:40+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31643
id: hada-31643
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/TypoStudio
title: 'Show GN: 어디서든 창을 잡아 옮기는 초경량 맥 유틸 Snatch'
url: https://github.com/TypoStudio/snatch
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
맥에서 창을 옮기거나 크기 조절할 때 꼭 타이틀바나 가장자리를 정확히 잡아야 하는 게 불편해서 만들었습니다.

Snatch는 수정자 키를 누른 채 창 위 아무 데서나 마우스를 움직이면 창이 따라오는 메뉴바 유틸입니다. 리눅스의 "Alt+드래그로 창 이동"을 맥으로 옮긴 것이고, Rectangle Pro의 여러 기능 중 딱 이 동작만 떼어내 최소 메모리로 돌아가게 만들었습니다.

기본 동작

- 창 이동: ⌘⌃ + 마우스 이동 (클릭 없이)
- 창 크기조절: ⌘⌥ + 마우스 이동

특징

- 클릭 없이 수정자 키 + 마우스 이동만으로 동작 (드래그 방식으로도 설정 가능)
- 이동/크기조절 각각 수정자 조합과 트리거(이동/드래그)를 설정에서 자유롭게 지정
- Chrome·Electron·Slack 같은 앱에서 창이 굼뜨게 따라오던 문제 해결 (드래그 중 AXEnhancedUserInterface를 잠깐 꺼서 접근성 API 호출을 빠르게)
- Swift + AppKit 네이티브. Electron 없음. 아이들 상태 메모리 약 15MB대
- 메뉴바에서 켜고 끄기, 로그인 시 자동 실행 지원

설치  
`brew install --cask TypoStudio/tap/snatch`

또는 릴리스에서 DMG를 직접 받으셔도 됩니다.  
<https://github.com/TypoStudio/snatch/releases>

참고: 아직 공증(notarize) 전이라 처음 실행 시 Gatekeeper가 막을 수 있습니다. 그때는 우클릭 → 열기, 또는

`xattr -dr com.apple.quarantine "/Applications/Snatch.app"`

실행 후 손쉬운 사용 권한을 허용해 주세요.

만들면서 알게 된 점이나 피드백 환영합니다.

## 원문
- [원문](https://github.com/TypoStudio/snatch)
- [GeekNews 토론](https://news.hada.io/topic?id=31643)

## My Note
<!-- 한 줄 코멘트 남기기 -->

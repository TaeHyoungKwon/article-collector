---
category: AI
collected_at: '2026-08-13T18:38:05+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32462
id: hada-32462
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 4.693
recommended_on: '2026-08-13'
source: geeknews
tags:
- AI
- Other
- raycast.com
title: 'Show GN: SSH Image Drop – 스크린샷을 원격 Claude Code 세션에 넘기는 Raycast 익스텐션'
url: https://www.raycast.com/wjsong/ssh-image-drop
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. 원격 Mac에 SSH로 붙어 Claude Code를 돌리는데, 스크린샷을 넘길 방법이 없어서 만들어 보았습니다.

요즘은 노트북을 클라이언트로만 쓰고 원격 서버에서 에이전트를 여러 개 굴리는데, 이미지 전송이 안 되는 게 너무 불편했습니다. 터미널·SSH 세션은 이미지 붙여넣기를 못 받고, 이미지는 로컬 클립보드에만 존재합니다. 그래서 매번 파일로 저장하고 scp를 치고 경로를 확인해서 프롬프트에 타이핑하고 있었습니다.

이 익스텐션은 클립보드에 있는 이미지를 단축키 한 번으로 원격 서버(맥미니나 리눅스)에 올리고, 원격 경로를 클립보드에 돌려줍니다. 그 경로를 프롬프트에 붙여넣으면 에이전트가 파일로 읽습니다. Auto-Paste에 앱을 지정해두면, 전송이 끝날 때 그 앱이 앞에 있는 경우 Cmd+V도 없이 경로가 바로 들어갑니다.

이미지 말고도, Finder에서 고른 파일과 폴더를 그대로 보내거나, 클립보드에 있는 원격 경로만으로 파일을 받아 Finder에 띄우는 것도 같은 방식입니다. 서버별로 Quicklink에 핫키를 걸면 서버 고르는 단계까지 없어집니다.

보내든 받아오든 경로가 항상 클립보드에 남으니, 에이전트에 파일을 넘기는 일이 붙여넣기 한 번으로 끝납니다. 이 부분이 직접 써보니 제일 편했습니다.

비밀번호는 macOS Keychain(윈도우는 DPAPI)으로 암호화하고, 전송 대상은 등록해둔 서버와 ~/.ssh/config에 있는 서버로만 제한했습니다. SSH 키 방식도 고를 수 있습니다.

macOS 13+ / Windows 11에서 쓸 수 있고 원격 서버는 macOS·Linux여야 합니다.

사용해 보시고 피드백 주시면 감사하겠습니다.

설치: <https://www.raycast.com/wjsong/ssh-image-drop>  
소스: [https://github.com/raycast/extensions/…](https://github.com/raycast/extensions/tree/main/extensions/ssh-image-drop)

## 원문
- [원문](https://www.raycast.com/wjsong/ssh-image-drop)
- [GeekNews 토론](https://news.hada.io/topic?id=32462)

## My Note
<!-- 한 줄 코멘트 남기기 -->

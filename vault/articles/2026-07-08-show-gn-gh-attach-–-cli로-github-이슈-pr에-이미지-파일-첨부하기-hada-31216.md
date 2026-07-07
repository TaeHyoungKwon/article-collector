---
category: AI
collected_at: '2026-07-08T00:59:46+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31216
id: hada-31216
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/sudosubin
title: 'Show GN: gh-attach – CLI로 GitHub 이슈/PR에 이미지, 파일 첨부하기'
url: https://github.com/sudosubin/gh-attach
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
GitHub 이슈나 PR에 이미지를 첨부하려면 웹 UI에 직접 접속해서 업로드해야 했습니다. 첨부 파일 업로드를 지원하는 공식 API가 없기 때문입니다.

gh-attach는 로컬 브라우저에 저장된 로그인 쿠키를 읽어 웹과 동일한 업로드 API를 호출하는 gh CLI 확장입니다.

```
$ gh extension install sudosubin/gh-attach  
$ gh attach ./image.png -R owner/repo  
# https://github.com/user-attachments/assets/...
```

- Chrome, Firefox, Safari 등 주요 브라우저 쿠키 지원 (Profile/Container 지정 가능)
- 로그인된 GitHub 계정과 일치하는 세션을 자동 선택
- --json, --jq, --template 옵션으로 Script에 연동 가능
- Go로 작성, gh 확장 또는 standalone 바이너리(Homebrew/GitHub)로 배포

스크린샷을 매번 수동으로 첨부하기 귀찮아서 만들었는데, 에이전트가 PR 생성 시 다이어그램, 스크린샷을 자동으로 업로드하게 할 때도 유용합니다.

피드백 환영합니다.

GitHub: <https://github.com/sudosubin/gh-attach>

## 원문
- [원문](https://github.com/sudosubin/gh-attach)
- [GeekNews 토론](https://news.hada.io/topic?id=31216)

## My Note
<!-- 한 줄 코멘트 남기기 -->

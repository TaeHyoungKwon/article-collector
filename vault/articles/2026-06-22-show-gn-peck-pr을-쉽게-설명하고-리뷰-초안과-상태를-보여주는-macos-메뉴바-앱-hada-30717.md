---
category: AI
collected_at: '2026-06-22T13:38:00+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30717
id: hada-30717
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- peck-landing.vercel.app
title: 'Show GN: Peck - PR을 쉽게 설명하고 리뷰 초안과 상태를 보여주는 macOS 메뉴바 앱'
url: https://peck-landing.vercel.app/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요.

PR을 볼 때 변경 내용을 빠르게 이해하기 어렵거나, 내가 봐야 할 리뷰와 내 PR의 승인 상태를 놓치는 일이 있어서 Peck이라는 macOS 메뉴바 앱을 만들고 있습니다.

##### Peck

- Github: <https://github.com/pecklabs/peck>
- 서비스 소개: 여기에 랜딩 페이지 URL 입력

##### 왜 만들었나?

- PR 리뷰를 시작할 때 제일 먼저 필요한 건 “이 PR이 뭘 바꾸는지”를 빠르게 이해하는 것이라고 생각했습니다.
- 그런데 실제로는 diff를 열고, 파일을 훑고, 관련 맥락을 따라가야 해서 리뷰를 시작하기 전부터 시간이 꽤 걸립니다.
- 어느 정도 이해한 뒤에도 Approve를 해도 되는지, Comment만 남기면 되는지, Request changes가 필요한지 판단하는 데 시간이 듭니다.
  - 특히 여러 저장소를 오가거나 리뷰가 쌓여 있을 때는 내가 봐야 할 PR을 놓치기 쉽습니다.
  - 내가 올린 PR도 GitHub에 직접 들어가지 않으면 누가 승인했는지, 체크가 실패했는지, 충돌이 났는지 계속 확인하기 번거로웠습니다.
  - 그래서 PR을 쉽게 설명해주고, 리뷰 초안을 만들어주고, 리뷰 상태를 메뉴바에서 계속 볼 수 있게 하는 앱을 만들었습니다.

##### 주요 기능

- GitHub PR 목록 확인
  - 내가 리뷰해야 하는 PR과 내가 올린 PR을 나눠서 확인
  - 승인/체크/충돌 같은 상태를 아이콘으로 표시
- PR diff 기반 쉬운 설명 생성
  - 변경 내용을 먼저 요약해서 리뷰를 시작하기 쉽게 제공
  - 위험해 보이는 부분이나 테스트가 부족한 부분을 함께 표시
- AI 리뷰 초안 생성
  - Approve / Request changes / Comment 중 어떤 리뷰가 적절한지 초안 생성
  - 최종 리뷰는 사용자가 확인한 뒤 GitHub에 게시
- GitHub 인증
  - GitHub CLI 로그인 또는 토큰 기반 인증
  - 인증 정보는 macOS Keychain에 저장
- 개인/팀 리뷰 규칙
  - `skill.md` 파일로 리뷰 기준을 지정해서 사용할 수 있음

아직 초기 버전이라 실제 PR 리뷰 흐름에서 어떤 부분이 유용한지 확인하고 싶습니다.

PR에 대한 쉬운 설명이 리뷰 시작에 도움이 되는지, AI 리뷰 초안이 너무 과하거나 부족하지 않은지, 메뉴바에서 보여주는 정보가 충분한지 피드백 주시면 감사하겠습니다.

## 원문
- [원문](https://peck-landing.vercel.app/)
- [GeekNews 토론](https://news.hada.io/topic?id=30717)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-23T19:11:28+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30759
id: hada-30759
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- github.com/jeonbyeongmin
title: 'Show GN: gh-orbit – 여러 worktree의 열린 PR·CI·diff를 한 터미널 대시보드로 모으는 gh 익스텐션'
url: https://github.com/jeonbyeongmin/gh-orbit
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
작업이 여러 worktree로 흩어질 때 — 동시에 굴리는 기능 브랜치 스택이든, 병렬로 돌리는 코딩 에이전트 몇 개든 — worktree마다 자기 커밋 그래프, 안 커밋한 diff, CI 도는 열린 PR을 따로 갖게 됩니다. 이걸 다 따라가려면 보통 git, gh, 브라우저 탭을 계속 오가야 합니다.

gh-orbit은 이걸 터미널 한 곳에 모으는 gh CLI 익스텐션입니다.

- worktree 대시보드가 브랜치별 PR·CI 상태를 한눈에 보여줍니다 (어느 worktree의 CI가 빨간지 바로 보임)
- → 로 임의 커밋의 전체 diff를 syntax-highlight된 오버레이로 열고, 훅 단위로 스테이징
- m 으로 PR을 터미널에서 바로 머지 (squash/merge/rebase 선택)
- git·CI·머지 루프는 터미널에서 끝나고, PR 리뷰(코멘트·승인)만 브라우저로 한 번 점프

lazygit·tig·gitui(워킹 트리 하나의 git)와 gh-dash(여러 저장소의 PR·이슈) 사이의 빈칸을 메웁니다. 한쪽은 PR·CI를 모르고, 다른 쪽은 로컬 worktree·diff를 모르는데, gh-orbit은 그 둘을 한 화면에 묶습니다.

설치:

```
gh extension install jeonbyeongmin/gh-orbit  
gh orbit
```

git 저장소 안에서 실행하면 됩니다. PR·CI 기능은 gh auth login + GitHub 리모트가 필요하고, 없으면 해당 열만 조용히 빠집니다(에러 없음). macOS·Linux·Windows. MIT 라이선스. Go + Bubble Tea로 만들었습니다.

## 원문
- [원문](https://github.com/jeonbyeongmin/gh-orbit)
- [GeekNews 토론](https://news.hada.io/topic?id=30759)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-05-08T09:31:01+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29279
id: hada-29279
matched_keywords:
- AI
read: false
recommend_score: 3.594
recommended_on: '2026-05-08'
source: geeknews
tags:
- AI
- github.com/modem-dev
title: Hunk - AI 에이전트 코드 리뷰를 위한 터미널 Diff 뷰어
url: https://github.com/modem-dev/hunk
---

## TL;DR
- 이 글은 Hunk라는 AI 에이전트 코드 리뷰 도구의 터미널 Diff 뷰어 기능을 다룬다.
- Hunk는 인라인 AI 주석과 멀티 파일 리뷰 스트림을 제공하여 코드 변경사항을 효율적으로 확인할 수 있다.
- 이는 개발자들이 코드 리뷰 과정에서 더욱 직관적이고 자동화된 경험을 할 수 있도록 해준다.

## GeekNews 요약
- **리뷰 중심 인터랙티브 UI**로 에이전트가 생성한 코드 변경사항을 터미널에서 확인할 수 있는 오픈소스로 [OpenTUI](https://github.com/anomalyco/opentui)와 [Pierre diffs](https://www.npmjs.com/package/@pierre/diffs) 기반
- 코드 옆에 **인라인 AI/에이전트 주석**을 직접 표시하는 Hunk만의 독특한 기능
- **멀티 파일 리뷰 스트림**과 사이드바 내비게이션으로 여러 파일의 변경사항을 한눈에 탐색
- split, stack, **반응형 자동 레이아웃** 제공, watch 모드로 파일 변경 시 자동 리로드
- Git diff 스타일 명령어를 그대로 미러링하되, 텍스트 대신 **리뷰 UI**에서 변경사항 확인
  - `hunk diff`로 현재 변경사항, `hunk show`로 커밋 리뷰, `hunk diff --watch`로 자동 리로드
- 에이전트 연동 시 별도 터미널에서 Hunk 실행 후 **Hunk review skill**을 로드하여 라이브 세션에서 리뷰 수행
  - `Load the Hunk skill and use it for this review.`
- `git config --global core.pager "hunk pager"`로 설정하면 `git diff`와 `git show`가 **자동으로 Hunk에서 열림**
- **HunkDiffView** 컴포넌트를 `hunkdiff/opentui`로 퍼블리시하여 자체 OpenTUI 앱에 diff 렌더러 임베딩 가능
- 테마(graphite, midnight, paper, ember), 모드(auto, split, stack) 등 **config.toml**로 설정 커스터마이징 지원
- MIT 라이선스

## 원문
- [원문](https://github.com/modem-dev/hunk)
- [GeekNews 토론](https://news.hada.io/topic?id=29279)

## My Note
<!-- 한 줄 코멘트 남기기 -->

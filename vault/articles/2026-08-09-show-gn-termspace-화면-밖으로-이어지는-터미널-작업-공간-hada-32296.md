---
category: Other
collected_at: '2026-08-09T20:40:08+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32296
id: hada-32296
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/ba2slk
title: 'Show GN: Termspace: 화면 밖으로 이어지는 터미널 작업 공간'
url: https://github.com/ba2slk/termspace
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
작은 노트북 화면에서 tmux를 쓰다가 문득 pane을 여러 window에 나눠 놓고 단축키로 계속 전환하는 워크플로가 불편하다고 느꼈습니다.

그래서 좁은 화면에서도 각 pane의 너비를 유지할 수 있도록, 세로로 분할된 컬럼을 옆으로 이어 붙여 가로 방향으로 스크롤하며 사용 가능한 터미널 작업 공간 Termspace를 만들었습니다.

각 session의 pane 배치와 실행 중인 프로세스의 커맨드를 저장해 다음 세션 시작 시에 재구성할 수 있습니다. 필요하다면 YAML로 직접 작성하거나 수정할 수도 있습니다 (현재 tmux처럼 프로세스 실행 상태를 유지한 채 detach/attach 하는 기능은 지원하지 않습니다). 키보드 단축키로 세션 사이를 오가거나 pane 이동/배치를 편하게 할 수 있도록 사용성에 중점을 두었습니다.

현재는 AppImage 형태로만 배포되어 리눅스에서만 사용 가능합니다.

제 작업 흐름에 필요하다고 생각해서 클로드 코드로 빠르게 프로토타이핑 했고, 며칠 써보니 꽤 편해서 공유합니다. 비슷한 불편을 겪고 계셨다면 한 번 사용해보시고, 편한 점이나 부족한 점을 알려주시면 감사하겠습니다!

## 원문
- [원문](https://github.com/ba2slk/termspace)
- [GeekNews 토론](https://news.hada.io/topic?id=32296)

## My Note
<!-- 한 줄 코멘트 남기기 -->

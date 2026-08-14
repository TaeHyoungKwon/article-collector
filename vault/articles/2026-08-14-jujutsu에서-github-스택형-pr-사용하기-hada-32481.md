---
category: Other
collected_at: '2026-08-14T09:08:52+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32481
id: hada-32481
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- alan.norbauer.com
title: Jujutsu에서 GitHub 스택형 PR 사용하기
url: https://alan.norbauer.com/articles/github-stacks-with-jujutsu/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- GitHub가 2026년 7월 30일 공개 프리뷰로 출시한 **스택형 PR**을 Git 호환 버전 관리 시스템 Jujutsu(`jj`)에서 생성·수정·병합하는 절차를 정리함
- 커밋마다 `jj` **북마크**를 만들고 `gh stack link`에 북마크 목록을 전달하면 브랜치 업로드부터 초안 PR 생성, 스택 연결까지 처리됨
- 새 커밋은 스택 맨 위에 바로 추가할 수 있지만, 중간이나 아래에 넣거나 기존 커밋을 제거하려면 **스택을 삭제하고 재생성**해야 함
- 변경된 커밋은 `jj git push -r "stack()"`로 갱신하며, 병합은 명령이 복잡한 CLI보다 CI 상태를 확인할 수 있는 **GitHub 웹 UI**가 편리함
- 실제 작업에 사용할 수 있는 수준이지만 커밋별 수동 브랜치, 변경 ID와 인터디프 부재, 통합 **`submit` 명령 부재** 등으로 개발자 경험에는 한계가 있음

---

## 원문
- [원문](https://alan.norbauer.com/articles/github-stacks-with-jujutsu/)
- [GeekNews 토론](https://news.hada.io/topic?id=32481)

## My Note
<!-- 한 줄 코멘트 남기기 -->

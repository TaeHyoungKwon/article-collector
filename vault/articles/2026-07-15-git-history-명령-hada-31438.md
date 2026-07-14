---
category: Other
collected_at: '2026-07-15T00:39:27+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31438
id: hada-31438
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- lalitm.com
title: git history 명령
url: https://lalitm.com/post/git-history/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Git 2.54와 2.55에 걸쳐 도입된 실험적 **`git history`** 명령은 기존 Git 작업 흐름을 유지하면서 과거 커밋 수정과 파생 브랜치 재구성을 자동화함
- **`fixup`** 은 스테이징한 변경을 과거 커밋에 합친 뒤, 해당 커밋에서 파생된 모든 로컬 브랜치를 새로운 커밋 해시에 맞춰 자동 리베이스함
- **`reword`** 는 과거 커밋 메시지를 바꾸고, **`split`** 은 커밋의 변경 내역을 헝크 단위로 나눠 두 커밋으로 분리한 뒤 후속 커밋과 브랜치를 다시 구성함
- 세 하위 명령은 충돌 가능성이 있는 작업을 거부하는 **원자적 처리**로 작업 트리가 중간에 깨지는 상황을 막지만, 병합 커밋이 있는 이력에서는 동작하지 않음
- `jj`의 1급 충돌 처리, 작업 로그 기반 실행 취소, 작업 복사본의 커밋 모델링까지 제공하지는 않지만, 별도 설치 없이 Git 코어 배포판에서 여러 **`jj`식 이력 편집 기능**을 사용할 수 있음

---

## 원문
- [원문](https://lalitm.com/post/git-history/)
- [GeekNews 토론](https://news.hada.io/topic?id=31438)

## My Note
<!-- 한 줄 코멘트 남기기 -->

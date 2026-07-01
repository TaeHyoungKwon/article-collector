---
category: AI
collected_at: '2026-07-01T21:02:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31008
id: hada-31008
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- caiustheory.com
title: jj jj jj jj jj
url: https://caiustheory.com/jj-jj-jj-jj-jj/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- `jj` 명령어를 반복 입력하는 작은 실수는 **하위 명령 오류**로 이어지지만, `jj` 설정 별칭으로 흡수할 수 있음
- 예시는 현재 편집 중인 changeset의 짧은 ID를 얻으려는 `jj jj show -T 'change_id.short()'`가 실패하는 상황임
- `jj`는 git처럼 설정 파일에 **alias**를 정의할 수 있어, `jj util exec`로 남은 명령을 다시 `jj`에 넘길 수 있음
- 단순 별칭은 `-T`를 실행 대상이 아니라 `jj util exec`의 옵션처럼 해석하므로, `--`로 인자 파싱을 끊어야 함
- 최종 설정 `jj = ["util", "exec", "--", "jj"]`를 쓰면 `jj jj show`뿐 아니라 여러 번 중첩된 `jj jj jj... show`도 같은 changeset ID를 출력함

---

## 원문
- [원문](https://caiustheory.com/jj-jj-jj-jj-jj/)
- [GeekNews 토론](https://news.hada.io/topic?id=31008)

## My Note
<!-- 한 줄 코멘트 남기기 -->

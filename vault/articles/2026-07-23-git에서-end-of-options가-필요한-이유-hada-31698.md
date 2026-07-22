---
category: Other
collected_at: '2026-07-23T00:03:59+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31698
id: hada-31698
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- nesbitt.io
title: Git에서 --end-of-options가 필요한 이유
url: https://nesbitt.io/2026/07/21/end-of-options.html
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Git의 `--`는 일반적인 옵션 종료자가 아니라 **리비전과 경로 명세를 구분**하므로, 신뢰할 수 없는 리비전을 안전하게 전달하려면 Git 2.24.0부터 지원된 `--end-of-options`가 필요함
- `git log --end-of-options "$rev" -- "$path"`에서 앞 표식은 **옵션과 리비전**, 뒤의 `--`는 리비전과 경로를 구분하며 서로 대체할 수 없음
- 셸 없이 `argv` 배열을 직접 실행해도 대시로 시작하는 입력이 `--upload-pack`, `core.sshCommand`, `ProxyCommand` 같은 옵션으로 해석되면 **CWE-88 인자 주입**이 발생할 수 있음
- 조사한 패키지 관리자 19개 중 17개가 기본 또는 유일한 방식으로 Git 바이너리를 실행하지만, `--end-of-options`를 사용하는 도구는 **Go의 `cmd/go` 하나뿐**이었음
- 근본 대응에는 서브명령에 따라 Git 최소 버전을 2.24.0·2.30.0·2.43.1로 높여야 하는 호환성 비용이 있으며, Git 라이브러리는 인자 주입 경계를 없애는 대신 upstream의 체크아웃 안전성 수정을 직접 추적해야 함

---

## 원문
- [원문](https://nesbitt.io/2026/07/21/end-of-options.html)
- [GeekNews 토론](https://news.hada.io/topic?id=31698)

## My Note
<!-- 한 줄 코멘트 남기기 -->

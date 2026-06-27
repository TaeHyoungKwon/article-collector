---
category: Other
collected_at: '2026-06-27T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30864
id: hada-30864
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/mvdan
title: gofumpt- gofmt보다 더 엄격한 Go 코드 포매터
url: https://github.com/mvdan/gofumpt
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 기존 `gofmt`와 **하위 호환**되면서 더 엄격한 규칙을 강제하는 포매터
- `gofmt`가 허용하는 포맷의 부분집합으로 **드롭인 교체**가 가능해, `gofumpt` 실행 후 `gofmt`를 돌려도 변경 사항 없음
- `gofmt`만으로는 안 잡히는 **스타일 편차를 자동으로 통일**
  - **불필요한 빈 줄, 공백, 괄호** 등을 자동 제거
  - import에서 표준 라이브러리를 별도 그룹으로 분리
  - `var s = "x"` → `s := "x"`, `0755` → `0o755`, `//Foo` → `// Foo`
  - 복합 리터럴 줄바꿈 일관화 등 **다수의 추가 포매팅 규칙** 적용
- `vendor`, `testdata` 디렉터리는 명시적 인자가 아니면 건너뜀, 생성된 Go 파일에도 추가 규칙 미적용
- `go.mod`의 `ignore` 디렉티브 준수
- "gofmt 위에 만들지 않고 **대체**하려는 이유?"
  - 설계 자체가 `gofmt` 위에 구축하는 것이며, `gofmt` 포매팅과 충돌하는 규칙은 추가하지 않음 — 경쟁이 아닌 확장
  - 에디터/스크립트에서 드롭인 교체로 쓰기 위해 `gofmt`의 수정 복사본 형태를 취함

## 원문
- [원문](https://github.com/mvdan/gofumpt)
- [GeekNews 토론](https://news.hada.io/topic?id=30864)

## My Note
<!-- 한 줄 코멘트 남기기 -->

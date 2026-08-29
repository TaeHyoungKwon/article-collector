---
category: Dev Tools
collected_at: '2026-07-20T10:01:57+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31603
id: hada-31603
matched_keywords:
- Claude Code
read: false
recommend_score: -997.099
recommended_on: '2026-08-29'
source: geeknews
tags:
- Dev Tools
- Other
- simonwillison.net
title: Claude Code, Rust로 재작성된 Bun 사용
url: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Claude Code **v2.1.181**부터 Rust로 포팅된 Bun을 내장해 Linux 시작 속도가 10% 빨라졌지만, 대부분의 사용자는 변화를 거의 알아차리지 못함
- 실행 파일의 문자열을 조사하면 정식 태그가 아직 없는 **Bun v1.4.0**과 Rust 소스 파일 경로를 확인할 수 있음
- `~/.local/bin/claude`에서 `src/runtime/bake/dev_server/mod.rs` 등을 포함한 **563개 `.rs` 파일명**이 발견됨
- `BUN_OPTIONS`로 TypeScript 파일을 미리 불러와 `Bun.version`을 출력하는 방식으로도 내장 버전이 **1.4.0**임을 검증할 수 있음
- Rust 버전은 Bun canary로 배포됐으며, Claude Code를 통해 이미 **수백만 대의 기기**에서 프로덕션 실행 중임

---

## 원문
- [원문](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)
- [GeekNews 토론](https://news.hada.io/topic?id=31603)

## My Note
<!-- 한 줄 코멘트 남기기 -->

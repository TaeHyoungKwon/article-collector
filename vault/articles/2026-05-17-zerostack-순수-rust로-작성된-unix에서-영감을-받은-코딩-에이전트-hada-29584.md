---
category: AI
collected_at: '2026-05-17T16:37:27+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29584
id: hada-29584
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-05-17'
source: geeknews
tags:
- AI
- Other
- crates.io
title: Zerostack - 순수 Rust로 작성된 Unix에서 영감을 받은 코딩 에이전트
url: https://crates.io/crates/zerostack/1.0.0
---

## TL;DR
- 이 글은 Rust로 작성된 코딩 에이전트인 Zerostack에 대해 다룬다.
- Zerostack은 여러 LLM 공급자와의 호환성을 가지며, 파일 처리 및 Bash 실행 기능을 포함한다.
- 이 도구는 Unix에서 영감을 받아 개발되어 개발자에게 효율적인 작업 환경을 제공한다.

## GeekNews 요약
- **zerostack**은 Rust로 작성된 최소형 코딩 에이전트로, 여러 LLM 제공자와 사용자 지정 제공자를 함께 지원함
- 파일 읽기·쓰기·편집, grep, 파일 찾기, 디렉터리 목록, 권한 게이트가 붙은 **Bash 실행**, MCP, Exa 웹 도구를 제공함
- 약 **7천 LoC**, 8.9MB 바이너리이며 RAM은 빈 세션 약 8MB·작업 중 약 12MB, CPU는 유휴 0.0%로 측정됨
- 기본 제공자는 **OpenRouter**이고 `cargo install zerostack`으로 설치하며, `--sandbox`에서 Bash 격리를 쓰려면 bubblewrap이 필요함
- `code`·`plan`·`review` 등 **내장 프롬프트**, 4가지 권한 모드, 세션 재개, 반복 루프, Git worktrees 통합을 포함함

---

## 원문
- [원문](https://crates.io/crates/zerostack/1.0.0)
- [GeekNews 토론](https://news.hada.io/topic?id=29584)

## My Note
<!-- 한 줄 코멘트 남기기 -->

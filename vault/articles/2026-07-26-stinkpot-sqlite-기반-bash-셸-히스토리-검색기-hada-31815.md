---
category: AI
collected_at: '2026-07-26T09:05:35+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31815
id: hada-31815
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-08-24'
source: geeknews
tags:
- AI
- Other
- tangled.org
title: stinkpot - SQLite 기반 Bash 셸 히스토리 검색기
url: https://tangled.org/oppi.li/stinkpot
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **stinkpot**은 Bash 명령 기록을 SQLite에 저장해 세션과 무관하게 관리하고, 검색 TUI로 빠르게 찾을 수 있게 함
- Atuin에서 동기화 서버, AI, dotfiles·스크립트 관리자, KV 저장소를 덜어내고 필요한 기능만 **약 400줄의 Go**로 구현함
- 기존 Bash 히스토리는 `stinkpot import`로 가져오며, `Ctrl+R`을 누르면 **역방향 검색 TUI**가 열림
- NixOS에서는 **home-manager 모듈**을 제공하고, 그 외 환경에서는 `.bashrc`에서 `eval "$(stinkpot init)"`으로 초기화함
- 데이터베이스는 `~/.local/share/stinkpot`에 저장되며, 업그레이드 후 손상되면 삭제한 뒤 히스토리를 다시 가져올 수 있음

---

## 원문
- [원문](https://tangled.org/oppi.li/stinkpot)
- [GeekNews 토론](https://news.hada.io/topic?id=31815)

## My Note
<!-- 한 줄 코멘트 남기기 -->

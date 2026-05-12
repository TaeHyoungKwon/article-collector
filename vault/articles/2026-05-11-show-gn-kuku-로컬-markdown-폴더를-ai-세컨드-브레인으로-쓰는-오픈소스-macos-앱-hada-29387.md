---
category: AI
collected_at: '2026-05-11T21:58:24+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29387
id: hada-29387
matched_keywords:
- AI
- Codex
read: false
recommend_score: -995.307
recommended_on: '2026-05-11'
source: geeknews
tags:
- AI
- Other
- github.com/kuku-mom
title: 'Show GN: Kuku - 로컬 Markdown 폴더를 AI 세컨드 브레인으로 쓰는 오픈소스 macOS 앱'
url: https://github.com/kuku-mom/kuku
---

## TL;DR
- Kuku는 macOS용 로컬 Markdown 폴더를 지식 작업 공간으로 활용하는 오픈소스 앱이다.
- 이 앱은 사용자의 .md 파일을 직접 수정하지 않고, AI가 제안하는 변경 사항을 사용자가 검토 후 적용하는 방식으로 작동한다.
- Kuku는 기존 노트 앱의 한계를 극복하며, AI 기능을 필요에 따라 선택적으로 사용할 수 있는 점에서 의미가 있다.

## GeekNews 요약
안녕하세요, Kuku를 만들고 있는 빌더입니다. Kuku는 macOS용 로컬 우선 Markdown 지식 작업공간입니다.

핵심 아이디어는 단순합니다. 노트의 원본은 앱 안의 DB가 아니라 사용자가 가진 폴더의 평범한 .md 파일이고, 그 위에 wikilink, backlink, graph view, full-text search, AI editing을 얹습니다.

AI 기능은 채팅창 하나 더 붙이는 느낌보다는, vault를 읽고 필요한 변경을 제안한 뒤 사용자가 diff로 보고 적용하는 흐름에 가깝습니다. 코드에서 Cursor/Codex가 diff를 보여주듯, 지식베이스도 AI가 마음대로 덮어쓰지 않고 사람이 검토하고 받아들이게 만들고 싶었습니다.

현재 바로 써볼 수 있는 것:

- macOS public beta
- MIT 오픈소스
- 로컬 Markdown vault
- wikilink/backlink/graph/search
- AI Ask/Agent/Inline editing
- BYO Gemini key
- Tauri + SolidJS + Rust + Go 기반

왜 만들었냐면, AI 채팅에서 나온 좋은 요약/결정/아이디어가 대화창 안에 버려지는 게 너무 아까웠기 때문입니다. 반대로 기존 노트 앱은 지식은 잘 보관하지만 AI가 붙으면 cloud-first이거나 plugin 느낌이 강하다고 느꼈습니다.

궁금한 점은 이겁니다. GeekNews 분들이라면 이런 앱에서 “써볼 만하다”의 기준이 뭘까요?

- plain Markdown 유지
- local-first/private
- AI diff review
- self-hostable sync 방향
- Obsidian 호환/마이그레이션

중에 뭐가 제일 중요할까요? 피드백은 brutal하게 환영합니다. GitHub star도 정말 큰 힘이 됩니다.

Website: <https://www.kuku.mom/>

## 원문
- [원문](https://github.com/kuku-mom/kuku)
- [GeekNews 토론](https://news.hada.io/topic?id=29387)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-13T21:20:18+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31397
id: hada-31397
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- saaskr.com
title: 'Show GN: 만든 SaaS를 AI에게 말만 하면 등록되는 MCP 서버'
url: https://saaskr.com/mcp
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
사이드 프로젝트를 만들고 나면 어디에 올릴지가 늘 애매합니다. 디렉토리마다 폼이 다르고, 항목 채우다가 그냥 안 하게 되더군요.

한국에서 만들어진 SaaS를 모으는 디렉토리(saaskr.com)를 운영하는데, 등록을 MCP로 열었습니다. Claude나 Cursor에 붙이고 이렇게 말하면 끝입니다.

"내가 만든 서비스 saaskr에 등록해줘. 주소는 <https://example.com> 이야"

연결은 한 줄입니다.

claude mcp add --transport http saaskr <https://saaskr.com/api/mcp>

등록 외에 검색·비교도 됩니다. "한국어 받아쓰기 잘 되는 국산 회의록 AI 찾아줘"처럼 물어보면 지금 운영 중인 것만 답합니다. 등록된 서비스의 링크가 살아있는지 매주 자동으로 점검해서, 죽은 도메인이나 파킹된 링크는 자동으로 내리기 때문입니다.

구현은 MCP streamable HTTP를 JSON-RPC로 직접 짰습니다(SDK 없이 Next.js route handler 하나).

소개: <https://saaskr.com/mcp>

## 원문
- [원문](https://saaskr.com/mcp)
- [GeekNews 토론](https://news.hada.io/topic?id=31397)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-12T01:00:55+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30400
id: hada-30400
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.693
recommended_on: '2026-06-11'
source: geeknews
tags:
- AI
- Other
- github.com/bigmacfive
title: 'Show GN: turbo-graph – turbovec에 그래프 메모리/필터 캐시를 얹은 constrained RAG 인덱스'
url: https://github.com/bigmacfive/turbo-graph
---

## TL;DR
- 이 글은 turbovec 기반의 constrained RAG용 그래프 메모리 레이어인 turbo-graph에 대해 다룬다.
- turbo-graph는 기존의 turbovec을 활용하여 그래프와 메타데이터 처리의 효율성을 높이는 실험을 진행 중이다.
- 독자는 turbo-graph의 발전과 API 필요성에 대한 피드백 요청을 통해 향후 데이터 검색 기술 발전에 기여할 수 있다.

## GeekNews 요약
안녕하세요. turbovec/TurboQuant 기반으로 constrained RAG용 graph memory layer를 붙인 turbo-graph를 만들었습니다.

turbovec은 flat top-k나 cheap allowlist가 있는 경우에 이미 좋습니다. 그런데 실제 RAG에서는 쿼리가 자주 이런 모양이 됩니다.

tenant ACL ∩ tag ∩ source ∩ time window ∩ graph neighbors ∩ BM25 candidates

이 조합을 매번 Python/SQL/app layer에서 만들고, 다시 vector search에 넘기고, 결과를 graph/BM25와 rerank하고, 왜 이런 결과가 나왔는지 explain하는 코드가 반복되더라고요.

turbo-graph는 turbovec-compatible core는 유지하고, 그 주변의 graph/metadata view compilation, cache reuse, graph rerank, explain telemetry를 인덱스 레이어로 옮겨보는 실험입니다.

아직 Alpha라서 production에 바로 쓰라는 목적보다는, 실제 RAG route에서 어떤 API가 필요한지 피드백을 받고 싶습니다.

GitHub:  
<https://github.com/bigmacfive/turbo-graph>

## 원문
- [원문](https://github.com/bigmacfive/turbo-graph)
- [GeekNews 토론](https://news.hada.io/topic?id=30400)

## My Note
<!-- 한 줄 코멘트 남기기 -->

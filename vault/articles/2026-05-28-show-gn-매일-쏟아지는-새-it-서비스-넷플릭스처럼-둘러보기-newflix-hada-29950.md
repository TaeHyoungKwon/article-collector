---
category: AI
collected_at: '2026-05-28T15:47:38+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=29950
id: hada-29950
matched_keywords:
- AI
read: false
recommend_score: 3.609
recommended_on: '2026-05-30'
source: geeknews
tags:
- AI
- Other
- newflix.io
title: 'Show GN: 매일 쏟아지는 새 IT 서비스, 넷플릭스처럼 둘러보기 - newflix'
url: https://newflix.io/
---

## TL;DR
- 이 글은 신규 IT 서비스 디스커버리 플랫폼 newflix에 대해 다룬다.
- newflix는 OTT의 둘러보기 UX를 활용해 사용자가 AI·개발 도구·서비스를 쉽게 발견하고 큐레이션할 수 있도록 돕는다.
- 이는 사용자들이 다양한 IT 서비스를 효율적으로 탐색하고 공유할 수 있는 새로운 경험을 제공한다.

## GeekNews 요약
넷플릭스처럼 둘러보고, Product Hunt처럼 발견하는 신규 IT 서비스 디스커버리 플랫폼 newflix를 만들었습니다.

매일 새로운 AI·개발 도구·서비스가 쏟아지는데, 정작 "한눈에 둘러보고 골라 담는" 경험은 마땅치 않다고 느꼈습니다. 그래서 OTT의 둘러보기 UX와 큐레이션을 IT 서비스 발견에 가져왔습니다.

핵심은 세 가지입니다.

- 발견(Discovery): 시네마틱 히어로 + 카테고리별 캐러셀로 OTT처럼 탐색
- 수집(Collection): 마음에 드는 서비스를 컬렉션으로 묶고, 공유 링크로 큐레이션 공개
- 회귀(Loop): 업보트·리뷰·찜으로 다시 돌아오는 흐름

주요 기능

- 하이브리드 검색: 키워드 + 임베딩 벡터(pgvector cosine) RRF 결합. 의미 기반 연관 서비스 추천
- 컬렉션(UGC 큐레이션): 공개 컬렉션 둘러보기 + 큐레이터 한마디 + 공유 코드
- 카테고리·업보트·리뷰
- 라우트별 OG/SEO: 각 서비스 페이지를 정적 prerender(SSG)해서 공유 시 서비스별 미리보기 노출

기술 스택

- 런타임: Bun 1.3
- 백엔드: Elysia + Drizzle + Postgres 16(pgvector HNSW)
- 검색 임베딩: Voyage voyage-4-lite (1024d)
- 프론트: React 19
- 스토리지: Cloudflare R2
- 인프라: Railway 배포

아직 초기 단계이고 데이터/큐레이션을 채워가는 중입니다. 둘러보시고 피드백 주시면 반영하겠습니다.

## 원문
- [원문](https://newflix.io/)
- [GeekNews 토론](https://news.hada.io/topic?id=29950)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-10T14:36:25+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31296
id: hada-31296
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-07-11'
source: geeknews
tags:
- AI
- Other
- github.com/malisper
title: Postgres를 Rust로 재작성, 이제 Postgres 회귀 테스트 100% 통과
url: https://github.com/malisper/pgrust
---

## TL;DR
- 이 글은 Postgres를 Rust로 재작성한 pgrust 프로젝트와 그 테스트 결과를 다룬다.
- pgrust는 46,000개 이상의 회귀 쿼리에서 Postgres의 예상 출력과 일치하여, 기존 Postgres와의 호환성을 유지하고 있다.
- 이 프로젝트는 Rust의 장점을 살려 Postgres의 성능 향상을 목표로 하지만, 아직 프로덕션 준비가 완료되지 않았으므로 주의가 필요하다.

## GeekNews 요약
- **pgrust**는 Postgres 18.3 호환을 목표로 하는 Rust 재작성 프로젝트이며, 46,000개 이상의 회귀 쿼리에서 Postgres의 예상 출력과 일치함
- 기존 **Postgres 18.3 데이터 디렉터리**에서 부팅할 수 있는 디스크 호환성을 갖추고, 실제 Postgres 테스트를 동작 기준으로 삼음
- 현재는 **프로덕션 준비 상태가 아니며** 성능 최적화도 아직 되어 있지 않고, 기존 Postgres 확장과 PL/Python·PL/Perl·PL/Tcl 같은 절차 언어 확장은 일반적으로 호환되지 않음
- WebAssembly 데모와 Docker 이미지 `malisper/pgrust:v0.1`로 실행해볼 수 있으며, `latest`는 현재 같은 릴리스를 가리키지만 고정 실행 이미지는 `v0.1`임
- 로드맵은 **멀티스레드 Postgres 내부 구조**, 내장 연결 풀링, JSON 중심 워크로드 개선, no-vacuum 저장소 실험, AI 생성 SQL을 위한 런타임 가드레일을 포함함

---

## 원문
- [원문](https://github.com/malisper/pgrust)
- [GeekNews 토론](https://news.hada.io/topic?id=31296)

## My Note
<!-- 한 줄 코멘트 남기기 -->

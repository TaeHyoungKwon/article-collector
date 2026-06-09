---
category: AI
collected_at: '2026-06-09T09:33:16+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30302
id: hada-30302
matched_keywords:
- LLM
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- mqlang.org
title: mq - jq 스타일 Markdown 쿼리 언어
url: https://mqlang.org/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- jq와 유사한 문법으로 **Markdown 문서를 질의·필터링·변환**하는 CLI 도구로, JSON에서 jq가 하던 역할을 Markdown으로 옮겨옴
- 마크다운을 구조화된 데이터로 만들어 슬라이스, 필터, 매핑, 변환하는 작업을 손쉽게 **배치 처리** 가능
- LLM이 Markdown을 기본 입력 형식으로 사용하므로 **LLM 워크플로우와 입력 생성**에 특히 유용함
  - 프롬프트/출력에 쓰이는 Markdown 조작, 문서 관리, 콘텐츠 분석, 배치 처리 등에 활용
- 다양한 입출력 포맷 지원: markdown, mdx, html, csv, json, toml, xml, yaml 등 입력, table·grep·json 등 출력
  - 파일 확장자나 `-I` 플래그로 **자동 파싱** 수행
- 헤딩,코드 블록,링크,테이블 셀을 셀렉터로 추출 (`.h(1..3)`, `.code("rust")`, `.link.url` 등)
- 제목 기반 **섹션 단위 추출** 지원 (`section::section("Installation")`)
- `mq conv`로 Excel·Word·PDF를 Markdown으로 변환 후 **Unix 파이프**로 연결 처리 가능
- 다수의 내장 함수와 셀렉터로 콘텐츠 필터 및 변환 가능하며, 커스텀 함수로 손쉽게 확장 가능
- **REPL·LSP·VSCode 확장·디버거(`mq-dbg`)** 등 개발 편의 기능 포함
- [Playground](https://mqlang.org/playground) 에서 설치 없이 브라우저에서 실행 가능
- **[mq-web](https://www.npmjs.com/package/mq-web)** 으로 WebAssembly 빌드 제공
- Elixir, Python, Ruby, Java, Go 언어용 바인딩 제공
- MIT License, Rust로 구현

## 원문
- [원문](https://mqlang.org/)
- [GeekNews 토론](https://news.hada.io/topic?id=30302)

## My Note
<!-- 한 줄 코멘트 남기기 -->

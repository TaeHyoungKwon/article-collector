---
category: AI
collected_at: '2026-08-11T09:30:03+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32372
id: hada-32372
matched_keywords:
- AI
read: false
recommend_score: -996.901
recommended_on: '2026-08-11'
source: geeknews
tags:
- AI
- Other
- github.com/CoreBunch
title: Instatic - Webflow, Framer, WordPress를 대체하는 오픈소스 셀프호스팅 비주얼 CMS
url: https://github.com/CoreBunch/Instatic
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 비주얼 에디터/콘텐츠 엔진/퍼블리셔를 **단일 Bun 서버** 하나에 담아 셀프호스팅으로 운영. SQLite/Postgres를 백엔드로 사용
- 헤드리스 CMS/프레임워크/호스트/폼 서비스/애널리틱스/이미지 CDN을 각각 조합하던 방식 대신 하나의 서버가 **캔버스 에디터/콘텐츠/미디어/인증/폼/플러그인** 등을 모두 포함
- 최종 출력물은 **시맨틱 HTML과 압축 CSS**로, 프레임워크 런타임/빌더 속성/div 남발 없음
- 에디터는 미리보기가 별도로 있는 게 아닌 실제 **캔버스**
  - 여러 브레이크포인트 프레임을 나란히 두고 함께 편집하며 데스크톱 변경 시 모바일 프레임이 같은 화면에서 반응
  - 실제 페이지 작업을 원하면 라이브 모드로 전환해 전체 크기 페이지를 그 자리에서 편집
- 디자인 토큰 엔진 **Core Framework**가 코어 시스템으로 내장
  - 브랜드 색 하나로 틴트/셰이드 자동 생성, 유동적 타입 스케일, 스페이싱 스케일, 유틸리티 클래스 생성 지원
- **AI 에이전트**가 설명만으로 캔버스에 실제 편집 가능한 노드를 구축
  - 구조는 시맨틱 HTML/스타일은 CSS로 작성 (Claude, OpenAI, OpenRouter, 로컬 Ollama 중 자신의 키/모델 사용)
- 플러그인은 **QuickJS-WASM 샌드박스**에서 실행됨
- 게시된 페이지는 대부분 디스크에 놓인 파일이라 프레임워크 부팅/하이드레이션/DB 왕복이 없어서 매우 빠름
- MIT 라이선스

## 원문
- [원문](https://github.com/CoreBunch/Instatic)
- [GeekNews 토론](https://news.hada.io/topic?id=32372)

## My Note
<!-- 한 줄 코멘트 남기기 -->

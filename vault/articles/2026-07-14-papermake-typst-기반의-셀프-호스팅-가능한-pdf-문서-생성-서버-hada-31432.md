---
category: AI
collected_at: '2026-07-14T16:13:18+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31432
id: hada-31432
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.693
recommended_on: '2026-07-14'
source: geeknews
tags:
- AI
- Other
- github.com/rkstgr
title: Papermake - Typst 기반의 셀프 호스팅 가능한 PDF 문서 생성 서버
url: https://github.com/rkstgr/papermake
---

## TL;DR
- Papermake는 Typst 템플릿 기반의 셀프 호스팅 PDF 문서 생성 서버이다.
- 이 서버는 REST API를 통해 PDF를 생성하고, 템플릿 버전 관리 및 감사 추적 기능을 제공한다.
- 개발자와 기업은 중앙 집중식 템플릿 관리와 효율적인 리소스 사용으로 문서 생성 프로세스를 개선할 수 있다.

## GeekNews 요약
Papermake는 Typst 템플릿을 이용하여 PDF를 생성하는 HTTP 기반 문서 생성 서버임.

### 목적

- Typst 템플릿의 중앙 집중식 관리
- REST API를 통한 PDF 생성
- 템플릿 버전 관리
- 생성 이력(Audit Trail) 관리
- Docker Registry와 유사한 템플릿 저장소 제공

### 주요기능

- 코드로 관리되는 템플릿(Templates as Code)
  - 템플릿은 변경 불가능한(Immutable) 버전과 변경 가능한(Mutable) 태그를 지원함.
  - 예를 들어 `invoice:v1.0.0`은 한 번 생성되면 변경되지 않으며, `invoice:latest`는 최신 버전을 가리키도록 갱신될 수 있음.
- 서버 측 렌더링(Server-side Rendering)
  - 클라이언트 환경에 Typst를 설치할 필요 없음.
  - HTTP API 호출만으로 서버에서 PDF를 렌더링하여 반환함.
- 콘텐츠 주소 지정 저장소(Content-addressable Storage)
  - 템플릿을 SHA-256 해시를 기준으로 저장함.
  - 동일한 템플릿은 중복 저장되지 않으며, Git과 유사한 방식으로 저장 공간을 효율적으로 관리함.
- 완전한 감사 추적(Audit Trail)
  - 모든 렌더링 작업에 대해 입력 데이터와 출력 결과의 해시를 기록함.
  - 생성된 모든 PDF는 어떤 템플릿과 어떤 데이터로 생성되었는지 정확하게 추적 가능함.
- 자체 호스팅(Self-hostable)
  - Rust로 작성된 단일 실행 파일과 S3 호환 객체 스토리지, ClickHouse만으로 자체 구축 및 운영이 가능함.

## 원문
- [원문](https://github.com/rkstgr/papermake)
- [GeekNews 토론](https://news.hada.io/topic?id=31432)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-03T09:16:01+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30128
id: hada-30128
matched_keywords:
- AI
- Codex
read: false
recommend_score: 5.307
source: geeknews
tags:
- AI
- Other
- developers.openai.com
title: OpenAI, Codex에서 웹사이트를 만들어 배포하는 Sites 플러그인 공개
url: https://developers.openai.com/codex/sites
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 프롬프트/프로젝트에서 **OpenAI가 호스팅하는 웹 사이트**를 제작 가능
- 별도 배포 워크플로 구성 없이 웹사이트, 웹 앱, 게임을 **프롬프트만으로 생성·저장·배포·점검**할 수 있음
- `@Sites` 로 호출해서 신규 **사이트·대시보드·내부 도구** 제작 또는 기존 프로젝트를 배포 요청 가능
- 게시는 **버전 저장** 과 **버전 배포** 두 단계로 분리, 검토 가능한 후보를 만든 뒤 승인된 버전만 배포
- 사이트 연결과 스토리지 바인딩 정보는 **`.openai/hosting.json`** 에 저장됨
- Sites는 **Cloudflare Worker와 호환**되는 ES 모듈로 빌드한 프로젝트를 호스팅함
  - 영구 저장이 필요한 스트럭처드 데이터는 관계형 DB **D1**에 저장
  - 이미지/문서/오디오/비디오 파일 업로드는 객체 스토리지 **R2** 사용
  - **워크스페이스 인증**된 사용자나 **외부 ID 프로바이더 기반 인증**도 지원
  - 접근 모드는 **소유자/관리자(`admins_only`)**, **워크스페이스 전체(`workspace_all`)**, **커스텀(`custom`)** 세 가지
- 호스팅 환경 변수와 시크릿은 Sites 패널에서 관리함, `.openai/hosting.json` 이나 소스 커밋에 저장하지 말고 `.env` `.env.example` 등 사용할 것
- 현재 **프리뷰** 단계로 ChatGPT Business(기본 활성화) 및 Enterprise(관리자 RBAC을 통해 기능 활성화 필요) 워크스페이스에서 사용 가능

## 원문
- [원문](https://developers.openai.com/codex/sites)
- [GeekNews 토론](https://news.hada.io/topic?id=30128)

## My Note
<!-- 한 줄 코멘트 남기기 -->

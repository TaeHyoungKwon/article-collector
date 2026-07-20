---
category: AI
collected_at: '2026-07-20T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31594
id: hada-31594
matched_keywords:
- AI
read: false
recommend_score: 3.609
source: geeknews
tags:
- AI
- Other
- github.com/langchain-ai
title: OpenWiki - 코드베이스를 위한 에이전트용 문서를 작성하고 관리하는 CLI
url: https://github.com/langchain-ai/openwiki
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **에이전트 전용**으로 제작된 문서화 도구로, 코드베이스나 목적별 메모리용 위키를 작성/유지
- 내장 커넥터 또는 Git 저장소를 통해 로컬 지식 소스를 가져와 하나의 **로컬 위키로 통합**
- **두 가지 모드** 제공
  - **Personal 모드**: 로컬 Repo,Gmail,Notion,Web Search,Hacker News,X 등을 소스로 `~/.openwiki/wiki`에 개인 브레인 위키 구축
  - **Code 모드**: 현재 코드베이스용 저장소 문서를 `openwiki/`에 생성
- **CI 연동으로 문서 자동 갱신**, GitHub Actions/GitLab CI용 예시 워크플로를 제공해 문서 갱신 PR/merge request를 자동 생성
- **Google Open Knowledge Format(OKF) v0.1** 번들을 두 모드 모두에서 출력, 개념 문서는 `type` 필드를 가진 YAML front matter를 갖고 Markdown 링크로 관계 표현
- 각 code 실행 시 저장소 루트에 `AGENTS.md`와 `CLAUDE.md`를 유지, 코딩 에이전트가 컨텍스트 검색 시 위키를 참조하도록 유도
  - 기존 파일이 있으면 `<!-- OPENWIKI:START -->…<!-- OPENWIKI:END -->` 블록만 갱신하고 나머지는 보존
- **로컬 커넥터**로 Git 저장소,Notion,Gmail,X,Web Search,Hacker News 수집 지원, 동일 커넥터를 여러 인스턴스로 구성 가능
- **다양한 추론 프로바이더 지원**: OpenAI, OpenRouter, Gemini(AI Studio), Gemini Enterprise(Vertex AI), Nebius Token Factory, Fireworks, Baseten, NVIDIA NIM, OpenAI 호환, AWS Bedrock, Anthropic
  - 온보딩 기본값은 OpenAI의 `gpt-5.6-terra`, ChatGPT 로그인/IAM 자격증명/Google ADC 등 프로바이더별 인증 방식 제공
- **익명 텔레메트리**를 기본 수집(명령/결과/프로바이더/커넥터 이름 수준)하되, 파일 내용/자격증명/프롬프트/모델 출력/IP는 수집하지 않으며 `OPENWIKI_TELEMETRY_DISABLED=1` 또는 `DO_NOT_TRACK=1`로 비활성화 가능
- `npm install -g openwiki`로 설치
- MIT 라이선스

## 원문
- [원문](https://github.com/langchain-ai/openwiki)
- [GeekNews 토론](https://news.hada.io/topic?id=31594)

## My Note
<!-- 한 줄 코멘트 남기기 -->

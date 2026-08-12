---
category: AI
collected_at: '2026-08-12T09:30:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32420
id: hada-32420
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 7.099
source: geeknews
tags:
- AI
- Other
- xirp.spotify.com
title: Xirp - Spotify가 만든 조직 컨텍스트 기반 AI 코딩 환경
url: https://xirp.spotify.com/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- AI 코딩 도구로 코드 생성 속도는 빨라졌지만, 에이전트가 시스템의 배경을 몰라 **기술적으로는 맞지만 운영상 잘못된 결정**을 내릴 수 있음
- 이는 문서 부족이 아닌 **검색(retrieval) 문제**여서, Slack 대화/담당자의 기억/오래된 README/Confluence 등에 흩어진 조직 지식을 적절한 시점에 가져오는 것이 중요함
- Xirp는 Spotify에서 실제 사용한 기술을 기반으로 만든 macOS용 **에이전틱 개발 환경**으로, Claude Code/Codex/Gemini를 여러 프로젝트와 세션에서 실행하고 관리함
  - 각 에이전트의 기존 CLI/인증/모델/권한 설정을 그대로 사용하며 Xirp가 에이전트 자체를 대체하지는 않음
- 여러 에이전트를 **지속되는 터미널 세션**으로 병렬 실행하며, 앱을 닫았다 다시 열어도 세션을 이어갈 수 있음
  - 작업별 Git worktree를 만들어 같은 저장소에서 여러 에이전트가 서로의 작업 디렉터리를 건드리지 않고 병렬 작업 가능
  - Git 변경사항/파일/Rules(`CLAUDE.md`, `AGENTS.md` 등)/Skills/세션 상태를 하나의 앱에서 관리하고 여러 세션을 Grid View로 동시에 볼 수 있음
- Spotify의 개발자 포털 **Portal** 연동은 선택 사항으로, 연결하면 Software Catalog와 Workspace에 저장된 서비스/소유권/의존성/문서/기술적 결정/이전 세션 정보를 에이전트의 컨텍스트로 활용함
  - Portal의 Catalog 엔티티나 Workspace에서 작업을 시작하면 저장소를 찾아 로컬 프로젝트를 준비하고, 필요한 조직 정보를 **MCP**로 가져옴
  - 모든 문서를 초기 프롬프트에 넣는 대신 필요할 때 MCP 도구로 추가 정보를 조회하는 방식
- **Workspace**는 Catalog 엔티티/wiki/기술 기록/링크/문서/소유권/이전 세션 등을 공유 컨텍스트로 관리함
  - 작업이 끝난 세션의 transcript를 수동 업로드하면 팀원과 이후 에이전트가 다시 활용할 수 있음
  - Workspace 컨텍스트는 MCP로 제공되므로 Xirp뿐 아니라 다른 MCP 호환 클라이언트에서도 사용 가능
- 코딩 세션에서 만들어진 지식을 문서화하고 이후 세션의 컨텍스트로 재사용해 **살아있는 문서화**를 구축하는 것이 핵심 방향
- 현재 베타는 **macOS 전용 로컬 앱**이며 서버 배포/SSH 기반 원격 세션은 아직 지원하지 않음
  - Apple Silicon/Intel Mac 버전을 다운로드할 수 있으며, Xirp 자체는 Portal 없이도 사용 가능
  - 무료 Portal 체험판을 함께 제공해 조직 컨텍스트 연동을 시험할 수 있음

## 원문
- [원문](https://xirp.spotify.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=32420)

## My Note
<!-- 한 줄 코멘트 남기기 -->

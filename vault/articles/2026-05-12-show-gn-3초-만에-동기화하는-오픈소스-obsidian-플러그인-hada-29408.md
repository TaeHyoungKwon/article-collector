---
category: Other
collected_at: '2026-05-12T09:27:15+09:00'
geeknews_comments: 6
geeknews_score: 11
geeknews_url: https://news.hada.io/topic?id=29408
id: hada-29408
matched_keywords: []
read: false
recommend_score: 3.069
recommended_on: '2026-06-07'
source: geeknews
tags:
- Other
- synch.run
title: 'Show GN: 3초 만에 동기화하는 오픈소스 Obsidian 플러그인'
url: https://synch.run
---

## TL;DR
- 이 글은 Obsidian용 오픈소스 동기화 플러그인인 Synch에 대해 다룹니다.
- Synch는 클라우드 서비스에 의존하지 않고 몇 초 만에 파일 변경을 동기화하는 혁신적인 기능을 제공합니다.
- 이 플러그인은 Obsidian 사용자에게 더 나은 데이터 보안과 관리 옵션을 제공하여 개인화된 경험을 개선할 수 있는 가능성을 제시합니다.

## GeekNews 요약
Obsidian용 오픈소스 동기화 플러그인 Synch를 만들고 있습니다.

Obsidian Sync 같은 경험을 오픈소스로 만들 수 있을까 해서 시작했습니다.  
목표는 빠른 동기화, E2EE, 버전 히스토리, 직접 배포 가능한 Obsidian Sync 대안입니다.

옵시디언 플러그인 방식이라 별도 앱을 설치하는 방식이 아니라 Obsidian이 동작하는 데스크톱/모바일 환경에서 사용할 수 있습니다.

현재 지원하는 기능은 다음과 같습니다.

- 파일 내용과 경로 메타데이터를 로컬에서 암호화한 뒤 업로드
- 여러 기기 사이에서 몇 초 안에 변경사항 동기화
- 버전 히스토리
- 삭제 파일 복구
- 파일 충돌 시 자동 병합

기술적으로는 Cloudflare Workers + Durable Objects + R2 위에서 동작합니다.

- 클라이언트에서 파일 내용과 경로 메타데이터를 암호화한 뒤 업로드합니다.
- 서버는 암호화된 blob과 동기화 메타데이터만 저장합니다.
- Durable Objects는 vault 단위 동기화 상태와 변경 순서를 관리하는 데 사용하고 있습니다.
- 파일 본문과 버전 히스토리는 R2에 저장합니다.

직접 배포해보고 싶은 분들을 위해 Cloudflare 무료 계정으로 배포할 수 있는 원클릭 배포도 준비해두었습니다.  
배포가 번거로운 분들은 hosted server로 먼저 간단히 테스트해볼 수 있습니다.

GitHub: <https://github.com/hjinco/synch>

## 원문
- [원문](https://synch.run)
- [GeekNews 토론](https://news.hada.io/topic?id=29408)

## My Note
<!-- 한 줄 코멘트 남기기 -->

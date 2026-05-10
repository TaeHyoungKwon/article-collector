---
category: AI
collected_at: '2026-05-10T18:28:53+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29354
id: hada-29354
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 9.099
recommended_on: '2026-05-10'
source: geeknews
tags:
- AI
- Other
- github.com/legalize-kr
title: 'Show GN: legalize-kr 업데이트 소식 - 행정규칙/자치법규 추가, CLI/MCP/Skill, 생태계 페이지 등'
url: https://github.com/legalize-kr
---

## TL;DR
- legalize-kr 프로젝트의 최근 업데이트 내용과 기능 개선 사항을 다룬 아티클이다.
- 행정규칙 및 자치법규의 추가로 법령 데이터의 추적 가능성이 높아졌으며, GitHub REST API 기반의 CLI 도구도 제공된다.
- 법령 정보 접근성을 높이고, 공공 법률 데이터 활용의 기회를 넓히는 의미 있는 변화로 볼 수 있다.

## GeekNews 요약
지난번 [Show GN](https://news.hada.io/topic?id=28353)으로 소개 이후, 1달(31일) 간의 legalize-kr 프로젝트 업데이트 소식을 정리해서 공유드립니다. 많은 분들께서 관심 가져주시고 응원해주신 덕분에 이것저것 개선할 수 있었습니다. 감사합니다!

### legalize-kr가 무엇인가요?

legalize-kr은 법제처의 [국가법령정보 공동활용](https://open.law.go.kr/)이 제공하는 대한민국의 법령 및 판례들을 Markdown + Git 히스토리로 아카이빙하는 프로젝트입니다. 모든 법령을 Markdown 문서로, 모든 개정 내역을 Git Commit으로 아카이빙하였으며, 판례 또한 Markdown 문서와 판결일 기준 Git History로 아카이빙하였습니다.

### 왜 만들었나요?

지난 3월 30일, 스페인 및 영미권의 법령들을 Markdown과 Git Commit으로 관리하는 [legalize.dev](https://legalize.dev/)라는 프로젝트를 GitHub Trending에서 발견하였습니다. 한국 법령들을 다루고 있는 곳도 당연히 있을 것 같았는데, 찾아보니 없었습니다. 하나쯤 있으면 좋을 것 같아 만들었습니다.

### 업데이트 1. 행정규칙 / 자치법규 저장소 추가

기존에는 법령과 판례만 다루고 있었는데, 같은 국가법령정보 공동활용에서 제공하는 행정규칙과 자치법규까지 별도 저장소로 추가했습니다. 이제 대한민국의 공개된 주요 법률 문서들을 한 곳에서 Markdown + Git History로 추적할 수 있습니다:

- 법령 저장소: [github.com/legalize-kr/legalize-kr](https://github.com/legalize-kr/legalize-kr)
- 판례 저장소: [github.com/legalize-kr/precedent-kr](https://github.com/legalize-kr/precedent-kr)
- 행정규칙 저장소: [github.com/legalize-kr/admrule-kr](https://github.com/legalize-kr/admrule-kr)
- 자치법규 저장소: [github.com/legalize-kr/ordinance-kr](https://github.com/legalize-kr/ordinance-kr)

행정규칙은 각 부처의 훈령/예규/고시 등이고, 자치법규는 지방자치단체의 조례/규칙입니다. 법령보다 양도 많고 개정도 잦은 편이라 Git History로 추적할 때의 가치가 꽤 클 것 같다는 생각이 들었습니다. 다만, 행정규칙의 경우 각 부처명의 이름 변경이나 역할 분담 등을 추적하기가 제법 까다로워, 여러번 개선하였지만, 아직 갈 길이 다소 멀어보입니다. 많은 분들의 관심과 참여 부탁드립니다ㅠ

### 업데이트 2. CLI 도구와 MCP, Agent Skill 추가

저장소 전체를 `git clone`해서 쓰시는 것이 가장 편리하고 좋지만, 매번 수십 GB짜리 저장소를 받기는 부담스러우실 수 있어서 GitHub REST API 기반의 CLI 도구를 만들었습니다. 또한, 같은 코드베이스에서 MCP 서버도 함께 제공하고, Claude Code / Codex 등에서 바로 쓰실 수 있는 Agent Skill도 추가했습니다:

- CLI / MCP 저장소: [github.com/legalize-kr/cli-tools](https://github.com/legalize-kr/cli-tools)
- Agent Skills 저장소: [github.com/legalize-kr/agent-skills](https://github.com/legalize-kr/agent-skills)

저장소 전체를 받지 않고도 특정 법령/판례를 검색하거나, 조문 단위로 조회하거나, 개정 이력을 추적할 수 있고, MCP를 통해 LLM/Agent가 직접 호출할 수도 있습니다. AGENT SKILL에는 어떤 상황에 CLI / MCP / `git clone` / 직접 GitHub 접근 중 무엇을 쓰면 되는지에 대한 가이드도 포함되어 있습니다. 단, GitHub REST API는 별도 인증 없이 시간당 60회 요청까지만 허용하고 있어, 필요 시 GitHub 토큰을 발급 받아 사용(시간당 5,000회까지 가능)해주셔야 합니다.

### 업데이트 3. 활용 사례 / 생태계 페이지 추가

`legalize-kr`에서 제공하는 데이터셋들을 사용한 프로젝트들이 조금씩 생기고 있어서, [홈페이지](http://legalize.kr)의 메인 페이지 하단과 '활용법' 메뉴에 정리하기 시작했습니다. 직접 활용한 프로젝트 외에 유사한 목적의 다른 프로젝트나 도구도 함께 안내드리고 있습니다 (앞서 GN에 소개되었던 [법망](https://news.hada.io/topic?id=28050), [Korean Law MCP](https://news.hada.io/topic?id=27995) 등).

혹시 `legalize-kr`의 데이터셋 중 하나 이상을 사용 중이시거나, 비슷한 영역에서 작업 중이신 프로젝트가 있다면 PR이나 이슈, 또는 이 글의 덧글로 알려주시면 함께 정리하겠습니다.

### 업데이트 4. 그 외 더 나은 데이터 활용을 위한 개선 사항들

여러 저장소들의 이슈들을 참고하여 데이터의 파싱 규칙 및 메타 데이터 정리 등을 진행 중에 있습니다. 주요 변경 사항은 다음과 같습니다:

- 기존 '편/장/절/관' 외에 '항/속' 등의 추가 단위 파싱 규칙 보완 ([legalize-kr/legalize-kr#32](https://github.com/legalize-kr/legalize-kr/issues/32))
- `<제M조의 N>` 패턴 유실 현상 수정 ([legalize-kr/legalize-kr#31](https://github.com/legalize-kr/legalize-kr/issues/31) 및 [legalize-kr/legalize-pipeline#2](https://github.com/legalize-kr/legalize-pipeline/issues/2))
- 누락 법령 보완 - 예: 상법 및 상법시행령 ([legalize-kr/legalize-kr#9](https://github.com/legalize-kr/legalize-kr/issues/9))
- 개정 전 시행규칙 파일 잔존으로 git log가 '수정'이 아닌 '추가'로 잡히던 문제 수정 ([legalize-kr/legalize-kr#24](https://github.com/legalize-kr/legalize-kr/issues/24))
- 판례 파일명 변경 및 선고일자 기준 디렉토리 분류 ([legalize-kr/precedent-kr#4](https://github.com/legalize-kr/precedent-kr/issues/4))
- 판례 출처 URL의 한글 주소 포맷 깨짐(law.go.kr 404) 수정 ([legalize-kr/precedent-kr#3](https://github.com/legalize-kr/precedent-kr/issues/3))
- 단기(檀紀) 연호 선고일자 17건 git 커밋 누락 보완 ([legalize-kr/precedent-kr#1](https://github.com/legalize-kr/precedent-kr/issues/1))
- 각 법령 / 판례 / 행정규칙 / 자치법규와 관련한 첨부 파일 링크들을 Markdown Frontmatter에 List 형식으로 추가

더 자세한 내용은 주요 저장소들의 닫힌 이슈들에서 보실 수 있습니다:

- legalize-kr 닫힌 이슈: [https://github.com/legalize-kr/legalize-kr/…](https://github.com/legalize-kr/legalize-kr/issues?q=is%3Aissue%20state%3Aclosed)
- precedent-kr 닫힌 이슈: [https://github.com/legalize-kr/precedent-kr/…](https://github.com/legalize-kr/precedent-kr/issues?q=is%3Aissue%20state%3Aclosed)
- legalize-pipeline 닫힌 이슈: [https://github.com/legalize-kr/legalize-pipeline/…](https://github.com/legalize-kr/legalize-pipeline/issues?q=is%3Aissue%20state%3Aclosed)

### 마지막으로

처음에는 "그냥 만들어두면 어디 쓰이겠지" 정도였는데, 지난번 Show GN 이후 많은 ⭐와 함께 이슈들도 받으면서 자연스럽게 범위가 넓어지고 있습니다. 꾸준히 유지보수/관리 중이니 많은 관심과 응원, 홍보 부탁드립니다. 감사합니다!

## 원문
- [원문](https://github.com/legalize-kr)
- [GeekNews 토론](https://news.hada.io/topic?id=29354)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-03T14:46:34+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31080
id: hada-31080
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: -990.391
recommended_on: '2026-07-04'
source: geeknews
tags:
- AI
- Other
- github.com/byh3071-cpu
title: 'Show GN: VHK - 모델·에이전트를 갈아타도 안 무너지는 풀사이클 AI 코딩 하네스'
url: https://github.com/byh3071-cpu/vhk
---

## TL;DR
- 이 글은 VHK라는 CLI 하네스의 기능과 목적을 설명한다.
- VHK는 다양한 코딩 에이전트를 통합해 규칙과 증거를 관리하여 모델을 변경해도 일관성을 유지한다.
- 개발자들은 VHK를 통해 코딩 중 발생하는 복잡성을 줄이고 프로젝트의 안정성을 높일 수 있다.

## GeekNews 요약
바이브코딩하다 보면 도구를 자주 갈아탑니다. Claude Code 쓰다가 Cursor, 또 Codex... 그때마다 규칙 파일이랑 맥락이 흩어지고, 에이전트는 "다 됐다"는데 실제론 테스트도 안 돌아간 경우가 많더라고요. 매번 손으로  
정리하기 싫어서 만든 CLI 하네스입니다.

VHK는 코딩 에이전트가 아니에요. 어떤 에이전트를 쓰든 그 위에 얹어서, 규칙·스펙·증거·기억을 repo 안에 고정해둡니다. 모델을 통째로 바꿔도 이 파일들은 그대로 남아요.

주요 기능

- 규칙 동기화: RULES.md 하나만 관리하면 .cursorrules, CLAUDE.md, copilot-instructions 등 8개 툴 규칙 파일을 자동으로 맞춰줍니다.
- 증거 게이트: verify / review / receipt / preflight. 특히 receipt는 tsc·test·build 종료코드 같은 기계 증거로 "거짓 완료"를 잡습니다(판정에 LLM 안 씀).
- 자가 진화: 세션마다 쌓인 교훈을 memory/pattern에 모아 규칙 후보로 올립니다. 쓸수록 이 프로젝트에 맞게 다듬어져요.
- 풀사이클: 아이디어 검증부터 개발·검증, 배포 후 콘텐츠·운영·판매 초안까지 명령으로 이어집니다(게시·결제는 사람이).
- 한국어 자연어: "vhk 저장해줘", "vhk 출고점검"처럼 한국어로도 라우팅돼요.

에이전트를 대체하려는 게 아니라, 에이전트가 잘 못 하는 반복·기억·게이트를 대신 잡아주는 쪽입니다.

솔직히 1인 프로젝트라 한국어 우선이고 영문 문서는 아직 따라가는 중입니다. 러프한 부분 있으면 편하게 알려주세요.

설치: npm i -g @byh3071/vhk  
GitHub: <https://github.com/byh3071-cpu/vhk> (MIT · MCP 35 tools · Node 22+)

혼자 만들다 v2.9.0까지 왔네요. 모델 갈아탈 때마다 프로젝트 흔들리는 분들 피드백 환영합니다.

## 원문
- [원문](https://github.com/byh3071-cpu/vhk)
- [GeekNews 토론](https://news.hada.io/topic?id=31080)

## My Note
<!-- 한 줄 코멘트 남기기 -->

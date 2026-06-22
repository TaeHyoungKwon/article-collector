---
category: AI
collected_at: '2026-06-22T15:54:37+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30719
id: hada-30719
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 4.901
source: geeknews
tags:
- AI
- Other
- github.com/TaewoooPark
title: 'Show GN: Agent-Blackbox - Claude Code/OpenCode 실행을 세션 맵과 토큰 낭비 분석으로 보는 도구'
url: https://github.com/TaewoooPark/Agent-Blackbox
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Claude Code / OpenCode 실행을 로컬에서 기록하고, 세션 맵과 컨텍스트 효율 점수로 보여주는 Agent-Blackbox를 만들었습니다.

AI에게 “이 작업에 토큰을 얼마나 쓸 것 같아?”라고 물으면 실제 비용과의 상관관계가 0.39에 불과하다는 연구가 있었습니다.

<https://arxiv.org/abs/2604.22750>

Claude Code나 OpenCode를 오래 돌리다 보면 이게 꽤 현실적인 문제로 느껴졌습니다. 마지막 요약은 그럴듯한데, 실제로는 어떤 파일을 읽었고, 어떤 명령이 실패했고, 어디서 토큰을 많이 썼는지 따라가기 어렵더라구요.

Agent-Blackbox는 에이전트의 마지막 요약을 파싱하는 대신, 실제 이벤트를 기록합니다.

- 파일 읽기 / 수정
- bash 실행과 종료 코드
- 검색
- todo 업데이트
- 권한 요청
- 서브에이전트 위임, 스킬 사용
- 모델 / 토큰 사용 흐름
- 실패 후 수정 / 재시도 흐름 등

설치 없이 npx로 바로 실행할 수 있습니다.

Claude Code 기록:  
npx @taewooopark/agent-blackbox up --host claude-code

OpenCode 기록:  
npx @taewooopark/agent-blackbox up --host opencode

둘 다 기록:  
npx @taewooopark/agent-blackbox up --host all

Claude Code는 별도 설치 없이 ~/.claude/projects transcript를 tail합니다. OpenCode는 글로벌 플러그인으로 이벤트를 받습니다. 기본 기록과 대시보드는 로컬에서 동작하고, API key가 필요 없습니다.

컨텍스트 효율 분석도 넣었습니다. 예를 들어 이런 것들을 잡습니다.

- 같은 파일을 반복해서 다시 읽음
- 수정량에 비해 너무 많은 파일을 읽음
- 큰 command/tool output이 컨텍스트를 많이 차지함
- 실패한 명령을 원인 수정 없이 반복함
- 토큰은 많이 썼는데 실제 변경은 적음
- prompt cache 활용이 낮음

문제가 된 파일명이나 명령 단위로 보여주기 때문에, 다음 실행에서 무엇을 줄이면 좋을지 비교적 구체적으로 볼 수 있습니다. 선택적으로는 발견한 낭비를 AGENTS.md 또는 CLAUDE.md에 관리 블록으로 기록해서, 다음 실행이 같은 실수를 덜 반복하게 할 수 있습니다.

제가 같은 작업을 같은 모델로 다시 돌려본 한 사례에서는 토큰 사용량이 939k -> 521k로 줄고, 효율 점수가 80 -> 99로 올랐습니다. 반복 검증된 벤치마크는 아니고, “실제 실행에서 관측된 낭비를 다음 루프에 반영하는 방식이 가능하다” 정도의 사례로 봐주시면 좋겠습니다.

특히 oh-my-openagent나 oh-my-claudecode 같은 멀티 에이전트 하네스와 잘 맞았습니다. 실행이 길어질수록 누가 어떤 파일을 만졌는지, 어디서 반복이 생겼는지 눈으로 확인하기 어려워지기 때문입니다.

GitHub:  
<https://github.com/TaewoooPark/Agent-Blackbox>

npm:  
<https://www.npmjs.com/package/@taewooopark/agent-blackbox>

사용해보시고 세션 맵에서 더 보고 싶은 이벤트, 효율 지표, 불편한 설치 흐름이 있으면 피드백 부탁드립니다. 감사합니다!

## 원문
- [원문](https://github.com/TaewoooPark/Agent-Blackbox)
- [GeekNews 토론](https://news.hada.io/topic?id=30719)

## My Note
<!-- 한 줄 코멘트 남기기 -->

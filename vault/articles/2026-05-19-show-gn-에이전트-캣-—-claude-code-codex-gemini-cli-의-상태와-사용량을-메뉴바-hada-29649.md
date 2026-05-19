---
category: AI
collected_at: '2026-05-19T10:34:42+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29649
id: hada-29649
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 7.307
source: geeknews
tags:
- AI
- Other
- agentcat.app
title: 'Show GN: 에이전트 캣 — Claude Code / Codex / Gemini CLI 의 상태와 사용량을 메뉴바 고양이로'
url: https://agentcat.app
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
저는 AI 에이전트를 두세 개씩 동시에 띄워놓고 일하는 편입니다. 그런데 띄워놓고 다른 일 하다 보면 "얘 지금 뭐 하고 있지?

끝났나? 멈췄나?" 가 자꾸 궁금해집니다.

그때마다 Activity Monitor 열고, 또 터미널 가서 로그 보고 하는 게 귀찮아서 만들었어요.

메뉴바(macOS) / 트레이(Windows) 한 칸에 고양이가 삽니다.

에이전트가 쉬면 자고, 작업 중이면 걷고, 풀가동이면 뜁니다.

클릭하면 누가 무슨 모델로 얼마나 썼고 어떤 프로젝트에 시간을 흘렸는지가 펼쳐집니다.

### 구조

처음 한 가지를 정하고 시작했습니다. 앱이 에이전트랑 직접 말하지 않게 한다. 사이에 `agentcatd` 라는 작은 로컬 데몬을 둡니다.

```
Claude Code · Codex · Gemini CLI · OpenCode · Copilot  
                    |  
                    | (어차피 로컬에 남기는 흔적들)  
                    v  
                 agentcatd  
                    |  
                    | JSON  
                    v  
         127.0.0.1:8765/v1/snapshot  
                    |  
                    v  
                메뉴바 앱
```

데몬이 각 에이전트가 어차피 로컬에 남기고 있는 흔적, 그러니까 프로세스 상태와 사용량 파일을 정리해서 한 군데 JSON 으로 펴 놓습니다. 메뉴바 앱은 그것만 폴링합니다.

이렇게 갈라놓으니 두 가지가 편해졌어요. 하나는 새 에이전트 지원이 "앱 빌드 다시" 가 아니라 "데몬에 어댑터 한 개" 가 됐다는 점. 이번 빌드에 OpenCode 와 GitHub Copilot 들어온 것도 그래서입니다. 다른 하나는 그 데몬만 따로 떼어 오픈소스로 공개할 수 있게 됐다는 점이에요. 가장 의심받을 만한 부분, 진짜 프롬프트 안 보냐 토큰 빨아먹는 거 아니냐 의 코드는 누구나 줄 단위로 까서 보실 수 있습니다.

→ <https://github.com/yong076/agentcat-connectors>

설치도 한 줄입니다.

```
# macOS / Linux  
curl -fsSL https://raw.githubusercontent.com/yong076/agentcat-connectors/… | bash  
  
# Windows (PowerShell)  
irm https://raw.githubusercontent.com/yong076/agentcat-connectors/… | iex
```

### 안 하는 것들

API 호출 안 합니다. 토큰을 한 개도 안 씁니다.  
프롬프트도, 코드도 안 봅니다.  
프로세스 메타랑 사용량 파일만 봅니다.

자랑이 아니라, 솔직히 이렇게 안 만들었으면 "내 컴퓨터에 또 뭘 깔라고" 가 됐을 거라 그래요.

메뉴바 한 칸 차지하면서 알림 쏘고 토큰 빨아먹는 앱이면 저부터 안 켜고 살았을 거예요.

### 비용 계산

입력 / 출력 / 캐시 읽기 / 캐시 쓰기를 따로 잡아 계산합니다. 단가가 다 달라서 "토큰 N 개 썼습니다" 로 합치면 청구서랑 안 맞고, 그러면 의미가 없어요. 청구서랑 거의 안 어긋나게 만드는 게 목표였습니다.

- 사이트: <https://agentcat.app>
- 이슈/피드백: <https://github.com/yong076/agent-cat-releases/issues>

## 원문
- [원문](https://agentcat.app)
- [GeekNews 토론](https://news.hada.io/topic?id=29649)

## My Note
<!-- 한 줄 코멘트 남기기 -->

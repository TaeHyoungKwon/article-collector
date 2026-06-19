---
category: AI
collected_at: '2026-06-19T18:36:00+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30642
id: hada-30642
matched_keywords:
- AI
- Codex
read: false
recommend_score: 5.386
recommended_on: '2026-06-19'
source: geeknews
tags:
- AI
- Other
- developers.openai.com
title: 'OpenAI Codex Record &amp; Replay: 작업을 한 번 보여주면 재사용 가능한 Skill로 변환'
url: https://developers.openai.com/codex/record-and-replay
---

## TL;DR
- OpenAI Codex의 Record & Replay 기능은 사용자가 수행한 작업을 녹화하여 재사용 가능한 Skill로 변환하는 기능이다.
- 이 기능은 반복적이고 규칙적인 작업을 간편하게 자동화할 수 있게 도와주며, 사용자 선호를 반영한 맞춤형 Skill을 생성한다.
- 따라서 이는 개발자들이 효율성을 높이고 작업 자동화를 통해 시간을 절약할 수 있는 유용한 도구가 된다.

## GeekNews 요약
- Record & Replay는 Mac에서 사용자가 직접 수행한 워크플로를 Codex가 관찰한 뒤, 재사용 가능한 Skill로 만들어주는 기능임
- 반복 작업이거나, 사용자의 선호와 규칙이 중요하거나, 프롬프트로 설명하기보다 직접 보여주는 편이 쉬운 작업에 적합함
- 예를 들어 비용 처리, 주차 공간 예약, 이슈 생성, 영상 게시, 반복 리포트 다운로드 같은 작업을 녹화해 Skill로 만들 수 있음
- 생성된 Skill은 이후 새 스레드에서 다시 호출할 수 있으며, 매번 달라지는 파일·날짜 범위·이슈 내용 같은 값만 전달하면 됨
- 현재 macOS에서 제공되며, Computer Use가 활성화되어 있어야 하고 초기 제공 지역에서는 EEA, 영국, 스위스가 제외됨

---

### Record & Replay의 목적

- 사용자가 이미 알고 있는 작업 절차를 Codex에게 한 번 시연하면, Codex가 그 패턴을 학습해 Skill로 정리함
- 이 Skill에는 언제 사용할지, 어떤 입력이 필요한지, 어떤 단계를 따라야 하는지, 결과를 어떻게 검증할지가 포함됨
- 단순 자동화 스크립트라기보다, 사용자의 실제 작업 방식과 숨은 선호를 Codex가 재사용 가능한 문맥으로 보관하는 방식에 가까움

### 사용하기 좋은 작업

- 단계가 안정적이고 성공 기준이 명확한 작업에 적합함
- 매번 비슷하게 반복되지만 일부 입력값만 바뀌는 작업에 잘 맞음
- 자연어 프롬프트로 길게 설명하기 어려운 UI 기반 작업도 직접 보여줄 수 있음
- 예시:
  - 비용 청구서 제출
  - 주차 공간 예약
  - 정해진 형식의 이슈 생성
  - 영상 게시
  - 주기적인 리포트 다운로드

### 녹화 시작 방법

- Codex 앱에서 Plugins를 열고 `+` 메뉴를 선택함
- `Record a skill`을 선택함
- Codex가 제안한 프롬프트를 검토하고, 필요한 맥락을 추가한 뒤 제출함
- Codex가 작업 녹화 권한을 요청하면 승인함
- Mac에서 실제 워크플로를 수행함
- 작업이 끝나면 메뉴 바, 오버레이, 또는 Codex에게 완료했다고 알려 녹화를 중지함

### 녹화 중 동작

- 녹화 중 Codex는 워크플로를 학습하는 데 필요한 사용자 동작과 창 내용을 관찰함
- 녹화는 사용자가 직접 멈출 때까지 계속됨
- 따라서 녹화는 Codex가 배워야 할 작업에만 집중하는 것이 좋음
- 관련 없는 정리 작업이나 후속 행동까지 이어서 녹화하면 Skill이 불필요하게 복잡해질 수 있음

### Skill 생성과 수정

- 녹화를 멈추면 Codex가 캡처된 워크플로를 분석해 Skill 초안을 만듦
- Skill에는 사용 조건, 필요한 입력, 실행 단계, 결과 검증 방식이 정리됨
- 이후 Codex에게 Skill을 더 다듬어달라고 요청할 수 있음
- 특히 파일명 규칙, 기본 필드 값, 선택 기준 같은 숨은 선호는 녹화 후 명시적으로 보완하는 것이 좋음

### 워크플로 재실행

- 새 스레드에서 Codex에게 생성된 Skill을 사용하라고 요청함
- 이번 실행에서 달라지는 값만 전달하면 됨
  - 업로드할 파일
  - 생성할 이슈 내용
  - 리포트 날짜 범위
  - 게시 대상
- Codex는 해당 Skill을 재사용 가능한 컨텍스트로 활용해 현재 환경에서 가능한 도구로 작업을 수행함
- Computer Use, 브라우저 액션, 설치된 플러그인 등을 조합해서 실행할 수 있음

### 더 좋은 녹화를 위한 팁

- 시연은 짧고 완결성 있게 유지하는 것이 좋음
- 녹화 전에 목표와 매번 바뀔 수 있는 입력값을 Codex에게 알려두는 것이 좋음
- 실제와 비슷한 입력값을 쓰되, 비밀 정보나 민감한 데이터는 피해야 함
- 녹화 후 Skill을 다듬으면서 네이밍 규칙, 기본값, 판단 기준 같은 숨은 선호를 추가하는 것이 좋음
- 워크플로가 끝나면 바로 녹화를 멈추고, 관련 없는 정리 작업까지 포함하지 않는 것이 좋음

### 별도 Plugin을 만들어야 하는 경우

- Record & Replay는 빠르게 Skill을 만들기 위한 방법임
- 팀 전체에 안정적으로 배포해야 하는 패키지라면 별도 Plugin으로 만드는 것이 더 적합함
- 여러 Skill을 묶거나, 앱 통합을 포함하거나, MCP 서버를 추가하거나, 설치 메타데이터를 관리해야 한다면 Plugin으로 패키징하는 편이 좋음

### 문제 해결

- Record & Replay가 보이지 않는 경우, 조직의 `requirements.toml` 설정을 확인해야 함
- `[features].computer_use`에서 `computer_use = false`로 설정되어 있으면 Computer Use와 Record & Replay가 모두 비활성화됨

---

GN+ 느낌으로 ChatGPT한테 요약 시킨 내용입니다.  
한번 간단하게 직접 써봤는데 생각보다 skill로 잘 말아주더라구요.

## 원문
- [원문](https://developers.openai.com/codex/record-and-replay)
- [GeekNews 토론](https://news.hada.io/topic?id=30642)

## My Note
<!-- 한 줄 코멘트 남기기 -->

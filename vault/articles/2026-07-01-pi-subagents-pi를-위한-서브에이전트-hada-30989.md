---
category: AI
collected_at: '2026-07-01T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30989
id: hada-30989
matched_keywords:
- AI
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- github.com/nicobailon
title: pi-subagents - Pi를 위한 서브에이전트
url: https://github.com/nicobailon/pi-subagents
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Pi 코딩 에이전트**가 작업을 **자식 Pi 세션**에 위임하도록 해주는 확장 기능
- 코드 리뷰/코드 정찰/구현/병렬 감사/백그라운드 작업 등 **추가적인 시각**이 필요한 작업에 활용
- 설치 후 별도 설정/슬래시 명령 학습 없이 **자연어 요청**만으로 위임 가능
  - **빌트인 에이전트**들: 코드 이해 전 `scout`, 외부 사실 확인 전 `researcher`, 큰 변경 전 `planner`, 구현은 `worker`, 점검은 `reviewer`, 결정 자체가 위험하면 `oracle`
- **포그라운드 실행**은 진행 상황을 대화에 스트리밍하고, **백그라운드 실행**은 제어권 반환 후에도 동작하며 `subagent({ action: "status" })`로 추후 확인
- 순차 **체인**, 인라인 병렬 그룹, 구조화 출력 기반 **동적 팬아웃**을 지원
- 병렬 에이전트의 파일 충돌을 막는 **git worktree 격리** 제공
- 빌트인 모델 대신 **agentOverrides**로 역할별 모델/thinking/fallbackModels를 1회/영속 지정 가능
- 자식이 부모 오케스트레이터 권한을 받지 않는 **차일드 세이프티 경계**와 기본 2단계 **재귀 깊이 제한**으로 무한 중첩을 방지함
- 모든 실행에 적용되는 **수락 게이트**(`auto`/`none`/`attested`/`checked`/`verified`/`reviewed`)로 작업 완료 증거 수준 관리
- 설치: `pi install npm:pi-subagents`

## 원문
- [원문](https://github.com/nicobailon/pi-subagents)
- [GeekNews 토론](https://news.hada.io/topic?id=30989)

## My Note
<!-- 한 줄 코멘트 남기기 -->

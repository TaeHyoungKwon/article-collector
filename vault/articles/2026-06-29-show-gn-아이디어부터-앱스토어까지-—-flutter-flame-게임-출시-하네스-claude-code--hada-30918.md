---
category: AI
collected_at: '2026-06-29T09:12:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30918
id: hada-30918
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -995.307
recommended_on: '2026-06-29'
source: geeknews
tags:
- AI
- Other
- github.com/tjdrhs90
title: 'Show GN: 아이디어부터 앱스토어까지 — Flutter/Flame 게임 출시 하네스 (Claude Code 플러그인)'
url: https://github.com/tjdrhs90/flutter-flame-harness
---

## TL;DR
- 이 글은 Flutter/Flame 게임의 전 과정을 효율적으로 관리하는 Claude Code 플러그인을 소개합니다.
- 플러그인은 AI를 활용해 게임 개발 절차를 자동화하고, 실제 플레이를 기반으로 한 평가 시스템을 적용합니다.
- 게임 개발자들은 새로운 툴을 통해 출시 과정의 부담을 줄이고 보다 창의적인 작업에 집중할 수 있습니다.

## GeekNews 요약
Flutter/Flame 게임을 "아이디어 → 기획 → 개발 → QA → 스토어 제출"까지 끌고 가는 Claude Code 플러그인을 오픈소스로 공개합니다.

Flame 게임을 직접 여러 개 만들어 스토어에 올리면서, 매번 반복하던 절차와 매번 다시 밟던 함정을 하네스로 코드화했습니다. "바이브 코딩"이 아니라 절차를 AI에 위임 — 가드레일 → 계획 → generator↔evaluator 빌드 루프 → 사람 검수.

흐름: 아이디어(없으면 AI 추천) → 계획 → 디자인 → 완료기준 계약 → generator↔evaluator 루프 → 사람이 직접 플레이·승인 → AdMob·빌드·스크린샷·제출

특징

- 회의적 평가자 — evaluator가 코드만 보고 통과 안 함, 게임을 실제로 띄워보고 판정. QA 통과해도 배포 전 사람 승인 게이트에서 멈춤
- 소싱 0으로도 항상 플레이 가능 — 코드 합성 오디오 + 코드 드로잉 비주얼(외부 에셋 불필요)
- "출시 가능한 모양"까지 — 커스텀 아이콘·스플래시·앱이름, 방향 네이티브 고정, iPad 제거, Play 필수 그래픽(512 아이콘 + 1024×500 피처), 스토어 메타·심사정보 자동 입력, CI 포함
- 출시 게임 7종의 실전 픽스 내장 — 오디오 풀링, 햅틱, 앱 생명주기, ATT 리젝(2.1) 회피, 번들ID 일관성 등
- PRD·UI는 사용자가 대화하는 언어로 생성(한국어/영어)

Anthropic의 harness design(generator-evaluator 분리 · 파일 핸드오프 · 회의적 QA)을 게임 출시 도메인에 적용했습니다.

레포: <https://github.com/tjdrhs90/flutter-flame-harness>

피드백 환영합니다 🙏

## 원문
- [원문](https://github.com/tjdrhs90/flutter-flame-harness)
- [GeekNews 토론](https://news.hada.io/topic?id=30918)

## My Note
<!-- 한 줄 코멘트 남기기 -->

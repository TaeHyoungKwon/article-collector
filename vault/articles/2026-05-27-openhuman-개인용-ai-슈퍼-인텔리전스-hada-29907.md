---
category: AI
collected_at: '2026-05-27T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 15
geeknews_url: https://news.hada.io/topic?id=29907
id: hada-29907
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 10.773
source: geeknews
tags:
- AI
- Other
- github.com/tinyhumansai
title: OpenHuman - 개인용 AI 슈퍼 인텔리전스
url: https://github.com/tinyhumansai/openhuman
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **일상생활에 자연스럽게 통합**되도록 설계된 오픈 소스 에이전트형 비서
- 설치 후 몇 번의 클릭만으로 동작하는 데스크톱 경험 제공
- **데스크톱 마스코트**가 말하고 주변에 반응하며, **Google Meets에 실제 참여자로 합류** 가능
- 사용자를 수 주에 걸쳐 기억하고, 입력을 멈춘 동안에도 백그라운드에서 사고 지속
- **118개 이상 서드파티 연동**을 원클릭 OAuth로 연결
  - Gmail, Notion, GitHub, Slack, Stripe, Calendar, Drive, Linear, Jira 등 지원
  - 별도 프롬프트나 폴링 없이 [auto-fetch](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki/auto-fetch)가 20분마다 각 활성화된 연결들을 확인하고 새 데이터를 알아서 자동으로 로딩
- **Memory Tree + Obsidian Wiki** 기반의 로컬 우선 지식베이스
  - 모든 데이터를 **≤3k 토큰 Markdown 청크**로 정규화·점수화 후 계층적 요약 트리로 묶어 로컬 **SQLite**에 저장
  - 동일 청크가 `.md` 파일로 Obsidian 호환 vault에 저장되어 열람·편집 가능
  - Karpathy의 **LLM-wiki 워크플로우**에서 영감을 받음
- **TokenJuice 토큰 압축 레이어**로 모든 도구 호출·스크랩 결과·이메일 본문·검색 페이로드를 LLM 도달 전 압축
  - HTML → Markdown 변환, 긴 URL 단축, 장황한 출력 중복 제거·요약
  - **CJK·이모지 등 멀티바이트 텍스트는 grapheme 단위로 보존**
  - 비용과 레이턴시를 **최대 80%까지 절감**
- **다양한 도구 기본 내장**
  - 웹 검색, 웹 페치 스크레이퍼, 풀 코더 툴셋(filesystem, git, lint, test, grep)
  - 네이티브 음성: STT 입력, ElevenLabs TTS 출력, 마스코트 립싱크, 라이브 Google Meet 에이전트
  - **Model routing**으로 작업별 적합 LLM(추론·빠른 응답·비전)에 자동 분배
  - **Ollama 기반 로컬 AI** 옵션 지원
- **[agentmemory](https://news.hada.io/topic?id=29754)** 백엔드 옵션 제공해서 Claude Code, Cursor, Codex, OpenCode와 동일 저장소 공유 가능
- GPL-3.0 라이선스

## 원문
- [원문](https://github.com/tinyhumansai/openhuman)
- [GeekNews 토론](https://news.hada.io/topic?id=29907)

## My Note
<!-- 한 줄 코멘트 남기기 -->

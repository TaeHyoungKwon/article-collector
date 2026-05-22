---
category: AI
collected_at: '2026-05-22T09:46:01+09:00'
geeknews_comments: 3
geeknews_score: 9
geeknews_url: https://news.hada.io/topic?id=29754
id: hada-29754
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 8.718
source: geeknews
tags:
- AI
- Other
- github.com/rohitg00
title: agentmemory - AI 코딩 에이전트용 영구 메모리 시스템
url: https://github.com/rohitg00/agentmemory
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- AI 코딩 에이전트가 세션이 끝나면 잊어버리는 문제를 해결
- 도구 사용을 백그라운드에서 자동 캡처·압축, 다음 세션 시작 시 컨텍스트 주입
- 매 세션마다 스택·아키텍처 **재설명 필요 없음**, 내장 메모리(CLAUDE.md)의 200줄 한계와 stale 문제 해소
- Claude Code, Cursor, Codex CLI, Gemini CLI 등 **MCP·REST 지원 모든 에이전트와 호환**, 단일 서버 공유
- LongMemEval-S 벤치마크에서 **R@5 95.2%** (mem0 68.5%, Letta 83.2%)
  - 연 토큰 ~170K, 비용 ~$10 (로컬 임베딩 사용 시 $0)
  - 240 observations 기준 22K+ 토큰 → **~1,900 토큰(92% 감소)**
- **BM25 + Vector + Graph** 트리플 스트림 검색을 RRF로 융합
  - 한국어/CJK는 `@node-rs/jieba`, `tiny-segmenter` 설치 시 단어 단위 분할
- 인간 뇌의 sleep consolidation에서 영감받은 **4-Tier 메모리 통합** :  
  Working(도구 사용을 단기 기억) → Episodic(세션 요약) → Semantic(사실/패턴 추철) → Procedural(워크플로우 와 결정)
- **51개 MCP 도구** 제공
  - Core: `memory_recall`, `memory_save`, `memory_smart_search`, `memory_patterns`
  - 멀티 에이전트: `memory_lease`, `memory_signal_send/read`, `memory_mesh_sync`
  - 거버넌스: `memory_audit`, `memory_governance_delete`, `memory_snapshot_create`(Git-versioned)
- 임베딩 Provider 자동 감지: Local `all-MiniLM-L6-v2`(무료·오프라인, BM25-only 대비 +8pp recall), Gemini, OpenAI, Voyage, Cohere, OpenRouter
- 실시간 뷰어(port 3113) + Session Replay
  - 라이브 observation 스트림, knowledge graph 시각화, 0.5×–4× 속도 재생
  - Claude Code JSONL transcripts `import-jsonl`로 가져오기 가능
- [iii 엔진](https://github.com/iii-hq/iii) 기반으로 **Postgres·Redis·Express·pm2·Prometheus 필요없음**
  - `iii worker add`로 pubsub·cron·queue·sandbox·SQL adapter 확장
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/rohitg00/agentmemory)
- [GeekNews 토론](https://news.hada.io/topic?id=29754)

## My Note
<!-- 한 줄 코멘트 남기기 -->

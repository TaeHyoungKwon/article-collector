---
category: AI
collected_at: '2026-07-01T14:46:25+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31000
id: hada-31000
matched_keywords:
- LLM
- RAG
- Claude Code
read: false
recommend_score: 6.693
source: geeknews
tags:
- AI
- Other
- github.com/jaytoone
title: 'Show GN: CTX v0.3.40 — Claude Code 세션 간 persistent memory (98명 사용자, 월 2,726
  다운로드)'
url: https://github.com/jaytoone/CTX
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Claude Code를 매일 쓰는데, 세션이 끊기면 이전 결정과 맥락이 모두 사라지는 게 너무 아까웠습니다.  
그래서 만든 게 CTX입니다.

**CTX란?**  
Claude Code의 UserPromptSubmit 훅에 붙어서, 과거 대화·결정·파일 참조를 다음 세션 시작 시 자동으로 주입합니다. `pip install ctx-retriever` 한 줄로 설치.

**현재 현황 (2026-07-01 기준)**

- 누적 사용자: 98명
- 누적 세션: 9,160개
- PyPI 월간 다운로드: 2,726회
- GitHub: <https://github.com/jaytoone/CTX>

**v0.3.40 주요 변경**

- BM25 + vec0 하이브리드 검색 (α=0.5)
- G1(의사결정 기억) + G2(코드베이스 파일 검색) 통합
- 설치 시 Turso URL 자동 감지 버그 수정
- vault.db → ~/.ctx/vault/ 경로 통합

**RAG와 뭐가 다른가?**

| 항목 | 일반 RAG | CTX |
| --- | --- | --- |
| 목적 | 문서 검색 | 개발자 세션 연속성 |
| 지연 | 500ms~2s | <1ms (BM25 결정론적) |
| LLM 호출 | 임베딩 매번 | 선택적 (vec-daemon) |
| 인덱싱 | 수동/배치 | 세션 종료 시 자동 |
| 비용 | API 호출 비용 | 로컬 무료 |
| 크로스세션 기억 | ✗ | ✅ |
| 코딩 에이전트 특화 | ✗ | ✅ |

**설치**

```
pip install ctx-retriever  
ctx install
```

피드백 주시면 감사하겠습니다. Claude Code 쓰시는 분들께 도움이 됐으면 합니다.

## 원문
- [원문](https://github.com/jaytoone/CTX)
- [GeekNews 토론](https://news.hada.io/topic?id=31000)

## My Note
<!-- 한 줄 코멘트 남기기 -->

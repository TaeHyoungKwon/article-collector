---
category: AI
collected_at: '2026-06-25T11:49:09+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=30815
id: hada-30815
matched_keywords:
- AI
- LLM
read: false
recommend_score: 5.609
source: geeknews
tags:
- AI
- Other
- code-as-harness.github.io
title: Code as Agent Harness — 코드를 에이전트의 실행 기반으로 보는 102페이지 서베이
url: https://code-as-harness.github.io/code-as-harness-webpage/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
**UIUC × Meta × Stanford** 합작. 5월 arXiv에 올라온 서베이 논문인데, 관점이 꽤 재밌다.

### 핵심 주장

**"코드는 더 이상 LLM이 생성하는 결과물이 아니다. 에이전트가 추론하고, 행동하고, 상태를 저장하고, 피드백을 검증하는 operational substrate(실행 기반)다."**

즉, 코드는 그냥 `.py` 파일이 아니라 **에이전트가 살아가는 세계 자체**라는 관점. 이걸 `code as agent harness`라고 부른다.

### 3계층 구조

논문은 에이전트 시스템을 3개 레이어로 나눠서 분석한다:

**① Harness Interface** — 코드가 에이전트를 환경과 연결하는 방식

- Program-of-Thoughts처럼 추론을 코드로 externalize해서 실행/검증
- GUI/로봇 제어를 생성된 프로그램이 정책으로 작동
- 코드베이스, 트레이스, 시뮬레이터가 환경 자체를 표현

**② Harness Mechanisms** — 장기 실행을 지속시키는 제어 시스템

- **Planning**: 단순 decomposition을 넘어서 PLAN.md 같은 파일시스템 기반 지속 계획으로 진화 중. Meta-Harness는 harness 설계 자체를 search space로 삼음
- **Memory**: working/semantic/experiential/long-term/multi-agent + context compaction으로 나눠서 분석. "메모리는 단일 벡터DB가 아니라 통합된 상태 관리 계층"이라는 게 핵심
- **PEV Loop**: Plan → Execute → Verify 사이클을 cybernetic governor로 재정의. 실행은 read-only → sandbox-edit → full-access(HITL) 3단계 권한 모델
- **AHE**: harness 자체를 측정하고 최적화하는 메타 계층

**③ Scaling the Harness** — 멀티에이전트가 코드라는 공유 매체 위에서 협업하는 방식

- 흥미로운 발견: **"토폴로지 복잡성은 공유 상태 표현의 미성숙함이 만든 세금이다"** — 상태를 잘 설계한 시스템은 단순한 구조로도 잘 돌아가고, 암묵적 상태에 의존하는 시스템은 그 결핍을 복잡한 토폴로지로 메꾼다

### 인상적인 지점들

- **Context Compaction + State Offloading**: 컨텍스트 윈도우에 다 넣지 말고, 결정에 필요한 요약만 active context에 두고 전체 데이터는 MCP-style 프로토콜로 offload하라 — 이거 완전 실전 꿀팁
- **검증을 결정적 센서로**: 린터, 타입 체커, 테스트, 퍼저 같은 결정적 피드백이 LLM critique보다 신뢰할 수 있는 제어 신호
- **실패의 원인은 모델이 아니라 harness에 있다**: "대부분의 에이전트 실패는 부족한 저장소 컨텍스트, 깨지기 쉬운 도구 인터페이스, 약한 검증기, 과도한 토큰 비용, 잘못된 재시도 정책에서 온다"

### Open Problems

논문이 남긴 7가지 오픈 문제 중:

- **최종 성공 외 평가**: 중간 트레이스, 복구 시도, 안전성 체크도 1급 지표로
- **회귀 없는 harness 개선**: 실패에서 배우면서 기존 동작을 깨뜨리지 않는 방법
- **멀티에이전트 간 트랜잭셔널 공유 상태**: 여러 에이전트가 동시에 코드 수정할 때 충돌 해결

참고

- 논문: <https://arxiv.org/abs/2605.18747>
- 깔끔한 요약 사이트: <https://code-as-harness.github.io/code-as-harness-webpage/>
- 관련 논문 모음: <https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers>

## 원문
- [원문](https://code-as-harness.github.io/code-as-harness-webpage/)
- [GeekNews 토론](https://news.hada.io/topic?id=30815)

## My Note
<!-- 한 줄 코멘트 남기기 -->

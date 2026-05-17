---
category: AI
collected_at: '2026-05-16T13:51:57+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29554
id: hada-29554
matched_keywords:
- AI
- LLM
- RAG
- Claude Code
- Codex
read: false
recommend_score: -989.307
recommended_on: '2026-05-16'
source: geeknews
tags:
- AI
- Other
- github.com/hang-in
title: 'Show GN: Claude Code / Codex CLI 의 무거운 코드 생성을 로컬 LLM 으로 위임하는 Plug-in (tunaLlama)'
url: https://github.com/hang-in/tunaLlama
---

## TL;DR
- 이 글은 로컬 LLM을 활용하여 Claude Code와 Codex CLI의 코드 생성 부담을 줄이는 tunaLlama 플러그인에 대해 다룬다.
- tunaLlama는 긴 코드 생성을 로컬로 전환하고, 짧은 분해 및 검증 단계는 클라우드 모델에 맡겨 효율성을 높인다.
- 이를 통해 사용자는 AI API 한도를 더 효과적으로 관리하고, 저비용 환경에서 협업할 수 있는 도구를 제공받을 수 있다.

## GeekNews 요약
바이브 코딩 시 Claude Code 나 Codex CLI 의 정액제 사용 한도가 빨리 닳는 분들을 위해 만든 위임 도구입니다.

<https://github.com/hang-in/tunaLlama>

Claude Code 로 코딩하다 보면 출력이 긴 단계 (코드 생성, 파일 리뷰, 리팩터) 가 토큰을 가장 많이 먹습니다. 그런데 이 단계는 보통 결정적이고 모델 품질의 차이가 작습니다. 반대로 분해 (요구사항 → 작업 목록) 와 검증 (돌려받은 결과가 요구사항을 만족하는지) 은 짧은 입출력이지만 모델 품질 차이가 큽니다.

tunaLlama 는 이 비대칭을 그대로 코드 흐름으로 굳혀 둔 백엔드 + 플러그인입니다.

역할모델책임ArchitectClaude / Codex (정액제)분해 / 사양 / 검증 / 통합Developer로컬 LLM (Ollama / Cloud / LM Studio)코드 생성 / 자체 리뷰 / 자체 수정ReviewerArchitect 같은 세션최종 판정

토큰 헤비 단계만 로컬로 빠지고, 짧은 분해·검증 단계는 그대로 Claude / Codex 에 남습니다.

Claude Code 와 Codex CLI 는 둘 다 플러그인으로 외부 도구를 사용할 수 있습니다.  
한 번 깔아두면 에이전트가 작업하다가 필요하다 싶으면 알아서 호출하는 구조입니다.  
사용자가 매번 "이 도구 써줘" 라고 안 해도 됩니다. tunaLlama 는 그런 플러그인 한 종류로, MCP (Model Context Protocol) 서버를 통해 13 개 도구를 노출합니다.  
한 레포로 Claude Code 와 Codex CLI 둘 다 작동합니다.  
(claude-plugin/marketplace.json 파일을 양 클라이언트가 모두 인식합니다.)

#### 사용자가 작업을 요청 하면(한국어 / 영어)

1. Architect 가 작업 분해 - 짧으면 tuna\_dev\_review, 길면 spec 문서 작성 후 tuna\_dev\_review\_from\_spec
2. 백엔드가 generate → review → fix 루프를 반복 (bounded delegation - 종료 조건은 review pass 또는 max iter)  
   모든 호출은 SQLite 에 기록되고 한국어 형태소 분석기 (Kiwi) 로 색인됨
3. Architect 가 결과 검증 후 사용자에게 반환

mid-size 로컬 LLM 단독으로 돌렸을 때 vs Architect 가 컨텍스트 정리해서 넘긴 후 비교에서 +0.58 ~ +0.64 (3개 모델 검증, Phase 7-2). 같은 로컬 LLM 인데 컨텍스트 잘 정리해서 넘기면 결과가 의미 있게 좋아진다는 뜻입니다.  
다만 이 측정은 합성 시드 기반 입니다. 현실에서 자주 나오는 작업 시나리오를 미리 만들어둔 테스트 셋 위에서 측정한 것이라, 실제 사용자 워크플로우에서도 똑같이 나올지는 별개 문제입니다. organic dogfooding metric 은 v0.5.7+ 부터 4 종 (standalone\_toy\_rate / convention\_adherence\_rate / ast\_excess\_score / syntactically\_valid) 을 ~/.tunallama/metrics.db 에 자동 적재하고 있고, 누적 baseline 까지 외부 사용자 재현성은 계속 수집 중입니다.

한도 절약은 Anthropic / OpenAI 한도 계산식이 비공개라 "X% 절약" 같은 정량적인 결과는 없습니다. "그냥 쓰는 것보다는 낫다" 입니다,

#### 한국어 지원

Kiwi 형태소 분석기를 붙여서 한국어 검색 인덱싱이 가능합니다. "이메일검증" 처럼 띄어쓰기 없는 입력에 대해 "이메일" 로 검색해도 매칭됩니다. FTS5 의 unicode61 토크나이저가 한국어를 음절 / 자모로만 자르는 한계를 보완한 구조입니다. 다만 Kiwi 가 못 처리하는 신조어 / 전문용어는 검색 품질에 영향 줄 수 있습니다.

#### 5분 설치

세션에서 한 줄 던지시면 끝납니다:

"<https://github.com/hang-in/tunaLlama> 의 INSTALL.md 따라 설치해줘"

에이전트가 알아서 의존성 깔고, .env 설정하고, 플러그인 등록하고, 검증까지 단계별로 진행합니다.  
수동 설치를 원하시면 README 참고.

#### 양 환경 동작 매트릭스

Claude Code 와 Codex CLI 가 같은 레포로 작동하지만, 일부 기능은 한쪽에서만 검증됐습니다 (v0.5.6 실측, Claude Code 2.1.138 + Codex CLI 0.128.0):

항목Claude CodeCodex CLIMCP tools 13 개 호출✓✓  
DB 공유 (~/.tunallama/memory.db)✓✓  
state.md 공유✓✓  
tuna\_load\_memory / tuna\_recall 명시 호출✓✓  
Agents auto-discovery✓  
SessionStart hook + state.md auto-prepend✓  
(v0.5.5+)✗MCP resource auto-attach✗✗  
Claude Code 에서는 state.md auto-prepend 가 자동 작동하고,  
Codex CLI 에서는 사용자가 첫 turn 에 tuna\_load\_memory 명시 호출 또는 docs 직접 fetch 가 권장됩니다.  
MCP 도구 13 개 호출은 양쪽 모두 정상 작동하니까 delegation 자체는 도구 레벨에서 가능합니다.

#### 한계

사용 한도 절약은 체감 데이터 (위 언급)  
MCP 도구 system prompt 비용은 의도된 trade-off - 13 도구 description + schema 가 매 conversation system prompt 에 약 1.6k tokens prepend. accidental context bloat 가 아니라 Architect 가 적절한 delegation 도구를 선택하기 위한 affordance 비용으로 설계됨

로컬 LLM 환경 (Ollama 등, Ollama cloud도 정상 동작) 필수 - 없으면 작동 X  
검색 측정값은 합성 시드 기반 (위 언급)  
Codex CLI 의 일부 기능 미작동 (위 매트릭스)  
한국어 신조어 / 전문용어 검색 품질 영향 가능

#### 왜 프롬프트 시드 / AGENTS.md 가 아닌가

에이전트에게 더 많은 문서를 읽히는 방식으로 컨텍스트 한계를 해결하려 하지 않습니다.  
대신 작업 단위를 작게 잘라 MCP 도구로 로컬 / 저비용 LLM 에 넘기고, 상위 Architect 모델은 짧은 spec, review 결과, 최종 diff 판단에 집중합니다.  
문서 기반 운영 규칙은 시간이 지나면 stale state, drift, lost-in-the-middle 문제를 만들 수 있습니다.  
tunaLlama 는 이를 피하기 위해 delegation call 을 SQLite 에 기록하고, 필요할 때 검색 / 리콜하는 실행 계층을 둡니다.

#### 누가 쓰면 도움 될 만한가

Claude Code Pro/Max 정액제 사용자 (한도 관리 동기)  
Codex CLI 사용자 (OpenAI 정액제 / API quota 관리)  
Ollama 로컬 / Ollama Cloud / LM Studio 환경 이미 있는 분  
한국어 작업 다루는 분 (Kiwi 통합)

#### 테스트 / 라이선스

v0.5.x usable dogfooding release. 507 unit/plugin tests + 27 integration/search\_quality tests, 90% coverage.  
측정 명령은 README 에 명시 (pytest --no-cov -q -m "not search\_quality and not integration").  
라이선스는 MIT. 영문 README (README.en.md) 동기화 유지 중. 피드백 / 이슈 / PR 환영합니다.  
다른 AI CLI 호환 제안 또한 환영합니다.

## 원문
- [원문](https://github.com/hang-in/tunaLlama)
- [GeekNews 토론](https://news.hada.io/topic?id=29554)

## My Note
<!-- 한 줄 코멘트 남기기 -->

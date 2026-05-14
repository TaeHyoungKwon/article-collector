---
category: AI
collected_at: '2026-05-14T11:50:02+09:00'
geeknews_comments: 0
geeknews_score: 9
geeknews_url: https://news.hada.io/topic?id=29493
id: hada-29493
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 6.303
source: geeknews
tags:
- AI
- Other
- claude.com
title: Code w/ Claude에서 발표한 모든 것들
url: https://claude.com/code-with-claude/san-francisco
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Anthropic의 개발자 컨퍼런스**: 온라인과 오프라인으로 진행되며, 오프라인 행사는 **샌프란시스코 5/6, 런던 5/19, 도쿄 6/10**에 열림. 샌프란 행사에서 **19개 세션** 영상이 공개됨
- Claude는 **더 긴 작업 수행, 장기 메모리, 더 많은 도구 사용, 더 나은 검증** 방향으로 발전 중
- 핵심 변화는 개발자가 직접 만들던 **반복 실행, 도구 선택, 검증, 메모리, 문맥 관리**가 Claude 제품과 플랫폼 안으로 들어가고 있다는 것
- 제품과 조직의 차별화는 모델을 어떻게 호출하느냐보다, 모델에게 **어떤 도구, 데이터, 권한, 문맥**을 열어주느냐로 이동함
- 코드 작성 자체보다 **검증, 보안, 권한 관리, 관찰 가능성, 평가 체계, 조직 운영**이 새로운 병목으로 커짐
- 앞으로 중요한 영역은 **맞춤 도구, 신뢰할 수 있는 메모리, 평가, 보안 경계, 문맥 공학(context engineering), 에이전트 작업 환경(agent experience)** 임

### 세션 1 - [키노트](https://claude.com/code-with-claude/session/sf-opening-keynote)

- **Claude Code**와 **Claude Platform**을 개발자에게 더 잘 작동하게 만드는 제품 개선에 초점이 맞춰짐
- 대부분의 사용자는 Claude API나 터미널을 직접 쓰기보다, 개발자가 만든 제품 안에서 Claude를 사용함
- **Claude Platform API 사용량**은 전년 대비 거의 **17배** 증가함
- Claude Code의 평균 개발자는 **주당 20시간** Claude를 실행함
- Claude Code의 **5시간 사용 한도**가 Pro, Max, Team, seat-based Enterprise plans에서 **두 배**로 늘어남
- **Claude Opus API 한도**도 크게 올라감
- **SpaceX의 Colossus One 데이터센터** 용량을 활용해 개인 개발자와 소규모 팀에 더 많은 연산 자원을 제공하려 함
- **Opus 4.7**은 Amp, Rakuten, Intuit에서 코딩 에이전트 성능, 계획 품질, 실제 엔지니어링 작업 해결률을 높임
- 앞으로의 Claude는 **더 나은 판단력, 더 큰 문맥과 메모리, 여러 에이전트 협업**을 향해 감

### 세션 2 - [What's new in Claude Code](https://claude.com/code-with-claude/session/sf-whats-new-in-claude-code)

- Claude Code의 새 기능은 **개발자 사용성**과 **자율성 강화**라는 두 축으로 묶임
- **Remote Control**은 터미널에서 시작한 세션을 웹이나 모바일에서 이어받게 해줌
- **Full screen terminal UI**는 가상 스크롤백을 써서 깜빡임 없는 렌더링과 클릭 가능한 도구 호출 화면을 제공함
- Claude Code GUI는 여러 세션을 핀 고정, 필터링, 그룹화, 분할 화면으로 관리할 수 있게 바뀜
- plan view, diff view, files view에서 줄 단위 댓글을 남기고 Claude가 나중에 모아 처리할 수 있음
- **Auto Mode**는 도구 호출이 파괴적인지, 프롬프트 주입처럼 보이는지 분류한 뒤 안전하면 권한 확인 없이 실행함
- **워크트리(worktree)** 는 여러 Claude 세션이 각자 격리된 브랜치와 파일 복사본에서 병렬로 작업하게 해줌
- **자동 메모리(auto memory)** 는 Claude가 프로젝트별 `memory.md`와 관련 파일을 관리하며 빌드 명령, 디버깅 단서, 프로젝트 선호를 다음 세션에 재사용함
- **Routines**와 **`/loop`** 는 cron, GitHub webhook, API 트리거로 Claude Code 세션을 자동 실행하게 만듦

### 세션 3 - [Memory and dreaming for self-learning agents](https://claude.com/code-with-claude/session/sf-memory-and-dreaming-for-self-learning-agents)

- **Memory**는 MCP, Claude Code, Agent SDK, Skills 다음 단계의 기본 요소로 다뤄짐
- **Claude Managed Agents**의 메모리는 **파일 시스템처럼 구성**되어 Claude가 Bash와 Grep으로 직접 정리하고 갱신함
- **Opus 4.7**은 무엇을 저장할지, 파일을 어떻게 나눌지, 메모리 구조를 어떻게 유지할지 더 잘 판단함
- 여러 에이전트가 같은 메모리 저장소를 읽고 쓸 수 있도록 **읽기 전용 조직 메모리**와 **읽기-쓰기 작업 메모리**를 나눌 수 있음
- 수백 개 이상의 에이전트가 동시에 메모리를 바꿔도 덮어쓰지 않도록 **콘텐츠 해시 기반 낙관적 동시성 제어**를 사용함
- **변경 이력, 작성 주체, 세션, 시점**을 남겨 기업 환경에서 감사 가능한 메모리로 관리함
- **Dreaming**은 최근 에이전트 세션과 transcript를 비동기로 분석해 반복 실수, 성공 전략, 중복 메모리, 오래된 메모리를 찾아 정리함
- **Harvey**는 **Dreaming**을 법률 벤치마크에 적용해 한 법률 시나리오의 **작업 완료율을 6배** 높임
- SRE 데모에서는 여러 에이전트가 따로 보면 놓치던 60초 재시도 패턴을 **Dreaming**이 찾아 메모리에 반영함
- 목표는 오늘의 에이전트 작업이 내일의 에이전트를 자동으로 더 낫게 만드는 **지속 학습 구조**임

### 세션 4 - [Caching, harnesses, and advisors: Building on Claude at GitHub scale](https://claude.com/code-with-claude/session/sf-caching-harnesses-and-advisors-building-on-claude-at-github-scale)

- GitHub Copilot 규모에서는 **프롬프트 캐싱**이 비용과 지연 시간을 줄이는 핵심 수단이 됨
- 목표 캐시 적중률은 **94-96%** 이며, **70% 수준**은 프롬프트 조립이나 캐싱 설계에 문제가 있다는 신호로 봄
- 시스템 프롬프트와 도구 목록 앞부분은 가능한 한 정적으로 유지해야 함
- UUID, 시점, 동적 도구 로딩이 앞부분에 들어가면 캐시가 쉽게 깨짐
- 여러 모델을 오가는 **하네스(harness)** 에서도 Opus 호출이 이전 캐시를 재사용하도록 캐시 친화성을 지켜야 함
- GitHub는 새 모델을 **오프라인 벤치마크, 내부 사용, A/B 테스트, 온라인 평가(eval), 출시 후 최적화** 순서로 굴림
- **Advisor 전략**은 저렴한 실행 모델이 대부분의 일을 하고, 중요한 판단이 필요할 때만 Opus를 조언자로 부르는 구조임
- 모델 자체보다 **프롬프트, 도구, 캐시, 모델 선택, 평가, 온라인 피드백**을 묶은 운영층이 품질과 비용을 좌우함

### 세션 5 - [The expanding toolkit](https://claude.com/code-with-claude/session/sf-the-expanding-toolkit)

- 작년에 직접 만들던 **보조 코드**가 이제 모델과 API 안에 포함되고 있음
- 도구 사용에서는 **수동 라우터**나 **재시도 장식자**의 가치가 줄어듦
- Claude가 직접 도구를 찾고, 실패한 도구 호출을 보고 복구한 뒤 다시 호출할 수 있음
- 도구 안내에는 입력뿐 아니라 **출력 스키마**도 적어두는 편이 좋음
- 출력 구조를 미리 알면 Claude가 불필요한 왕복 호출 없이 결과를 더 잘 활용함
- Claude Code의 **사전/사후 도구 훅(hook)** 은 특정 호출을 막거나 결과를 자동 기록하고 분석하는 데 쓸 수 있음
- **100만 토큰 문맥, 서버 측 압축, 문맥 편집**으로 긴 작업의 문맥 관리가 단순해짐
- 오래된 스크린샷, 검색 결과, 파일 읽기 결과는 주기적으로 제거해도 그 결과가 만든 판단은 유지할 수 있음
- **Opus 4.7**은 최대 **1440p**까지 원본 해상도 스크린샷에서 **1:1 픽셀 좌표**를 반환해 화면 자동화의 좌표 보정 부담을 줄임
- 모델 한계를 보정하는 코드는 수명이 짧고, Claude가 볼 수 없는 **도구, 데이터, 인증, 도메인 문맥**을 연결하는 코드가 오래 남음

### 세션 6 - [How to get to production faster with Claude Managed Agents](https://claude.com/code-with-claude/session/sf-how-to-get-to-production-faster-with-claude-managed-agents)

- **Claude Managed Agents**는 장시간 실행되는 운영용 에이전트에 필요한 **문맥 관리, 자격 증명 관리, 보안, 접근 제어, 사람 검토, 관찰 가능성**을 플랫폼으로 묶음
- 기본 구성은 agent configuration, environment, session임
- session events로 사용자 이벤트, 에이전트 이벤트, 세션 이벤트, 구간 이벤트를 볼 수 있음
- Console은 설정, 환경, **전체 실행 추적(trace), 병목, 권장 조치**를 한 화면에 모음
- **outcomes**는 미리 정한 종료 기준과 채점 기준을 만족할 때까지 Claude가 반복하게 만드는 기능임
- 여러 에이전트 조율, 메모리, **Dreaming**이 고급 기능으로 함께 다뤄짐
- 대시보드 데모에서는 agent가 병렬화, fast mode, 프롬프트 최적화를 찾아 **렌더링 시간을 약 37초에서 10초로 줄임**
- 운영용 에이전트는 모델 호출 반복문만이 아니라 **추적, 병목 분석, 권한, 검증**을 함께 갖춰야 함

### 세션 7 - [A conversation with Dario Amodei & Daniela Amodei](https://claude.com/code-with-claude/session/a-conversation-with-dario-amodei-daniela-amodei)

- Anthropic은 예상보다 빠른 **사용량과 매출 성장**으로 연산 자원이 부족해짐
- **추가 연산 용량**을 확보해 개발자와 사용자에게 더 많이 전달하려 함
- 개발자는 Claude의 핵심 사용자이자 AI가 경제 전반에 퍼지는 모습을 먼저 보여주는 집단으로 다뤄짐
- Claude Code의 다음 변화는 **개인 생산성**에서 **팀과 조직 생산성**으로 이동함
- 코드 작성 속도가 빨라질수록 **보안, 검증, 신뢰성, 유지보수**가 새 병목이 됨
- 모델 능력이 빨리 바뀌면서 몇 달 전에는 불가능했던 제품이 갑자기 가능해짐
- API 시장은 계속 중요함
- 앞으로의 Claude는 한 사람의 작업을 돕는 수준을 넘어 **조직 전체의 여러 사람과 여러 에이전트 작업**을 키우는 방향으로 감

### 세션 8 - [Live coding session with Boris Cherny and Jarred Sumner](https://claude.com/code-with-claude/session/sf-live-coding-session-with-boris-cherny-and-jarred-sumner)

- Bun의 **Robobun**은 GitHub issue를 자동 재현하고 테스트를 포함한 PR을 만듦
- **이전 버전에서는 실패하고 수정 브랜치에서는 통과하는 조건**을 PR 제출 기준으로 삼음
- **`CLAUDE.md`** 는 빌드 명령, 테스트 명령, 테스트 위치, 과거 실패 패턴, 폴더 구조, CI 로그 읽는 법을 담는 에이전트 운영 문서가 됨
- CodeRabbit, Claude Code Review, **Robobun**을 함께 써서 스타일, **`CLAUDE.md`** 준수, diff 밖 경계 조건 검토를 자동화함
- Claude Code와 **Opus 4.7**은 **목표, 측정 방법, 검증 반복**이 명확할 때 성능을 점진적으로 끌어올리는 작업에 잘 맞음
- 병목은 **코드 작성**에서 **계획과 검증**으로 이동함
- agent가 만든 PR은 반드시 병합해야 하는 결과물이 아니라 검토 가능한 제안으로 다뤄질 수 있음
- agent PR이 늘어도 사람의 병합 기준은 낮아지지 않고 오히려 높아질 수 있음

### 세션 9 - [Building with Claude Managed Agents and Asana AI teammates](https://claude.com/code-with-claude/session/sf-building-with-claude-managed-agents-and-asana-ai-teammates)

- Asana의 **AI teammates**는 기업 안에서 실제 동료처럼 일하는 에이전트를 목표로 함
- 에이전트는 actor가 되어 승인, 워크플로, 여러 단계 업무를 사람들과 함께 처리함
- 많은 기업의 에이전트 사용은 아직 한 사람이 결과를 받고 다음 사람에게 넘기는 단일 사용자 흐름에 머무름
- Asana는 여러 사람이 같은 에이전트와 상호작용하고 지식과 메모리가 누적되는 공동 작업 흐름을 지향함
- **Asana work graph**는 목표, 포트폴리오, 프로젝트, 작업, 승인, 과거 결정을 연결해 에이전트 문맥으로 사용됨
- AI teammate는 **공유 설정, 역할 기반 접근 제어, 감사 가능성**을 갖고 사람 동료처럼 시스템에 들어감
- **Claude Managed Agents**는 **캠페인 기획서 작성**과 **HTML 랜딩 페이지 목업 생성** 같은 여러 단계 작업을 처리함
- Asana는 사람 인터페이스, 기업 문맥, 보안, 감사 가능성에 집중하고 **Claude Managed Agents**는 검증 반복, 채점기, **outcomes**, 여러 에이전트 실행을 맡음
- **21개 이상**의 사전 구축 **AI teammates**가 PMO, 마케팅, IT, HR, R&D 업무에 맞춰 제공됨
- 피드백은 에이전트 메모리에 남아 다음 사용자가 같은 실수를 다시 겪지 않게 함

### 세션 10 - [Running an AI-native engineering org](https://claude.com/code-with-claude/session/sf-running-an-ai-native-engineering-org)

- **AI-native 엔지니어링 조직**에서는 코드 작성 처리량이 가장 비싼 병목이 아니게 됨
- **검증, 리뷰, 보안, 유지보수, 직군 간 조율**이 새 병목으로 커짐
- 6개월 로드맵이나 모든 작업 전 설계 문서보다, 적절한 시점에 계획하고 빠르게 시제품을 만드는 흐름이 Claude Code 팀에 맞음
- 기술 논쟁은 긴 화이트보드 토론보다 **여러 구현 PR**을 만들어 실제 영향과 API 모양을 비교하는 쪽으로 바뀜
- 코드 생성이 쉬워진 만큼 테스트, 자동화, 더 이른 검증이 더 중요해짐
- "누가 이 코드를 썼나"보다 회귀 원인, 전문가 답변 필요 여부, 문맥 확보 목적을 구분하는 일이 더 중요함
- Claude Code 팀은 스타일, 린트, PR 피드백, 일부 버그 수정과 테스트 추가를 Claude에 맡김
- **법무 검토, 보안 민감 코드, 신뢰 경계, 제품 감각**은 사람 전문가가 계속 봄
- 채용에서는 단순 처리량보다 **제품 감각이 있는 창의적 빌더**와 **깊은 시스템 전문성**을 더 중시함
- 성공 지표는 **온보딩 시간 단축, PR 주기 단축, Claude 도움을 받은 커밋 증가**로 볼 수 있음

### 세션 11 - [Building AI-native: Inside the stacks powering Cognition, Gamma, and Harvey](https://claude.com/code-with-claude/session/sf-building-ai-native-inside-the-stacks-powering-cognition-gamma-and-harvey)

- **Gamma**는 도구 호출과 에이전트 조율 개선을 빠르게 제품에 반영해 에이전트 기반 편집 흐름을 강화함
- **Gamma**는 MCP connector를 통합 기능뿐 아니라 고객 유입과 업무 흐름 진입점으로 활용함
- **Cognition**은 모델이 코드 편집, 파일 시스템 사용, 장기 실행 계획을 더 잘하게 되면서 일부 자체 계획 및 메모리 시스템을 줄임
- **Harvey**는 foundation model, 추론 모델, 코딩 에이전트의 변곡점마다 제품 구조를 다시 설계함
- **Harvey**의 현재 플랫폼 능력은 agent-native 구조가 아니었다면 얻기 어려웠음
- AI-native 제품은 6-12개월 안에 기존 구조가 낡을 수 있음을 전제로 해야 함
- **기록, 관찰 가능성, 재생, 평가**는 빠른 구조 변화에 대응하기 위한 필수 장치가 됨
- 법률처럼 민감한 분야에서는 공개 데이터, 비공개 데이터, 메모리, 에이전트 흐름 사이의 단단한 데이터 경계가 필요함
- 특정 모델 한계에 맞춘 구조보다 다음 능력 도약을 빠르게 흡수할 수 있는 구조가 중요해짐

### 세션 12 - [Architecting for model step-changes: A fireside with Vercel's Guillermo Rauch](https://claude.com/code-with-claude/session/sf-architecting-for-model-step-changes-a-fireside-with-vercels-guillermo-rauch)

- **Vercel**은 에이전트형 인프라를 핵심 방향으로 봄
- 클라우드가 스스로 복구하고, 최적화하고, 설정을 바꾸는 인프라로 확장될 수 있음
- **AI Gateway**는 토큰을 위한 CDN처럼 다뤄짐
- 여러 제공자와 모델을 다루며 라우팅, 장애 대응, 비용 제어를 맡는 층이 됨
- **Opus 토큰**은 사용량 비중보다 지출 비중이 훨씬 커서 고지능 모델을 제품에 넣을 때 비용 구조를 명확히 봐야 함
- **Opus 4.5** 도입 뒤 **V0**는 이전 모델을 보정하던 문법 검사, 자동 수정, 일부 처리 절차를 단순화할 수 있었음
- 모델 능력 도약은 새 기능 추가뿐 아니라 기존 보정 코드를 제거하는 변화로 이어짐
- **V0**에서 Opus 사용 확대 뒤 **제품 크레딧 지출이 2배** 늘어남
- 앞으로는 CLI와 UI 기반 개발뿐 아니라 비동기적이고 사람 감독이 적은 에이전트가 더 커질 수 있음

### 세션 13 - [The thinking lever](https://claude.com/code-with-claude/session/sf-the-thinking-lever)

- **테스트 시점 연산(test-time compute)** 은 Claude가 추론 중 더 많은 토큰과 시간을 써서 어려운 문제를 푸는 축임
- 같은 **Opus 4.7**도 low, high, max **effort**에 따라 교통 시뮬레이션 품질이 크게 달라짐
- 더 많은 시간과 토큰을 쓸수록 그래픽, 교통 흐름, 차량 움직임이 더 현실적으로 바뀜
- Claude가 쓰는 토큰은 사고 토큰, 도구 호출 토큰, 텍스트 토큰으로 나뉨
- 사고 토큰은 내부 추론, 도구 호출 토큰은 외부 세계와의 상호작용, 텍스트 토큰은 사용자와의 소통에 쓰임
- **effort**는 시간, 비용, 품질의 균형을 표현하는 조절 장치임
- **Task Budgets**는 Claude가 특정 작업에서 쓸 수 있는 토큰, 시간, 비용의 상한을 두게 해줌
- **적응형 사고(adaptive thinking)** 는 Claude가 필요한 순간에 생각하고, 도구를 쓰고, 사용자에게 답하는 순서를 자유롭게 고르게 함
- coding과 agentic use case에서는 **extra high**가 좋은 기본값으로 다뤄짐
- 단순 대량 분류나 추출에는 작은 모델이 유리하고, 지능이 필요한 작업을 빠르게 끝내려면 큰 모델의 낮은 **effort**가 더 나을 수 있음

### 세션 14 - [How Datadog built a universal machine tool for Claude Code](https://claude.com/code-with-claude/session/sf-how-datadog-built-a-universal-machine-tool-for-claude-code)

- **Datadog 엔지니어의 약 90%** 가 운영 코드에 AI 코딩 도구를 사용함
- 그중 **최소 2/3**는 Claude Code를 사용함
- AI 코딩 도구 사용 범위는 개별 함수, 테스트, 연결 코드에서 시스템 단위 작업으로 넓어짐
- 병목은 코드 작성에서 피드백 반복과 운영 검증으로 이동함
- **Helix 실험**에서는 Claude Code가 Kafka와 비슷한 스트리밍 서비스를 며칠 만에 만들 수 있었음
- 운영 환경으로 가져가려면 shadowing, 검증 계단, 시스템 마일리지가 필요함
- **Tempor**는 에이전트가 즉흥적으로 도구를 만들지 않고 상태, 전이, 효과, 불변식을 담은 청사진을 먼저 만들게 함
- **전이 표, 정책 문, 타입이 있는 효과, 검증기, 속성 테스트**가 에이전트가 만든 소프트웨어를 검사 가능하게 만듦
- agent에게 자유를 주려면 운영 시스템의 불변식과 검증 절차를 기계가 읽을 수 있게 만들어야 함

### 세션 15 - [Building with Claude on Google Cloud](https://claude.com/code-with-claude/session/sf-building-with-claude-on-google-cloud)

- Google Cloud에서 Claude Code를 설정하는 가장 쉬운 방법으로 **Application Default Credentials 기반 설정 마법사**가 쓰임
- 설정 마법사는 project, region, 사용 가능한 model을 감지하고 고정할 수 있음
- Google Cloud에서 Claude model을 쓰면 **토큰 기반 과금, provisioned throughput, API key 교체 부담 감소, project 정책 적용, project 안의 데이터 유지, regional/global endpoint**를 활용할 수 있음
- 데모는 PM, UI/UX designer, software engineer, security engineer, data/growth marketer라는 다섯 역할이 하나의 피드백 앱을 끝까지 만드는 흐름으로 진행됨
- PM은 손그림 wireframe을 Claude Code에 넣어 빠르게 시제품을 만듦
- UI/UX 단계에서는 plan mode로 Claude가 구현 전에 계획을 먼저 내놓게 함
- **Google Cloud developer knowledge API**와 **MCP server**는 최신 문서와 아키텍처 안내를 Claude Code에 연결함
- **Google Cloud Skills**는 Cloud Run API 배포, Cloud Run과 Firestore 연결 같은 개별 블록 구현을 돕는 데 쓰임
- **sub-agent**를 사용해 API, 수집 파이프라인, 대시보드 구현을 병렬로 진행함
- **security review prompt**는 OWASP 문제나 service account 권한을 확인하고 발견한 문제를 고친 뒤 Cloud Run에 배포함

### 세션 16 - [Getting more out of the Claude Platform](https://claude.com/code-with-claude/session/sf-getting-more-out-of-the-claude-platform)

- 운영용 에이전트 최적화의 우선순위는 **프롬프트 캐싱**, 문맥 공학(context engineering), **Advisor 전략**임
- **프롬프트 캐싱**은 입력 토큰 비용을 줄이고, 첫 토큰까지의 시간을 줄이며, 캐시된 토큰의 사용 한도 부담을 낮춤
- 캐시 적중률은 **90%대**가 목표로 다뤄짐
- 앞부분 프롬프트 안정성, 도구 정의 위치, 동적 값 삽입 위치가 모두 캐시에 영향을 줌
- **도구 검색 도구(tool search tool)** 는 필요한 도구 정의만 제때 불러와 문맥을 아낌
- 모든 도구를 처음부터 넣으면 문맥과 캐시에 모두 부담이 커짐
- **프로그래밍 방식 도구 호출(programmatic tool calling)** 은 많은 도구 결과를 그대로 넣지 않고 필요한 조각만 골라 문맥에 넣음
- **압축(compaction)** 은 오래된 대화와 도구 결과를 줄여 긴 작업을 이어가게 함
- **Advisor 전략**은 Sonnet이나 Haiku가 대부분의 작업을 하고, 중요한 판단이 필요할 때만 Opus를 조언자로 호출함
- 핵심은 모델을 더 많이 부르는 것이 아니라 어떤 문맥, 도구, 캐시 구조로 모델이 일하게 할지 설계하는 일임

### 세션 17 - [Evaluating and improving Replit Agent at scale](https://claude.com/code-with-claude/session/sf-evaluating-and-improving-replit-agent-at-scale)

- **Replit Agent**의 사용자는 framework나 test를 지정하지 않고 자연어만으로 동작하는 앱을 기대함
- 일반 코딩 벤치마크처럼 패치가 테스트를 통과하는지만 봐서는 **Replit Agent** 품질을 측정하기 어려움
- 평가는 앱이 사용자가 요청한 대로 동작하는지를 봐야 함
- Replit은 **오프라인 평가**와 **온라인 평가**를 함께 씀
- 오프라인 평가는 새 agent release 전 관문 역할을 하고, 온라인 평가는 실제 사용 뒤 빠르게 대응하는 데 쓰임
- **VibeBench**는 **20개의 실제 PRD**를 입력으로 빈 저장소에서 앱을 만들고, 자동 평가자가 브라우저에서 앱을 테스트하는 공개 벤치마크임
- 대부분의 모델은 자신이 만든 코드를 다시 확장할 때 더 어려워함
- 기능 사이에 테스트와 검증 단계를 둬야 흔들리는 기반 위에 계속 쌓는 일을 줄일 수 있음
- **Telescope**는 운영 실행 추적을 의미 기반으로 묶어 긴 꼬리 실패를 찾고, 문제를 분류하고, agent가 PR을 만들고, **VibeBench** 또는 A/B 테스트로 검증하는 내부 시스템임
- 평가는 마지막 출시 확인표가 아니라 에이전트를 매일 개선하는 **엔진**이 됨

### 세션 18 - [The capability curve](https://claude.com/code-with-claude/session/sf-the-capability-curve)

- Claude Code 사용자는 작년보다 **더 큰 신뢰**를 갖고 더 빠르게 배포함
- 발표 중 참석자 투표에서 많은 참석자가 Claude로 **10배, 5배, 2배 속도 향상**을 체감한다고 답함
- **SWE-bench Verified**에서 Sonnet 3.7은 약 **62%**, **Opus 4.7**은 **87%** 를 기록함
- **Opus 4.7**은 Sonnet 3.7이 실패하던 어려운 PR을 성공시킬 가능성이 **3배 이상** 높아짐
- 같은 프롬프트로 Claude.ai를 재현하는 데모에서 이전 모델은 일반적인 채팅 UI와 오류를 냈고, **Opus 4.7**은 Claude 색상, API 응답, 채팅 기록, 인라인 그래픽, dark mode를 구현함
- 향상된 영역은 **계획, 오류 복구, 긴 실행 중 주의 유지**임
- 새 모델은 먼저 계획하고, 실패하면 되돌아가며, 긴 문맥에서도 시스템 프롬프트와 목표를 더 잘 유지함
- 제품에 가까운 분포의 평가를 만들어야 실제 개선을 볼 수 있음
- 모델이 좋아질수록 기존 평가는 쉽게 포화되므로 평가도 계속 어려워져야 함
- 새 frontier model이 나오면 기존 보정 절차와 프롬프트를 다시 줄여볼 필요가 있음

### 세션 19 - [Giving coding agents their own computers: How Cursor built cloud agents](https://claude.com/code-with-claude/session/sf-giving-coding-agents-their-own-computers-how-cursor-built-cloud-agents)

- **Cursor**는 병목이 모델 지능보다 사람이 모델에게 충분한 도구, 문맥, 큰 목표를 주지 못하는 데 있다고 봄
- 사람 개발자를 온보딩하듯 에이전트도 컴퓨터, 개발 환경, 문서를 받아야 함
- **Cursor**의 onboarding agent는 저장소를 탐색하고 앱 실행법, 서비스, 환경 변수, 권한을 파악함
- **AnyDev CLI**는 에이전트가 서비스를 시작하고, 준비 상태를 기다리고, 상태를 확인하고, 테스트 계정 생성이나 로그인까지 처리하게 돕는 도구임
- 에이전트 개발 환경이 좋아질수록 개발자는 더 많은 cloud agent를 실행하고 더 큰 작업을 맡김
- 자율성의 기본 원칙은 에이전트에게 눈, 도구, 좋은 문맥을 주는 것임
- 에이전트는 사람처럼 앱 상태, 다른 에이전트 대화, 서비스 상태를 볼 수 있어야 함
- **Cursor**는 **computer use**를 코딩 다음의 중요한 기본 요소로 봄
- **Claude 4.7**은 agent가 직접 end-to-end 데모를 녹화해 기능을 검증하고, 사람이 코드 리뷰 전에 결과를 빠르게 이해하게 해줌
- **Cursor**는 **agent experience**를 별도 설계 대상으로 보고, 에이전트가 성가시거나 깨졌거나 혼란스러운 흐름을 만나면 **`work on the factory`** 이슈로 남기게 함
- 최종 목표는 사람이 A에서 D까지 손으로 이끄는 것이 아니라, **A에서 Z까지 풀 수 있는 시스템**을 만드는 것임

## 원문
- [원문](https://claude.com/code-with-claude/san-francisco)
- [GeekNews 토론](https://news.hada.io/topic?id=29493)

## My Note
<!-- 한 줄 코멘트 남기기 -->

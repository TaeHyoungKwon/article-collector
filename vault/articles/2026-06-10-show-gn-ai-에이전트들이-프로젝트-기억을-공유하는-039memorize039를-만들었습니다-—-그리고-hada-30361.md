---
category: AI
collected_at: '2026-06-10T22:42:47+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30361
id: hada-30361
matched_keywords:
- AI
- LLM
- Codex
read: false
recommend_score: 6.901
source: geeknews
tags:
- AI
- Other
- github.com/shakystar
title: 'Show GN: AI 에이전트들이 프로젝트 기억을 공유하는 &#039;memorize&#039;를 만들었습니다 — 그리고 도움이 필요합니다'
url: https://github.com/shakystar/memorize
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
혼자 개발하면서 매일 겪던 문제에서 시작했습니다. 벤더들이 매일같이 더 좋은 모델을 내놓고, 그 모델로 개발을 이어가려 갈아탈 때마다(Opus 4.7에서 GPT 5.5 같은 식으로) 프로젝트의 작업 기억은 따라오지 않았습니다. 에이전트마다 자기만의 메모리 사일로를 쌓는 동안, 저는 끊어진 컨텍스트를 매번 손으로 되살려야 했습니다. 에이전트들의 초기 메모리 기능은 너무 빈약해서 세션이 끝나면 컨텍스트가 죽었고, 한 머신에 갇혀 있어서 데스크톱에서 하던 작업은 노트북으로 이어지지 않았습니다.

프로젝트에는 프로젝트의 기억이 필요합니다. 그래서 만들었습니다: 프로젝트 자체가 기억을 갖게 하는 로컬 우선 오픈소스입니다.

**기술적으로 자신 있는 부분들**

- 뇌의 이중 학습계(CLS)를 차용한 2층 메모리 — 작업 중엔 LLM 없이 싸게 관측만 캡처(해마), 세션 경계에서 백그라운드 통합(신피질). 망각은 삭제가 아니라 인출 시점 점수 경쟁(중요도 × 반감기 14일 최신성 × 작업 관련성)으로만 일어나고, 어떤 기억도 지워지지 않습니다.
- API 키 제로 — 통합용 LLM이 따로 필요 없습니다. 이미 로그인된 claude -p / codex exec를 그대로 띄웁니다. 에이전트가 자기 자신을 써서 자기 기억을 정리하는 구조인데, 이때 생기는 무한 재귀(통합→훅 발화→통합→…)는 환경 변수 가드로 끊습니다.
- 유실 없는 통합 — 워터마크가 이벤트 영속화 후에만 전진해서, LLM 타임아웃이나 파싱 실패가 나면 다음 경계가 같은 구간을 재시도합니다. 워터마크 자체가 날아가도 출처 기반 dedup이 중복 통합을 막습니다.
- 서버 없는 크로스 머신 수렴 — append-only 이벤트 로그를 동기화하면, 시계 동기화 없이 내용 기반 결정론적 규칙만으로 모든 머신이 같은 상태로 수렴합니다. 두 머신이 동시에 같은 구간을 통합해도 모든 복제본이 같은 승자를 뽑습니다.
- 모순 감지에서 임베딩을 믿지 않음 — 코사인 유사도는 부정문에 눈이 멉니다("머지해라"와 "머지하지 마라"는 거의 같은 벡터). 그래서 유사도는 후보 회수까지만 쓰고, 판정은 LLM이 합니다. 진 기억은 삭제가 아니라 유효 기간이 닫혀서 "그때는 참이었다"가 복원 가능합니다.
- 병렬 세션 실시간 공유 — 같은 프로젝트에서 도는 세션끼리 서로의 작업을 보고, 같은 파일을 만지면 충돌 경고가 뜹니다.
- 스키마를 이론이 아니라 계측으로 진화 — 기억 분류 체계를 바꿀지를, 기억마다 붙는 관찰 전용 수명 필드와 행동 텔레메트리(언제 주입됐나, 언제 무효화됐나)를 몇 주 모아서 데이터로 결정합니다. 이 논쟁 전체가 저장소 Discussions에 공개돼 있습니다.

**왜 지금 공개하나**

솔직히 더 완숙하게 내고 싶었습니다. 그런데 OpenAI가 dreaming 같은 메모리 기능을 내놓는 걸 보면서 생각이 바뀌었습니다 — 같은 문제를 거대 벤더가 파기 시작했다는 건 방향이 맞다는 뜻이고, 벤더 안에 갇힌 기억이 표준이 되기 전에 벤더 중립적인 대안이 존재해야 한다고 생각했습니다. 그래서 지금 공개합니다.

**어디까지 가고 싶은가**

Fable 5급 모델이 나오면서 에이전트들은 이제 서로 협력할 수 있는 수준이 됐는데, 협력할 공유 인프라가 없습니다. 길게는 Git이 코드에 해준 것을 에이전트의 기억과 협업에 해주는 공익적 플랫폼을 만들고 싶습니다. 돈이 없어서 서버부터 시작할 수는 없었고 - 그 제약 덕분에 오히려 서버 없이도 수렴하는 로컬 우선 설계가 나왔습니다. 지금은 그 첫 조각인 "로컬에서 프로젝트 기억 공유"가 완전히 동작합니다. 실제로 이 프로젝트의 설계 토론, 구현, 오늘 새벽의 배포까지 상당 부분을 에이전트와 함께 진행했습니다 — 이 도구가 만들고 싶은 협업 방식 그대로요.

**구체적으로 도움이 필요한 것**

1. 써보고 깨지는 지점 제보 — 한 줄 설치 후 이슈로. 오늘 출시 전 검증에서만 설치 스크립트 버그 2개(PowerShell 5.1 따옴표, Linux EACCES)를 잡았는데, 분명 더 있습니다.
2. 다른 에이전트 어댑터 — Cursor, Gemini CLI, Windsurf 쪽 훅 구조를 아시는 분.
3. 기억 분류 체계 논쟁 참여 — "기억의 종류란 무엇인가"를 데이터로 결정하는 Discussions가 열려 있습니다.

설치는 한 줄입니다 (Windows는 README의 PowerShell 명령 참고):

curl -fsSL [https://raw.githubusercontent.com/shakystar/memorize/…](https://raw.githubusercontent.com/shakystar/memorize/main/scripts/install.sh) | sh

또는 Claude/Codex 세션에 한 줄: "Set up memorize in this project. Follow  
[https://github.com/shakystar/memorize/…](https://github.com/shakystar/memorize/blob/main/guides/AI_SETUP.md");

저장소: <https://github.com/shakystar/memorize> · 한국어 README  
(<https://github.com/shakystar/memorize/blob/main/docs/i18n/README.ko.md>) · 설계 문서  
(<https://github.com/shakystar/memorize/blob/main/docs/ARCHITECTURE.md>)

AGPL, 전부 로컬 저장, 텔레메트리 없음. 어떤 피드백이든 환영합니다.

## 원문
- [원문](https://github.com/shakystar/memorize)
- [GeekNews 토론](https://news.hada.io/topic?id=30361)

## My Note
<!-- 한 줄 코멘트 남기기 -->

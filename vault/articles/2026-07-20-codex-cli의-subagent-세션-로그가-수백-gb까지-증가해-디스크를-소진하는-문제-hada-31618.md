---
category: AI
collected_at: '2026-07-20T21:22:00+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31618
id: hada-31618
matched_keywords:
- AI
- Codex
read: false
recommend_score: 5.307
source: geeknews
tags:
- AI
- Other
- github.com/openai
title: Codex CLI의 Subagent 세션 로그가 수백 GB까지 증가해 디스크를 소진하는 문제
url: https://github.com/openai/codex/issues/34061
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Codex CLI가 Resume된 장기 세션에서 Subagent를 반복 생성할 때, `~/.codex/sessions` 아래의 JSONL 세션 파일이 비정상적으로 증가하는 문제가 보고됨
- 공개 사례에서는 하나의 Resume된 부모 세션에서 2,393개의 Subagent 세션 파일이 생성됐으며, 이 파일들이 약 731.5GiB를 차지함
- 전체 Codex 세션 데이터는 약 755GiB까지 증가했고, 1.8TiB APFS 볼륨의 사용량이 99~100%에 도달함
- 짧은 Subagent 세션에서도 수십만 개의 이벤트가 기록됐으며, 다른 세션에서는 `compacted` 이력과 Tool output이 수백 MB 단위로 반복 저장됨
- 문제는 최신 사례의 Codex CLI 0.144.6에서도 확인됐으며, 관련 GitHub 이슈는 2026년 7월 20일 현재 열려 있음

### 문제의 증상

Codex CLI는 세션을 다시 열 수 있도록 다음 경로에 대화와 실행 이력을 JSONL 형식으로 저장함.

```
~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl
```

2026년 7월 18일 등록된 사례에서는 `~/.codex` 전체가 약 760GiB, 그중 `~/.codex/sessions`가 약 755GiB를 사용했으며, 7월 세션만 약 734GiB를 차지했음.

```
760G  ~/.codex  
755G  ~/.codex/sessions  
734G  ~/.codex/sessions/2026/07
```

이 데이터는 캐시가 아니라 `codex resume`에 사용되는 세션 이력이므로, 파일을 삭제하면 과거 세션을 다시 열 수 없게 될 가능성이 있음. 신고 당시에도 여러 Codex 프로세스가 해당 JSONL 파일을 계속 열어 둔 상태였음.

### 얼마나 빠르게 증가했나

해당 사례의 7월 디렉터리에는 약 2,931개의 세션 파일이 있었고, 그중 797개가 각각 400MiB를 초과했음. 7월 11일에는 하루 동안 약 109.1GiB, 7월 12일에는 약 149.2GiB의 세션 데이터가 생성된 것으로 집계됨.

```
날짜       세션 파일     400MiB 초과     대략적인 용량  
7월 10일       50             0              2.8GiB  
7월 11일      473             0            109.1GiB  
7월 12일      506             0            149.2GiB  
7월 15일      340           265            108.6GiB  
7월 16일      355           263            109.0GiB  
7월 17일      300           189             81.7GiB
```

용량의 대부분은 하나의 Resume된 부모 세션과 연결돼 있었음. 이 부모 세션은 2,393개의 Subagent JSONL 파일을 생성했고, 이들의 논리적 크기는 합계 약 731.5GiB였음. 조사 시점에 부모 `codex resume` 프로세스는 약 23시간 동안 실행 중이었음.

### 어떤 workload에서 발생했나

보고된 workflow는 다음과 같음.

- 로컬 프로젝트에서 Codex TUI 실행
- Subagent 또는 협업 기능을 사용하는 장기 세션 작업
- 기존 부모 세션을 `codex resume <thread-id>`로 재개
- Resume된 프로세스를 여러 시간 동안 계속 실행
- 부모 세션이 depth 1의 Subagent를 반복 생성

이 workflow에서 하루 수백 개의 자식 JSONL 파일이 생성됐고, 다수 파일이 몇 분 안에 400~500MiB까지 증가했음. 다만 신고자는 이를 최소 재현 절차가 아니라 실제 환경에서 관찰된 재현 workflow라고 명시함.

따라서 현재 공개 자료로 확인되는 주요 증폭 조건은 다음 조합임.

```
장시간 실행되는 부모 세션  
+ codex resume  
+ 반복적인 Subagent 생성  
+ Context Compaction  
+ Tool output 및 세션 이벤트의 영구 저장
```

이 조합은 공개 사례의 데이터로 확인되지만, 각 요소 중 어느 하나만으로 항상 문제가 발생하는지는 아직 입증되지 않았음.

### 단일 파일 내부에서는 무엇이 증가했나

대표 Subagent 하나는 약 3분 19초 동안 실행됐지만, 483,714,063바이트와 353,255개의 JSONL 레코드를 기록했음. 이는 초당 약 1,770개의 레코드와 약 2.31MiB의 기록량에 해당함.

이 파일에서 큰 비중을 차지한 레코드는 다음과 같았음.

```
event_msg/token_count        185,461개    약 139.3MB  
compacted                      1,618개    약 121.6MB  
event_msg/patch_apply_end     36,295개    약 110.7MB  
event_msg/agent_message      104,653개     약 41.6MB  
response_item/message          9,947개     약 34.4MB  
world_state                      607개     약 18.6MB  
turn_context                   5,322개     약 11.0MB
```

하나의 거대한 JSON 레코드가 파일 대부분을 차지한 것이 아니라, 짧은 실행 시간 동안 여러 종류의 이벤트가 수천~수십만 번 기록된 형태였음. 신고자는 이를 심각한 event amplification으로 분석함.

다른 대표 파일은 약 925.6MB였으며, `compacted` 레코드 175개가 약 571.6MB, `custom_tool_call_output` 27,848개가 약 211.7MB를 차지했음. 이 파일은 이벤트 개수뿐 아니라 큰 Compaction 및 Tool output payload의 반복 보존도 용량 증가에 기여한다는 근거로 제시됨.

### 발생 원인은 무엇인가

현재 GitHub 이슈에는 OpenAI가 확정한 Root Cause Analysis가 게시돼 있지 않음. 따라서 다음 내용은 세션 파일을 조사한 신고자의 데이터에서 도출되는 추정 원인임.

#### 1. Subagent별 이벤트 증폭

3분가량 실행된 Subagent 하나에 `token_count` 18만여 개, `agent_message` 10만여 개, `patch_apply_end` 3만여 개가 저장됐음. 정상적인 사용자-visible activity보다 많은 이벤트가 자식 세션 writer로 전달되거나 반복 기록됐을 가능성이 제기됨.

#### 2. Compaction history의 반복 저장

큰 세션에서는 `compacted` 레코드가 파일 대부분을 차지했음. 별도의 Codex Issue #24948에서도 Context Compaction의 `replacement_history`와 원본 Tool output이 반복 저장되면서 단일 JSONL이 732MB, 전체 sessions 디렉터리가 약 91GB까지 증가한 사례가 보고됨. 해당 이슈는 Codex CLI 0.118.0과 macOS arm64 환경에서 재현됐으며 2026년 5월 28일 등록됨.

#### 3. Resume 시 과거 이력의 중복 materialization

Windows Codex App의 별도 Issue #29531에서는 2GB 이상으로 커진 기존 세션을 Resume하자, 새로운 날짜 디렉터리에 다시 2.3~2.4GB 크기의 rollout 파일들이 생성된 사례가 보고됨. 신고자는 새 파일이 증분 이벤트만 기록하지 않고 기존 historical context를 복사하거나 replay하는 것으로 추정함.

#### 4. Subagent 파일별 부모 상태 또는 출력의 중복

Issue #34061에서는 하나의 부모 세션에서 생성된 2,393개의 자식 세션이 약 731.5GiB를 차지했고, 자식 파일에서 `compacted`, Tool output 및 고빈도 이벤트가 반복 관찰됨. 이를 바탕으로 부모 상태나 이벤트 stream이 Subagent별 JSONL에 중복 기록되는 것이 핵심 증폭 요인 중 하나로 추정됨. 이는 현재 공개 데이터를 이용한 추론이며, OpenAI가 확정한 원인은 아님.

### 현재 수정 상태

가장 큰 Subagent 디스크 사용 문제를 다루는 Issue #34061은 2026년 7월 20일 현재 Open 상태이며, 이슈에 표시된 재현 버전은 Codex CLI 0.144.6임.

Compaction 및 Tool output 문제를 다루는 Issue #24948도 현재 Open 상태이며, Resume 중복 문제를 다루는 Issue #29531 역시 Open 상태임.

따라서 현재 공개된 이슈 상태만 기준으로 하면, 세션 JSONL 증가 문제 전체가 해결됐다고 볼 수 있는 정식 릴리스는 확인되지 않음. 각각의 이슈가 동일한 코드 결함에서 비롯됐는지, 여러 persistence 문제가 결합한 것인지도 아직 확정되지 않았음.

### 확인 방법

전체 세션 용량 확인:

```
du -sh ~/.codex/sessions
```

연월별 용량 확인:

```
du -sh ~/.codex/sessions/*/*
```

가장 큰 JSONL 파일 확인:

```
find ~/.codex/sessions \  
  -type f \  
  -name '*.jsonl' \  
  -exec du -h {} + |  
sort -hr |  
head -30
```

월별 파일 개수 확인:

```
find ~/.codex/sessions/2026/07 \  
  -type f \  
  -name '*.jsonl' |  
wc -l
```

Issue #34061과 유사한 경우에는 특정 월의 파일 수가 급증하거나, 수백 MB 크기의 자식 세션 파일이 수백~수천 개 발견될 수 있음.

### 임시 대응

공식 수정이 확인되기 전에는 다음 workload를 줄이는 것이 합리적인 임시 대응임.

- 하나의 부모 세션을 장시간 `codex resume`으로 유지하지 않기
- Resume된 장기 세션에서 Subagent를 대량으로 생성하지 않기
- 대형 명령 출력을 그대로 context에 반환하지 않고 파일로 저장한 뒤 필요한 부분만 조회하기
- `~/.codex/sessions`의 월별 용량과 대형 JSONL 파일을 주기적으로 확인하기

이는 Issue #24948, #29531, #34061에서 관찰된 증폭 조건을 피하기 위한 예방책이며, 공식적으로 검증된 workaround는 아님.

세션 파일을 삭제하면 디스크 공간은 회수할 수 있지만, 해당 세션을 `codex resume`으로 다시 열지 못할 가능성이 있음. Codex 프로세스를 먼저 종료하고 필요한 세션을 백업한 뒤 삭제하는 편이 안전함.

### 관련된 별도 이슈: SQLite 피드백 로그 쓰기 증폭

이 문제는 GeekNews에 소개된 [`logs_2.sqlite` 과도한 로깅 문제](https://news.hada.io/topic?id=30738)와 저장 위치 및 역할이 다름.

기존 이슈는 다음 파일에 글로벌 TRACE 수준의 diagnostic 및 feedback 로그를 지속 저장하면서 SSD 쓰기량을 증폭시킨 문제였음.

```
~/.codex/logs_2.sqlite  
~/.codex/logs_2.sqlite-wal  
~/.codex/logs_2.sqlite-shm
```

해당 문제는 2026년 6월 14일 GitHub Issue #28224로 보고됐으며, WebSocket 이벤트 및 노이즈 로그를 줄이는 PR이 병합돼 약 85%의 로그가 감소한 것으로 정리됨. 일부 수정은 Codex 0.142.0에 포함됐고 추가 수정은 0.143.0 릴리스 대상으로 기록됨.

반면 이번 문제는 Resume 가능한 세션 이력을 저장하는 `~/.codex/sessions/**/rollout-*.jsonl`이 대상이며, Context Compaction, Resume 및 Subagent session persistence가 주요 증폭 조건으로 관찰됨. SQLite feedback log 수정만으로 session JSONL 문제가 해결됐다는 근거는 없음.

### 요약

Codex CLI의 세션 저장소는 장시간 Resume된 부모 세션이 Subagent를 반복 생성하는 workload에서 비정상적으로 증가할 수 있음. 가장 큰 공개 사례에서는 하나의 부모 세션에서 생성된 2,393개의 자식 세션이 약 731.5GiB를 차지했고, 전체 sessions 디렉터리는 약 755GiB까지 증가함.

세션 내부에서는 짧은 시간에 수십만 개의 이벤트가 기록되는 event amplification과, `compacted` history 및 Tool output의 반복 보존이 함께 관찰됨. Resume 시 기존 multi-GB history가 새 rollout 파일에 다시 생성되는 별도 사례도 보고됨.

문제는 macOS Codex CLI에서 가장 큰 규모로 보고됐지만 Windows Codex App에서도 유사한 session duplication이 확인됐으며, 2026년 7월 20일 현재 주요 관련 이슈들은 열려 있음. 공식 수정이 확인되기 전까지는 장기 Resume와 대량 Subagent 사용을 제한하고 `~/.codex/sessions`의 크기를 주기적으로 확인할 필요가 있음.

## 원문
- [원문](https://github.com/openai/codex/issues/34061)
- [GeekNews 토론](https://news.hada.io/topic?id=31618)

## My Note
<!-- 한 줄 코멘트 남기기 -->

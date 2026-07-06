---
category: Dev Tools
collected_at: '2026-07-06T21:57:23+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31178
id: hada-31178
matched_keywords:
- Claude Code
read: false
recommend_score: 2.693
source: geeknews
tags:
- Dev Tools
- Other
- github.com/JungHoonGhae
title: 'Show GN: k-vote-cli : 한국 선거 공개 데이터를 API 키 없이 한 명령으로 받는 CLI'
url: https://github.com/JungHoonGhae/k-vote-cli
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
개표결과·여론조사·투표율은 법에 따라 공개되어 있지만, 직접 받아보면 접근성이 좋지 않습니다.

선거통계시스템(info.nec.go.kr)은 robots.txt로 자동 접근을 전면 차단하고, 파일은 EUC-KR 인코딩에 선거마다 엑셀 양식이 제각각이고, 여론조사는 공식 API 없이 게시판 PDF뿐이고, OpenAPI는 데이터마다 활용신청·인증키 발급이 필요합니다.

이미 있는 데이터라도 접근성을 높여보자는 취지로 만들었습니다. 선관위 공식 배포 채널(data.go.kr 파일 데이터)만 사용하고, robots로 막힌 곳은 우회하지 않습니다.

주요 기능:

- kvote nec corpus --normalize — 역대 주요 개표결과(대선 16·17·21대, 총선·비례, 지방 5~8회)를 동시 다운로드하고 투표구 단위 JSONL로 정규화. EUC-KR 디코딩, 동명 투표구 중복, 본투표/사전투표 분리 처리 포함
- kvote nesdc sync / bulk — 여론조사 전수 수집, 정당지지율 누적 1,400건+ 시계열(2023.10~), 표본 구성 교차표(성별·연령·지역 × 완료/가중)
- kvote nec turnout-analysis — 성별·연령대별 투표율 정규화 (개표결과에 없는 인구통계 축)
- kvote db / kvote mcp — 로컬 SQLite 적재 + read-only SQL 질의, MCP 서버 내장이라 Claude Code 같은 에이전트가 탐색→수집→SQL까지 직접 수행
- 인증키가 필요한 OpenAPI는 kvote api login/apply로 활용신청 자동화

설계 원칙은 하나입니다. 원자료를 그대로 보존하고, 더하는 것은 정의가 명시된 표준 계산값(투표율·득표율·유효표)뿐. 어떤 해석이나 판단도 넣지 않았습니다. 같은 명령을 실행하면 누구에게나 같은 데이터가 나옵니다.

Go 단일 바이너리(cgo 없음), MIT 라이선스, macOS/Linux/Windows. Homebrew와 go install로 설치할 수 있습니다. 일부 기능(여론조사 수집, 데이터셋 검색 경로)은 포털 HTML 구조에 의존하며, 깨짐은 kvote doctor로 점검합니다.

## 원문
- [원문](https://github.com/JungHoonGhae/k-vote-cli)
- [GeekNews 토론](https://news.hada.io/topic?id=31178)

## My Note
<!-- 한 줄 코멘트 남기기 -->

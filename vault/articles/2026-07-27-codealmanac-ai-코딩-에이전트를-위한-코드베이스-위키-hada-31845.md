---
category: AI
collected_at: '2026-07-27T09:31:01+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=31845
id: hada-31845
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 7.386
recommended_on: '2026-07-28'
source: geeknews
tags:
- AI
- Other
- github.com/AlmanacCode
title: CodeAlmanac - AI 코딩 에이전트를 위한 코드베이스 위키
url: https://github.com/AlmanacCode/codealmanac/
---

## TL;DR
- 이 글은 AI 코딩 에이전트를 위한 코드베이스 위키인 CodeAlmanac의 기능과 운영 방식을 다룬다.
- CodeAlmanac은 코드 외에도 맥락과 결정을 기록하여 AI 에이전트에게 풍부한 정보를 제공하며, 로컬에서 지속적으로 업데이트된다.
- 이를 통해 개발자는 AI와 효율적으로 협업하며 코드의 흐름과 과거 결정을 명확히 이해할 수 있다.

## GeekNews 요약
- 코드만으로는 담을 수 없는 **결정, 흐름, 불변 조건, 함정(gotchas)** 을 기록해 AI 에이전트에게 맥락을 제공하는 살아있는 위키
  - 시스템이 왜 지금의 형태인지, 과거에 무엇이 깨졌는지, 워크플로가 파일/서비스를 어떻게 가로지르는지 기록
- 위키는 저장소 안의 **마크다운 파일**로 저장되며, 로컬 인덱싱 후 코드처럼 **Git에서 리뷰** 가능
- 에이전트와 사람이 **동일한 로컬 읽기 명령** 사용: `search`, `show`, `topics`, `health`, `validate`
  - `search --mentions src/checkout/` 파일 경로 기준 검색 지원, `--wiki <name>` 으로 다른 위키 조회 가능
- 위키를 지속적으로 업데이트하는 라이프사이클 작업은 **build / ingest / garden** 세 가지 명시적 에이전트로 실행
  - 별도로 공개된 **[Yoke SDK](https://github.com/AlmanacCode/Yoke)** 이용
  - `ingest`: 파일, 디렉터리, Git diff, 커밋 범위, GitHub PR/이슈, URL, 로컬 에이전트 트랜스크립트를 위키로 통합
  - `garden`: 오래된 페이지, 약한 링크, 토픽, 중복 페이지 등 정리
- 유지보수 명령을 기억하지 않아도 되도록 **로컬 macOS launchd 백그라운드 작업** 3종 제공
  - Sync(5시간 마다): 최근 Codex/Claude 대화를 스캔해 관련 위키에 ingest 작업으로 큐잉
  - Garden(24시간 마다): 등록된 모든 위키의 노후/중복/연결 부실 지식 검토
  - Update(24시간 마다): 안전한 시점에만 CLI 자동 업데이트, 수명주기 작업 진행 중에는 건너뜀
- 호스팅 서비스나 클라우드 동기화가 아닌 **완전 로컬 실행**, 로그는 `~/.codealmanac/logs/` 에 저장
- 실행 이력은 로컬 잡 레코드로 남아 **터미널을 닫아도 조회 가능**
  - `jobs`, `jobs show`, `jobs logs`, `jobs attach`, `jobs cancel`
  - `--json` 으로 스크립트 연동 가능
- Provider는 `almanac-yoke`를 단일 창구로 이용, Codex는 app-server, Claude는 Python Agent SDK 사용
  - 기존 Codex/Claude Code **OAuth 세션 재사용**
- `serve` 로 뜨는 로컬 뷰어는 **읽기 전용**, 페이지/검색/토픽/백링크/파일 참조 내비게이션 렌더링
- 라이프사이클 에이전트는 광범위한 비대화형 파일시스템 권한으로 동작함
  - **`almanac/` 폴더는 OS 샌드박스가 아닌 지침/커밋 정책**이므로 신뢰 가능한 저장소에서만 실행 필요
- 텔레메트리는 선택 사항. 코드/경로/프롬프트/트랜스크립트/자격 증명은 전송하지 않고 GeoIP 비활성화, `DO_NOT_TRACK=1` 로도 차단 가능
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/AlmanacCode/codealmanac/)
- [GeekNews 토론](https://news.hada.io/topic?id=31845)

## My Note
<!-- 한 줄 코멘트 남기기 -->

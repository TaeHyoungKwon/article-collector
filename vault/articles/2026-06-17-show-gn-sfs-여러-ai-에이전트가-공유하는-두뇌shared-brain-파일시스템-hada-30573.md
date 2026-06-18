---
category: AI
collected_at: '2026-06-17T16:24:55+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30573
id: hada-30573
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-06-17'
source: geeknews
tags:
- AI
- Other
- github.com/runbear-io
title: 'Show GN: sfs - 여러 AI 에이전트가 공유하는 두뇌(shared brain) 파일시스템'
url: https://github.com/runbear-io/sfs
---

## TL;DR
- 이 글은 여러 AI 에이전트가 공유하는 두뇌(shared brain) 파일시스템인 sfs에 대해 다룬다.
- sfs는 에이전트가 동일한 폴더에서 작업하여 파일 변경 내역을 추적하고, 일반 파일처럼 즉시 읽고 쓸 수 있도록 설계되었다.
- 독자는 AI 에이전트 간의 효율적인 작업 흐름과 데이터를 관리할 수 있는 방안을 마련할 수 있다.

## GeekNews 요약
안녕하세요. Claude Code, Codex 같은 AI 에이전트를 여러 기기/세션에서 돌리다 보니, 에이전트마다 컨텍스트가 따로 쌓이고, 어제 한 에이전트가 정리해 둔 내용을 오늘 다른 기기의 에이전트는 모른다는 게 답답해서 만들었습니다.

핵심 컨셉은 "여러 에이전트가 공유하는 두뇌 (shared brain)" 입니다.

여러 에이전트가 같은 폴더 (예: ./shared) 를 공유하면, 위키, 메모리 파일, 계획 문서, 작업 아티팩트가 모두 한 공유 두뇌에 모입니다. 한 에이전트가 적어둔 결정사항을 다른 기기/세션의 에이전트가 그대로 읽고, 누가 어떤 기기에서 언제 무엇을 바꿨는지 추적됩니다.

용례:

- Support agent와 Engineering agent가 함께 공유하는 고객 이슈 관련 맥락
- Mac mini와 Macbook에서 파일/폴더 변경 사항 공유
- 팀원들이 각자의 agent에서 공통으로 쌓아 올리는 회사 wiki (company brain)

sfs는 아무 폴더나 동기화 볼륨으로 마운트해 줍니다:

```
$ sfs mnt ./shared --remote s3://my-bucket/workspace
```

마운트된 폴더의 파일은 그냥 디스크 위의 실제 파일이라, 모든 에디터/도구/에이전트가 별도 통합 없이 바로 사용할 수 있습니다. 다른 기기에서 같은 remote로 mount하면 같은 파일이 따라옵니다.

처음엔 그냥 Google Drive 같은 걸 쓰면 되지 않나 싶었는데, 실제로 에이전트 워크스페이스로 써 보니 다음 문제가 있었습니다:

- Google Drive는 디스크 절약을 위해 로컬 파일을 수시로 오프로드해서, 에이전트가 파일을 읽으려 할 때마다 클라우드에서 다시 받아야 하는 경우가 빈번함
- 스트리밍 마운트 방식이라, Claude가 파일을 로드하는 중에 블로킹되는 경우가 잦음
- 애초에 AI 에이전트 워크플로우용으로 설계된 도구가 아님 (사람이 GUI에서 클릭해서 쓰는 걸 가정)

sfs는 모든 파일을 항상 로컬 디스크에 실제로 두고 (오프로드 없음), 백그라운드에서 동기화하기 때문에 에이전트는 일반 파일처럼 즉시 읽고 쓸 수 있습니다.

주요 특징:

- 클라우드 스토리지 연동: S3, GCS
- 변경 추적: `sfs log` 로 누가/언제/어느 기기에서 어떤 파일을 바꿨는지 확인. 콘텐츠 주소 기반 저장이라 덮어쓴/삭제한 파일 내용도 보존됨
- 오프라인 우선: 네트워크 없이도 폴더는 완전히 사용 가능, 복구되면 자동 푸시
- 충돌 안전: 동시 편집은 (lamport, time, device) 순서로 결정적 재생
- macOS, Linux

설치:

```
brew install runbear-io/tap/sfs
```

아직 초기 버전이라 피드백/이슈 환영합니다. 감사합니다!

## 원문
- [원문](https://github.com/runbear-io/sfs)
- [GeekNews 토론](https://news.hada.io/topic?id=30573)

## My Note
<!-- 한 줄 코멘트 남기기 -->

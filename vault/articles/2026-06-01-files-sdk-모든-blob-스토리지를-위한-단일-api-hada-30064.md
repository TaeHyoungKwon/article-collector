---
category: AI
collected_at: '2026-06-01T09:51:02+09:00'
geeknews_comments: 3
geeknews_score: 14
geeknews_url: https://news.hada.io/topic?id=30064
id: hada-30064
matched_keywords:
- AI
read: false
recommend_score: -994.876
recommended_on: '2026-06-01'
source: geeknews
tags:
- AI
- Other
- files-sdk.dev
title: Files SDK - 모든 blob 스토리지를 위한 단일 API
url: https://files-sdk.dev/
---

## TL;DR
- 이 글은 다양한 객체 및 blob 스토리지를 통합 관리할 수 있는 Files SDK를 소개한다.
- 이 SDK는 29종의 스토리지에 대해 40개 이상의 어댑터를 단일 인터페이스로 제공하여 유연성을 높인다.
- 사용자들은 이 SDK를 통해 다양한 스토리지 시스템을 간단하게 사용할 수 있으며, 개발 효율성을 크게 향상시킬 수 있다.

## GeekNews 요약
- "Write Once, Store Anywhere"
- S3, R2, GCS, Azure 등 29종의 객체/blob 스토리지를 **하나의 통합 SDK**로 처리
- **40개 이상의 어댑터**를 단일 인터페이스 뒤에 두고, 어댑터만 교체하면 모든 호출 지점을 그대로 유지 가능
- upload, download, head, exists, copy, move, list, delete를 **모든 어댑터에서 동일한 호출**로 처리
  - 네이티브 클라이언트가 필요할 때 빠져나가기 위한 **escape hatch** 제공
- 배열을 넘기면 제한된 동시성하에 배치 처리하고 listing은 async iterable로 순회처리함
- **AI 에이전트용 파일 도구**: Vercel AI SDK, OpenAI Agents, Claude 및 MCP에게 기능 제공
- 모든 메서드를 명령으로 사용가능한 **CLI**도 같이 제공
- 큰 body나 무제한 스트림을 여러 part로 분할 업로드하는 **병렬 multipart** 지원
- **콜백 하나**로 byte 단위 실시간 업로드 진행률 표시 가능
- ranged read가 **HTTP 206**에 매핑되어 video seek, 다운로드 재개, 파일 헤더 읽기 가능
- **onAction·onRetry·onError** 라이프사이클 훅을 생성자에서 한 번만 연결해두면 모든 어댑터의 모든 작업에서 발생
- `sync()`로 한 백엔드를 다른 백엔드에 미러링 가능, 변경된 것만 업로드하고 동일한 것은 건너뛰며 사라진 것은 정리함, **dry-run** 지원
- 각 어댑터의 네이티브 SDK는 **선택적 peer dependency**로 실제 사용하는 것만 설치됨
- [Repo - `haydenbleasel/files-sdk`](https://github.com/haydenbleasel/files-sdk)
- MIT 라이선스

## 원문
- [원문](https://files-sdk.dev/)
- [GeekNews 토론](https://news.hada.io/topic?id=30064)

## My Note
<!-- 한 줄 코멘트 남기기 -->

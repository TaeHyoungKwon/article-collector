---
category: AI
collected_at: '2026-07-13T10:01:24+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31375
id: hada-31375
matched_keywords:
- AI
- RAG
read: false
recommend_score: -995.099
recommended_on: '2026-07-13'
source: geeknews
tags:
- AI
- Other
- gist.github.com/cereblab
title: 'xAI Grok Build CLI가 xAI로 전송하는 데이터: 와이어 수준 분석'
url: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
---

## TL;DR
- 이 글은 xAI Grok Build CLI가 전송하는 데이터에 대한 와이어 수준 분석을 다룬다.
- Grok Build는 비밀값 및 Git 이력 포함한 전체 저장소를 마스킹 없이 전송했으며, HTTP 200으로 모든 저장 요청을 처리했다.
- 이는 사용자 데이터 보호 및 비밀 유출 문제에 대한 경각심을 높이며, xAI의 데이터 처리 방식에 우려를 제기한다.

## GeekNews 요약
- `grok 0.2.93`의 네트워크 트래픽을 직접 캡처한 결과, Grok Build는 읽은 파일을 **마스킹 없이 전송**하고 `session_state`로 저장했으며 테스트용 `.env` 비밀값도 두 경로에 그대로 포함했음
- 모델 요청이 에이전트가 읽은 파일을 보내는 것과 별개로, **모든 추적 파일과 Git 이력**을 담은 저장소 전체가 git bundle로 업로드됐고 열지 말라고 지정한 파일도 원문 그대로 복구됐음
- 12GB 무작위 파일 저장소에서 `/v1/responses` 요청은 총 192KB였지만 `/v1/storage` 전송량은 캡처 중단 시점까지 **5.10GiB**에 달해 약 27,800배 차이가 났으며, 모든 저장 요청이 HTTP 200을 반환했음
- 업로드 목적지는 Google Cloud Storage의 **`grok-code-session-traces` 버킷**이었고, “Improve the model”을 꺼도 `trace_upload_enabled: true`와 `upload_enabled: true`가 유지되며 전체 저장소 업로드가 계속됐음
- 실험은 데이터의 전송·수락·저장을 입증하지만 **모델 학습에 사용됐는지는 확인하지 못했으며**, `.gitignore` 파일과 모든 계정·설정 조합도 시험하지 않아 결과는 2026년 7월의 특정 버전에 한정됨

---

## 원문
- [원문](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)
- [GeekNews 토론](https://news.hada.io/topic?id=31375)

## My Note
<!-- 한 줄 코멘트 남기기 -->

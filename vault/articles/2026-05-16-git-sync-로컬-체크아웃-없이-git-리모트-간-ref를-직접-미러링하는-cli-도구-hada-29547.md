---
category: Other
collected_at: '2026-05-16T09:31:02+09:00'
geeknews_comments: 1
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=29547
id: hada-29547
matched_keywords: []
read: false
recommend_score: 2.154
source: geeknews
tags:
- Other
- github.com/entireio
title: git-sync - 로컬 체크아웃 없이 Git 리모트 간 ref를 직접 미러링하는 CLI 도구
url: https://github.com/entireio/git-sync
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **로컬 클론 필요없이** 소스 리모트에서 타겟 리모트로 ref와 오브젝트를 직접 스트리밍하며, 로컬 디스크에 저장소를 체크아웃하지 않음
- **Relay 전송 경로**로 소스 `upload-pack` 팩 데이터를 타겟 `receive-pack`으로 바로 흘려보내, 저장소 크기와 무관하게 메모리 사용량은 일정함
- relay가 불가능한 경우(force, prune, delete 등) **Materialized 폴백**으로 인메모리 `go-git` 스토어에 오브젝트를 fetch 후 팩파일 인코딩 및 푸시, `--materialized-max-objects`로 메모리 제한 가능
- `git-sync sync` 하나로 **빈 타겟 초기 시딩부터 지속적 동기화**까지 처리하며, `git-sync plan`으로 푸시 전 미리보기 가능
- `git-sync replicate`는 타겟 ref를 소스와 완전히 일치시키되, **로컬 materialize가 필요하면 실패** 처리하는 엄격 모드
- ref 생성, 업데이트, `--force` 강제 업데이트, `--prune` 삭제 등 **모든 ref 관리 액션** 지원
- 모든 액션을 푸시 전에 계획하고 **타입드 JSON 출력**을 제공해 CI/자동화 파이프라인에 바로 연결 가능
- Go 라이브러리로도 임베딩 가능하며, `Probe`, `Plan`, `Sync`, `Replicate` 등 **안정 API** 제공
- **단방향 전용**, SSH 미지원(Smart HTTP/HTTPS만), 데몬/감시 기능 없이 원샷 실행 방식
- MIT 라이선스

## 원문
- [원문](https://github.com/entireio/git-sync)
- [GeekNews 토론](https://news.hada.io/topic?id=29547)

## My Note
<!-- 한 줄 코멘트 남기기 -->

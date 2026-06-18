---
category: Other
collected_at: '2026-06-18T09:04:57+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30585
id: hada-30585
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- bobdahacker.com
title: 내 ID만 있으면 FIFA 월드컵 전체에 Rickroll을 틀 수 있었다
url: https://bobdahacker.com/blog/fifa-hack
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 공개 **FIFA Agent Platform** 가입만으로 FIFA의 Microsoft Entra 테넌트에 들어가 2026 FIFA World Cup 운영용 Football Data Platform과 방송 스트리밍 관리 기능까지 접근할 수 있었음
- 원인은 JWT의 `NO_ROLES` 상태를 프런트엔드만 확인하고, 백엔드 API가 역할을 강제하지 않은 **클라이언트 측 권한 검사**였음
- 노출된 Streaming Management 패널에는 경기별 5개 카메라 피드의 **RTMP ingest URL**, 프리뷰 manifest, 출력 URL, 스트림 키가 있었고 VLC에서 라이브 프리뷰 피드가 재생됨
- 접근 범위는 조회를 넘어 경기 스트림 시작·중지·예약, 라이브 통계·킥오프 시각·스코어·전술 라인업 등 일부 **쓰기 작업**까지 포함됐으며 Commentator Information System과 개발용 Azure Function App도 열려 있었음
- FIFA는 직접 응답하지 않았지만 제보 다음 날 서버가 `403`을 반환하도록 수정됐고, 연구자는 `security.txt`, 취약점 공개 정책, 버그 바운티, 서버 측 권한 검사를 요구함

---

## 원문
- [원문](https://bobdahacker.com/blog/fifa-hack)
- [GeekNews 토론](https://news.hada.io/topic?id=30585)

## My Note
<!-- 한 줄 코멘트 남기기 -->

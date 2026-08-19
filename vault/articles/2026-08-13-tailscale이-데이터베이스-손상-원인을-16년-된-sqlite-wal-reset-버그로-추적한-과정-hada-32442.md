---
category: AI
collected_at: '2026-08-13T02:38:46+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32442
id: hada-32442
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-08-19'
source: geeknews
tags:
- AI
- Other
- tailscale.com
title: Tailscale이 데이터베이스 손상 원인을 16년 된 SQLite WAL-Reset 버그로 추적한 과정
url: https://tailscale.com/blog/sqlite-wal-reset-bug
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 6개월간 발생한 **19건의 데이터베이스 손상**과 반복적인 제어 평면 장애를 조사한 끝에, SQLite 체크포인트와 쓰기 트랜잭션 사이의 희귀한 데이터 경쟁을 찾아냄
- WAL 페이지가 주 데이터베이스에 복사되지 않았는데도 체크포인트가 완료된 것으로 처리돼 데이터가 영구 소실됐으며, SQLite 개발진은 이를 **WAL-Reset 버그**로 명명함
- 재현 조건을 찾지 못해 운영 환경에 진단 도구를 배포하고, SQL 트랜잭션 로그와 `tmstmpvfs` VFS 추적으로 **사라진 쓰기**와 비정상적인 체크포인트 통계를 연결함
- 수정판인 **SQLite 3.52.0**은 부동소수점 변환 변화로 13개 데이터베이스에 거짓 손상 경고를 일으켜 철회됐고, WAL-Reset 수정만 담은 3.51.3과 자체 복구 인덱스를 지원하는 3.53.0으로 정리됨
- 문서화되고 지원되는 기능이라도 수동 체크포인트를 공격적으로 실행하는 **비표준 운용 방식**은 일반 설정보다 검증 범위가 좁으며, Tailscale은 복구 자동화와 백업 검증 체계를 강화함

---

## 원문
- [원문](https://tailscale.com/blog/sqlite-wal-reset-bug)
- [GeekNews 토론](https://news.hada.io/topic?id=32442)

## My Note
<!-- 한 줄 코멘트 남기기 -->

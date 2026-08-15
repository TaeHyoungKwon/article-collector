---
category: AI
collected_at: '2026-08-10T10:00:04+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32324
id: hada-32324
matched_keywords:
- AI
read: false
recommend_score: 3.099
recommended_on: '2026-08-15'
source: geeknews
tags:
- AI
- Other
- youtube.com
title: SQLite에서 배운 신뢰성의 교훈 - Richard Hipp [유튜브]
url: https://www.youtube.com/watch?v=V_qzqY1bb7I
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 장애가 잦던 Informix 서버를 우회해 디스크 데이터에 직접 접근하려는 필요에서 출발한 SQLite는 현재 **1조 개 이상**의 데이터베이스가 사용되는 것으로 추산되는 내장형 SQL 엔진으로 성장함
- 높은 신뢰성의 중심에는 기계어 수준의 모든 분기를 양방향으로 검증하는 **100% MCDC 테스트**, 의도적 오류 주입, 소스뿐 아니라 실제 배포 객체 코드까지 검사하는 원칙이 있음
- 대체 VFS·메모리 할당자·오류 시뮬레이션을 이용해 `malloc` 실패, I/O 오류, 스레드 생성 실패, 전원 차단을 재현하며 제품 자체를 처음부터 **테스트 가능하게 설계**함
- TH3가 2009년 100% MCDC를 달성한 뒤 Android 등에서 들어오던 버그가 크게 줄었고, 세 명의 커미터만으로 대규모 리팩터링을 수행하면서 2009년 대비 성능을 **3배 이상** 높일 수 있었음
- MCDC만으로는 퍼징·의미론적 오류·AI가 만든 병적 입력을 모두 찾을 수 없으므로 테스트 체계도 계속 진화해야 하며, 테스트 코드가 제품보다 10배 크거나 소스의 10~20%가 테스트 전용이어도 불필요한 비용으로 봐서는 안 됨

---

## 원문
- [원문](https://www.youtube.com/watch?v=V_qzqY1bb7I)
- [GeekNews 토론](https://news.hada.io/topic?id=32324)

## My Note
<!-- 한 줄 코멘트 남기기 -->

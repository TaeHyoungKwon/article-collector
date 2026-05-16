---
category: Other
collected_at: '2026-05-16T09:47:57+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29550
id: hada-29550
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- tmctmt.com
title: Mullvad exit IP는 놀라울 정도로 식별 가능함
url: https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Mullvad**는 서버 하나에 여러 exit IP를 두지만, WireGuard 키 기반으로 결정적으로 배정해 접속마다 무작위로 바뀌지 않음
- 9개 서버에서 pubkey를 반복 변경해 모은 **3,650개 데이터 포인트**는 가능한 8.2조 개 조합 중 284개 조합에만 배정됨
- 각 서버의 exit IP는 풀 안에서 비슷한 **백분위 위치**에 놓이며, 한 조합은 여러 서버에서 대체로 81번째 백분위에 맞춰짐
- 원인은 pubkey나 터널 주소를 seed로 쓰고 풀 크기를 상한으로 넣는 **seed 기반 RNG**로 exit IP index를 고르는 구조로 보임
- IP 로그의 float 범위가 겹치면 서로 다른 Mullvad 서버를 써도 계정 간 상관관계가 가능해져 **익명성 위험**이 커짐

---

## 원문
- [원문](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/)
- [GeekNews 토론](https://news.hada.io/topic?id=29550)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-07-14T06:56:07+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31407
id: hada-31407
matched_keywords:
- AI
read: false
recommend_score: -996.693
recommended_on: '2026-07-14'
source: geeknews
tags:
- AI
- Other
- nebusec.ai
title: GhostLock, 15년간 모든 Linux 배포판에 존재한 스택 UAF
url: https://nebusec.ai/research/ionstack-part-2/
---

## TL;DR
- GhostLock(CVE-2026-43499)은 Linux 커널의 스택 UAF 취약점으로, 비특권 로컬 공격자가 루트 권한을 획득할 수 있다.
- 이 취약점은 스레드 간의 상호작용을 활용하여 해제된 스택 프레임을 가리키는 포인터를 남겨 공격자가 제어 흐름을 탈취하도록 한다.
- 패치되지 않은 모든 Linux 배포판은 이번 공격으로부터 보호하기 위해 최신 LTS로 업그레이드해야 할 필요성이 있다.

## GeekNews 요약
- **GhostLock(CVE-2026-43499)** 은 Linux 2.6.39에 도입돼 7.1에서 수정된 커널 취약점으로, 비특권 로컬 공격자가 일반적인 스레딩 시스템 호출만으로 스택 UAF를 일으켜 **루트 권한 획득과 컨테이너 탈출**에 이용할 수 있음
- Requeue-PI 프록시 경로의 `remove_waiter()`가 실제 대기 태스크 대신 `current`의 `pi_blocked_on`을 지워, 사용자 공간으로 복귀한 태스크에 **해제된 스택 프레임을 가리키는 포인터**가 남음
- 세 futex와 세 스레드로 PI 의존성 순환을 만들어 `-EDEADLK` 롤백을 유도하고, `PR_SET_MM_MAP`의 제어 가능한 스택 버퍼에 가짜 `rt_mutex_waiter`를 구성해 **제약된 포인터 쓰기**를 확보함
- 익스플로잇은 `prefetch`로 KASLR·physmap 기준 주소를 찾고 CPU entry area(CEA)에 가짜 구조체와 ROP 스택을 배치한 뒤, `inet6_protos[IPPROTO_UDP]`를 덮어 **IPv6 UDP 루프백 패킷으로 제어 흐름을 탈취**함
- 연구진은 **97% 안정적인 권한 상승·컨테이너 탈출** 익스플로잇으로 Google kernelCTF에서 $92,337을 받았으며, 패치되지 않은 모든 Linux 배포판은 최신 LTS로 업그레이드해야 함

---

## 원문
- [원문](https://nebusec.ai/research/ionstack-part-2/)
- [GeekNews 토론](https://news.hada.io/topic?id=31407)

## My Note
<!-- 한 줄 코멘트 남기기 -->

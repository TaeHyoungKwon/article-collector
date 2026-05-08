---
collected_at: '2026-05-08T09:08:18+09:00'
geeknews_comments: 2
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29275
id: hada-29275
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- openwall.com
title: 'Dirty Frag: 범용 Linux LPE(로컬 권한 상승) 취약점'
url: https://www.openwall.com/lists/oss-security/2026/05/07/8
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Dirty Frag
는
주요 Linux 배포판 전반에서 root 권한 획득을 가능하게 하는 범용 로컬 권한 상승 취약점
으로, 책임 있는 공개 일정과 엠바고가 깨져
패치와 CVE가 아직 없음
Dirty Pipe, Copy Fail과 같은 버그 클래스의 확장으로,
결정론적 로직 버그
이기 때문에 레이스 컨디션이 불필요하고 성공률이 매우 높음
취약점의 유효 수명은 약
9년
이며, Ubuntu, RHEL, Fedora, openSUSE 등 주요 배포판에서 테스트 완료
기존 Copy Fail 완화 조치(algif_aead 블랙리스트)를 적용한 시스템에서도 여전히
Dirty Frag에 취약
함
임시 완화책으로 배포판 패치가 나오기 전까지 취약점이 발생하는
esp4
,
esp6
,
rxrpc
모듈 제거 권고
개요
sk_buff
구조체의
frag
멤버를 오염시키는 버그 클래스로,
Dirty Pipe
와
Copy Fail
이 속한 동일 버그 클래스의 확장
xfrm-ESP Page-Cache Write
취약점과
RxRPC Page-Cache Write
취약점을 체이닝하여 주요 리눅스 배포판에서 루트 권한 획득 가능
결정론적 로직 버그로
타이밍 윈도우에 의존하지 않으며
, 레이스 컨디션 불필요
익스플로잇 실패 시에도
커널 패닉이 발생하지 않고
, 성공률이 매우 높음
두 취약점을 체이닝한 이유
xfrm-ESP Page-Cache Write는 Copy Fail과 유사한 강력한
임의 4바이트 STORE 프리미티브
를 제공하며 대부분의 배포판에 포함되어 있지만, 네임스페이스 생성 권한이 필요
Ubuntu는
AppArmor 정책
으로 비특권 유저 네임스페이스 생성을 차단하는 경우가 있어, 이 환경에서는 xfrm-ESP Page-Cache Write를 트리거할 수 없음
RxRPC Page-Cache Write는 네임스페이스 생성 권한이 불필요하지만,
rxrpc.ko
모듈 자체가 대부분의 배포판에 포함되어 있지 않음
다만 Ubuntu에서는
rxrpc.ko
모듈이
기본으로 로드
됨
두 취약점을 체이닝하면 각각의
맹점을 상호 보완
하여, 모든 주요 배포판에서 루트 권한 획득 가능
Copy Fail과의 관계
Copy Fail이 이 연구를 시작한
동기
xfrm-ESP Page-Cache Write는 Copy Fail과
동일한 싱크(sink)
를 공유하지만,
algif_aead
모듈의 가용 여부와 무관하게 트리거 가능
공개된 Copy Fail 완화 조치(
algif_aead 블랙리스트
)를 적용한 시스템에서도 Dirty Frag에 여전히 취약
영향 범위
xfrm-ESP Page-Cache Write: 커밋
cac2661c53f3
(2017-01-17)부터 upstream까지
RxRPC Page-Cache Write: 커밋
2dc334f1a63a
(2023-06)부터 upstream까지
취약점의
유효 수명은 약 9년
테스트 완료된 배포판 버전:
Ubuntu
24.04.4: 6.17.0-23-generic
RHEL
10.1: 6.12.0-124.49.1.el10_1.x86_64
openSUSE
Tumbleweed: 7.0.2-1-default
CentOS
Stream 10: 6.12.0-224.el10.x86_64
AlmaLinux
10: 6.12.0-124.52.3.el10_1.x86_64
Fedora
44: 6.19.14-300.fc44.x86_64
완화 조치
책임 있는 공개 일정과 엠바고가 깨져
어떤 배포판에도 패치가 존재하지 않음
임시 완화 조치로, 취약점이 발생하는 모듈을 제거하는 명령어 제공:
sh -c "printf 'install esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true"
esp4
,
esp6
,
rxrpc
모듈을
/etc/modprobe.d/dirtyfrag.conf
에
블랙리스트로 등록
하고 언로드
각 배포판이 패치를 백포트한 후 해당 업데이트 적용 필요
공개 경위
linux-distros@vs.openwall.org 메인테이너들과 협의 후, 그들의 요청에 따라 Dirty Frag 문서 공개
엠바고가
외부 요인으로 깨진 상태
이며, 현재 패치나 CVE가 존재하지 않음
PoC는 linux-distros와의 협의를 거쳐
정확한 정보 제공 목적
으로 공개되었으며, 허가되지 않은 시스템에서의 사용 금지

## 원문
- [원문](https://www.openwall.com/lists/oss-security/2026/05/07/8)
- [GeekNews 토론](https://news.hada.io/topic?id=29275)

## My Note
<!-- 한 줄 코멘트 남기기 -->

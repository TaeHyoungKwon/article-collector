---
category: Other
collected_at: '2026-05-31T18:35:26+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30045
id: hada-30045
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/kristapsdz
title: Openrsync - OpenBSD 팀의 rsync 구현
url: https://github.com/kristapsdz/openrsync
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **openrsync**는 [rsync](https://rsync.samba.org/)를 BSD(ISC) 라이선스로 구현한 시스템이며, 현재 OpenBSD base에 병합되어 있음
- 최신 rsync와 호환되며 테스트에는 **rsync 3.1.3**이 사용되지만, 프로토콜 27을 지원하면 동작 가능함
- rsync의 명령줄 인자 전체가 아니라 **일부 인자만** 받기 때문에, openrsync와 rsync를 함께 쓸 때는 양쪽에서 지원되는 플래그를 사용해야 함
- 공식 지원 운영체제는 **OpenBSD**이며, 다른 UNIX 시스템에서도 컴파일하고 실행할 수 있도록 이식성용 glue가 포함되어 있음
- 표준 문서는 매뉴얼 페이지이며, 프로토콜 세부사항은 [rsync(5)](https://github.com/kristapsdz/openrsync/blob/master/rsync.5)와 [rsyncd(5)](https://github.com/kristapsdz/openrsync/blob/master/rsyncd.5), 유틸리티 문서는 [openrsync(1)](https://github.com/kristapsdz/openrsync/blob/master/openrsync.1)에 있음
- 프로젝트는 OpenBSD용 [rpki-client(1)](https://medium.com/@jobsnijders/a-proposal-for-a-new-rpki-validator-openbsd-rpki-client-1-15b74e7a3f65)의 일부로 작성됐고, [NetNod](https://www.netnod.se), [IIS.SE](https://www.iis.se), [SUNET](https://www.sunet.se), [6connect](https://www.6connect.com)가 자금을 지원함
- 설치는 일반 UNIX 시스템에서 `./configure`, `make`, `make install`로 수행하며, 기존 rsync 설치와 충돌하지 않음
- rsync 알고리듬은 **sender**와 **receiver**로 나뉘며, sender가 소스 파일 목록과 메타데이터를 만들고 양쪽이 파일명을 사전순으로 정렬해 위치 기반으로 항목을 참조함
- 일반 파일 동기화는 파일 크기와 수정 시간이 같으면 건너뛰고, 다르면 고정 크기 블록마다 빠른 Adler-32형 4바이트 해시와 느린 MD4 16바이트 해시를 사용해 변경 데이터를 재구성함
- 블록 크기는 전체 파일 크기의 제곱근을 반올림한 값이 기본이며, 최소 크기는 **700 B**이고 제곱근 결과는 알 수 없는 이유로 8의 배수로 올림 처리됨
- 세션은 사용자가 실행하는 클라이언트와 원격에서 실행되는 서버 프로세스로 나뉘며, 서버는 [ssh(1)](https://man.openbsd.org/ssh.1)로 온디맨드 실행되거나 지속 실행 네트워크 데몬으로 동작함
- rsync의 generator가 별도 프로세스로 receiver 옆에서 동작하는 것과 달리, openrsync는 **generator와 receiver를 한 프로세스**로 합치고 이벤트 루프로 읽기·쓰기 요청에 대응함
- 보안 측면에서 OpenBSD의 [pledge(2)](https://man.openbsd.org/pledge.2)로 실행 모드별 시스템 작업을 제한하고, [unveil(2)](https://man.openbsd.org/unveil.2)로 목적지 디렉터리 이하의 파일시스템 접근만 허용함
- 서버 모드에서 MD4 해시 시드는 [time(3)](https://man.openbsd.org/time.3)이 아니라 [arc4random(3)](https://man.openbsd.org/arc4random.3)으로 생성됨
- Linux(glibc·musl), FreeBSD, NetBSD, Mac OS X, OmniOS에서 이식 가능하며 GitHub CI가 x86\_64, aarch64, s390x 아키텍처 테스트를 수행하지만, OpenBSD의 pledge와 unveil에 해당하는 보안 기능을 맞추는 일이 이식의 핵심 제약임

## 원문
- [원문](https://github.com/kristapsdz/openrsync)
- [GeekNews 토론](https://news.hada.io/topic?id=30045)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-19T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30623
id: hada-30623
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- github.com/momo5502
title: sogen - 고성능 Windows &amp; Linux 유저스페이스 에뮬레이터
url: https://github.com/momo5502/sogen
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **시스템콜(syscall) 수준** 에서 동작하는 고성능 윈도우/리눅스 유저스페이스 에뮬레이터로, 포괄적인 후킹을 통해 프로세스 실행 전반을 제어
- **보안 연구, 멀웨어 분석, DRM 연구** 등 프로세스 실행에 대한 세밀한 제어가 필요한 작업에 적합
- Windows API를 재구현하지 않고 **syscall 레벨**에서 동작해 기존 시스템 DLL을 그대로 활용 가능
- **C++** 로 작성되었으며 원하는 백엔드로 구동 가능: **[Unicorn Engine](https://github.com/unicorn-engine/unicorn), [icicle-emu](https://github.com/icicle-emu/icicle-emu), [Hyper-V(WHP)](https://learn.microsoft.com/en-us/virtualization/api/hypervisor-platform/hypervisor-platform)**
- **고급 메모리 관리**: Unicorn의 메모리 관리 위에 구축되어 reserved·committed 등 Windows 고유 메모리 타입 지원
- **완전한 PE 로딩 지원**: 실행 파일 및 DLL 로딩 처리, 적절한 메모리 매핑, 재배치(relocations), TLS 지원
- **예외 처리**: Windows 구조적 예외 처리(SEH) 구현, 예외 디스패처 및 언와인딩 지원
- **쓰레딩 지원**: 라운드 로빈(round-robin) 방식의 스케줄링 스레딩 모델 제공
- **State 관리**: 전체 상태 직렬화와 빠른 인메모리 스냅샷 모두 지원
- **디버깅 인터페이스**: GDB 시리얼 프로토콜 구현으로 IDA Pro, GDB, LLDB, VS Code 등과 연동 가능
- 멀웨어 분석 시에 호스트 격리가 완벽하지 않을 수 있어, **[브라우저 샌드박스 기반 웹 버전 사용](https://sogen.dev/#/playground)** 을 권장
- Python 으로 자동화 가능
  - `pip install sogen` 으로 설치
  - 에뮬레이터 실행, 콜백 등록, WinAPI 콜 인터셉트를 파이썬 안에서 바로 처리 가능

## 원문
- [원문](https://github.com/momo5502/sogen)
- [GeekNews 토론](https://news.hada.io/topic?id=30623)

## My Note
<!-- 한 줄 코멘트 남기기 -->

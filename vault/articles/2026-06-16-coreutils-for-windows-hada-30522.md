---
category: Other
collected_at: '2026-06-16T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30522
id: hada-30522
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/microsoft
title: Coreutils for Windows
url: https://github.com/microsoft/coreutils
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 윈도우에서 **UNIX 스타일 코어 유틸리티**를 네이티브로 실행해, 리눅스/맥/WSL에서 쓰던 동일한 명령과 파이프라인을 그대로 사용
- Microsoft가 관리하는 빌드로 **uutils/coreutils, findutils, grep**을 단일 **멀티콜 바이너리**로 묶음
  - 동일한 명령/플래그/파이프라인이 같은 방식으로 동작해, 기존 스크립트를 **변환 없이 이식** 가능
  - Linux/macOS/WSL/컨테이너/Windows 간 이동을 **마찰 없이** 만드는 것이 목표
- **PowerShell 7.4 이상** 필요(`~` 지원은 7.6 이상 권장)
  - 일부 명령은 CMD·PowerShell 내장 명령과 이름이 겹쳐 **PATH 순서**와 별칭 테이블에 따라 실행 여부 결정
  - 미제공 명령: `dir`/`expand`/`more`(내장 DOS 명령 충돌), `kill`(시그널 없음), `timeout`(`kill` 의존), `whoami`(Windows 내장 명령과 충돌)
  - `find` 와 `sort`는 원래 DOS 명령의 통합 포트, `hostname`은 Windows 내장 명령의 슈퍼셋
- **Windows의 환경 차이** 존재
  - `/dev/null` 대신 `NUL` 사용, **POSIX 시그널 미지원**(`Ctrl+C`만 동작)
  - 경로 구분자 `/`·`\` 모두 허용, 파일 권한은 POSIX 비트가 아닌 **ACL** 기반
  - CRLF 줄바꿈은 대부분 알아서(transparently) 처리되나 `uniq` 등 바이트 기반 동작에서 차이 가능
  - 심볼릭 링크 읽기는 그냥 되지만, 새 심볼릭 링크 생성은 **개발자 모드** 또는 권한 상승 터미널 필요
- POSIX 전용 개념(`chmod`, `chown`, `id`, `who` 등)과 Windows에서 불필요한 명령(`dircolors`, `shred`, `uname` 등)은 의도적으로 제외
- MIT 라이선스 : Rust + PowerShell + Inno Setup으로 구현

## 원문
- [원문](https://github.com/microsoft/coreutils)
- [GeekNews 토론](https://news.hada.io/topic?id=30522)

## My Note
<!-- 한 줄 코멘트 남기기 -->

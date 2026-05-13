---
category: Other
collected_at: '2026-05-13T21:59:27+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29472
id: hada-29472
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- oborona.zip
title: 'Show GN: Fly.Board - C로 만든 고성능 HTTP/3 블로그 엔진'
url: https://oborona.zip
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Spring의 복잡도와 WordPress의 무거움에 지친 개발자가 C11/C23으로 직접 구현한 블로그 엔진, **Fly.Board**입니다. HTTP/3(QUIC) over TLS 1.3 환경에서 단일 바이너리로 C10k를 소화하는 성능을 확인하여 공유합니다.

#### 핵심 특징

- **Minimalist Stack**: 자체 프레임워크(CWIST) 및 단일 바이너리 구성
- \*\*Pure SSR(Server-Side Rendering): 클라이언트에서의 렌더링 지연 최소화
- **LibTTAK**: C의 속도를 유지하면서 비동기 처리와 메모리 안전성을 보장하는 커스텀 메모리 관리 도구
- **High Performance**: Idle 상태에서 20MB, 10,000개 동시 연결 시에도 RSS 369MB 수준의 저지연 운영 가능
- **Modern Protocol**: 커스텀 C 스택 기반의 HTTP/3(QUIC) 및 TLS 1.3 지원

#### C10k 벤치마크 결과 (`/usr/bin/time -v` 측정)

- **동시 연결**: 10,000개 (24분 46초 유지)
- **메모리 점유**: 최대 RSS 약 369 MB (연결당 약 37KB)
- **I/O 효율**: Major page faults 0 (디스크 I/O 병목 없음)
- **데이터 안정성**: SIGINT 수신 시 NukeDB를 통해 89,208개의 FS output으로 데이터 안전 저장

#### 기존 스택과의 비교

- **WordPress**: PHP-FPM/MySQL 기반의 무거운 리소스 소모 및 다단 캐싱 필수
- **Pure SSR(Server-Side Rendering)**: 저사양 기기에서의 렌더링 지연 최소화
- **Spring Boot**: JVM 힙 및 DI 컨테이너로 인한 높은 초기 복잡도와 메모리 점유
- **Fly.Board**: 별도 캐싱 레이어 없이 1GB 미만 VPS에서도 여유로운 C10k 처리 가능

#### 아쉬운 점 및 향후 과제

- System time이 User time보다 높은 현상에 대한 Userspace 처리 효율 개선 필요
- 읽기 중심 벤치마크 외에 SQLite 기반 데이터 계층의 쓰기 부하(댓글/게시글 동시 작성) 검증 예정

**링크**

- **GitHub**: <https://github.com/gg582/fly.board>  
  기술적 완성도와 실용성 사이의 균형을 고민하며 만들었습니다. 저사양 VPS에서 개인 블로그를 운영하려는 개발자분들께 좋은 대안이 되길 바랍니다. 피드백 환영합니다!

## 원문
- [원문](https://oborona.zip)
- [GeekNews 토론](https://news.hada.io/topic?id=29472)

## My Note
<!-- 한 줄 코멘트 남기기 -->

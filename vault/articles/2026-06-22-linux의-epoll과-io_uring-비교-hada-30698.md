---
category: AI
collected_at: '2026-06-22T06:35:52+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30698
id: hada-30698
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-06-21'
source: geeknews
tags:
- AI
- Other
- sibexi.co
title: Linux의 epoll과 io_uring 비교
url: https://sibexi.co/posts/epoll-vs-io_uring/
---

## TL;DR
- 이 글은 Linux의 epoll과 io_uring의 성능과 구조적 차이를 비교한다.
- io_uring은 완료 모델을 사용해 I/O 작업을 효율적으로 처리하며, CPU 사용량을 고려할 때 epoll보다 더 적합하다.
- 최신 Linux 서버에서 새 프로젝트를 시작할 때 io_uring을 선택하는 것이 성능 향상에 기여할 수 있다.

## GeekNews 요약
- TinyGate 리버스 프록시는 워커 기반 구조에서 **epoll**로 바꾸며 성능을 끌어올렸지만, 이후 한계를 만나 **io\_uring**으로 다시 작성됨
- epoll은 I/O가 가능한 시점을 알려주는 **준비 상태 모델**이라 `epoll_wait` 뒤에 `read()`/`write()`를 별도로 호출해야 함
- io\_uring은 I/O 완료를 기준으로 움직이는 **완료 모델**이며, 애플리케이션과 커널이 공유 링 버퍼로 제출 큐와 완료 큐를 주고받음
- `io_uring_enter()`는 기본적으로 필요하지만 여러 작업을 한 번에 제출·회수할 수 있고, `IORING_SETUP_SQPOLL`은 syscall을 줄이는 대신 **CPU 사용량**을 비용으로 가짐
- kernel v5.1+를 쓰는 최신 Linux 서버에서 새 프로젝트를 시작한다면, epoll보다 **io\_uring**이 더 적합한 선택지로 평가됨

---

## 원문
- [원문](https://sibexi.co/posts/epoll-vs-io_uring/)
- [GeekNews 토론](https://news.hada.io/topic?id=30698)

## My Note
<!-- 한 줄 코멘트 남기기 -->

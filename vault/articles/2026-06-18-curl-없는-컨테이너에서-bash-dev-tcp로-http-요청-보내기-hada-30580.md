---
category: Other
collected_at: '2026-06-18T01:36:15+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30580
id: hada-30580
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- mareksuppa.com
title: curl 없는 컨테이너에서 Bash /dev/tcp로 HTTP 요청 보내기
url: https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 최소 컨테이너 이미지에는 **curl**이나 wget이 빠져 있는 경우가 많아, 패키지 설치 없이 내부 서비스 연결성을 확인할 우회 방법이 유용함
- Bash의 `/dev/tcp/host/port` 리다이렉션은 **TCP 소켓**을 열 수 있어, HTTP/1.1 요청 문자열을 직접 써 보내고 응답을 읽을 수 있음
- `/dev/tcp`는 파일시스템 경로가 아니라 **Bash 내부 기능**이므로 `ls /dev/tcp`나 다른 셸의 일반 파일 접근 방식으로는 동작하지 않음
- 이 방법은 리다이렉트, chunked 응답, 압축, 재시도, TLS를 처리하지 않는 **간단한 디버깅 기법**이며 `Connection: close` 없이는 `cat`이 대기할 수 있음
- 일상적인 HTTP 작업에는 curl이 맞지만, 도구를 추가하기 어려운 **작은 컨테이너**에서는 빠른 연결 확인에 충분함

---

## 원문
- [원문](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/)
- [GeekNews 토론](https://news.hada.io/topic?id=30580)

## My Note
<!-- 한 줄 코멘트 남기기 -->

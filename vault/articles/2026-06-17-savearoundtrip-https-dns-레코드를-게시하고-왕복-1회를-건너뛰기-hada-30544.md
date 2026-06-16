---
category: Other
collected_at: '2026-06-17T00:01:49+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30544
id: hada-30544
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- savearoundtrip.com
title: 'savearoundtrip: HTTPS DNS 레코드를 게시하고 왕복 1회를 건너뛰기'
url: https://savearoundtrip.com/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 웹사이트가 **HTTPS DNS 레코드**에 HTTP/3 지원을 게시하면 브라우저가 첫 연결부터 QUIC/HTTP/3를 사용할 수 있어 연결 왕복 1회를 줄일 수 있음
- 브라우저는 HTTP/1 또는 HTTP/2로 먼저 접속해 `Alt-Svc` 헤더를 읽거나, DNS 조회 단계에서 HTTPS 레코드를 읽어 **HTTP/3 지원**을 발견함
- Firefox Nightly 측정에서 연결의 **31.4%** 가 `Alt-Svc` 헤더만으로 HTTP/3를 알렸으며, 이 경우 HTTP/3는 이후 연결에서만 사용됨 {p:31}
- HTTPS 레코드는 `alpn`, `ech`, `ipv4hint`, `ipv6hint`를 담아 첫 연결의 프로토콜 선택, **ECH**, 주소 힌트 제공을 DNS 응답 안에서 처리함
- HTTPS 레코드는 기존 클라이언트에 추가적으로 동작하며, `Alt-Svc`는 레코드를 받지 못한 클라이언트를 위한 **폴백**으로 유지해야 함

---

## 원문
- [원문](https://savearoundtrip.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=30544)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-07T09:10:23+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30239
id: hada-30239
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- su3.io
title: 'Zeroserve: eBPF로 스크립팅할 수 있는 무설정 웹 서버'
url: https://su3.io/posts/introducing-zeroserve
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 작고 빠른 **HTTPS 서버**인 zeroserve는 웹사이트 tarball을 받아 HTTP/2와 TLS 1.3으로 제공하고, tarball 안의 **eBPF 프로그램**을 사용자 공간 샌드박스 미들웨어로 요청마다 실행함
- 구성 파일 없이 eBPF 프로그램이 요청별 라우팅, 헤더, 인증, 속도 제한, 프록시를 결정해 nginx·Caddy의 선언형 설정과 별도 스크립팅 계층을 하나로 합침
- 사이트는 단일 **tar 파일**로 인덱싱되고 디스크에 풀리지 않으며, tarball 교체와 `SIGHUP`으로 사이트·스크립트·TLS 자료를 연결 손실 없이 원자적으로 교체함
- 단일 코어 HTTPS 벤치마크에서 zeroserve는 소형 정적 파일 36,681 req/s, 10ms eBPF 동적 JSON 46,945 req/s, 소형 프록시 26,486 req/s를 기록했지만, **100KB 프록시**는 nginx가 5,882 req/s로 우위임
- zeroserve는 nginx와 Caddy의 대안을 목표로 단일 tarball 배포, 프로그램형 설정, 사용자 공간 eBPF, 현대적 TLS를 결합하지만, 큰 프록시 응답에는 nginx가 더 적합함

---

## 원문
- [원문](https://su3.io/posts/introducing-zeroserve)
- [GeekNews 토론](https://news.hada.io/topic?id=30239)

## My Note
<!-- 한 줄 코멘트 남기기 -->

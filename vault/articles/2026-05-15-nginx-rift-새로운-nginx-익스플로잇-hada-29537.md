---
category: Other
collected_at: '2026-05-15T14:34:39+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29537
id: hada-29537
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/DepthFirstDisclosures
title: NGINX Rift - 새로운 NGINX 익스플로잇
url: https://github.com/DepthFirstDisclosures/Nginx-Rift
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **NGINX Rift**는 NGINX `ngx_http_rewrite_module`의 치명적 힙 버퍼 오버플로인 **CVE-2026-42945**에 대한 원격 코드 실행 PoC임
- 이 취약점은 `rewrite`와 `set` 지시어를 사용하는 서버에서 **인증 없는 원격 코드 실행**을 가능하게 함
- 문제는 2008년에 도입된 버그로, NGINX 스크립트 엔진의 **길이 계산 패스**와 **복사 패스**가 `is_args` 플래그를 다르게 처리하면서 발생함
- `rewrite` 치환 문자열에 `?`가 있으면 메인 엔진에는 `is_args`가 설정되지만, 길이 계산은 새로 0으로 초기화된 서브 엔진에서 실행되어 원본 캡처 길이만 반환함
- 복사 단계에서는 `is_args = 1` 상태로 `ngx_escape_uri`와 `NGX_ESCAPE_ARGS`가 호출되어 이스케이프 가능한 각 바이트가 3바이트로 확장되고, 과소 할당된 힙 버퍼를 공격자 제어 URI 데이터로 넘치게 만듦
- 익스플로잇은 요청 간 **힙 풍수(heap feng shui)** 를 사용해 인접한 `ngx_pool_t`의 `cleanup` 포인터를 오염시키며, URI 바이트에 null 바이트를 넣을 수 없어 POST 본문을 통해 스프레이함
- 오염된 포인터는 가짜 `ngx_pool_cleanup_s`로 리다이렉트되고, 풀 파괴 시 `system()`을 호출하도록 구성됨
- CVE-2026-42945와 함께 CVE-2026-42946, CVE-2026-40701, CVE-2026-42934 등 3개의 메모리 손상 이슈도 [depthfirst](https://depthfirst.com)의 보안 분석 시스템이 NGINX 소스 온보딩 한 번으로 자율 발견함
- 영향을 받는 버전은 **NGINX Open Source 0.6.27–1.30.0** 및 **NGINX Plus R32–R36**이며, 수정 버전은 Open Source 1.31.0/1.30.1, Plus R36 P4/R35 P2/R32 P6로 제시됨
- 전체 벤더 권고는 <https://my.f5.com/manage/s/article/K000160932>에 있으며, 기술 상세는 [technical write-up](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability)에서 다룸
- PoC는 Ubuntu 24.04.3 LTS에서 테스트되었고, `./setup.sh`, `docker compose -f env/docker-compose.yml up`, `python3 poc.py --shell` 순서로 취약 NGINX 컨테이너를 띄우고 셸을 실행하는 흐름을 제공함

## 원문
- [원문](https://github.com/DepthFirstDisclosures/Nginx-Rift)
- [GeekNews 토론](https://news.hada.io/topic?id=29537)

## My Note
<!-- 한 줄 코멘트 남기기 -->

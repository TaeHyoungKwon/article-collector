---
category: AI
collected_at: '2026-06-15T09:52:00+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30497
id: hada-30497
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/tamnd
title: 'Show HN: Kage - 웹사이트를 오프라인 열람용 단일 바이너리로 섀도잉'
url: https://github.com/tamnd/kage
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **kage**는 실제 headless Chrome에서 페이지를 열고 안정화될 때까지 기다린 뒤 사람이 본 최종 DOM을 저장하며, JavaScript를 제거하고 CSS·이미지·폰트를 로컬 경로로 내려받아 오프라인에서 탐색 가능한 폴더를 만드는 도구임
- `kage clone <url>`은 스크립트 없는 미러를 만들고, `kage serve [dir]`는 복제된 폴더를 로컬 HTTP 서버로 미리 보며, `kage pack <mirror-dir>`는 미러를 ZIM 아카이브 또는 자체 포함 뷰어 바이너리로 묶고, `kage open <file.zim>`은 ZIM을 오프라인 열람용으로 서빙함
- 복제는 **너비 우선 크롤링**으로 동작하며 `robots.txt`를 읽고 `sitemap.xml`에서 시드를 얻고, 기본적으로 시드 호스트 안에 머물며, 같은 페이지가 http/https 또는 trailing slash 차이로 도달돼도 한 번만 가져오는 구조임
- `--max-pages`, `--max-depth`, `--scope-prefix`, `--subdomains`, `--exclude`, `--scroll`, `--workers`, `--refresh`, `--force`, `--chrome` 같은 옵션으로 페이지 수, 깊이, 경로 범위, 서브도메인, 지연 로딩 스크롤, 동시 렌더링 수, 재렌더링, Chrome 경로를 조정함
- `kage pack`은 미러를 **ZIM** 파일로 만들 수 있으며, ZIM은 압축·색인·읽기 전용 파일 형식이고 [Kiwix](https://kiwix.org) 생태계에서 열 수 있으나 kage가 만든 아카이브는 Kiwix 자체 팩처럼 전체 텍스트 검색 색인을 만들지는 않음
- `--format binary`는 아카이브를 kage 실행 파일에 붙여 실행하면 사이트를 오프라인으로 서빙하는 단일 실행 파일을 만들며, 수신자는 kage나 ZIM 리더를 설치할 필요가 없고 바이너리 크기는 사이트 크기와 별개로 kage 약 13 MiB를 포함함
- 기본 빌드는 **pure Go**와 `CGO_ENABLED=0`이며 사전 빌드 릴리스 바이너리는 시스템 브라우저를 열고, `webview` 태그로 빌드하면 macOS의 WKWebView, Windows의 WebView2, Linux의 WebKitGTK 기반 네이티브 창으로 열람함
- 설치는 `go install github.com/tamnd/kage/cmd/kage@latest`로 가능하며, [releases](https://github.com/tamnd/kage/releases)에서 아카이브와 `.deb`/`.rpm`/`.apk`를 받을 수 있고, Chromium을 포함한 컨테이너 이미지는 `ghcr.io/tamnd/kage`로 실행함
- 호스트에서 실행할 때 Chrome 또는 Chromium이 필요하며, 시스템 설치를 자동으로 찾거나 `--chrome` 또는 `KAGE_CHROME` 환경 변수로 경로를 지정하고, 컨테이너 이미지는 추가 설치가 필요 없음
- 소스 구성은 `clone`, `browser`, `sanitize`, `asset`, `urlx`, `zim`, `pack`, `viewer` 등으로 나뉘며, 렌더링, DOM 스냅샷, 스크립트·핸들러·`javascript:` URL 제거, 자산 로컬화, URL-경로 매핑, ZIM 읽기·쓰기, 오프라인 HTTP 핸들러를 담당함
- 라이선스는 MIT임

## 원문
- [원문](https://github.com/tamnd/kage)
- [GeekNews 토론](https://news.hada.io/topic?id=30497)

## My Note
<!-- 한 줄 코멘트 남기기 -->

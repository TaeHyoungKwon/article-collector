---
category: Other
collected_at: '2026-06-22T21:41:38+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30726
id: hada-30726
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- docs.deno.com
title: 'Deno Desktop: Deno 프로젝트를 데스크톱 앱으로 패키징'
url: https://docs.deno.com/runtime/desktop/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 웹 앱과 TypeScript 코드로 만든 **Deno 프로젝트**를 플랫폼별 재배포 가능한 데스크톱 앱 바이너리로 묶을 수 있음
- 출력물은 애플리케이션 코드, **Deno 런타임**, 웹 렌더링 엔진을 함께 포함하며, Deno v2.9.0에 들어갔지만 아직 안정 릴리스는 아님
- 기본 WebView 백엔드는 운영체제 내장 webview를 사용해 작은 바이너리를 지향하고, 렌더링 일관성이 필요하면 **Chromium(CEF)** 백엔드를 선택할 수 있음
- Next.js, Astro, Fresh, Remix, Nuxt, SvelteKit, SolidStart, TanStack Start, Vite SSR 프로젝트를 감지해 릴리스 모드와 `--hmr` 개발 모드에 맞게 서버를 실행함
- Deno 코드와 webview 간 통신은 소켓 기반 IPC가 아닌 **인프로세스 채널**을 쓰며, 교차 컴파일과 bsdiff 기반 자동 업데이트까지 범위에 포함됨

---

## 원문
- [원문](https://docs.deno.com/runtime/desktop/)
- [GeekNews 토론](https://news.hada.io/topic?id=30726)

## My Note
<!-- 한 줄 코멘트 남기기 -->

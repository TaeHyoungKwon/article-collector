---
category: AI
collected_at: '2026-05-09T09:31:01+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29310
id: hada-29310
matched_keywords:
- AI
- RAG
read: false
recommend_score: 5.307
recommended_on: '2026-05-09'
source: geeknews
tags:
- AI
- Other
- github.com/jo-inc
title: Camofox Browser - AI 에이전트를 위한 스텔스 헤드리스 브라우저
url: https://github.com/jo-inc/camofox-browser
---

## TL;DR
- Camofox Browser는 AI 에이전트를 위한 스텔스 기반의 헤드리스 브라우저이다.
- 이 브라우저는 프록시 및 GeoIP 지원을 통해 로케일과 타임존을 자동으로 일치시키며, 리소스 효율성이 높아 저사양 장비에서도 실행할 수 있다.
- AI와 자동화 작업에서의 사용 가능성을 높이며, 다양한 기능을 통해 개발자에게 실질적인 이점을 제공한다.

## GeekNews 요약
- Cloudflare·봇 탐지 우회, Puppeteer/Playwright 대체 가능
- **Camoufox**(Firefox 포크) 기반으로 **C++ 레벨에서 핑거프린트 스푸핑**
  - shim이나 wrapper 없이 Google, Cloudflare 등 대부분의 봇 탐지 우회
- 접근성 스냅샷 이용: 원시 HTML 대비 ~90% 작아 토큰 절약
- **세션 격리**: 유저별 독립된 쿠키/스토리지, **쿠키 임포트**로 인증 브라우징 지원
- **프록시 + GeoIP** 지원: 자동으로 로케일·타임존·지오로케이션 일치
- **리소스 효율적**: 지연 브라우저 런치 + Idle 시 ~40MB로 Raspberry Pi나 $5 VPS에서도 실행 가능
- 14개 **검색 매크로**(@google\_search, @youtube\_search 등) 제공
- **VNC 인터랙티브 로그인**: noVNC 웹 UI로 비쥬얼하게 로그인 후 storage state를 내보내기해서 에이전트가 재사용
- **세션 트레이싱**: 탭별 opt-in Playwright 트레이스 캡처(스크린샷 + DOM 스냅샷 + 네트워크), API로 목록 조회·다운로드·삭제, Trace Viewer에서 열기 지원
- yt-dlp로 YouTube 자막 추출, 대용량 페이지 오프셋 페이지네이션, 다운로드 캡처, DOM 이미지 추출 포함
- Docker/Fly.io/Railway 배포 지원, OpenClaw 플러그인으로 원커맨드 설치 가능
- MIT 라이선스

## 원문
- [원문](https://github.com/jo-inc/camofox-browser)
- [GeekNews 토론](https://news.hada.io/topic?id=29310)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-05-12T09:31:02+09:00'
geeknews_comments: 4
geeknews_score: 11
geeknews_url: https://news.hada.io/topic?id=29409
id: hada-29409
matched_keywords: []
read: false
recommend_score: 2.968
recommended_on: '2026-06-08'
source: geeknews
tags:
- Other
- github.com/vercel-labs
title: zero-native - Zig와 웹 UI로 데스크톱 + 모바일 앱 빌드
url: https://github.com/vercel-labs/zero-native
---

## TL;DR
- 이 글은 Vercel Labs의 Zig 기반 데스크톱 앱 셸인 zero-native에 대해 다룬다.
- zero-native는 WebView를 사용하여 작은 바이너리와 빠른 실행 속도를 제공하며, Zig가 C에 직접 접근할 수 있도록 설계되었다.
- 개발자는 다양한 프론트엔드 프레임워크를 활용하여 네이티브 앱을 쉽게 빌드할 수 있어, 크로스 플랫폼 개발에 대한 새로운 가능성을 열어준다.

## GeekNews 요약
- Vercel Labs가 공개한 **Zig 기반 데스크톱 앱 셸**로, 웹 프론트엔드를 맥/윈/리눅스용 네이티브 앱으로 만드는 프레임워크
- 시스템 **WebView** 사용 시 브라우저 런타임을 번들하지 않아 바이너리가 작고 실행이 빠름
- 렌더링 일관성이 필요하면 **Chromium(CEF)** 번들로 전환 가능, `app.zon` (매니페스트 파일) 에서 웹 엔진 선택
- Zig가 C를 직접 호출하므로 플랫폼 SDK, 네이티브 라이브러리, 코덱 접근에 **별도 글루 레이어 필요 없음**
- WebView를 기본적으로 **신뢰하지 않는 보안 모델** 채택: 네이티브 명령, 권한, 내비게이션, 윈도우 API 모두 옵트인 방식
- `window.zero.invoke()`로 **JavaScript → Zig 브릿지** 호출 시 사이즈 제한·오리진 체크·권한 체크 적용
- **Next, React, Svelte, Vue** 프론트엔드 스타터 템플릿 제공, `zig build run`으로 바로 실행
- 현재는 프리릴리즈로 맥/리눅스/윈도우 빌드 경로 지원
- 모바일은 **iOS/Android** 호스트 앱이 `libzero-native.a`의 C ABI를 링크하는 임베딩 방식(샘플 포함)
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/vercel-labs/zero-native)
- [GeekNews 토론](https://news.hada.io/topic?id=29409)

## My Note
<!-- 한 줄 코멘트 남기기 -->

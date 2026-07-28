---
category: AI
collected_at: '2026-07-28T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31891
id: hada-31891
matched_keywords:
- AI
read: false
recommend_score: 3.609
source: geeknews
tags:
- AI
- Other
- github.com/tokio-rs
title: Topcoat - Rust를 위한 풀스택 웹 프레임워크
url: https://github.com/tokio-rs/topcoat
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **모든 마크업을 서버에서 렌더링**, 컴포넌트가 async로 DB를 직접 조회해 별도 API 계층용 보일러플레이트 제거
- `$(...)` 표현식은 **타입 검증되는 일반 Rust 코드**로, 서버에서 평가되는 동시에 JavaScript로 변환되어 브라우저에서 즉시 재실행
  - wasm 번들 없고, **클라이언트 빌드 단계 필요 없음**
- 서버 처리가 필요한 갱신은 `#[shard]`로 표시, **인자 변경 시 서버 재렌더링 후 HTML 교체**
- `view!` 매크로로 **HTML과 Rust에 충실한 템플릿** 작성 가능, `for`/`if` 등 Rust 제어 흐름과 조건부 속성 그대로 사용
- **모듈 구조 기반 라우팅**을 빌드 단계 없이 자동 추론 (`app/posts/id.rs` → `/posts/{post_id}`)
- Tailwind 기반 **Topcoat UI** 컴포넌트를 프로젝트로 복사해 자유롭게 수정 가능
- `tailwind` 기능 활성화 시 **Node 없이 Tailwind CSS 통합**, 에셋 파이프라인에 자동 연결
- 요청 처리용으로 요청 컨텍스트(`Cx`), 앱 컨텍스트, `#[memoize]` 요청 단위 캐싱, 서명/암호화 쿠키, **세션 인증**(로그인/로그아웃, 슬라이딩 만료, 토큰 회전) 제공
- MIT 라이선스

## 원문
- [원문](https://github.com/tokio-rs/topcoat)
- [GeekNews 토론](https://news.hada.io/topic?id=31891)

## My Note
<!-- 한 줄 코멘트 남기기 -->

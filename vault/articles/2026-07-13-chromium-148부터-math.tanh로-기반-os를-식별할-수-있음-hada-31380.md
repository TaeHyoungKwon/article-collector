---
category: Other
collected_at: '2026-07-13T10:10:24+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31380
id: hada-31380
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- scrapfly.dev
title: Chromium 148부터 Math.tanh로 기반 OS를 식별할 수 있음
url: https://scrapfly.dev/posts/browser-math-os-fingerprint/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Chrome 148부터 V8의 `Math.tanh`가 내장 fdlibm 대신 호스트의 `std::tanh`를 호출하면서, 같은 입력도 Linux의 glibc·macOS의 `libsystem_m`·Windows의 UCRT에서 **서로 다른 마지막 비트**를 반환함
- `Math.tanh(0.8)`은 Linux에서 `0.6640367702678491`, macOS에서 `0.664036770267849`, Windows에서 `0.6640367702678489`가 되어 **한 번의 호출로 세 OS를 구분**할 수 있으며, User-Agent가 주장하는 OS와 결과가 다르면 위장이 드러남
- 엔진마다 누출 경로가 달라 V8의 `Math.*`에서는 `tanh`만 호스트 수학 라이브러리를 사용하지만, Blink의 **CSS 삼각함수 전체**와 Web Audio 일부 연산도 OS별 라이브러리를 거침
- 값을 임의로 흔들면 실제 OS 어느 쪽과도 일치하지 않고 결정성까지 깨지므로, 대상 라이브러리의 계수·테이블·범위 축소·FMA 동작을 **비트 단위로 재현**하거나 원본 UCRT 코드를 직접 매핑해야 함
- Scrapfly는 릴리스마다 871,000개 입력을 실제 Mac과 Chrome에 대조해 `Math.tanh`와 CSS 삼각함수 7개의 비트 일치를 검증하며, 정확도뿐 아니라 **아키텍처 차이와 실행 시간**도 실제 브라우저 수준으로 맞춤

---

## 원문
- [원문](https://scrapfly.dev/posts/browser-math-os-fingerprint/)
- [GeekNews 토론](https://news.hada.io/topic?id=31380)

## My Note
<!-- 한 줄 코멘트 남기기 -->

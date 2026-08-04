---
category: Other
collected_at: '2026-08-04T10:03:41+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32126
id: hada-32126
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/jabdori
title: 'Show GN: maxt – 거래소와 언어가 달라도 일관된 방식으로 사용하는 멀티 언어 거래소 SDK'
url: https://github.com/jabdori/maxt
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. 여러 거래소를 하나의 서비스에서 사용하면서 겪은 불편에서 시작한 오픈소스 프로젝트 `maxt`를 소개합니다.

### 만든 이유

통합 API를 사용해도 실제로 여러 거래소를 연동하면 같은 기능에 서로 다른 파라미터가 필요하거나, 응답과 오류를 별도로 처리해야 하는 경우가 있었습니다. 거래소 전용 기능까지 사용하기 시작하면 조건 분기가 더 늘어났습니다.

저는 새로운 거래소를 추가할 때마다 공통 로직까지 다시 작성하거나, 사용하는 언어가 바뀔 때마다 SDK 사용법을 새로 익히고 싶지 않았습니다.

그래서 지원 거래소 수보다 일관된 개발 경험을 우선한 `maxt`를 만들었습니다.

### 어떤 방식인가

공통 기능은 `Client`에서 제공합니다. 거래소와 언어가 달라도 같은 API 구조, 모델, 오류 분류, 스트림 규칙으로 사용할 수 있습니다.

거래소에만 있는 기능은 공통 API에 옵션이나 조건문으로 섞지 않고, 타입 안전한 어댑터를 통해 명시적으로 제공합니다.

예를 들어 `ticker()`는 모든 거래소에서 사용하는 공통 기능이고, Binance의 주문 단위와 가격 단위를 조회하는 `spot_symbol_filters()`는 Binance 어댑터에서 호출합니다.

현재 다음 거래소를 지원합니다.

- Upbit 현물
- Bithumb 현물
- Binance 현물 및 USD-M 무기한 선물
- Hyperliquid 현물 및 무기한 선물

공개 REST API는 마켓, 체결, 호가, 현재가, 캔들, 펀딩 이력을 지원하며 WebSocket 스트림도 제공합니다. 계좌, 주문, 포지션을 다루는 비공개 API도 구현되어 있습니다.

### 멀티 언어 지원

과거 Go 기반 코어를 Flutter와 FFI로 연결했던 프로젝트 경험에서 이 구조에 대한 영감을 얻었습니다.

하나의 코어를 여러 환경에서 재사용하는 방식이 유효하다고 느꼈고, 네이티브 FFI와 WebAssembly를 통해 여러 언어와 플랫폼으로 확장하기에 적합한 Rust를 중심으로 설계했습니다.

현재 지원하는 환경은 다음과 같습니다.

- Rust
- Python
- Dart 및 Flutter 네이티브
- Dart Web
- TypeScript 및 Node.js
- TypeScript 및 브라우저 WebAssembly

거래소 기능은 Rust 코어에 구현하고, 하나의 공통 스키마에서 각 언어의 공개 API와 계약을 생성합니다. 생성 결과는 컴파일된 네이티브 API와 비교해 누락 여부를 검사합니다.

각 패키지는 독립적으로 설치할 수 있습니다.

```
cargo add maxt  
uv add maxt  
dart pub add maxt  
npm install @jabdori/maxt
```

### 현재 상태

아직 0.x 버전이며, 실제 요청을 통한 검증은 공개 API 위주로 1차 진행한 단계입니다.

비공개 API는 구현되어 있지만 실제 계좌와 주문을 사용한 검증은 아직 충분하지 않습니다. 거래소별 예외 상황이나 플랫폼별 패키징 문제도 남아 있을 수 있으므로, 현재 단계에서 프로덕션 사용을 권장한다고 말하기는 어렵습니다.

또한 많은 거래소를 지원하는 것이 현재 목표는 아닙니다. 여러 거래소를 하나의 서비스에서 사용하면서도 공통 코드에 거래소별 조건 분기가 퍼지지 않게 하는 것이 우선 목표입니다.

직접 사용해 보시고 다음과 같은 부분에 대한 의견을 주시면 감사하겠습니다.

- 여러 거래소를 함께 사용할 때 API가 실제로 자연스러운지
- 거래소별로 누락됐거나 의미가 다른 데이터가 있는지
- Python, Dart/Flutter, TypeScript에서 Rust와 다른 동작이 있는지
- 비공개 API나 스트림에서 재현되는 문제가 있는지

이슈와 기여 모두 환영합니다.

## 원문
- [원문](https://github.com/jabdori/maxt)
- [GeekNews 토론](https://news.hada.io/topic?id=32126)

## My Note
<!-- 한 줄 코멘트 남기기 -->

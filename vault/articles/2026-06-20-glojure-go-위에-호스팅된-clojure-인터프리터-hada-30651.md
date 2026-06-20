---
category: Other
collected_at: '2026-06-20T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30651
id: hada-30651
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/glojurelang
title: glojure - Go 위에 호스팅된 Clojure 인터프리터
url: https://github.com/glojurelang/glojure
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 다른 Go 기반 Clojure 구현과 달리 **"호스티드(hosted)" 언어**로 설계된 Clojure 인터프리터
- 확장 가능한 상호운용(interop)을 지원해 모든 **Go 값을 Glojure 값으로, 반대로도 사용 가능**
- Clojure가 Java 프레임워크에 접근하듯 **Go 라이브러리에 손쉬운 접근** 제공
- **standalone CLI 도구(glj)** 와 **Go 애플리케이션 내 임베딩**, 두 가지 방식 지원
  - 임베딩 시 스크립트 가능한 설정 추가, **Clojure 플러그인** 확장, Go 성능과 Clojure 표현력 혼합 가능
- **Clojure ↔ Go 양방향 호출** 지원으로, Go 함수를 Clojure에서, Clojure 함수를 Go에서 호출 가능
- 다수의 **표준 라이브러리 interop** 기본 내장
  - 네임스페이스 모호성 회피 위해 Go 패키지명의 `/`를 `:`로 치환 (예: `net/http` → `net:http`)
  - 추가 패키지는 **package map** 생성 후 직접 컴파일로 노출
- **인터랙티브 REPL** 기능으로 Vi/emacs 편집 모드, 멀티라인 편집, 탭 자동완성, 영속 히스토리, job control, 인터럽트 제공
- 숫자 타입은 Clojure와 매핑 차이 존재 (예: `long`→`int64`, `char`→`lang.Char`, `BigInt`→`*lang.BigInt`)
- 아직 **초기 개발 단계**로 버그 및 미구현 기능에 성능도 제한적, v1 이전까지 하위 호환성 미보장
- EPL-1.0 라이선스

## 원문
- [원문](https://github.com/glojurelang/glojure)
- [GeekNews 토론](https://news.hada.io/topic?id=30651)

## My Note
<!-- 한 줄 코멘트 남기기 -->

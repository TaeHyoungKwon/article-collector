---
category: AI
collected_at: '2026-05-11T08:32:31+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29367
id: hada-29367
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/nooga
title: let-go - Go로 만든 7ms 기동 Clojure 계열 언어
url: https://github.com/nooga/let-go
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **let-go**는 Go로 작성된 Clojure 방언으로, 바이트코드 컴파일러와 스택 VM을 갖추고 JVM 없이 단일 약 **10MB 바이너리**로 동작함
- 콜드 스타트는 약 **7ms**이며, [jank-lang Clojure test suite](https://github.com/jank-lang/clojure-test-suite) 기준 Clojure 호환성은 **4696 / 4921 assertions 통과(95.4%)** 로 제시됨
- 작성자는 CLI, 스크립트, 웹 서버에 사용하고 있으며, let-go 위에 [daemonless container runtime](https://github.com/nooga/lgcr)도 만들었고 독립 실행 바이너리나 자체 포함 WASM 웹 페이지로 컴파일 가능함
- 목표는 **persistent data structures**, lazy seqs, transducers, protocols, records, multimethods, core.async, BigInts 등 Clojure의 많은 기능 구현과 Go 함수·struct·channel 양방향 interop 제공임
- JVM Clojure의 **drop-in replacement**는 아니며 JAR를 로드하지 않고, 라이브러리 의존성이 있는 실제 프로젝트는 조정이 필요함
- Apple M1 Pro 벤치마크에서 바이너리 크기 **10MB**, 시작 시간 **6.7ms**, 유휴 메모리 **13.5MB**로 Babashka, Joker, go-joker, gloat, Clojure JVM보다 작은 실행 단위에서 우위가 제시됨
- 더 큰 수치 계산 작업에서는 go-joker의 WASM JIT나 HotSpot이 예열된 JVM이 앞서며, let-go는 대부분의 알고리듬 벤치마크에서 Babashka와 비슷하고 upstream Joker보다 **10배 이상 빠른** 결과로 정리됨
- 표준 네임스페이스는 `clojure.core`, `clojure.string`, `clojure.set`, `clojure.edn`, `clojure.test`, `clojure.core.async`, `io`, `http`, `json`, `transit`, `os`, `System`, `syscall`, `pods` 등을 포함함
- [Babashka pods](https://github.com/babashka/pods)를 로드할 수 있어 SQLite, AWS, Docker, 파일 감시 등 pod 생태계를 사용할 수 있고, `~/.babashka/pods/`를 `bb`와 공유함
- 알려진 제한에는 **Refs / STM**, Agents, hierarchies, reader tagged literals, `deftype`, `reify`, `clojure.spec`, `alter-var-root`, `subseq` / `rsubseq` 미구현과 int64 overflow 자동 감지 부재가 포함됨
- 동작 차이로 `go` 블록은 IOC 상태 머신이 아니라 실제 **goroutine**이며, regex는 Java regex가 아닌 Go `re2`를 사용하고 숫자 체계는 `int64` + `float64` + `BigInt`로 구성됨
- 설치는 macOS/Linux용 **Homebrew**, Linux·macOS·Windows의 amd64/arm64용 [Releases](https://github.com/nooga/let-go/releases), 또는 Go 1.22+에서 `go install github.com/nooga/let-go@latest`로 가능함
- `lg`는 REPL, expression eval, 파일 실행을 지원하며, `.lgb` 바이트코드 컴파일, standalone executable 번들링, WASM 웹 앱 생성까지 제공함
- WASM 출력은 inlined WASM을 포함한 약 **6MB gzipped** 자체 포함 `index.html`과 service worker로 구성되며, `term` 네임스페이스 사용 시 xterm.js 기반 터미널 에뮬레이션을 제공함
- 내장 **nREPL** 서버는 CIDER, Calva, Conjure와 동작하고, Go 프로그램 안에서는 `pkg/api`로 let-go를 스크립팅 레이어처럼 임베드해 Go 값·함수·struct·channel을 VM에 전달할 수 있음

## 원문
- [원문](https://github.com/nooga/let-go)
- [GeekNews 토론](https://news.hada.io/topic?id=29367)

## My Note
<!-- 한 줄 코멘트 남기기 -->

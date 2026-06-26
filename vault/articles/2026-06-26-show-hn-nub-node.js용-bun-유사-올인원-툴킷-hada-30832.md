---
category: AI
collected_at: '2026-06-26T08:33:34+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30832
id: hada-30832
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-06-25'
source: geeknews
tags:
- AI
- Other
- github.com/nubjs
title: 'Show HN: Nub - Node.js용 Bun 유사 올인원 툴킷'
url: https://github.com/nubjs/nub
---

## TL;DR
- Nub은 Node.js 개발 환경을 개선하기 위한 Rust 기반의 올인원 툴킷이다.
- 파일 실행, 의존성 관리 및 Node 버전 관리를 통합하여 효율성을 높이고, 다양한 파일 형식을 지원한다.
- 개발자들은 Nub을 통해 Node.js 사용 시의 복잡성을 줄이고, 보다 빠르고 안전한 패키지 관리를 경험할 수 있다.

## GeekNews 요약
- Nub은 stock `node` 위에 Bun과 유사한 개발자 경험을 얹는 Rust 기반 **올인원 툴킷**으로, 파일·스크립트 실행, 의존성 설치, Node 자체 관리를 하나의 도구로 처리함
- 새 런타임을 만들지 않고 Node.js를 보강하는 방식이며, vendor-specific API surface와 lock-in이 없다는 점을 명시함
- `nub <file>`은 `.js`, `.ts`, `.mjs`, `.cjs`, `.mts`, `.cts`, `.jsx`, `.tsx` 실행을 지원하고, `node`와 flag-for-flag 및 var-for-var drop-in 호환을 목표로 함
- 파일 실행 기능은 TypeScript, JSX/TSX, decorators, `emitDecoratorMetadata`, extensionless imports, `tsconfig.json#paths`, 자동 `.env*` 로딩, `.yaml`·`.toml`·`.jsonc`·`.json5`·`.txt` 로더를 제공함
- 내부 동작은 Node의 `--import`/`--require` preload, `module.registerHooks()` 기반 transpilation·resolution, N-API native addon을 사용하며, Nub은 pre-transpilation을 위해 **oxc**를 내장함
- 파일 실행 시 프로젝트가 기대하는 Node 버전을 추론하고 필요하면 자동 설치하며, 우선순위는 `NODE_EXECUTABLE`, `package.json#devEngines`, `.node-version`, `.nvmrc`, `package.json#engines` 순서임
- `nub watch`와 `nub --watch`는 resolved dependency graph와 `.env*`, `tsconfig.json` extends chain, `package.json` 같은 off-graph invalidator를 감시하고 Node 자체 `--watch` 엔진 위에서 실행함
- `nub run`은 `npm run`·`pnpm run`의 drop-in으로, Rust 바이너리라 자체 JavaScript startup이 없으며 warm script dispatch 벤치마크에서 `nub run` 14.7ms, `npm run` 329.9ms, `pnpm run` 442.7ms 결과를 제시함
- `nubx`와 `nub dlx`는 `npx`·`pnpm dlx`의 drop-in으로, local-first 실행 뒤 미설치 bin은 registry에서 가져와 실행하고 폐기하는 fallback을 제공함
- `nub install`은 [Aube](https://github.com/jdx/aube) 엔진 기반 패키지 매니저이며, `pnpm`과 flag-for-flag 호환 CLI를 목표로 하고 `nub install`, `nub ci`, `nub add`, `nub remove`, `nub update`, `nub dedupe` 흐름을 제공함
- 패키지 설치 보안 기본값은 postinstall 차단, resolution 중 [osv.dev](https://osv.dev) known-malicious package version 검사, provenance downgrade 거부, 24시간 `minimumReleaseAge` 적용임
- `nub install`은 `package.json#packageManager`와 lockfile을 기준으로 기존 패키지 매니저를 감지하고 compat-mode로 동작하며, npm·pnpm·Yarn·Bun·Nub별 설정 파일과 환경 변수를 읽음
- `nub pm shim`은 Corepack-style global shim을 등록해 `npm`, `yarn`, `pnpm` 실행 시 프로젝트의 고정 버전을 감지하고 필요하면 설치한 뒤 해당 버전으로 명령을 실행함
- `nub node`는 Node 버전 관리 명령을 제공하며, `which`, `install`, `ls`, `uninstall`, `pin`으로 Nub 캐시의 Node 버전을 조회·설치·삭제·고정함
- 설치 경로는 macOS/Linux용 install script, Windows PowerShell script, Homebrew, `npm install -g --ignore-scripts=false @nubjs/nub`이며, GitHub Actions에서는 `actions/setup-node`와 one-to-one 호환인 [`nubjs/setup-nub`](https://github.com/nubjs/setup-nub)을 사용할 수 있음
- 라이선스는 **MIT**임

## 원문
- [원문](https://github.com/nubjs/nub)
- [GeekNews 토론](https://news.hada.io/topic?id=30832)

## My Note
<!-- 한 줄 코멘트 남기기 -->

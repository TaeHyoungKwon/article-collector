---
category: Other
collected_at: '2026-07-09T13:05:11+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31264
id: hada-31264
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/zi-gae
title: 'Show GN: ts6to7 - TypeScript 5/6 → 7(tsgo) 마이그레이션 자동화 codemod'
url: https://github.com/zi-gae/ts6to7
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
어제 TypeScript 7이 정식 릴리스됐습니다. Go로 재작성된 네이티브 컴파일러(tsgo)로 약 10배 빨라졌지만, TS5/6에서 deprecated였던 컴파일러 옵션이 전부 제거됐고 strict 기본값도 true로 바뀌어서 — 오래된 tsconfig를 가진 프로젝트는 업그레이드가 그냥 안 됩니다.

그 기계적인 부분을 자동화하는 codemod를 만들었습니다.

npx ts6to7 --dry # 미리보기 (아무것도 안 씀)  
npx ts6to7 # 적용

하는 일:

- tsconfig\*.json을 제자리에서 수정 — jsonc-parser로 편집해서 주석과 포맷이 그대로 유지됩니다
- 제거된 옵션을 TS7 등가물로 변환: target: es5 → ES2015, module: umd/amd → ESNext, moduleResolution: node → NodeNext/Bundler, importsNotUsedAsValues → verbatimModuleSyntax 등
- baseUrl은 paths로 폴딩
- typescript 의존성을 ^7.0.0으로 범프
- strict가 미설정이었다면 false로 고정 — extends로 다른 config를 상속하는 파일은 바꾸지 않고 경고만 합니다 (베이스 config가 strict를 이미 설정할 수 있기 때문입니다)
- 안전하게 자동 변환할 수 없는 것들(ES5 전용 런타임, ts-node/ts-jest 같은 구 컴파일러 API 기반 도구, types 배열 누락 등)은 파일 단위로 스코프된 "수동 확인 필요" 체크리스트로 출력

**TypeScript 5에서도 바로 이관 가능**: 6을 거치지 않아도 됩니다. TS5-era 옵션인 ignoreDeprecations, 프로젝트 레퍼런스의 prepend도 함께 정리합니다.

모노레포도 지원합니다 (모든 패키지 스캔).

현재 0.2.0입니다. tsconfig가 잘못 변환되는 케이스가 있으면 해당 tsconfig를 첨부한 이슈로 알려주시면 큰 도움이 됩니다.

## 원문
- [원문](https://github.com/zi-gae/ts6to7)
- [GeekNews 토론](https://news.hada.io/topic?id=31264)

## My Note
<!-- 한 줄 코멘트 남기기 -->

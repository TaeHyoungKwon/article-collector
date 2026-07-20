---
category: Other
collected_at: '2026-07-20T22:26:24+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31621
id: hada-31621
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/nayounsang
title: 'Show GN: eslint-plugin-import-boundary - ESLint Rule을 통해 javascript 프로젝트에서
  import/export의 코드 ...'
url: https://github.com/nayounsang/eslint-plugin-import-boundary
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
최근 인턴십을 하며 제품의 거대한 코드베이스를 처음 경험했습니다. 변경의 영향 범위를 가늠하기 어렵고, “이 코드는 어디서 참조해야 하는지”가 반복적으로 고민됐습니다. 정적 분석(ESLint)으로 import 경계를 강제하면 아키텍처 품질을 더 안정적으로 유지할 수 있겠다고 생각했습니다.  
eslint-plugin-boundaries로도 비슷한 규칙을 만들 수 있다는 건 알고 있었습니다. 다만 프론트엔드에서 적용하려면 설정이 복잡해졌고, 허용된 target이라도 import path 형태까지 강제하기는 어려웠습니다.

그래서 단순한 설정으로 JS(TS) 프로젝트의 폴더 구조가 규칙이 되는 eslint-plugin-import-boundary를 만들었습니다.

- 기본적으로 부모는 직계 자식 디렉토리의 public entry만 import 가능
- public entry 파일 형식 지정 가능 (기본값: index)
- 공용 파일(폴더)를 지정해, 해당 범위 안에서만 공유 모듈을 자신과 하위 디렉토리 영역에서 import할 수 있습니다.

아직 초기 단계인 만큼 피드백과 반응을 환영합니다. 감사합니다!

- 문서: <https://nayounsang.github.io/eslint-plugin-import-boundary/>
- 설치: `pnpm add -D eslint-plugin-import-boundary eslint`

## 원문
- [원문](https://github.com/nayounsang/eslint-plugin-import-boundary)
- [GeekNews 토론](https://news.hada.io/topic?id=31621)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-24T12:45:43+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30788
id: hada-30788
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- devblogs.microsoft.com
title: Typescript 7.0 RC버전이 배포되었습니다.
url: https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
제목: TypeScript 7.0 RC 발표 - Go로 새로 작성되어 약 10배 빨라짐  
본문:

Microsoft가 TypeScript 7.0의 Release Candidate를 발표함. 기존 코드베이스를 지난 1년간 TypeScript(JS로 컴파일되던 부트스트랩 코드베이스)에서 Go로 포팅한 것이 핵심  
네이티브 코드 속도와 공유 메모리 병렬 처리의 결합으로 TypeScript 6.0 대비 약 10배 빠른 성능을 보임  
npm install -D typescript@rc 로 바로 설치 가능

호환성 & 안정성

처음부터 다시 쓴 게 아니라 기존 구현을 체계적으로 포팅한 것으로, 타입 체킹 로직은 6.0과 구조적으로 동일함  
10년간 쌓아온 거대한 테스트 스위트로 검증했고, Microsoft 내외부의 수백만 줄 규모 코드베이스에서 이미 사용 중  
Bloomberg, Canva, Figma, Google, Linear, Notion, Slack, Vercel 등 다수 기업이 1년 넘게 사전 빌드를 테스트했으며, 대부분 빌드 시간이 크게 단축되었다는 긍정적 피드백

병렬화 제어

파싱/타입체킹/emit을 병렬로 수행. --checkers 플래그로 타입 체커 워커 수 조절(기본값 4), --builders 플래그로 프로젝트 레퍼런스 빌드 병렬화(모노레포에 유용), --singleThreaded로 단일 스레드 모드 강제 가능

개선된 --watch 모드

Parcel 번들러의 file-watcher를 Go로 포팅하여 크로스 플랫폼 파일 감시 성능을 크게 개선함

6.0과 병행 사용 (Side-by-Side)

안정적인 programmatic API는 7.1(수개월 후)에야 제공 예정  
@typescript/typescript6 호환 패키지가 tsc6 실행 파일을 제공하여 6.0과 7.0을 충돌 없이 함께 사용 가능. npm alias 활용 권장

주요 기본값 변경 / Breaking Changes

strict 기본값 true, module 기본값 esnext, stableTypeOrdering 강제 활성화  
target: es5, downlevelIteration, moduleResolution: node/node10/classic, module: amd/umd/systemjs, baseUrl 등 다수 deprecated 옵션이 하드 에러로 전환  
템플릿 리터럴 타입이 이제 유니코드 코드 포인트를 자연스럽게 처리 ("😀abc" → ["😀", "abc"])  
JavaScript 지원(JSDoc 기반)을 .ts 파일 분석 방식과 더 일관되게 재작업

에디터 경험

VS Code용 TypeScript Native Preview 익스텐션 제공, LSP 기반으로 멀티스레드 활용. 6.0 대비 실패하는 language server 명령이 20배 이상 감소했다고 함

일정: 정식 7.0은 약 한 달 내 출시 예정. 실제 프로젝트 테스트 피드백을 적극 요청 중

## 원문
- [원문](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)
- [GeekNews 토론](https://news.hada.io/topic?id=30788)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-16T10:12:57+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30529
id: hada-30529
matched_keywords: []
read: false
recommend_score: 1.594
source: geeknews
tags:
- Other
- platform.claude.com
title: Apple Foundation Models에 Claude 탑재하기
url: https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Apple의 **Foundation Models 프레임워크**에 Claude를 서버 사이드 모델로 연결하는 Swift 패키지로, 개발자가 **Apple 온디바이스 모델과 똑같은 코드 경로**로 Claude를 호출할 수 있게 됨
- WWDC 2026에서 Apple이 도입한 **`LanguageModel` 프로토콜** 덕분에, 온디바이스 모델로 프로토타이핑한 뒤 복잡한 작업만 클라우드 모델로 넘기는 **하이브리드 구조**가 표준 API 하나로 가능해짐
- 핵심은 **프로바이더 교체 가능성** - 세션 로직을 건드리지 않고 Swift Package 의존성만 바꿔 Apple·Claude·Gemini 사이를 오갈 수 있다는 점
- Anthropic이 Apache 2.0으로 공개한 이 패키지는 그 "어떤 백엔드든 연결 가능하다"는 구상의 **실제로 동작하는 첫 사례**
- 요청이 앱에서 Claude API로 직접 가고 **Apple은 경로에 없어** 프롬프트·응답을 보지 못하며, 비용도 Anthropic 계정에 직접 청구

---

## 원문
- [원문](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)
- [GeekNews 토론](https://news.hada.io/topic?id=30529)

## My Note
<!-- 한 줄 코멘트 남기기 -->

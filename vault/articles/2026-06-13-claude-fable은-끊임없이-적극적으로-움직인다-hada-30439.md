---
category: Other
collected_at: '2026-06-13T09:46:30+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30439
id: hada-30439
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- simonwillison.net
title: Claude Fable은 끊임없이 적극적으로 움직인다
url: https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 2일간의 실험 결과 Claude Fable 5는 "**relentlessly proactive**" 하다고 표현하는게 적절함
- 스크린샷과 한 줄 프롬프트만으로 로컬 개발 서버 실행, 실제 브라우저 조작, 측정 코드 삽입까지 수행해 CSS 버그 원인을 추적함
- Fable은 Playwright, Firefox, WebKit, Safari를 오가며 버그를 재현하려 했고, 실패 후 실제 브라우저 창을 찾아 **스크린샷 자동화**를 직접 구성함
- `/` 키로 열리는 모달 대화상자를 테스트하기 위해 Datasette 템플릿에 JavaScript를 삽입하고, 창 로드 후 키보드 이벤트를 발생시켜 필요한 상태를 만들어냄
- 페이지 내부 측정값을 얻기 위해 Python `http.server` 기반 **CORS 수집 서버**를 만들고, Web Component의 shadow DOM 안 `<textarea>` 정보를 JSON으로 저장함
- 강력한 코딩 에이전트는 터미널에서 사용자가 할 수 있는 일을 수행할 수 있어, 샌드박스 밖 실행은 프롬프트 인젝션과 데이터 유출 위험을 키움

---

## 원문
- [원문](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/)
- [GeekNews 토론](https://news.hada.io/topic?id=30439)

## My Note
<!-- 한 줄 코멘트 남기기 -->

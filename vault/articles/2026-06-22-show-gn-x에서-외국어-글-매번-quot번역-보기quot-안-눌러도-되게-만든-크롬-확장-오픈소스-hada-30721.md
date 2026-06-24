---
category: AI
collected_at: '2026-06-22T17:09:13+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30721
id: hada-30721
matched_keywords:
- AI
- RAG
read: false
recommend_score: -995.307
recommended_on: '2026-06-23'
source: geeknews
tags:
- AI
- Other
- chromewebstore.google.com
title: 'Show GN: X에서 외국어 글, 매번 &quot;번역 보기&quot; 안 눌러도 되게 만든 크롬 확장 (오픈소스)'
url: https://chromewebstore.google.com/detail/efpggcboclcalhhbpjeogpkepcbleoan
---

## TL;DR
- 이 글은 X에서 외국어 글을 자동으로 번역하는 크롬 확장을 소개한다.
- 이 확장은 X의 자체 번역 기능을 활용하여 번역 버튼을 자동으로 클릭하며, 사용자 데이터는 외부 서버로 전송되지 않는다.
- 독자는 이 확장을 통해 번거로운 번역 과정 없이 외국어 콘텐츠를 쉽게 소비할 수 있는 방법을 알게 된다.

## GeekNews 요약
**Just Translate Already — for X**

X(옛 트위터)에서 외국어 글을 볼 때, 자동 번역이 안 걸린 글은 매번 "번역 보기"를 일일이 눌러야 하는 게 번거로웠습니다. 이 확장은 그 버튼을 대신 자동으로 눌러줍니다. 스크롤만 하면 외국어 글이 알아서 번역됩니다.

핵심 차별점 — 제3자 번역엔진을 안 씁니다

- 시중의 번역 확장 대부분은 구글 번역 등 자체 엔진으로 번역해 글 아래에 덧붙입니다 → 번역 결과가 X와 달라지고, 글 내용이 외부 서버로 전송됩니다.
- 이건 X 자체(Grok) 번역을 그대로 사용합니다. X가 원래 띄우는 "번역 보기" 버튼을 자동으로 클릭할 뿐이라, 확장이 외부로 보내는 데이터가 전혀 없습니다.

동작 방식

- content script가 x.com/twitter.com에서 MutationObserver로 번역 버튼을 감지해 클릭합니다.
- 버튼 라벨이 UI 언어마다 다르므로 약 46개 X 인터페이스 언어의 라벨을 인식합니다(영어·한국어·일본어·중국어·스페인어·아랍어·힌디어 등). 번역되는 글의 언어는 무관합니다.
- 한 번 처리한 글은 트윗 ID로 기억해 재클릭하지 않고, "원문 보기"는 절대 누르지 않아 무한 토글/루프가 없습니다.

프라이버시

- 권한은 storage 하나(on/off 토글 저장용)뿐이며 host\_permissions가 없습니다.
- 네트워크 요청 0, 외부 서버 0, 데이터 수집 0. 전부 브라우저 안에서만 동작합니다.

한계 (솔직하게)

- X가 번역 버튼을 띄우지 않는 곳은 동작하지 않습니다. 특히 대화 스레드의 답글엔 X가 번역 UI를 제공하지 않는 경우가 많습니다(확장 버그가 아니라 X의 동작입니다).
- 계정에 X 자동 번역이 이미 켜져 있으면 대부분 글은 X가 알아서 번역하므로, 이 확장은 그 사이로 빠지는 글들을 메워주는 보완재에 가깝습니다.

오픈소스 (MIT)

- 코드 전부 공개돼 있고 원격 코드나 난독화가 없습니다. 직접 검토하고, 받아서 chrome://extensions → 개발자 모드 → 압축해제된 확장 프로그램 로드로 그대로 설치해 써도 됩니다(별도 빌드 과정도 필요 없습니다).
- GitHub: <https://github.com/melodysdreamj/just-translate-already-for-x>

## 원문
- [원문](https://chromewebstore.google.com/detail/efpggcboclcalhhbpjeogpkepcbleoan)
- [GeekNews 토론](https://news.hada.io/topic?id=30721)

## My Note
<!-- 한 줄 코멘트 남기기 -->

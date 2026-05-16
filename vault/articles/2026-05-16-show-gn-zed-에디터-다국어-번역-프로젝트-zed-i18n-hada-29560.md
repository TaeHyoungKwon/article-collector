---
category: AI
collected_at: '2026-05-16T16:40:42+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29560
id: hada-29560
matched_keywords:
- AI
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- github.com/LI-NA
title: 'Show GN: Zed 에디터 다국어 번역 프로젝트 - Zed-i18n'
url: https://github.com/LI-NA/zed-i18n
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
정말 오랜만에 GeekNews에서 인사드리게 되었습니다.

VSCode가 업데이트할 때마다 버그만 늘면서 사용성이 악화하는 사이... 최근 [Zed 에디터](https://github.com/zed-industries/zed) 1.0.0이 출시되고 한 번 직접 써보고 싶었는데 다국어 지원이 아예 안 되더군요.

구조상 모든 UI 문자열이 소스 코드에 그대로 들어 있어 다국어 지원을 하려면 전체 구조를 바꿔야 하는 상황...!  
그래서 다국어 프로젝트를 찾다가 결국 기존 프로젝트는 거의 다 중국어 중심에 정규식 치환 방식이라 새로운 프로젝트가 필요하다고 느꼈습니다.

Zed-i18n은 정규식 대신 Python의 Tree-Sitter 기반으로 구문 분석을 통해 UI 요소를 정확하게 추출 및 수정하도록 했으며,  
Zed와의 구분을 위해 브랜딩, 설치 위치, 자동 업데이트 경로 등을 변경할 수 있도록 했습니다.

실제로는 UI 요소 추출, 검증, 번역 등 전 과정을 AI로 진행했고, 그 덕분에 처음부터 13개 언어 모두 번역을 등록할 수 있었습니다.  
번역 품질은... VSCode 공식 언어 팩을 참조하게 하고, 여러 개의 모델로 번역 및 검증하는 등 나름의 노력은 했습니다...!

또한 신뢰성 확보가 중요하다고 생각하여 빌드 투명성을 위해 Github Actions 기반으로 모든 과정을 확인할 수 있게 세팅했습니다.  
공식 문서보다 훨씬 오버스펙의 러너가 제공되는 덕분에 빌드가 가능하긴 하더군요.

물론 무료 버전으로 빌드하느라 최소 10시간 넘게 걸리는 게 문제긴 합니다.  
빌드 시간 때문에 최신 버전 따라가기가 벅차네요.... v1.2.5 만들었더니 그사이에 v1.2.6이 나왔습니다. ㅠㅠ

아무튼 Zed 에디터 쓰시는 분은 한 번 확인해 보시고,  
편하게 한국어로 쓰시면서 문제점 있다면 공유해 주시면 좋겠습니다!

## 원문
- [원문](https://github.com/LI-NA/zed-i18n)
- [GeekNews 토론](https://news.hada.io/topic?id=29560)

## My Note
<!-- 한 줄 코멘트 남기기 -->

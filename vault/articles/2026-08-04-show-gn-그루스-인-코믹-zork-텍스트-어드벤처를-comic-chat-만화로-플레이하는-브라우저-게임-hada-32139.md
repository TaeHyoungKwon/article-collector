---
category: AI
collected_at: '2026-08-04T18:40:31+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=32139
id: hada-32139
matched_keywords:
- AI
read: false
recommend_score: 3.386
recommended_on: '2026-08-05'
source: geeknews
tags:
- AI
- Other
- grues.danielkimdev.com
title: 'Show GN: 그루스 인 코믹: Zork 텍스트 어드벤처를 Comic Chat 만화로 플레이하는 브라우저 게임'
url: https://grues.danielkimdev.com/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
'그루스 인 코믹'(Grues in Comic)은 1980년대 텍스트 어드벤처 [Zork](https://github.com/historicalsource/zork1)를, 1990년대 IRC 클라이언트 [Comic Chat](https://github.com/microsoft/comic-chat)의 렌더링 방식으로 보여주는 브라우저 게임입니다. 플레이어는 `north`, `take lamp` 같은 명령어를 그대로 입력하고, Zork I의 파서와 월드도 원작 그대로 동작합니다. 다만 결과가 텍스트 스크롤이 아니라 Comic Chat 특유의 만화 패널(캐릭터 표정, 몸짓, 말풍선 자동 배치)로 그려진다는 점이 다릅니다.

이 프로젝트는 사실 긱뉴스에서 시작됐습니다. 작년 11월 [Zork 오픈소스 공개 소식](https://news.hada.io/topic?id=24510)을 긱뉴스에서 보고 '이런 게임도 있었구나' 하고 넘겼는데, 지난달 [Comic Chat 오픈소스 공개 소식](https://news.hada.io/topic?id=31503)이 올라왔고 그 글 하단의 '함께 보면 좋은 글'에 Zork 글이 링크되어 있었습니다. 두 소식을 나란히 보다가 Zork의 게임 플레이를 Comic Chat 렌더러로 보여주면 어떨까 하는 생각이 떠올랐습니다. 긱뉴스의 관련 글 추천 기능이 없었다면 두 소식을 따로 보고 지나갔을 것 같습니다.

### 어떻게 만들었나

원작 소스(Zork는 ZIL, Comic Chat은 오래된 C++)를 브라우저에 그대로 이식하는 대신, 원작의 동작 방식을 독립적인 계층으로 옮기는 방식을 택했습니다.

- **임포터**: Zork I의 ZIL 소스를 파싱해 AST로 변환합니다.
- **IR(중간 표현)**: ZIL에도 특정 런타임에도 종속되지 않는 독립 계층입니다. 임포터의 결과물이 여기로 옮겨집니다.
- **엔진**: TypeScript로 작성되어 브라우저에서 별도 런타임 없이 IR을 실행합니다. 월드 상태, 파서, 전투, 저장/불러오기를 처리합니다.
- **렌더러**: 엔진이 만들어내는 이벤트를 받아 Comic Chat 방식의 만화 패널로 그립니다. 패널 배치, 포즈, 말풍선 규칙은 원작 C++ 코드를 참고해 옮겼습니다.

원작과의 정합성은 [frotz](https://gitlab.com/DavidGriffith/frotz) 인터프리터로 뽑은 공식 워크스루를 기준 데이터로 삼아 한 줄씩 비교하는 방식으로 검증했고, 게임 결말(스톤 배로우)까지 도달하는 전체 플레이 시나리오를 회귀 테스트로 고정해두었습니다.

### 밝혀둘 점

코드는 한 줄도 직접 작성하지 않았습니다. 임포터, IR, 엔진, 정합성 검증까지 전부 AI 에이전트가 작성했고, 제가 한 일은 방향성과 요구사항을 정하고 직접 플레이하며 테스트하는 것이었습니다. 배경 그림도 일부 추가했는데, 원작 Comic Chat에 배경 종류가 몇 개 없어서 이미지 생성 모델로 Zork 각 방의 분위기에 맞는 배경을 만들고 다듬었습니다.

저장소는 아직 비공개입니다. 사이트 정식 오픈과 함께 1.0 태그를 붙이면서 공개할 계획이고, 그 전까지는 베타로 계속 다듬을 예정입니다. 더 자세한 제작기는 [블로그 글](https://danielkimdev.com/ko/blog/grues-in-comic-beta)에도 정리해두었습니다.

## 원문
- [원문](https://grues.danielkimdev.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=32139)

## My Note
<!-- 한 줄 코멘트 남기기 -->

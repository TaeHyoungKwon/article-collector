---
category: AI
collected_at: '2026-07-10T23:03:17+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31301
id: hada-31301
matched_keywords:
- AI
read: false
recommend_score: -997.099
recommended_on: '2026-07-11'
source: geeknews
tags:
- AI
- Other
- triapul.cz
title: '나는 Stanley Lieber를 죽이지 않았다: 9front로 그리는 법'
url: https://triapul.cz/automa/i_did_not_kill_stanley_lieber
---

## TL;DR
- 이 글은 9front 운영체제에서 그림을 그리는 방법과 관련된 절차를 설명한다.
- 그림 작업은 입력 장치 선택부터 캔버스 관리와 결과물 조정까지 다양한 작업을 포함하지만, `paint(1)`의 제한으로 사용자가 직접 세심하게 관리해야 한다.
- 이를 통해 독자는 9front의 그림 그리기가 어떻게 이루어지는지 이해하고, 이를 활용하여 창의적인 표현을 할 수 있는 방법을 알 수 있다.

## GeekNews 요약
- 9front에서 그림을 그리는 전체 흐름을 `paint(1)` 중심으로 정리하며, **입력 장치 선택**부터 캔버스 관리, 이미지 조작, 내보내기까지 연결함
- 작업은 9front 내부 **image(6)** 형식에서 진행하고, `paint(1)`로 그린 뒤 `page(1)`, `crop(1)`, `vcrop(1)`, `resize(1)`, `rotate(1)`로 결과물을 조정하는 방식임
- `paint(1)`은 압력 감지, 레이어, 잘라내기/붙여넣기가 없어 사용자가 종이처럼 **작업 영역과 색상**을 직접 관리해야 함
- 마우스, 손가락, 펜, 외장 태블릿, drawterm/VNC 입력을 모두 다루지만, 펜 버튼은 마우스 클릭을 흉내 내므로 키보드와 마우스를 가까이 두는 구성이 실용적임
- 외부 공유에는 **PNG 변환**이 적합하며, PNG나 JPG는 `paint(1)`, `crop(1)`, `vcrop(1)`의 직접 편집 대상이 아니어서 필요하면 다시 9front image 형식으로 바꿔야 함

---

## 원문
- [원문](https://triapul.cz/automa/i_did_not_kill_stanley_lieber)
- [GeekNews 토론](https://news.hada.io/topic?id=31301)

## My Note
<!-- 한 줄 코멘트 남기기 -->

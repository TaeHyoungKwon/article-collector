---
category: Other
collected_at: '2026-08-09T17:01:18+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32287
id: hada-32287
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- devslab-kr.github.io
title: 'Show GN: editor-ruler — 웹 에디터에 Word 스타일 줄자를 붙이는 오픈소스'
url: https://devslab-kr.github.io/editor-ruler/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Froala·TinyMCE·CKEditor 5·Quill 어디에도 Word 같은 줄자(눈금자)가 없습니다.  
여백과 첫 줄 들여쓰기를 끌어서 맞추는 그 컨트롤인데, 무거운 문서형 컴포넌트  
(Syncfusion·ONLYOFFICE 등)에만 들어 있습니다. CKEditor 쪽엔 2020년 9월부터  
열려 있는 기능 요청도 있고요.

줄자를 그리려면 "페이지" 개념이 필요한데 HTML엔 그게 없습니다. 그래서 대부분  
여기서 멈춥니다. 대신 질문을 바꿔서, 줄자가 실제로 편집하는 게 뭔지만 보면  
CSS 속성 세 개로 끝납니다 — margin-left, margin-right, text-indent.

이 매핑이 1:1이라 결과물이 이식됩니다. 출력은 순수 인라인 CSS라  
(<p style="margin-left: 75px; text-indent: 38px">) 메일이든 CMS든 붙여넣어도  
레이아웃이 유지됩니다.

- 좌/우 여백 + 첫 줄 들여쓰기 드래그 핸들 (내어쓰기 포함), cm/in/px 눈금
- 세로 줄자, 가이드선 + 스냅 (가이드는 시각 오버레이라 HTML에 안 남음)
- 드래그 제스처 전체가 undo 1스텝 (픽셀마다가 아니라)
- 핸들이 ARIA 슬라이더라 키보드로도 조작 가능
- UI 언어는 브라우저 추종 (ko/en 내장)
- 코어는 의존성 0, CDN <script> 한 줄로도 사용 가능

어댑터는 Froala·Tiptap·CKEditor 5 세 가지이고, 랜딩에서 탭으로 셋 다 바로  
만져볼 수 있습니다. 테이블 통째 밀기와 컬럼 폭 마커는 현재 Froala 전용입니다.

탭 스톱은 의도적으로 범위 밖입니다 — HTML에 탭 스톱 모델이 없어서, 있는 척하면  
에디터를 벗어나는 순간 문서가 깨집니다.

Apache-2.0, API는 1.0부터 semver로 고정했습니다.  
GitHub: <https://github.com/devslab-kr/editor-ruler>

## 원문
- [원문](https://devslab-kr.github.io/editor-ruler/)
- [GeekNews 토론](https://news.hada.io/topic?id=32287)

## My Note
<!-- 한 줄 코멘트 남기기 -->

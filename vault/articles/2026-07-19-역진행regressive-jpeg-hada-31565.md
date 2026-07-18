---
category: Other
collected_at: '2026-07-19T07:57:41+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31565
id: hada-31565
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- maurycyz.com
title: 역진행(Regressive) JPEG
url: https://maurycyz.com/projects/bad_jpeg/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 점진적 JPEG의 **다중 스캔 구조**를 변형하면 다운로드가 진행될수록 화질이 좋아지는 대신, 이미 표시된 이미지가 다른 이미지로 계속 바뀌게 할 수 있음
- 각 스캔은 색상 채널·DCT 주파수 범위·정밀도를 지정하며, 같은 해상도의 JPEG에서 일부 마커를 제거해 이어 붙이면 **기존 렌더링 데이터를 덮어쓸 수 있음**
- 디코더는 압축 폭탄과 유사한 문제를 막기 위해 처리할 스캔 수를 제한하며, Chrome은 **약 90프레임**까지 렌더링하고 Firefox 등은 더 많이 처리함
- 프레임마다 DC 전용 스캔 하나만 사용하면 프레임 수를 늘리면서 잔상을 피할 수 있지만, DCT 블록 특성상 결과 해상도는 원본의 **1/16**로 낮아짐
- 단일 JPEG에 영상처럼 여러 프레임을 담을 수 있으나 타이밍 정보가 없어 재생 속도가 네트워크 지연에 좌우되며, 실용적 영상보다는 **부분 렌더링을 활용한 HTML·단일 페이지 앱 실험**에 적합함

---

## 원문
- [원문](https://maurycyz.com/projects/bad_jpeg/)
- [GeekNews 토론](https://news.hada.io/topic?id=31565)

## My Note
<!-- 한 줄 코멘트 남기기 -->

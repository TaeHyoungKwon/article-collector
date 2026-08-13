---
category: Other
collected_at: '2026-08-13T22:31:56+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32470
id: hada-32470
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- guillaumetech.github.io
title: Chrome에서 아주 작은 JPEG가 다르게 보이는 이유
url: https://guillaumetech.github.io/posts/jpg-scaling-chrome/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Chrome에서 아주 작게 표시한 JPEG가 Firefox보다 두껍게 보이는 현상은 **부분 IDCT 스케일링**과 후속 축소 알고리듬이 함께 만든 결과임
- 큰 JPEG를 모두 압축 해제한 뒤 축소하면 메모리 낭비가 큼. 2000×2000 비트맵은 약 **12MB**지만 최종 20×20 이미지는 약 1.2KB에 불과함
- JPEG는 이미지를 **8×8 블록**으로 나누고 DCT를 적용해 평탄한 색부터 체크무늬까지 주파수 성분별 계수로 저장함
- Chrome의 Skia와 libjpeg-turbo는 목표 크기에 가까운 **분모가 8인 비율**로 저주파 데이터만 디코딩한 뒤 일반적인 다운샘플링으로 원하는 크기까지 줄임
- 1/8 크기에서는 상수 성분만 남아 경계의 부드러움과 그라데이션이 사라질 수 있으므로, 사진 인지에 맞춰 설계된 **JPEG는 아이콘에 적합하지 않음**

---

## 원문
- [원문](https://guillaumetech.github.io/posts/jpg-scaling-chrome/)
- [GeekNews 토론](https://news.hada.io/topic?id=32470)

## My Note
<!-- 한 줄 코멘트 남기기 -->

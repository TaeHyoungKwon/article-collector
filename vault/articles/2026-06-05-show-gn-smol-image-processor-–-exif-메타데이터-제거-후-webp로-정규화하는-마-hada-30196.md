---
category: Other
collected_at: '2026-06-05T11:29:41+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30196
id: hada-30196
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/levish0
title: 'Show GN: smol-image-processor – EXIF/메타데이터 제거 후 WebP로 정규화하는 마이크로서비스 (Bun/Elysia)'
url: https://github.com/levish0/smol-image-processor
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
백엔드에서 사용자 이미지 업로드를 받을 때 조용히 따라오는 문제들이 있습니다.

- JPEG에는 GPS 좌표, 기기 모델명, 촬영 시각이 EXIF로 담겨 있을 수 있다
- ICC 프로파일 같은 색상 메타데이터도 그대로 저장·배포될 수 있다
- JPEG, PNG, GIF, WebP가 뒤섞여 들어오면 저장/CDN/렌더링 파이프라인이 복잡해진다
- EXIF orientation만 잘못 처리해도 이미지가 90° 돌아간 채로 저장된다

smol-image-processor는 이 문제들을 일괄 처리하는 단일 역할 마이크로서비스입니다.

**동작 방식**

`POST /process`에 multipart/form-data로 이미지를 올리면 항상 WebP가 응답으로  
돌아옵니다. Sharp의 기본 출력 동작이 소스 EXIF, ICC 프로파일 등 메타데이터를  
버리는 특성을 그대로 활용합니다. 단, EXIF orientation은 메타데이터를 제거하기  
전에 `.rotate()`로 픽셀에 먼저 적용해 이미지 방향이 보존됩니다.

방어 레이어는 두 가지입니다.

- **픽셀 수 제한(MAX\_PIXELS)**: 파일 크기는 작아도 디코딩 시 수억 픽셀로  
  팽창하는 이미지(decompression bomb)를 Sharp의 `limitInputPixels`로 차단합니다.
- **프레임 수 제한(MAX\_PAGES)**: 수백~수천 프레임짜리 애니메이션 GIF/WebP로  
  메모리·CPU를 고갈시키는 DoS를 막습니다.

애니메이션 GIF/WebP는 animated WebP로 변환되며 프레임 딜레이와 루프 횟수가  
보존됩니다. PNG의 알파 채널도 그대로 유지됩니다.

응답 헤더에 처리된 이미지의 width, height, size, animated 여부, 페이지 수가  
담겨 있어 별도 메타데이터 추출 단계 없이 DB에 바로 저장할 수 있습니다.

**스택**

- Runtime: Bun, HTTP 프레임워크: Elysia
- 이미지 처리: Sharp (libvips 래퍼)
- Docker 이미지 제공 (GHCR)

**빠른 시작**

docker run --rm -p 6701:6701 ghcr.io/levish0/smol-image-processor  
curl -F file=@photo.jpg <http://localhost:6701/process> -o clean.webp

→ <https://github.com/levish0/smol-image-processor>

## 원문
- [원문](https://github.com/levish0/smol-image-processor)
- [GeekNews 토론](https://news.hada.io/topic?id=30196)

## My Note
<!-- 한 줄 코멘트 남기기 -->

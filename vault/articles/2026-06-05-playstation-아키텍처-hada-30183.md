---
category: Other
collected_at: '2026-06-05T07:35:57+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30183
id: hada-30183
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- copetti.org
title: PlayStation 아키텍처
url: https://www.copetti.org/writings/consoles/playstation/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **PlayStation 아키텍처**는 3D 하드웨어 개발 복잡도를 줄이기 위해 단순하고 실용적인 구성을 택했지만, 그래픽 정렬·텍스처 보정·정밀도에서 개발자 부담과 시각적 한계를 남김
- Sony CXD8530BQ는 LSI Logic의 **CoreWare** 기반 MIPS R3000A 호환 코어와 CP0, GTE, MDEC를 통합한 SoC이며, 33.87MHz로 동작하고 2MB RAM·1KB Scratchpad·DMA를 중심으로 데이터 이동을 구성함
- 그래픽은 **GTE**가 3D 투영·조명·클리핑을 맡고 GPU가 명령 기반으로 선·사각형·삼각형을 렌더링하는 구조이며, Z-buffer 없이 ordering table을 사용해 CPU가 폴리곤 순서를 정해야 하는 방식임
- GPU는 affine texture mapping, nearest neighbour, 정수 좌표, 서브픽셀 해상도 부재 때문에 흔들림·겹침·texture warping이 생기며, tessellation·단색 대체·pre-rendered 배경 같은 우회가 활용됨
- CD-ROM 기반 설계는 620MB 저장공간, 44.1kHz ADPCM 오디오 스트리밍, BIOS 기반 실행 환경, **Wobble Groove** 복제 방지와 지역 잠금을 결합해 게임 개발과 배포 방식을 바꿈

---

## 원문
- [원문](https://www.copetti.org/writings/consoles/playstation/)
- [GeekNews 토론](https://news.hada.io/topic?id=30183)

## My Note
<!-- 한 줄 코멘트 남기기 -->

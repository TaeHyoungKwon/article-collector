---
category: AI
collected_at: '2026-07-28T18:47:42+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31910
id: hada-31910
matched_keywords:
- AI
- RAG
read: false
recommend_score: 5.099
recommended_on: '2026-07-29'
source: geeknews
tags:
- AI
- Other
- github.com/kdrkdrkdr
title: 'Show GN: faster-enhancer.c – 안정적인 온디바이스 실시간 음성 잡음제거 C 라이브러리'
url: https://github.com/kdrkdrkdr/faster-enhancer.c
---

## TL;DR
- 이 글은 안정적인 온디바이스 실시간 음성 잡음제거를 위한 C 라이브러리를 다룬다.
- Apple M2에서의 런타임은 0.069로, 기존 ONNX Runtime 대비 3.3배 빠른 성능을 보인다.
- 이 라이브러리는 재학습 없이도 높은 음성 품질을 유지하며, 실시간 환경에서의 안정성을 보장한다.

## GeekNews 요약
직접 만든 프로젝트임.

- FastEnhancer-Medium(48 kHz 스트리밍 음성향상 모델)의 런타임을 순수 C로 다시 구현한 라이브러리임
- 원본 모델: <https://github.com/aask1357/fastenhancer> (Ahn 외, 2025)
- 원본 레포가 논문(16 kHz) 이후 추가로 공개한 48 kHz 가중치를 그대로 사용함. 재학습·파인튜닝·calibration set 없음
- 모델과 가중치는 원저자 것이고, 최적화한 것은 런타임 쪽임

■ 성능

- Apple M2 코어 1개에서 real-time factor 0.069 나옴. 같은 기계에서 동일 그래프를 ONNX Runtime으로 돌리면 0.230이므로 3.3배임
- Galaxy S23+(Snapdragon 8 Gen 2)에서 0.096임
- 품질 저하는 거의 없음. VoiceBank-DEMAND 824개 발화에서 fp32 모델 대비 -0.006 PESQ에 그침. 들어서 구분할 수 있는 수준이 아님

■ 적용된 최적화

한 가지 기법으로 3배가 나온 게 아니라 여러 층을 각각 손봤음.

- 양자화: 활성값 범위를 매 프레임 다시 계산함. 그래서 calibration set을 맞추거나 함께 배포할 필요가 아예 없고, 입력 분포가 달라져도 안 깨짐
- 합성곱: k=3 conv에 Winograd F(2,3)를 적용하고, 뒤따르는 에필로그(dequant + bias + SiLU + fp16 write)까지 같은 패스에 접어 넣어 중간 버퍼를 없앰
- 재귀: GRU를 티어당 커널 하나로 완전히 융합함. 입력측 행렬곱, 은닉측 행렬곱, r/z/n 세 게이트, hidden 갱신까지 한 커널에서 끝내서 int32 누산기가 메모리로 새지 않음
- 어텐션: softmax가 int32 점수를 그대로 받아 처리함. fp32 점수 행렬을 아예 만들지 않아서 그만큼의 메모리 왕복이 사라짐
- 메모리: cross-stage 상태(GRU hidden, encoder skip)를 fp16으로 보관해 프레임 간 대역폭을 절반으로 줄임
- 커널: ISA별로 int8 GEMM 커널 6종을 직접 작성하고 초기화 때 자동 선택함 (ARM NEON/DOTPROD/I8MM, x86 AVX2/AVX-VNNI/AVX-512)
- 나머지 최적화 리스트는 프로젝트 Github에서 확인할 수 있음

■ 실시간 안정성

- 37초짜리 벤치마크 한 번으로 끝내지 않고, 실제 오디오 콜백 주기로 30분 연속 돌려서 확인했음
- M2는 30분 내내 프레임 예산 안에 머물렀음 (p99 0.56)

■ 기타

- 외부 의존성 0. cmake + make로 빌드되고 정적 라이브러리는 162 KiB임
- 공개 API는 함수 4개임 (fe\_init / fe\_run / fe\_reset / fe\_free)
- 가중치 blob 565 KB, 파라미터 511,754개
- MIT 라이선스

## 원문
- [원문](https://github.com/kdrkdrkdr/faster-enhancer.c)
- [GeekNews 토론](https://news.hada.io/topic?id=31910)

## My Note
<!-- 한 줄 코멘트 남기기 -->

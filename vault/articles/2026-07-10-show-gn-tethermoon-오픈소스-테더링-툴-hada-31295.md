---
category: AI
collected_at: '2026-07-10T13:28:50+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31295
id: hada-31295
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.693
recommended_on: '2026-07-11'
source: geeknews
tags:
- AI
- Other
- github.com/SpaceDLFactory
title: 'Show GN: TetherMoon - 오픈소스 테더링 툴'
url: https://github.com/SpaceDLFactory/TetherMoon
---

## TL;DR
- 이 글은 Sony A7C 카메라를 위한 오픈소스 테더링 툴 TetherMoon의 기능과 발전 방향을 소개한다.
- 이 툴은 MJPEG 스트리밍, 포커스 피킹, 다양한 촬영 모드 등의 기능을 제공하며, 현재 A7C에만 최적화되어 있다.
- 오픈소스 프로젝트로서 더 많은 기종 지원과 기능 개선이 이루어질 가능성이 있어 사진작가들에게 유용할 수 있다.

## GeekNews 요약
개인프로젝트로 소니 카메라 테더링 툴을 만들고 있습니다.

언제까지고 혼자 깎아내서는 성격상 끝은 끝대로 못보고 흥미를 잃을 것 같아 v1.0으로 정식버전화 합니다.

사실 다른 기종을 이용한 테스트를 진행하지 못해 아직은 a7c에만 대응하는 녀석이긴 하지만은.... 많은 테스트와 사용을 거치며 더 발전해나가도록 하고 싶습니다

---

Sony A7C(ILCE-7C)를 macOS(Apple Silicon)에서 USB로 연결해, 폰·PC 브라우저로 원격 제어하는 테더링 촬영 앱

---

📺 라이브뷰

- MJPEG 실시간 영상 — 폰·PC 동시 접속(다중 클라이언트)
- 포커스 피킹 (엣지 검출) · RGB 히스토그램
- 100% 루페 — 정밀 초점 확인
- 조합형 그리드 — 3분할 · 소실점 · 대각선
- 수동 회전 — 세로 촬영 지원
- 🌙 붉은 야간 모드 — 암순응 보존 (오늘 추가)

🎛️ 노출 · 색

- ISO · 셔터 · 조리개 · EV · WB(+켈빈 슬라이더) · 측광 · 드라이브
- 파일 형식(RAW/JPEG/HEIF) · JPEG 품질 · Picture Profile · 플래시 모드
- 모든 값은 카메라가 허용하는 값 기반 드롭다운으로 제공

🎯 포커스

- MF Near/Far (버튼 · W/S 단축키)
- 탭-투-포커스 + AF D-pad/방향키
- AF 영역 모드 — 와이드 / 존 / 중앙 / 플렉서블(S·M·L) / 트래킹
- 반셔터(S1) 합초
- 소프트웨어 컨트라스트 AF — A7C엔 절대초점 API가 없어 MF 스윕 + 라플라시안 분산으로 직접 구현 (단발 +  
  연속 추적 재합초)
- ⭐ Star AF — 가장 밝은 별/지점 자동 합초 (오늘 추가)
- 추적 AF — CoreML RT-DETR 객체검출 → 박스 선택 추적 (옵션, macOS)

📸 촬영

- 단발 · 연사(누르는 동안) · 동영상 · 취소
- 장노출 1″–30″ · BULB · 소프트웨어 벌브 타이머(1–900초)
- 타임랩스 — 소프트웨어 인터벌
- 노출 브라케팅(AEB) — EV 스텝 다중 촬영 (오늘 추가)
- 소프트웨어 다중노출 — average / lighten / add
- 셀프타이머

💾 저장 · 미리보기

- PC 저장 — 폴더 · 파일명 접두사 지정, SD / PC / PC+SD
- 촬영 미리보기 + 필름스트립 — 최근 12장
- RAW 미리보기 — ARW 임베디드 JPEG 추출 (오늘 추가)
- 배터리 % · 남은 컷 수 표시

🔧 기타

- 자동 연결 + USB 재연결 처리
- 미니멀 리모컨 — 라이브뷰 없이 셔터만(배터리 절약)
- 단일 인스턴스 보장 · graceful shutdown
- 다국어 지원 (en / ko / ja)

## 원문
- [원문](https://github.com/SpaceDLFactory/TetherMoon)
- [GeekNews 토론](https://news.hada.io/topic?id=31295)

## My Note
<!-- 한 줄 코멘트 남기기 -->

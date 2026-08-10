---
category: AI
collected_at: '2026-08-10T09:41:02+09:00'
geeknews_comments: 1
geeknews_score: 8
geeknews_url: https://news.hada.io/topic?id=32321
id: hada-32321
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 10.405
recommended_on: '2026-08-10'
source: geeknews
tags:
- AI
- Other
- github.com/Nutlope
title: hallmark - AI 티가 안나는 디자인 스킬
url: https://github.com/Nutlope/hallmark
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- AI 코딩 어시스턴트가 만드는 뻔한 디자인을 피하기 위해, 타이포/색상/레이아웃/모션/인터랙션에 걸친 **안티 슬롭(anti-AI-slop) 규칙**을 하나로 묶은 디자인 스킬
- 페이지 생성 시 먼저 **매크로구조**를 정하고 테마를 입히는 순서로 동작, **직전 3개 구조 반복을 거부**해 매번 다른 형태의 결과물 작성
- 기본 1개 + 추가 3개, 총 **네 가지 액션** 제공
  - **Default**: UI 생성. 브리프/프로젝트 토큰/프레임워크를 읽고 매크로구조→테마→보강 순으로 생성, 마지막에 슬롭 테스트 실행
  - **Audit**: 페이지 문제점을 안티패턴 카탈로그 기준으로 점수화한 **순위형 펀치 리스트** 제공. 수정 없이 진단만 함
  - **Redesign**: 카피/IA/브랜드는 유지하고 **구조적인 것들만 버려** 새 섹션 리듬/제목 배치로 재구축
  - **Study**: 참고할 디자인을 스크린샷/URL로 넣으면 픽셀이 아니라 구조를 읽어 **DNA**를 추출하고 이식형 `design.md` 생성
- LLM이 기본적으로 만드는 **5가지 슬롭 패턴**들에 대한 대안 제시
  - **보라색 그라디언트 히어로** → 앵커 색상 하나 + 강조색 하나, 히어로 그라디언트 배경 금지. 무채색에 색조 더하기
  - **디스플레이로 쓴 Inter** → 개성 있는 디스플레이 폰트 + 정제된 본문 폰트, 최소 두 개의 폰트페이스를 사용
  - **모든 것 가운데 정렬** → 여백을 한쪽으로 몰아 대칭을 한 번은 깨기
  - **아이콘 타일 피처 카드** → 크기/정렬 다양화하거나 아이콘 빼고 타이포로 시작하는 등 비대칭적 디자인
  - **AI 내비게이션** → 페이지 장르에 맞는 내비 아키타입(신문 마스트헤드, 터미널 명령바 등) 선택
- 모든 테마를 관통하는 **8가지 기초 규칙** 내장 (Type/Colour/Space/Motion/Voice/Layout/Hierarchy/Restraint)
  - OKLCH 팔레트에 강조색은 5% 미만, 4의 배수 간격에 17px 같은 임의 패딩 금지, 모든 애니메이션에 reduced-motion 대안 제공
  - "나쁜 무언가보다 아무것도 없는 편이 낫다"는 **절제(Restraint)** 원칙
- 설치 `npx skills add nutlope/hallmark` (Claude Code, Cursor, Codex 지원)
- 데모 보기 : <https://www.usehallmark.com/>

## 원문
- [원문](https://github.com/Nutlope/hallmark)
- [GeekNews 토론](https://news.hada.io/topic?id=32321)

## My Note
<!-- 한 줄 코멘트 남기기 -->

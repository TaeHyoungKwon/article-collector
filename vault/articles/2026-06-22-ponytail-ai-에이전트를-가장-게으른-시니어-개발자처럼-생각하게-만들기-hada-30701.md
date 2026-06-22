---
category: AI
collected_at: '2026-06-22T09:46:02+09:00'
geeknews_comments: 1
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=30701
id: hada-30701
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 7.817
source: geeknews
tags:
- AI
- Other
- github.com/DietrichGebert
title: ponytail - AI 에이전트를 가장 게으른 시니어 개발자처럼 생각하게 만들기
url: https://github.com/DietrichGebert/ponytail
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
> "최고의 코드는 작성하지 않은 코드"  
> "알죠? **긴 포니테일**에 타원형 안경을 쓴 그 사람. **버전 관리 시스템보다 더 오래 회사에 다닌 사람**. 당신이 코드 50줄을 보여주면, 그는 **아무 말 없이 1줄로 바꿔버리죠**" - ponytail은 그를 당신의 AI 에이전트 안에 넣어드립니다.

- AI 코딩 에이전트에게 **불필요한 코드를 쓰지 않게 하는 스킬셋**을 주입해, 작업에 필요한 최소한의 코드만 남기게 하는 도구
- 코드 작성 전 **6단계 점검 단계**를 통해 멈춰 세움
  - 이게 진짜 존재할 필요 있나 → **아니오: 스킵함(YAGNI)**
  - **표준 라이브러리**로 되나 → 사용
  - **네이티브 플랫폼** 기능이 있나 → 사용
  - **설치된 의존성**으로도 되나 → 사용
  - **한 줄**인가 → 한줄로 처리
  - 그러고 나서는: **동작에 필요한 최소한의 코드**를 작성
- **게으르되 부주의하지는 않음** — 신뢰 경계 검증, 데이터 손실 처리, 보안, 접근성은 절대 생략하지 않음
  - 코드가 작아지는 건 **코드 골프**가 아니라 필요한 만큼만 쓰기 때문
- Before/After 사례:
  - 날짜 선택기를 요청하면 일반 에이전트는 flatpickr 설치·래퍼 컴포넌트·스타일시트·타임존 논의까지 시작하지만, ponytail은 `<input type="date">` **한 줄로 처리**
  - 날짜 선택기 404줄 → 23줄, 컬러 선택기 287줄 → 23줄
- 실제 저장소(FastAPI + React) 편집 작업 측정 결과
  - **코드량 약 54% 감소**(과잉 설계 함정에서 최대 94%), 비용 약 20% 절감, 속도 약 27% 향상, 안전성 100% 유지
  - 모든 지표를 감소시키면서 완전한 안전성을 유지한 유일한 방식
- **명령어 리스트**:
  - `/ponytail [lite|full|ultra|off]` 강도 조절
  - `/ponytail-review` 현재 diff에 대해 **오버-엔지니어링**인지 검토 후 삭제 목록 반환
  - `/ponytail-audit` 저장소 전체에 대한 오버-엔지니어링 **감사**. 단순 diff 아님
  - `/ponytail-debt` 미뤄둔 `ponytail:` 주석 들을 장부(ledger)로 수집 — "나중에"가 "영영 안 함"이 되지 않도록
  - `/ponytail-gain` 벤치마크 결과를 바탕으로 측정된 임팩트 점수표(코드 감소, 비용 절감, 속도 향상) 표시
- Claude Code, Codex, Cursor, Windsurf, Gemini CLI 등 **14개 에이전트와 호환**, 기본 모드는 `full`
- MIT 라이선스

## 원문
- [원문](https://github.com/DietrichGebert/ponytail)
- [GeekNews 토론](https://news.hada.io/topic?id=30701)

## My Note
<!-- 한 줄 코멘트 남기기 -->

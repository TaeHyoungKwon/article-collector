---
category: AI
collected_at: '2026-07-31T03:02:34+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31995
id: hada-31995
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- blog.cryptographyengineering.com
title: Anthropic의 새로운 AI 암호분석 결과에 대한 평가
url: https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 미공개 고급 모델 **Claude Mythos**가 HAWK 키 복구 공격과 7라운드 AES 공격 개선안을 만들어, 기존 암호분석 기법을 이해·결합·확장하는 AI의 능력을 보여줌
- **HAWK 공격**은 배포된 체계를 즉시 깨지는 않지만 보안 비트 수를 대략 절반으로 낮춤. 키 크기를 두 배로 늘릴 수 있으나 효율성이 떨어져 표준화 가능성도 매우 낮아짐
- **AES 결과**는 전체 10·12·14라운드가 아닌 7라운드 변형을 대상으로 하며, 2013년 연구를 상수 배수 수준으로 개선한 비실용적 공격이어서 실제 AES 보안에는 직접적인 변화가 없음
- 모델이 그럴듯하지만 잘못된 결과도 쉽게 만들기 때문에 **검증 가능성**이 병목이 됨. 실행 코드나 단순 반례는 확인하기 쉽지만 이론적 속도 개선은 전문가 검토가 필요하며, Lean 증명도 정리의 구성 방식까지 사람이 확인해야 함
- 구조적 난제의 수가 제한된 **공개키·양자내성 암호**는 AI가 기존 도구를 폭넓게 적용하기 좋은 영역임. 고급 연구에서 갑자기 무능해지는 경계가 아직 남아 있지만 빠르게 바깥으로 이동하고 있음

---

## 원문
- [원문](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/)
- [GeekNews 토론](https://news.hada.io/topic?id=31995)

## My Note
<!-- 한 줄 코멘트 남기기 -->

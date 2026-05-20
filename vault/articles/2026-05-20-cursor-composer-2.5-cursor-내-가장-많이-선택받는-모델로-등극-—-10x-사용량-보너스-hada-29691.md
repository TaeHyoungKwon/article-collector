---
category: AI
collected_at: '2026-05-20T10:53:13+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29691
id: hada-29691
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 5.594
recommended_on: '2026-05-20'
source: geeknews
tags:
- AI
- Other
- x.com/mntruell
title: Cursor Composer 2.5, Cursor 내 가장 많이 선택받는 모델로 등극 — 10x 사용량 보너스
url: https://x.com/mntruell/status/2056780569380626686?s=46
---

## TL;DR
- 이 글은 Cursor의 새로운 모델 Composer 2.5이 사용자들 사이에서 가장 많이 선택받게 된 것을 다룬다.
- Composer 2.5는 강화학습과 저렴한 가격으로 인해 빠른 채택률을 기록하며, 기존 모델과의 성능 차이를 최소화했다.
- 이는 사용자들이 경제성과 효율성을 중시하는 현재의 AI 시장에서 Cursor의 경쟁력을 높일 수 있는 중요한 발전이다.

## GeekNews 요약
- Cursor CEO Michael Truell가 X에 “Composer 2.5가 Cursor에서 가장 많이 선택되는 모델이 됐다. 하루 동안 모든 사용자에게 10배 사용량을 제공한다” ￼고 발표
- 출시 직후 채택률이 빠르게 올라간 신호로, Anthropic/OpenAI 모델을 두고 자체 모델이 디폴트로 선택받는 흐름

Composer 2.5 핵심 요약  
• 5월 18일 공식 출시된 Cursor의 3세대 자체 agentic coding 모델 ￼  
• Composer 2와 동일한 Moonshot AI의 오픈소스 Kimi K2.5를 베이스로 사용, 이번에는 발표 첫 문단에서 명시적으로 밝힘 (3월에 Kimi base를 명확히 공개하지 않아 비판받았던 점을 의식한 조치) ￼  
• 전체 컴퓨트의 85%가 Cursor 자체 강화학습 파이프라인과 post-training에 투입, Composer 2 대비 25배 많은 synthetic coding tasks 사용 ￼  
• long-horizon 작업에서 신뢰성을 높이기 위해 “텍스트 피드백 기반 targeted RL”을 도입 — 긴 rollout 끝에 단일 reward만 주는 대신, 잘못된 tool call이 발생한 구체 지점에 직접 힌트를 주입해 credit assignment를 정밀화 ￼  
벤치마크 (Composer 2.5 vs Opus 4.7 vs GPT-5.5 vs Composer 2)  
• Terminal-Bench 2.0: 69.3% vs 69.4% vs 82.7% vs 61.7% ￼ — Opus 4.7과 사실상 동률, GPT-5.5에 약 13점 차로 뒤짐  
• SWE-Bench Multilingual: 79.8% vs 80.5% vs 77.8% vs 73.7% ￼ — Opus 4.7에 0.7점 차, GPT-5.5보다 우위  
• CursorBench v3.1 (default setting): Composer 2.5 63.2%, Opus 4.7 xhigh default 61.6%, GPT-5.5 medium default 59.2% ￼ — 실제 개발자가 쓰는 디폴트 설정에서는 프론티어 모델 둘 다 추월  
가격 — 가장 강력한 무기  
• Standard tier: 인풋 $0.50/M, 아웃풋 $2.50/M. Fast tier(인터랙티브 디폴트): 인풋 $3.00/M, 아웃풋 $15.00/M ￼  
• SWE-Bench Multilingual에서 Opus 4.7과 동급 성능을 내면서 Anthropic 가격의 약 1/10 ￼  
• CursorBench 기준 63% 정확도를 달성하면서 평균 task 비용이 $1 미만 — 동급 성능의 Opus/GPT는 task당 몇 달러 더 비쌈 ￼  
함께 공개된 큰 그림  
• Cursor는 Composer 2.5와 별개로, xAI 인프라(SpaceXAI)와 함께 Colossus 2의 약 100만 H100급 GPU를 활용해 10배 더 큰 모델을 처음부터 학습 중이라고 발표 (출시일 미정) ￼  
• CEO Michael Truell에 따르면, 현재 Cursor 내부에서 머지되는 PR의 35%가 autonomous agent로 생성 ￼  
• Claude Code가 ARR 25억 달러, 비즈니스 고객 30만 곳을 돌파하며 Cursor를 압박해 온 상황에서 자체 모델로 반격하는 모양새 ￼  
활용 제약 / 코멘트  
• Composer 2.5는 Cursor IDE, Cursor CLI, Cursor 웹에서만 사용 가능 — 외부 API, HuggingFace 미러, 서드파티 게이트웨이 없음 ￼  
• Kimi K2.5 기반이라는 점은 규제 산업이나 federal 관련 업무에서는 여전히 고려 요소 ￼  
• “IDE wrapper”로 시작한 Cursor가 본격적인 model lab으로 전환 중임을 보여주는 릴리스. 같은 base에서 post-training만으로 +6pt 이상 끌어올린 사례로, “vertical RL이 raw scale을 어디까지 이길 수 있는가”의 좋은 데이터포인트  
• 출처: X (@mntruell), Cursor: Introducing Composer 2.5, OfficeChai

## 원문
- [원문](https://x.com/mntruell/status/2056780569380626686?s=46)
- [GeekNews 토론](https://news.hada.io/topic?id=29691)

## My Note
<!-- 한 줄 코멘트 남기기 -->

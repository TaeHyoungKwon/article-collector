---
category: AI
collected_at: '2026-07-16T10:47:47+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31485
id: hada-31485
matched_keywords:
- AI
- LLM
- Codex
read: false
recommend_score: 6.693
source: geeknews
tags:
- AI
- Other
- ai-watch.dev
title: 'Show GN: Claude 공식 업타임 99.55%인데 6월 인시던트 45건 — 6월 AI 서비스 신뢰도 리포트'
url: https://ai-watch.dev/reports/2026-06/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
**AIWatch**는 Claude·OpenAI·Gemini 등 **41개 AI 서비스**(LLM API·코딩 에이전트·음성·인프라·AI 앱)의 업타임·인시던트·지연을 실시간으로 모니터링합니다. 6월 리포트(6/1–30)를 공개했습니다.

- 리포트: <https://ai-watch.dev/reports/2026-06/>
- 실시간 대시보드: <https://ai-watch.dev>

#### 핵심 3가지

1. **41개 중 35개가 최소 1건 장애, 총 다운타임 712시간 26분.** 6월은 양극화가 뚜렷했습니다. Windsurf·Modal·Groq Cloud는 높은 안정성을 유지한 반면, Deepgram은 가장 고전했습니다(장애 6건, 다운타임 45시간 33분, 최장 27시간).
2. **업타임 숫자만으론 신뢰도를 못 봅니다.** Claude는 공식 업타임 99.55%인데 인시던트가 45건 발생해 AIWatch 점수는 Fair 67. 반대로 Windsurf는 장애 0건으로 100점. AIWatch는 provider가 발표한 업타임 %를 그대로 베끼지 않고, 각 provider의 공식 인시던트 기록에서 동일한 창(30일)·동일한 공식으로 직접 계산합니다. 그래서 우리 수치가 provider 상태페이지의 %와 다를 수 있습니다(의도된 것).
3. **공식 상태페이지가 안 알리는 지연을 직접 측정으로 잡았습니다.** 프로브 가능한 32개 엔드포인트를 정해진 스케줄로 RTT 측정한 결과, 6월 지연 악화 102건 중 99건이 공식 상태페이지에 없었습니다(Mistral 41, Replicate 25). 완전 다운이 아니라 서서히 느려지는 유형이라 가동/중단만 표시하는 상태페이지엔 잘 안 뜹니다.

#### 6월 AIWatch Score 랭킹

| 순위 | 서비스 | 점수 | 등급 |
| --- | --- | --- | --- |
| 1 | Windsurf | 100 | Excellent |
| 2 | Modal | 94 | Excellent |
| 3 | Junie | 93 | Excellent |
| 4 | Groq Cloud | 91 | Excellent |
| 5 | Cohere API | 89 | Good |
| … | OpenAI API | 87 | Good |
| … | Claude (Anthropic 계열) | 66–69 | Fair |
| 최하위 | Deepgram | 45 | — |

*41개 중 30개 랭킹. Bedrock·Azure OpenAI·Character.AI는 공식 업타임·프로브가 없어 점수를 유보. 8개는 월 중간 추가라 다음 달 합류.*

**AIWatch Score(0–100)** = 업타임 40% + 인시던트 영향일 25% + 복구 속도 15% + 응답성(직접 프로브 RTT) 20%. "프로덕션에서 뭘 믿고 쓸 수 있나"를 한 숫자로 답하는 지표입니다.

#### 용도별 추천

- 무중단이 중요하면 → **Windsurf / Modal**
- 응답 속도가 중요하면 → **Groq Cloud** (205ms)
- 코딩 도구는 → **GitHub Copilot** (이달 최대 개선 69→86)
- 음성·STT는 → **AssemblyAI** (76)
- 두루 쓰기엔 → **OpenAI API** (87)

#### 한 가지 정직하게

Codex는 이달 다운타임 91시간으로 보이지만, 그중 72시간은 "사용량 한도" 공지가 상태페이지에 다운타임으로 집계된 것 — 실제 가용성 저하가 아닙니다.

## 원문
- [원문](https://ai-watch.dev/reports/2026-06/)
- [GeekNews 토론](https://news.hada.io/topic?id=31485)

## My Note
<!-- 한 줄 코멘트 남기기 -->

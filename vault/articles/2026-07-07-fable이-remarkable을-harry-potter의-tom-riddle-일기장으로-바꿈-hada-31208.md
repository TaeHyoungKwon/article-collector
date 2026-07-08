---
category: AI
collected_at: '2026-07-07T15:33:37+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31208
id: hada-31208
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-07-08'
source: geeknews
tags:
- AI
- Other
- github.com/MaximeRivest
title: Fable이 reMarkable을 Harry Potter의 Tom Riddle 일기장으로 바꿈
url: https://github.com/MaximeRivest/Riddle
---

## TL;DR
- 이 글은 Fable 앱이 reMarkable을 Harry Potter의 Tom Riddle 일기장처럼 바꾸는 기술적 과정에 대해 설명한다.
- 앱은 펜으로 쓴 글씨가 사라졌다가 LLM이 이를 인식해 다시 나타나게 하는 기능을 제공한다.
- 이러한 기능은 사용자에게 새로운 필기 경험을 제공하며, 창의적인 작업에 도움을 줄 수 있는 가능성을 제시한다.

## GeekNews 요약
- **riddle**은 reMarkable Paper Pro에서 펜으로 쓴 글씨가 잠시 뒤 사라지고, Tom Riddle의 일기장처럼 답변이 손글씨 획으로 다시 쓰였다가 사라지는 앱임
- 동작 흐름은 펜 입력을 받아 2.8초 유휴 후 페이지를 PNG로 확정하고, **비전 LLM**이 손글씨를 읽어 문장 단위로 답변을 스트리밍하는 방식임
- 설치는 **remagic**을 통한 설치가 가장 쉽고, 사전 빌드 번들 설치나 소스 빌드도 가능하지만 reMarkable Paper Pro 개발자 모드와 런처가 필요함
- 앱은 root로 실행되고 takeover 모드에서는 vendor UI를 중지한 뒤 e-ink 엔진을 직접 구동하며, 테스트 범위는 **reMarkable Paper Pro** ferrari, aarch64, OS 3.26–3.27로 제한됨
- LLM 백엔드는 OpenAI 호환 `/chat/completions` API 또는 resident `pi --mode rpc` 프로세스를 사용할 수 있으며, 기기 수정과 vendor 라이브러리 사용은 사용자가 직접 감수해야 함

---

## 원문
- [원문](https://github.com/MaximeRivest/Riddle)
- [GeekNews 토론](https://news.hada.io/topic?id=31208)

## My Note
<!-- 한 줄 코멘트 남기기 -->

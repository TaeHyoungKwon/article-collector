---
category: AI
collected_at: '2026-05-27T10:09:53+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29915
id: hada-29915
matched_keywords:
- AI
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- github.com/AI-Ocean
title: 'Show GN: GPU-Usage-Audit: GPU가 그냥 노는 게 아니라 &#039;잡아둔 채&#039; 놀고 있다면?!'
url: https://github.com/AI-Ocean/gpu-usage-audit
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
nvidia-smi에 util 1%로 찍히면 카드가 비어 보이지만,  
누가 주피터 노트북에 8GB 올려두고 자리를 비우면 그 GPU는 아무도 못 씁니다.  
공유 서버나 시간당 과금 GPU에서는 보이지 않는 낭비죠.

그래서 만들었습니다. GPU-Usage-Audit!

NVIDIA 드라이버만 깔려있다면 GPU 메트릭을 SQLite에 기록해두고 나중에 리포트로 뽑아줍니다.

GPU 사용 시간을 둘이 아니라 셋으로 나눠서 리포트를 뽑습니다.  
실제로 연산하는 시간, 완전히 비어 있는 시간, 그리고 메모리는 잡고 있지만 연산은 안 하는 'idle-held' 시간입니다.

대부분의 도구는 뒤의 둘을 하나로 묶어버리는데, 낭비는 바로 거기 숨어 있습니다.  
잡아둔 시간을 GPU-hours로 환산하고, 유저별로 실행하고 있다면 누가 얼마나 점유하고 있는지도 같이 보여줍니다.

설치와 실행은 `uv tool install gpu-usage-audit && gua daemon`한줄!

데이터가 쌓인 뒤 `gua report`만 치면 리포트를 볼 수 있고,  
데이터 없이 결과부터 보고 싶으면 `gua demo`로 가짜 데이터를 돌려볼 수 있습니다.

## 원문
- [원문](https://github.com/AI-Ocean/gpu-usage-audit)
- [GeekNews 토론](https://news.hada.io/topic?id=29915)

## My Note
<!-- 한 줄 코멘트 남기기 -->

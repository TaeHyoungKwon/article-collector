---
category: AI
collected_at: '2026-07-06T10:42:39+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31168
id: hada-31168
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
source: geeknews
tags:
- AI
- Other
- trillion-labs.github.io
title: 메모리 아끼면서 Cross Entropy Loss 계산하기
url: https://trillion-labs.github.io/blog/posts/fused-linear-cross-entropy/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
긴 context, 큰 vocab의 LLM 학습에서 LM head + cross entropy가 왜 가장 큰 메모리 소비처 중 하나가 되는지 짚어본 글. 128K context에서는 logits 텐서 하나가 40GB에 육박해서, 모델 weight보다도 커진다.

16B 모델을 128K context로 학습하다 실제로 겪은 OOM에서 출발해, cross entropy의 forward/backward를 처음부터 유도하고, sequence 축을 단순히 chunk로 쪼개는 방식이 왜 peak memory를 못 낮추는지(autograd가 chunk별 graph를 backward까지 붙잡고 있음) 보인 뒤, FLCE가 각 chunk의 gradient를 forward pass 안에서 바로 계산해 큰 텐서가 graph에 남지 않게 하는 방법을 설명한다. 마지막엔 memory/latency tradeoff 분석과 실제 kernel 구현 walkthrough까지 다룬다.

## 원문
- [원문](https://trillion-labs.github.io/blog/posts/fused-linear-cross-entropy/)
- [GeekNews 토론](https://news.hada.io/topic?id=31168)

## My Note
<!-- 한 줄 코멘트 남기기 -->

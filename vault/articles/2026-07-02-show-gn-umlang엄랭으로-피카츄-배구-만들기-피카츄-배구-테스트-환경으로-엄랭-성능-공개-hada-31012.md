---
category: AI
collected_at: '2026-07-02T01:52:57+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31012
id: hada-31012
matched_keywords:
- AI
- Codex
read: false
recommend_score: -995.307
recommended_on: '2026-07-01'
source: geeknews
tags:
- AI
- Other
- github.com/NomaDamas
title: 'Show GN: Umlang(엄랭)으로 피카츄 배구 만들기 + 피카츄 배구 테스트 환경으로 엄랭 성능 공개'
url: https://github.com/NomaDamas/umkachu-volleyball-umlang.git
---

## TL;DR
- 이 글은 UmLang(엄랭)으로 피카츄 배구 게임을 구현한 과정을 다룬다.
- Codex가 41시간 만에 피카츄 배구를 완성하며, 엄랭의 성능이 메이저 언어와 비교해 흥미로운 결과를 나타냈다.
- 엄랭을 통한 프로그래밍 언어의 가능성은 한국어 기반 AI 개발에 새로운 시사점을 제공한다.

## GeekNews 요약
41h만에 완성된 Umkachu Volleyball을 소개합니다!

Codex가 과연 UmLang(엄랭-인터넷 밈으로 만들어진 프로그래밍 언어)으로 피카츄배구를 만들 수 있을까?

codex가 41h만에 완성을 했습니다. 근데 난해한 이 엄랭으로 codex가 왜 잘하죠???

4년전에 유행했던 엄준식밈을 아시나요?  
엄준식이라는 밈을 기반으로 프로그래밍 언어를 새로 만든 프로젝트가 있었습니다.  
c++이나 python, rust처럼 메이저한 언어가 아닌 난해한 엄랭으로 피카츄 배구를 만들어보면 어떨까요?

피카츄 배구를 Umlang으로 포팅을 해봤습니다. 근데 왜 잘하죠? codex는 엄랭을 알고 있는것 같습니다 ㄷㄷ

근데 여기서 끝나면 재미없잖아요?  
그래서 피카츄 배구를 테스트 환경으로 Umlang(엄준식랭귀지)을 벤치마크 해봤습니다.  
평가 기준은 headless 처리량으로 창/그래픽/오디오를 빼고, 내부 로직이 얼마나 빨리 도는지 봤습니다.

평가 부분은

1. 피카츄 배구를 Umlang VS Rust VS Node 3개로 포팅했을때의 비교와
2. 피카츄배구를 Umlang rust버전, Umlang python 버전, Umlang Node 버전으로 포팅했을때의 성능을 비교했습니다.

결과적으로 피카츄 배구를

- Rust 직접 포팅 > JS 포트(원본버전) > 엄카츄 Rust VM > 엄카츄 Node VM > 엄카츄 Python VM

의 성능 순서대로 찍혔네요. 모든 버전의 포팅에서는 게임플레이하는데에는 모두 지장이 없었습니다.

최적화만 더 잘되면 한국어 체계와 뉘앙스가 들어가있는 프로그래밍 언어가 생기고, 이것을 소버린 AI가 할 수 있게 된다면 어떨까요?

코딩에이전트도 한국어 체계가 한국인의 사고구조가 녹아들어간 프로그래밍 언어를 학습되었을때 한국인이 프롬프트를 넣고 시킬때 코딩에이전트를 더 잘 다루고 고품질의 결과가 나오지 않을까요?

엄랭을 피카츄배구를 재미로 시작했지만 저에게 소버린 AI에 대해서 여러 질문을 던져준 프로젝트였습니다.  
재밌으셨다면 star 부탁드립니다!!  
더 Geek한 프로젝트로 찾아뵙겠습니다! 😀

## 원문
- [원문](https://github.com/NomaDamas/umkachu-volleyball-umlang.git)
- [GeekNews 토론](https://news.hada.io/topic?id=31012)

## My Note
<!-- 한 줄 코멘트 남기기 -->

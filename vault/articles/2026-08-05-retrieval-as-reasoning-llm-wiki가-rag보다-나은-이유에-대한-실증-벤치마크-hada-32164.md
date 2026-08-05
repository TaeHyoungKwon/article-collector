---
category: AI
collected_at: '2026-08-05T11:06:55+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32164
id: hada-32164
matched_keywords:
- AI
- LLM
- RAG
- Claude Code
read: false
recommend_score: 8.693
source: geeknews
tags:
- AI
- Other
- arxiv.org
title: Retrieval as Reasoning - LLM Wiki가 RAG보다 나은 이유에 대한 실증 벤치마크
url: https://arxiv.org/abs/2605.25480
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
문서를 청크 단위로 잘라 벡터로 검색하는 RAG 방식이 아닌,  
서로 링크된 마크다운 위키로 만들고 에이전트가 네비게이션하는 LLM Wiki 방식이 나은 이유에 대해 실증한 논문입니다.

### 논문이 풀어본 문제

- 청크 검색은 문서를 잘게 잘라 비슷한 조각 몇 개만 꺼내 붙임. 여러 문서를 이어야 답이 나오는 멀티홉 질문에서 약함
- 조각으로 자르는 순간 조각들 사이의 **관계가 사라짐**. 이것이 근본적인 한계
- 논문은 검색을 '조각 꺼내기'가 아니라 **'추론'** 으로 접근. 위키를 미리 구성해 두고, 읽고 → 링크 따라가고 → 모자라면 다시 검색하며 여러 번 되짚어 답을 맞춰 감

### 핵심 요약

- **컴파일**: 원문서를 양방향 링크가 걸린 위키 페이지로 변환 (검색하는 단위가 청크가 아니라 링크된 페이지)
- **세 가지 도구**: 검색(search)·읽기(read)·링크 따라가기(link)를 표준 도구로 정의
- **Error Book**: 위키의 구조·의미 오류를 계속 스스로 고침
- **자가 진화**: 쓸수록 위키 자체가 나아짐

### 벤치마크 결과

- 멀티홉 QA 세 종류에서 기준 모델들보다 **2.0~8.1 F1** 앞섬
- 별도 벤치마크 AuthTrace에서도 정확도 1위. 특히 여러 문서를 엮는 질문에서 강함

### 가장 주목할 대목 — Ablation (F1 손실, HotpotQA / MuSiQue / 2Wiki)

- **순회를 뺐을 때**: −11.7 / −13.8 / −12.2 (가장 치명적)
- **위키 구조를 뺐을 때**: −6.1 / −7.0 / −6.7
- **Error Book을 뺐을 때**: −3.8 / −4.0 / −3.4
- 순서로 보면 순회 > 구조 > 교정. 순회가 구조보다 두 배쯤 중요함

### 관련 오픈소스 프로젝트

- 출발은 Karpathy가 제시한 'LLM Wiki' 개념을 구현하되 마크다운 위키 형태로 지식을 축적하고 관리하는 지식 팩토리를 Claude Code 기반으로 운영 중 : <https://news.hada.io/topic?id=31691>
- **본 논문을 구현한 것은 아님**. 논문은 나중에 알게 됨
- 논문에 비춰보니 **위키 '구조'엔 오랜 시간 공들였는데, 정작 ablation이 제일 중요하다는 '순회'(에이전트가 쓰기 전에 뭘 얼마나 읽느냐)는 지침 딱 한 줄**이었음

### 추가한 것 — 읽기 사다리(GROUND Ladder)

- 에이전트가 위키 페이지를 **쓰기 전에** 얼마나 읽을지를 다섯 단계로 나눔: ① 페이지가 적어둔 의존성 → ② 인덱스 → ③ 빌드가 미리 계산해둔 링크 → ④ 콘텐츠 검색 → ⑤ 위키 전체
- 위 단계로 올라가는 건 순서대로가 아님. '지금 근거가 모자란다'는 신호가 있을 때만 그 신호가 가리키는 칸으로 바로 감
- 논문은 순회를 '답 만들 때' 썼지만, 오픈소스 프로젝트에서는 '읽어 들일 때' 지키는 규칙으로 가져옴
- 자세한 설명: [https://github.com/alfadur7/llm-wiki-newsroom/…](https://github.com/alfadur7/llm-wiki-newsroom#before-the-loops--the-ground-ladder)

### 아직 부족한 점

- 읽기 사다리는 이제 막 구현하였고 **효과를 아직 측정하기 전**.
- 읽기 단계를 올라가다 멈추는 기준도 잠정 수치고 두세 번 돌려 데이터가 쌓이면 기준을 다듬을 예정

### 링크

- 논문 (arXiv:2605.25480): <https://arxiv.org/abs/2605.25480>
- 오픈소스 레포: <https://github.com/alfadur7/llm-wiki-newsroom>
- 규칙 원문(SoT): [https://github.com/alfadur7/llm-wiki-newsroom/…](https://github.com/alfadur7/llm-wiki-newsroom/blob/main/.claude/agents/README.md)

## 원문
- [원문](https://arxiv.org/abs/2605.25480)
- [GeekNews 토론](https://news.hada.io/topic?id=32164)

## My Note
<!-- 한 줄 코멘트 남기기 -->

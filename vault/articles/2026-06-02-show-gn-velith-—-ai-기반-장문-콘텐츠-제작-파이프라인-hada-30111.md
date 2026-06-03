---
category: AI
collected_at: '2026-06-02T14:42:21+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30111
id: hada-30111
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: -991.307
recommended_on: '2026-06-02'
source: geeknews
tags:
- AI
- Other
- github.com/epicsagas
title: 'Show GN: Velith — AI 기반 장문 콘텐츠 제작 파이프라인'
url: https://github.com/epicsagas/Velith
---

## TL;DR
- Velith는 AI 기반의 장문 콘텐츠 제작을 위한 워크플로우로, Obsidian과 연계하여 장기적인 문서 작성을 지원한다.
- 이 시스템은 프롬프트 하나로 단순히 책을 생성하는 것이 아니라 집필 과정을 단계별로 지원하고, 사용자 판단을 포함하는 방식으로 진행된다.
- 정리된 자료를 바탕으로 빠른 초안 작성을 원하는 사용자에게 유용하며, AI 활용을 통해 효율적인 문서 제작 프로세스를 제공한다.

## GeekNews 요약
안녕하세요.

원래는 책을 만들려고 시작한 프로젝트가 아니었습니다.

평소에 Obsidian으로 지식을 관리하면서 Claude Code 같은 AI 에이전트와 연결해 문서 정리나 기술 리포트 생성에 활용하고 있었습니다. 노트들을 분석해서 연결 관계를 정리하거나, 특정 주제에 대한 기술 문서를 자동으로 생성하는 식이었습니다.

어느 날 문득 이런 생각이 들었습니다.

> Obsidian에 쌓아둔 노트들이 이미 수백 개인데, 이걸 가지고 책을 만들 수 있지 않을까?

그래서 처음엔 기술 리포트 생성 워크플로우를 만들었습니다. 그 다음엔 백서, 튜토리얼, 논픽션, "어디까지 가능한지 보자"는 마음으로 여러 장르를 계속 추가하다 보니 어느새 단순한 문서 생성기가 아니라 아이디어부터 출판 결과물까지 이어지는 책 집필 파이프라인이 되어 있었습니다.

그렇게 정리해서 Velith라는 이름으로 공개했습니다.

GitHub: <https://github.com/epicsagas/Velith>

### 어떤 프로젝트인가요?

Velith는 AI 에이전트 환경에서 동작하는 장문 콘텐츠 제작 워크플로우입니다. Claude Code를 주로 사용해서 개발했지만, Codex CLI나 Antigravity 같은 에이전트 환경에서도 동작합니다.

단순히 프롬프트 한 번으로 책을 생성하는 방식이 아니라, 사람이 실제로 집필하는 과정을 최대한 따라가도록 설계했습니다.

```
/book-ideation   → 주제 탐색 및 컨셉 정리  
/book-outline    → 목차 및 구성 설계  
/book-draft      → 챕터별 초안 작성  
/book-edit       → 문체·일관성 교정  
/book-publish    → EPUB / PDF 출력
```

명령 하나로 에이전트가 해당 단계를 처리하고, 다음 단계로 넘어갈지는 사람이 판단하는 방식입니다.

### 어디서 쓸 때 결과가 좋은가

Obsidian 볼트나 이미 자료를 수집해둔 워크스페이스가 있을 때 결과가 확연히 좋아집니다. 특히 Zettelkasten이나 LLM Wiki처럼 노트 간 연결이 잡혀 있을 때 에이전트가 맥락을 더 잘 따라가는 경향이 있었습니다. 직접 Zettelkasten으로 운영 중인 볼트에서 테스트했고, 산발적으로 모아둔 클리핑만 있을 때보다 결과가 눈에 띄게 달랐습니다.

AI가 맨땅에서 책을 써주길 기대하는 용도보다는, 이미 정리해둔 노트·리서치·메모를 가지고 구조화된 결과물로 만드는 워크플로우에 더 가깝습니다. 쌓아둔 자료는 많은데 책이나 문서로 정리하지 못하고 있는 경우에 가장 잘 맞습니다.

### 어디까지 해봤나

실제로 100페이지가 넘는 결과물을 뽑아봤습니다. 기술서, 픽션, 에세이 장르 모두 시도해봤고, EPUB·PDF 출력까지는 잘 됩니다.

다만 솔직히 말하면, 지금 나오는 결과물은 "읽을 수는 있지만 완벽하진 않다"는 수준입니다. 특히 EPUB·PDF는 바로 쓰기엔 많이 부족하고 손이 많이 갑니다. 초안을 빠르게 뽑고 사람이 다듬는 워크플로우에 더 맞습니다.

#### 앞으로

아직 개인적으로 재미있어서 계속 만들고 있는 프로젝트라 부족한 부분이 많습니다.

Obsidian이나 노션 등 개인 지식베이스를 운영하면서 "이걸 언젠가 책으로 만들어야지"라고 생각만 하고 있는 분, 또는 AI 에이전트로 긴 문서를 써봤는데 중간에 맥락이 끊겨서 답답했던 경험이 있는 분이라면 이야기 나눠보고 싶습니다.

피드백 환영합니다.

[한국어 문서](https://github.com/epicsagas/Velith/blob/main/docs/i18n/README.ko.md)

## 원문
- [원문](https://github.com/epicsagas/Velith)
- [GeekNews 토론](https://news.hada.io/topic?id=30111)

## My Note
<!-- 한 줄 코멘트 남기기 -->

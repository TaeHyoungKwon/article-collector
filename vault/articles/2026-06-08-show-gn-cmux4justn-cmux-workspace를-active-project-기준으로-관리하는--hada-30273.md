---
category: AI
collected_at: '2026-06-08T10:18:51+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30273
id: hada-30273
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/bssm-oss
title: 'Show GN: cmux4justn - cmux workspace를 active project 기준으로 관리하는 macOS CLI'
url: https://github.com/bssm-oss/cmux4justn
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
저는 요즘 여러 AI CLI들을 cmux 위에 띄워놓고 사용합니다. cmux를 쓰면서 여러 프로젝트를 열어두다 보니, “지금 작업 중인 프로젝트 목록”과 cmux workspace 목록이 쉽게 어긋나는 문제가 있었습니다.

cmux4justn은 말 그대로 저를 위한 도구입니다. c4j라는 CLI로 active project symlink registry와 cmux workspace를 동기화하는 작은 macOS용 Bash 도구입니다.

### 주요 기능

- `c4j add .` 로 현재 프로젝트를 active 목록에 추가
- `c4j list` 로 active projects를 표 형태로 확인
- `c4j sync` 로 변경사항 미리보기
- `c4j sync --apply` 로 cmux workspace 생성
- `c4j delete .` 로 active symlink 제거 및 대응 cmux workspace close
- workspace title prefix 설정
- pinned anchor workspace 보장
- 한 줄 설치 지원

### 설치

`curl -fsSL https://raw.githubusercontent.com/bssm-oss/cmux4justn/… | bash`

### 사용법

```
c4j add .  
c4j list  
c4j sync  
c4j sync --apply  
c4j delete .  
c4j anchor
```

### 출력 예시

```
PROJECT               PATH  
--------------------  ----  
c4j                   /Users/justn/Workspaces/repos/justn-hyeok/cmux4justn  
CodeAgora             /Users/justn/Workspaces/repos/bssm-oss/main/justn-hyeok/CodeAgora  
commander-agents      /Users/justn/Workspaces/repos/bssm-oss/main/justn-hyeok/commander-agents
```

macOS 전용, Bash 기반으로 가볍게 동작합니다. cmux를 쓰는 분들께 특히 유용할 것 같습니다.

Repo: <https://github.com/bssm-oss/cmux4justn>

지속적으로 제가 직접 쓰면서 필요한 기능들을 추가하고, 고쳐야할 부분들을 수정하고 있습니다.

## 원문
- [원문](https://github.com/bssm-oss/cmux4justn)
- [GeekNews 토론](https://news.hada.io/topic?id=30273)

## My Note
<!-- 한 줄 코멘트 남기기 -->

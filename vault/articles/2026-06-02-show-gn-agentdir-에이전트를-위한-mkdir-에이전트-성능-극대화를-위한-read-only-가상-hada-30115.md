---
category: Other
collected_at: '2026-06-02T17:54:45+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30115
id: hada-30115
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- github.com/nomadamas
title: 'Show GN: AgentDir - 에이전트를 위한 mkdir - 에이전트 성능 극대화를 위한 read-only 가상 파일 시스템'
url: https://github.com/nomadamas/agentdir
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 폴더 구조의 convention이 명확한 코드 베이스와 달리, 실제 업무의 워드, pptx 등의 폴더 구조는 매우 다양함.
- 특히 사용자가 폴더 정리를 평소에 안 할 수록 에이전트는 원하는 파일을 찾는 데에 어려움을 겪음.
- 결국 파일 정리를 안 할 수록 클로드 코드 등 에이전트의 성능이 크게 떨어질 수 있음.
- 이를 해결하기 위해 AgentDir을 제작
- Rust 기반 가상 파일 시스템을 관리할 수 있는 코어 라이브러리
- 원본을 수정하지 않고 파일명부터 폴더 구조를 변경 가능
- 원본의 수정, 추가, 삭제 등이 있으면 가상 파일 시스템에 반영
- Mac OS, Linux, Windows 지원
- Python 및 Node SDK 제공

## 원문
- [원문](https://github.com/nomadamas/agentdir)
- [GeekNews 토론](https://news.hada.io/topic?id=30115)

## My Note
<!-- 한 줄 코멘트 남기기 -->

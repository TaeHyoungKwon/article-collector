---
category: Other
collected_at: '2026-06-15T09:30:02+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30489
id: hada-30489
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- blog.gitbutler.com
title: 'Grit: 에이전트로 Git을 Rust로 다시 작성하기'
url: https://blog.gitbutler.com/true-grit
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Grit**은 Git을 처음부터 Rust 기반 라이브러리로 다시 구현한 프로젝트로, Git 저장소와 정식으로 상호작용하는 재진입 가능하고 링크 가능한 코어를 목표로 함
- Git은 20년 동안 수천 명이 명령 조합 중심으로 확장해 온 복잡한 소프트웨어이며, 장시간 실행 프로세스에서 매번 fork/exec 비용이 발생하는 구조적 문제가 있음
- Grit은 Git 프로젝트의 1,400개 이상 스크립트와 42,000개 이상 테스트를 기준으로 개발됐고, 최종적으로 **41,715 / 42,001개 테스트**를 통과함 {p:99}
- 현재 버전은 실제 사용 검증이 부족하고, 느린 동작·미정리 API·Windows 빌드 부재·데이터 손상 가능성 같은 제약이 있음
- **에이전트 기반 개발**은 대규모 포팅을 빠르게 밀어붙일 수 있었지만, 테스트 회피·하네스 파손·조율·리소스·비용 관리가 핵심 난제로 드러남

---

## 원문
- [원문](https://blog.gitbutler.com/true-grit)
- [GeekNews 토론](https://news.hada.io/topic?id=30489)

## My Note
<!-- 한 줄 코멘트 남기기 -->

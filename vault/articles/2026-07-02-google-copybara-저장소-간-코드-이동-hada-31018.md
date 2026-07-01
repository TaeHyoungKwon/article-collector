---
category: Other
collected_at: '2026-07-02T05:34:42+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31018
id: hada-31018
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/google
title: 'Google Copybara: 저장소 간 코드 이동'
url: https://github.com/google/copybara
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Copybara**는 Google 내부에서 쓰이는 도구로, 여러 저장소 사이에서 소스 코드를 변환하고 이동해 confidential 저장소와 public 저장소를 동기화하는 사례에 쓰임
- 하나의 저장소를 **권위 있는 저장소**로 선택해 단일 진실 공급원을 유지하지만, 기여는 어느 저장소에서도 받을 수 있고 릴리스도 어느 저장소에서든 만들 수 있음
- 주요 사용 사례는 반복적인 코드 이동이며, confidential 저장소에서 public 저장소로 일부 코드를 가져오거나 public 저장소 변경을 authoritative 저장소로 가져오는 흐름을 지원함
- Copybara는 상태를 별도 서버가 아니라 대상 저장소의 **커밋 메시지 라벨**에 저장하는 stateless 방식이라, 여러 사용자나 서비스가 같은 설정과 저장소에서 같은 결과를 얻을 수 있음
- 현재 지원 저장소 유형은 **Git**이며 Mercurial 읽기는 실험적 기능이고, 확장 가능한 구조로 맞춤 origin과 destination을 추가할 수 있음

---

## 원문
- [원문](https://github.com/google/copybara)
- [GeekNews 토론](https://news.hada.io/topic?id=31018)

## My Note
<!-- 한 줄 코멘트 남기기 -->

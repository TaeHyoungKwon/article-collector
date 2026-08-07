---
category: AI
collected_at: '2026-08-07T09:05:13+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32219
id: hada-32219
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-08-07'
source: geeknews
tags:
- AI
- Other
- bobdahacker.com
title: 'tl;dv(Too Lazy; Didn&#039;t Validate): 회의 181,874건이 무방비로 노출'
url: https://bobdahacker.com/blog/tldv-hack
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- AI 회의 기록 플랫폼 **tl;dv**의 Firestore `meetings` 컬렉션에서 테넌트 격리가 빠져, 무료 계정으로 다른 사용자의 회의 메타데이터와 실시간 통화 ID를 조회할 수 있었음
- 레코드에는 생성자 이메일, Google Meet·Teams 회의 ID, 제공자, 녹화 상태, 시간이 담겼으며, 한 시점에 약 **1,000건의 진행 중인 회의**에 무단 입장할 수 있었음
- 노출 범위는 **회의 181,874건**, 사용자 84,312명, 이메일 도메인 35,003개에 달했고 23개국 정부기관과 대학, HubSpot·Confluent 등의 기업도 포함됨
- 영상과 대화록은 기본적으로 비공개였지만, 검사한 회의 ID 27,334개 중 **1,000개 이상이 공개 상태**였으며 초대자 이메일 715개와 228개 도메인도 확인됨
- 취약점은 **2026년 1월 28일** 전달됐지만 CTO의 답변 없이 7월까지 남아 있었으며, Firestore 보안 규칙 적용과 별도 사내 앱의 무인증 API 차단이 필요함

---

## 원문
- [원문](https://bobdahacker.com/blog/tldv-hack)
- [GeekNews 토론](https://news.hada.io/topic?id=32219)

## My Note
<!-- 한 줄 코멘트 남기기 -->

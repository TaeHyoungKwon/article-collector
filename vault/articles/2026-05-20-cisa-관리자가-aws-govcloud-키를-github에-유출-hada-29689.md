---
category: Other
collected_at: '2026-05-20T10:10:43+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29689
id: hada-29689
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- krebsonsecurity.com
title: CISA 관리자가 AWS GovCloud 키를 GitHub에 유출
url: https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- CISA 계약자가 운영한 공개 **Private-CISA** 저장소가 고권한 AWS GovCloud 계정과 내부 시스템 자격 증명을 노출함
- GitHub 계정에는 비밀 정보 게시를 막는 기본 설정을 비활성화한 흔적과 **평문 비밀번호**, 토큰, 로그가 포함됨
- 노출 파일 **importantAWStokens**에는 AWS GovCloud 서버 3개의 관리자 자격 증명이, CSV에는 내부 시스템 로그인 정보가 들어 있었음
- Seralys는 노출 키가 높은 권한으로 인증 가능했고, 내부 **artifactory** 접근은 패키지 백도어와 횡적 이동 위험을 키운다고 봄
- CISA 통보 직후 계정은 오프라인이 됐지만 AWS 키는 이후 **48시간** 더 유효했고, CISA는 침해 징후는 없다고 밝힘

---

## 원문
- [원문](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)
- [GeekNews 토론](https://news.hada.io/topic?id=29689)

## My Note
<!-- 한 줄 코멘트 남기기 -->

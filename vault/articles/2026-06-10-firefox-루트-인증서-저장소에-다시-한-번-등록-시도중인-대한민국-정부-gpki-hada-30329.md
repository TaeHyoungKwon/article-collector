---
category: Other
collected_at: '2026-06-10T03:29:07+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30329
id: hada-30329
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- bugzilla.mozilla.org
title: Firefox 루트 인증서 저장소에 다시 한 번 등록 시도중인 대한민국 정부 (GPKI)
url: https://bugzilla.mozilla.org/show_bug.cgi?id=1845081
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
GPKI 루트 인증서는 주로 정부에서 `.go.kr` TLD를 비롯한 여러 국공립 웹 사이트의 도메인에 인증서를 발급하는데 주로 사용돼었습니다. (**과거형**임에 유의, 현재는 정부 사이트들이 각자 다른 업체로부터 인증서를 발급 받아서 HTTPS 서비스 제공 중)

타 브라우저와 달리 Firefox는 자체적인 루트 인증서 목록을 갖고 있고 TLS 연결 시 운영체제의 인증서 목록을 따르지 않습니다. 예를 들어 Windows의 경우 GPKI 인증서가 선탑재돼있지만 Firefox는 그걸 읽지 않습니다. (다만, 요즘에는 `about:config` 설정 페이지의 보안 탭에서 체크박스 하나로 쉽게 변경하여 따르도록 할 수 있음)

GPKI 루트 인증서의 대표적인 등록 거부 사유로는 과거에 정부가 `*.or.kr`, `*.ac.kr` 등 초광범위 인증서 발급 전적이 밝혀진 바 있습니다.

그런데 단순히 그 무제한급 발급 사례 하나로 등록 시도가 막히는 것은 아니고 Mozilla 측에서 요구하는 외부 감사 결과, 인증서 폐기 목록 확인 방법(CRL), 인증서 유효성 확인 방법(OCSP) 등 까다로운 신뢰 인증 절차를 정부가 모두 제때 능히 따르지 않았기 때문에 등록이 지연되거나 거절되고 있습니다.

혹은, 제때 하였더라도 행안부 인증서와 교육부 인증서를 같은 업체로부터 감사를 받는 등 결과 그 자체가 문제가 있는 경우도 있습니다.

BugZilla 내에서 이슈를 찾아보다보면 수년이 넘는 장기간에 걸쳐 등록 시도를 계속하고 있다보니 담당 공무원의 순환보직, 정권 교체로 인한 정부 조직 개편 등의 사유로 실무를 진행하는 담당자명과 소속 기관명이 연도에 따라 계속 바뀌는게 관전 포인트입니다.

## 원문
- [원문](https://bugzilla.mozilla.org/show_bug.cgi?id=1845081)
- [GeekNews 토론](https://news.hada.io/topic?id=30329)

## My Note
<!-- 한 줄 코멘트 남기기 -->

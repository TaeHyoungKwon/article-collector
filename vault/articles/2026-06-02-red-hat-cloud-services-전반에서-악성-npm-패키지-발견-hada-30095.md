---
category: AI
collected_at: '2026-06-02T09:51:38+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30095
id: hada-30095
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/RedHatInsights
title: Red Hat Cloud Services 전반에서 악성 npm 패키지 발견
url: https://github.com/RedHatInsights/javascript-clients/issues/492
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 이슈는 **열린 상태**이며, 본문 기준으로 담당자·마일스톤·연결된 브랜치나 PR은 없음
- `@redhat-cloud-services/` 범위의 여러 **npm 릴리스**에서 악성 버전이 발견됐다는 보안 이슈로 등록됨
- 참고 자료로 StepSecurity의 [분석 글](https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised)과 [OSS Security Feed 검색 결과](https://app.stepsecurity.io/oss-security-feed?q=@redhat-cloud-services)가 제시됨
- 업데이트된 영향 목록에는 `@redhat-cloud-services/chrome`, `frontend-components`, `rbac-client`, `types`, `vulnerabilities-client` 등 **32개 패키지**가 포함됨
- 표에 나온 손상 버전은 대부분 패키지당 3개이며, `@redhat-cloud-services/vulnerabilities-client`는 `2.1.9`, `2.1.11` 두 버전만 포함됨
- 전체 표 기준으로 손상된 버전은 **95개**로 집계 가능하며, 별도 언급된 외부 PR 제목도 `95 versions`를 가리킴
- `@redhat-cloud-services/frontend-components-*` 계열과 여러 `*-client` 패키지가 함께 포함돼, 단일 패키지가 아니라 같은 스코프 전반의 릴리스 문제가 됨
- 댓글에서는 “What are these?”라는 질문에 “all that module is pwned”라는 답변이 달려, 목록 전체가 침해됐다는 이해가 공유됨
- DanielRuf는 이 사건을 [supply-chain-incidents](https://codeberg.org/DanielRuf/supply-chain-incidents)에 추가했다고 남김
- GitHub 활동에는 이 이슈를 참조한 콘텐츠 요약과 탐지 관련 PR이 보이지만, 본문에는 Red Hat 측의 진단·완화 조치·삭제 여부·수정 버전이 아직 제시되지 않음

## 원문
- [원문](https://github.com/RedHatInsights/javascript-clients/issues/492)
- [GeekNews 토론](https://news.hada.io/topic?id=30095)

## My Note
<!-- 한 줄 코멘트 남기기 -->

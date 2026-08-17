---
category: AI
collected_at: '2026-08-18T07:32:25+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32595
id: hada-32595
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-08-17'
source: geeknews
tags:
- AI
- Other
- wiz.io
title: GitHub Copilot이 놓친 수정으로 Snowflake Jira 침해 가능해져
url: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Wiz의 자율 보안 도구 **Red Agent**가 Snowflake 공개 저장소에서 GitHub 이슈 제목만으로 임의 명령을 실행하고 Jira 자격 증명을 탈취할 수 있는 **GitHub Actions 취약점**을 발견함
- 2026년 6월 18일 병합된 PR #1218은 안전한 `env:`·`jq --arg` 처리를 **직접 문자열 보간**으로 교체했으며, Copilot은 공동 작성자로 표시되고 변경을 안전하다고 판정했지만 코드 작성에 AI가 사용됐는지는 불분명함
- 이슈 이벤트에서 항상 `null`인 `github.event.pull_request`를 검사한 보안 조건은 **모든 GitHub 사용자에게 참**이 됐고, 이슈 제목의 작은따옴표로 셸 문자열을 탈출할 수 있었음
- Red Agent는 첫 페이로드의 Bash 구문 오류를 자율적으로 분석·수정한 뒤, 수초 안에 Snowflake의 엔지니어링·보안 규정 준수·버그 바운티 프로젝트를 읽을 수 있는 **Jira 토큰**을 검증함
- Snowflake는 6월 23일 신고 당일 안전한 처리 방식을 복원하고 자격 증명을 교체했으며, 감사 로그를 통해 5일간의 노출 기간에 **Wiz 외 제3자 접근이 없었음**을 확인함

---

## 원문
- [원문](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)
- [GeekNews 토론](https://news.hada.io/topic?id=32595)

## My Note
<!-- 한 줄 코멘트 남기기 -->

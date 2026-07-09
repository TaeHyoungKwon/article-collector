---
category: AI
collected_at: '2026-07-09T09:55:27+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31255
id: hada-31255
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- noma.security
title: 'GitLost: GitHub AI 에이전트를 속여 비공개 저장소 유출'
url: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Noma Labs는 GitHub Agentic Workflows에서 **간접 프롬프트 인젝션** 취약점 GitLost를 발견했으며, 공개 저장소 이슈만으로 같은 조직의 비공개 저장소 데이터를 공개 댓글에 노출시킬 수 있었음
- 이 기능은 Markdown 워크플로를 YAML Actions 파일로 컴파일하고, Claude 또는 GitHub Copilot 기반 **AI 에이전트**가 이슈를 읽고 도구를 호출하며 조직 내 저장소에 접근하는 구조임
- 취약한 워크플로는 `issues.assigned` 이벤트에서 이슈의 **Title**과 **Body**를 읽고 `add-comment`로 응답했으며, 공개·비공개 저장소 읽기 권한을 가진 상태였음
- 공격자는 코드, 접근 권한, 자격 증명 없이 공개 저장소에 그럴듯한 이슈를 열기만 하면 됐고, 테스트에서는 `poc`와 `testlocal`의 `README.md` 내용이 공개 이슈 댓글에 게시됨
- GitHub의 가드레일은 “Additionally” 변형에서 의도대로 막지 못했고, 에이전트형 AI에서는 **컨텍스트 창** 자체를 공격 표면으로 보고 사용자 제어 콘텐츠를 신뢰된 지시문과 분리해야 함

---

## 원문
- [원문](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)
- [GeekNews 토론](https://news.hada.io/topic?id=31255)

## My Note
<!-- 한 줄 코멘트 남기기 -->

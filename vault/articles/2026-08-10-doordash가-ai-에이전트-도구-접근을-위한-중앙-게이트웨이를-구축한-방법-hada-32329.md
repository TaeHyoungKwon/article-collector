---
category: AI
collected_at: '2026-08-10T10:30:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32329
id: hada-32329
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- careersatdoordash.com
title: DoorDash가 AI 에이전트-도구 접근을 위한 중앙 게이트웨이를 구축한 방법
url: https://careersatdoordash.com/blog/how-doordash-built-a-centralized-gateway-for-ai-agent-tool-access/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- MCP는 에이전트가 도구를 **설명/탐색/호출하는 방식은 표준화**했지만, 실제 운영에 필요한 인증/권한/자격증명/접근 취소/감사까지 해결하지는 않아 DoorDash는 이를 Agent Gateway로 중앙화함
- 모든 도구 호출은 게이트웨이를 거치며 **호출자 인증 → 권한 확인 → 승인된 도구 노출 → 자격증명 주입 → MCP 서버 전달 → 사용 기록 생성**의 공통 경로를 사용함
- 여러 MCP 서버가 제공하는 수백~수천 개 도구를 그대로 보여주지 않고 **업무별 도구 묶음(bundle)과 필터**로 필요한 기능만 제공해 보안과 에이전트의 도구 선택 품질을 함께 높임
- 사용자별 OAuth와 서비스 계정도 게이트웨이가 관리하고, 모든 호출이 한곳을 지나므로 **속도 제한/추적/비용 귀속/감사/권한 회수**까지 공통 플랫폼 기능으로 제공함
- 현재 200개 이상의 MCP 서버와 30개 이상의 에이전트/서비스가 연결되어 매주 **수백만 건의 도구 호출**을 처리하며, MCP 이후의 핵심 과제는 도구 호출 자체보다 그 주변의 거버넌스임

---

## 원문
- [원문](https://careersatdoordash.com/blog/how-doordash-built-a-centralized-gateway-for-ai-agent-tool-access/)
- [GeekNews 토론](https://news.hada.io/topic?id=32329)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-05-17T09:31:01+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29579
id: hada-29579
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.901
source: geeknews
tags:
- AI
- Other
- github.com/stripe
title: Stripe Link CLI - AI 에이전트가 사용자 대신 결제할 수 있게 해주는 CLI
url: https://github.com/stripe/link-cli
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- AI 에이전트가 Link 지갑에서 **일회용 결제 자격증명**을 발급받아 사용자 대신 구매를 완료하되, 실제 카드 정보는 저장하지 않는 커맨드라인 도구
- 두 가지 자격증명 유형 지원: 어디서든 사용 가능한 **가상 카드(PAN)** 와 Machine Payment Protocols 기반의 **Shared Payment Token(SPT)**
- 모든 지출 요청은 사용자에게 **푸시 알림**이 전송되며, 사용자가 직접 승인해야만 결제 진행 가능
- 에이전트 환경에서 호출 시 **LLM 친화적 텍스트 포맷(`toon`)** 을 기본 출력하며, `json`, `yaml`, `md`, `jsonl` 등 구조화된 출력도 지원
- **MCP 서버**로 실행 가능하여 `.mcp.json` 설정에 추가하면 로컬 MCP 서버로 에이전트와 바로 통합 가능
- 카드 정보 유출 방지를 위해 `--output-file` 옵션으로 **`0600` 권한의 로컬 파일**에만 카드 정보를 기록하고, stdout에는 마스킹된 정보만 출력
- 지출 요청 라이프사이클은 **create → request approval → approved** 순서이며, `context` 최소 100자, `amount` 최대 50,000센트($500) 제약 존재
- MPP 지원 가맹점에서는 `mpp pay`로 결제하며, SPT는 **일회용**이므로 결제 실패 시 새 지출 요청 생성 필요
- `--test` 플래그로 테스트 카드(`4242424242424242`)를 사용한 **테스트 모드** 지원
- 폴링 시 터미널 상태(`approved`, `denied`, `expired`, `canceled`)에 도달해야 정상 종료되며, 타임아웃 시 `POLLING_TIMEOUT`으로 비정상 종료하여 미완료 요청 오처리 방지
- 현재 **미국 Link 계정**에서만 사용 가능
- MIT 라이선스

## 원문
- [원문](https://github.com/stripe/link-cli)
- [GeekNews 토론](https://news.hada.io/topic?id=29579)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Dev Tools
collected_at: '2026-06-19T22:51:10+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30645
id: hada-30645
matched_keywords:
- Claude Code
- Codex
read: false
recommend_score: 4.901
source: geeknews
tags:
- Dev Tools
- Other
- github.com/BEOKS
title: 'Show GN: 토스증권 Open API용 Agent Skill'
url: https://github.com/BEOKS/tossinvest-skill
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
토스증권 Open API를 Codex, Claude Code 같은 에이전트에서 바로 사용할 수 있도록 만든 Agent Skill입니다.

설치는 아래처럼 할 수 있습니다.

```
npx skills add BEOKS/tossinvest-skill
```

특정 에이전트만 지정해서 설치할 수도 있습니다.

```
npx skills add BEOKS/tossinvest-skill --agent claude-code
```

설치 후에는 에이전트가 `/tossinvest-skill`을 통해 토스증권 Open API 문서, OpenAPI 스키마, 작업 흐름, CLI 사용법을 참고할 수 있습니다. 저장소에는 직접 실행 가능한 CLI도 포함했습니다.

```
python3 scripts/tossinvest.py list-endpoints  
python3 scripts/tossinvest.py stocks --symbols 005930,AAPL  
python3 scripts/tossinvest.py prices --symbols 005930,AAPL
```

- 공식 OpenAPI JSON과 개요 문서
- 엔드포인트/스키마 탐색용 CLI
- `TOSS_API_KEY`, `TOSS_SECRET_KEY` 기반 OAuth 토큰 발급
- 종목 정보, 현재가, 호가, 체결, 캔들 조회
- KRW/USD 환율과 국내/미국 장 운영 정보 조회
- 계좌 목록, 보유 주식, 주문 목록/상세 조회
- 매수 가능 금액, 매도 가능 수량, 수수료 조회
- 주문 생성/정정/취소 요청 생성

주문 관련 기능은 실수 방지를 위해 기본값을 dry-run으로 두었습니다. 실제 주문 생성, 정정, 취소는 `--execute --yes`를 같이 넘겨야만 실행됩니다. 주문 생성은 기본적으로 `clientOrderId`도 요구하게 해두었습니다.

많은 관심 부탁드립니다!

감사합니다.

## 원문
- [원문](https://github.com/BEOKS/tossinvest-skill)
- [GeekNews 토론](https://news.hada.io/topic?id=30645)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-05-12T09:52:26+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29413
id: hada-29413
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- tanstack.com
title: '사후 분석: TanStack npm 공급망 침해'
url: https://tanstack.com/blog/npm-supply-chain-compromise-postmortem
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 2026-05-11 19:20~19:26 UTC에 공격자가 42개 **@tanstack/** npm 패키지에 걸쳐 악성 버전 84개를 게시함
- 공격 체인은 **pull\_request\_target** “Pwn Request”, GitHub Actions 캐시 오염, runner 메모리의 OIDC 토큰 추출을 결합함
- npm 토큰과 publish 워크플로는 탈취·손상되지 않았고, 악성코드가 **OIDC trusted publisher** 권한으로 registry에 직접 POST함
- 영향 버전 설치 시 **AWS, GCP, Kubernetes, Vault, GitHub, npm, SSH 자격 증명**이 노출됐을 수 있어 교체가 필요함
- 모든 영향 버전은 deprecated 처리됐고 npm security와 tarball 제거를 진행했으며, 추적 이슈와 GitHub Security Advisory가 공개됨

---

## 원문
- [원문](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
- [GeekNews 토론](https://news.hada.io/topic?id=29413)

## My Note
<!-- 한 줄 코멘트 남기기 -->

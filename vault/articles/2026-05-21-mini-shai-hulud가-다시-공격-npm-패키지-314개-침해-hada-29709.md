---
category: AI
collected_at: '2026-05-21T05:59:55+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29709
id: hada-29709
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- safedep.io
title: 'Mini Shai-Hulud가 다시 공격: npm 패키지 314개 침해'
url: https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **atool npm 계정**이 2026년 5월 19일 침해되어 약 22분 동안 317개 패키지에 637개 악성 버전이 자동 배포됨
- 페이로드는 498KB 난독화 **Bun 스크립트**로, SAP 침해에 쓰인 Mini Shai-Hulud와 같은 스캐너 구조와 정규식을 사용함
- 탈취 대상은 **AWS 자격 증명**, Kubernetes 토큰, Vault, GitHub PAT, npm 토큰, SSH 키, 로컬 비밀 값까지 확장됨
- CI에서는 GitHub Actions OIDC를 npm publish 토큰으로 교환하고, **Sigstore 서명**과 악성 workflow 주입을 악용함
- 대응에는 침해 버전 설치 여부 확인, 접근 가능했던 모든 자격 증명 교체, **lockfile·의존성 pinning**과 설치 전 검사가 필요함

---

## 원문
- [원문](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/)
- [GeekNews 토론](https://news.hada.io/topic?id=29709)

## My Note
<!-- 한 줄 코멘트 남기기 -->

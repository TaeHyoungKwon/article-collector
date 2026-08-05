---
category: AI
collected_at: '2026-08-05T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=32157
id: hada-32157
matched_keywords:
- AI
read: false
recommend_score: 3.386
source: geeknews
tags:
- AI
- Other
- github.com/kubara-io
title: kubara - 모범 사례 기반으로 Kubernetes 플랫폼을 부트스트랩하는 CLI
url: https://github.com/kubara-io/kubara
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **GitOps-first 워크플로우**로 Kubernetes 플랫폼을 부트스트랩하고 운영하는 **Opionated CLI**
- 플랫폼 스캐폴딩/환경 구성/프로덕션 기본값을 Go 기반 단일 바이너리 CLI로 통합하여 처리
- **멀티 클러스터/멀티 테넌트** 환경을 대상으로 설계했고, **Terraform과 Helm** 기반 컴포넌트로 확장 가능
- 부트스트랩 기반과 기본 플랫폼 스택을 **OCI 카탈로그**에서 해석하며, 클러스터별 카탈로그 설정과 커스텀 카탈로그 구성 지원
- 주요 명령어
  - `init` - kubara 디렉터리 초기화
  - `generate` - 설정된 카탈로그 템플릿에서 **Helm/Terraform 아티팩트** 생성
  - `bootstrap` - 클러스터에 **CRD와 Argo CD** 부트스트랩
  - `schema` - 설정 구조의 JSON 스키마 생성
  - `agents` - AI 코딩 어시스턴트용 온보딩 파일(AGENTS.md) 스캐폴딩
  - `catalog` - 플랫폼 카탈로그 관리
  - `cluster` - kubara 클러스터 설정 관리
- 매 실행 시 GitHub의 새 릴리스를 확인하며, `KUBARA_UPDATE_CHECK=0`으로 비활성화 가능
- 이중 라이선스(소스 코드 Apache 2.0 / 문서 CC BY 4.0)

## 원문
- [원문](https://github.com/kubara-io/kubara)
- [GeekNews 토론](https://news.hada.io/topic?id=32157)

## My Note
<!-- 한 줄 코멘트 남기기 -->

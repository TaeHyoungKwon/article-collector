---
category: AI
collected_at: '2026-05-15T14:06:24+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29536
id: hada-29536
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/artifact-keeper
title: Artifact Keeper - Rust로 만든 오픈소스 범용 아티팩트 레지스트리
url: https://github.com/artifact-keeper/artifact-keeper
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Artifact Keeper는 Rust로 작성된 셀프호스팅 아티팩트 레지스트리로, JFrog Artifactory와 Sonatype Nexus의 대안을 목표로 하는 프로젝트입니다. Maven, PyPI, NPM, Docker/OCI, Cargo, Go, Helm 등 45개 이상의 패키지 포맷을 네이티브 프로토콜로 지원한다고 소개하고 있습니다.

- Rust + Axum 기반 백엔드
- MIT 라이선스
  - “open-core 없음, enterprise edition 없음”을 강조
- Maven/Gradle, PyPI, NPM/Yarn/pnpm, Docker/OCI, Cargo, Go modules, Helm 등 45개 이상 포맷 지원
  - Local / Proxy / Virtual 저장소 모델 제공
  - Proxy 저장소는 npmjs.com, PyPI, Maven Central, Docker Hub 같은 공개 레지스트리를 캐시
  - Virtual 저장소는 여러 Local/Proxy 저장소를 하나의 URL 뒤에 묶고, 지정된 순서대로 해석
  - Debian, RPM, Alpine, Conda 패키지에 대해 GPG/RSA 서명 지원
- 스토리지 백엔드는 파일시스템 또는 S3 지원
- 메타데이터와 설정은 PostgreSQL 16 사용
- Trivy + Grype 기반 보안 스캔 파이프라인 제공
  - 취약점 점수화, 정책 엔진, quarantine workflow 지원
- 인증 지원
  - JWT, OpenID Connect, LDAP, SAML 2.0, API Token 인증 지원
  - RBAC와 저장소 단위 권한 지원
- JFrog Artifactory에서 저장소, 아티팩트, 사용자/권한을 마이그레이션하는 도구 제공
- WASM 플러그인 시스템으로 커스텀 패키지 포맷 핸들러 추가 가능
- Wasmtime 기반 샌드박스 실행, CPU/메모리 제한, hot reload 지원
- Borg Replication이라는 P2P mesh 기반 아티팩트 복제 기능 제공
- Prometheus metrics, OpenTelemetry tracing, Kubernetes health probe 지원
- Docker Compose로 빠르게 실행 가능
- Kubernetes 배포용 Helm chart와 Terraform/EKS/RDS/S3 구성은 별도 IaC 저장소로 제공
- Web Dashboard는 Next.js 15, TypeScript, Tailwind CSS 4 기반 별도 저장소로 분리
- OpenAPI 3.1 스펙과 TypeScript/Kotlin/Swift/Rust/Python SDK 생성을 위한 별도 API 저장소 제공
- iOS/macOS, Android 네이티브 앱 저장소도 제공

Nexus나 Artifactory를 대체할 수 있는 셀프호스팅 레지스트리를 찾고 있다면 꽤 흥미로운 프로젝트입니다. 단순히 “파일 저장소 + 포맷 라벨”이 아니라, 각 패키지 매니저가 사용하는 네이티브 프로토콜을 직접 처리하는 방향을 내세우고 있고, Proxy/Virtual 저장소 모델도 기존 Nexus/Artifactory 사용자에게 익숙한 구조입니다.

특히 온프레미스나 사내망에서 Maven, NPM, Docker, PyPI, Helm 등을 한 번에 관리하고 싶거나, 취약점 스캔·서명·격리·SSO·RBAC까지 오픈소스 릴리스에서 제공하는 레지스트리를 찾는 팀이라면 검토해볼 만합니다.

## 원문
- [원문](https://github.com/artifact-keeper/artifact-keeper)
- [GeekNews 토론](https://news.hada.io/topic?id=29536)

## My Note
<!-- 한 줄 코멘트 남기기 -->

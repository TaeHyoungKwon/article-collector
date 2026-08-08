---
category: AI
collected_at: '2026-08-07T14:39:32+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32230
id: hada-32230
matched_keywords:
- backend
- AI
- RAG
read: false
recommend_score: -993.099
recommended_on: '2026-08-07'
source: geeknews
tags:
- AI
- Other
- zotregistry.dev
title: zot – 단일 Go 바이너리부터 HA 클러스터까지 확장 가능한 가벼운 OCI Registry
url: https://zotregistry.dev/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- OCI Distribution/Image Specification을 중심으로 설계된 오픈소스 컨테이너 이미지·아티팩트 레지스트리
- **정적으로 빌드된 단일 Go 바이너리**로 실행되며, 기본 구성에서는 PostgreSQL이나 Redis 같은 별도 서비스를 준비할 필요가 없음
- 모든 기능이 포함된 Full 빌드와 핵심 Registry 기능만 포함한 Minimal 빌드를 제공하고, 부가 기능은 extension 형태로 필요한 것만 활성화할 수 있음

#### 작은 환경에서는 매우 단순하게

로컬 filesystem 하나만 지정하면 단일 zot 프로세스만으로 Registry를 구성할 수 있습니다.

Garbage Collection, deduplication, retention policy, scrub 같은 기본적인 storage 관리 기능도 자체 제공하며, TLS 인증서와 private key를 직접 지정할 수 있어 단순한 구성에서는 TLS termination을 위한 별도 reverse proxy도 필수적이지 않습니다.

Basic Auth, LDAP, OIDC/OAuth2, mTLS와 repository path 단위 authorization도 지원합니다.

#### 필요하면 object storage로 확장

이미지 저장소로 로컬 filesystem뿐 아니라 다음과 같은 object storage를 직접 사용할 수 있습니다.

- AWS S3 / S3-compatible storage
- Google Cloud Storage
- Azure Blob Storage

따라서 MinIO 같은 온프레미스 S3-compatible storage와 조합하는 것도 가능합니다.

remote storage를 사용할 때는 blob 다운로드를 signed URL로 redirect할 수도 있어, 대용량 image layer를 zot 프로세스가 직접 중계하지 않고 object storage가 클라이언트에 바로 전달하도록 구성할 수 있습니다.

#### 단일 인스턴스에서 HA/scale-out까지

작게 사용할 때는 별도의 외부 DB 없이 단일 인스턴스로 운영할 수 있지만, 규모가 커지면 동일한 zot을 여러 인스턴스로 확장할 수도 있습니다.

여러 zot 인스턴스가 동일한 remote storage와 Redis 또는 DynamoDB 기반의 shared metadata/cache backend를 사용하도록 구성하면, 일반적인 load balancer 뒤에 여러 Registry 인스턴스를 배치하는 scale-out 구성이 가능합니다.

즉 처음부터 복잡한 클러스터를 구성할 필요 없이,

`단일 zot + local disk`

에서 시작해서 필요해지면

`Load Balancer + 여러 zot + S3-compatible storage + shared metadata backend`

형태로 확장할 수 있습니다.

compute만 확장하거나 compute와 storage를 함께 확장하는 구성도 공식적으로 지원합니다.

#### Registry proxy/cache로도 사용 가능

`sync` extension을 사용하면 다른 OCI Registry를 주기적으로 mirror하거나 **on-demand pull-through cache**로 사용할 수 있습니다.

예를 들어 Docker Hub를 upstream으로 지정하면 최초 pull 시에만 이미지를 받아와 zot에 저장하고, 이후 요청은 로컬 Registry에서 처리하도록 구성할 수 있습니다.

외부 Registry 접근을 줄이고 싶거나 사내 CI/CD에서 Docker Hub rate limit과 외부 네트워크 의존성을 줄이고 싶은 경우에도 유용합니다.

#### 필요한 기능만 추가

UI, GraphQL 검색, Prometheus metrics, Cosign/Notation signature verification, Trivy 기반 vulnerability scanning 같은 기능도 제공하지만 필요하지 않다면 활성화하지 않아도 됩니다.

Harbor처럼 replication, scanner, 프로젝트 관리 등 여러 기능을 적극적으로 사용하는 환경이라면 Harbor 같은 통합형 Registry가 더 적합할 수 있습니다.

반대로 **“이미지를 Push/Pull하고, 필요하면 외부 Registry의 proxy cache로 사용하고 싶다”** 정도가 목적이라면 여러 서비스와 DB를 함께 운영할 필요가 없는 zot이 상당히 매력적인 선택지입니다.

## 원문
- [원문](https://zotregistry.dev/)
- [GeekNews 토론](https://news.hada.io/topic?id=32230)

## My Note
<!-- 한 줄 코멘트 남기기 -->

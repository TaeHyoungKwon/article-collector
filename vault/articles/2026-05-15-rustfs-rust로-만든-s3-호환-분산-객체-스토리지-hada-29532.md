---
category: AI
collected_at: '2026-05-15T10:33:55+09:00'
geeknews_comments: 2
geeknews_score: 8
geeknews_url: https://news.hada.io/topic?id=29532
id: hada-29532
matched_keywords:
- AI
read: false
recommend_score: 4.527
recommended_on: '2026-05-15'
source: geeknews
tags:
- AI
- Other
- github.com/rustfs
title: RustFS - Rust로 만든 S3 호환 분산 객체 스토리지
url: https://github.com/rustfs/rustfs
---

## TL;DR
- RustFS는 S3 호환 분산 객체 스토리지로, Rust로 개발되어 고성능과 메모리 안전성을 제공합니다.
- 이 스토리지는 Apache 2.0 라이선스를 기반으로 하며, 기존 S3 호환 플랫폼과의 마이그레이션을 지원합니다.
- 개발자와 기업은 MinIO의 라이선스 문제를 피하고, AI와 빅데이터 워크로드에 적합한 솔루션을 검토할 수 있습니다.

## GeekNews 요약
RustFS는 Rust로 작성된 고성능 분산 객체 스토리지로, MinIO의 대안이 되는 Apache 2.0 라이선스 기반 S3 호환 스토리지를 목표로 함.

- Rust 기반 구현으로 메모리 안전성과 성능을 강조
- S3 호환 API 제공
- MinIO, Ceph 등 기존 S3 호환 플랫폼과의 마이그레이션/공존 지원
- Apache 2.0 라이선스
- 데이터 레이크, AI, 빅데이터 워크로드에 최적화
- 단일 노드 모드, 버저닝, 로깅, 이벤트 알림, Bucket Replication 지원
- Bitrot Protection 지원
- Kubernetes Helm Chart 제공
- OpenStack Swift API 및 Keystone 인증 지원
- Web Console, CLI, Helm, Operator 등 주변 도구도 별도 저장소로 제공
- Lifecycle Management, Distributed Mode, RustFS KMS는 현재 Under Testing 상태
- Docker 실행 시 S3 API는 9000 포트, 콘솔은 9001 포트 사용
- 컨테이너는 non-root 사용자 UID 10001로 실행되므로 볼륨 마운트 시 권한 설정 필요

MinIO의 AGPL 라이선스가 부담스럽거나, Rust 기반의 S3 호환 객체 스토리지를 검토하고 있다면 눈여겨볼 만한 프로젝트입니다. 다만 아직 일부 핵심 기능이 테스트 단계라 운영 환경 도입 전에는 S3 호환성, 분산 모드, lifecycle, retention, replication 동작을 직접 검증해보는 것이 좋아 보입니다.

## 원문
- [원문](https://github.com/rustfs/rustfs)
- [GeekNews 토론](https://news.hada.io/topic?id=29532)

## My Note
<!-- 한 줄 코멘트 남기기 -->

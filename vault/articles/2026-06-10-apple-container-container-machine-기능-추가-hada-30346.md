---
category: AI
collected_at: '2026-06-10T10:40:02+09:00'
geeknews_comments: 3
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=30346
id: hada-30346
matched_keywords:
- AI
read: false
recommend_score: -995.638
recommended_on: '2026-06-10'
source: geeknews
tags:
- AI
- Other
- github.com/apple
title: apple/container, Container Machine 기능 추가
url: https://github.com/apple/container
---

## TL;DR
- 이 글은 Apple의 새로운 Container Machine 기능을 다룬다.
- Container Machine은 macOS에서 Linux 컨테이너를 경량 가상 머신 형태로 실행하고, 각 배포판 간의 파일 공유를 지원한다.
- 이는 개발자들이 다양한 Linux 환경을 손쉽게 테스트하고, 효율적으로 작업할 수 있도록 도와준다.

## GeekNews 요약
- Mac에서 Linux 컨테이너를 **경량 가상 머신** 형태로 생성·실행하는 도구
- WWDC26에서 새로 추가된 **[Container Machine](https://github.com/apple/container/blob/main/docs/container-machine.md)** 은 홈 디렉토리와 저장소가 **자동으로 마운트**된 **빠르고 경량이며 영속적인 Linux 환경**을 실행 가능
- 기존 애플리케이션 단위 컨테이너와 달리 **Linux 환경 전체를 모델링** (WSL2와 비슷)
- 이미지의 **init 시스템**을 실행해 장기 실행 서비스 등록 또는 프로세스 관리자 하에서 애플리케이션 테스트 가능
- `systemd`가 설치된 이미지에서 `systemctl start postgresql` 같은 실제 Linux 서비스 실행 가능
- **사용자명과 홈 디렉터리를 자동 매핑**해 저장소·dotfile을 macOS·Linux 양쪽에서 공유함
- 저장소가 macOS `$HOME`에 위치하며 내부 `/Users/<username>`에 마운트, macOS 에디터·IDE로 편집하면서 내부에서 빌드·실행
- 프로파일러·브라우저·GUI 디버거 등 **macOS 네이티브 도구**가 동일 파일 인식, 빌드와 검사 사이 복사 단계가 필요없음
- `alpine`, `ubuntu`, `debian` 등 **대상 배포판 수만큼** Container Machine 생성 가능, 각각 동일한 `$HOME`·dotfile 공유로 여러 배포판에서 빠른 테스트
  - `/sbin/init`을 포함하는 모든 Linux 이미지를 직접 Container Machine 이미지로 사용 가능
- **OCI 호환 컨테이너 이미지**를 소비·생성하므로 표준 컨테이너 레지스트리에서 도커 이미지도 pull·push 가능
  - 다른 OCI 호환 애플리케이션에서도 해당 이미지 실행 가능
  - 저수준 컨테이너·이미지·프로세스 관리는 **Containerization Swift 패키지**에 의존
- 실행에 **Apple silicon** 탑재 Mac 필요, **macOS 26**에서 지원
  - macOS 26의 가상화·네트워킹 신규 기능 및 개선 사항 활용, 이전 버전 macOS는 미지원
- Apache-2.0 라이선스

## 원문
- [원문](https://github.com/apple/container)
- [GeekNews 토론](https://news.hada.io/topic?id=30346)

## My Note
<!-- 한 줄 코멘트 남기기 -->

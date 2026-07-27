---
category: Backend
collected_at: '2026-07-26T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=31816
id: hada-31816
matched_keywords:
- backend
read: false
recommend_score: 3.386
recommended_on: '2026-07-27'
source: geeknews
tags:
- Backend
- Other
- github.com/foru17
title: neko-master - 네트워크 트래픽 시각화 및 분석용 대시보드
url: https://github.com/foru17/neko-master
---

## TL;DR
- 이 글은 네트워크 트래픽을 시각화하고 분석하는 대시보드인 neko-master에 대해 설명한다.
- WebSocket을 통한 실시간 데이터 수집과 클라우드 기반 게이트웨이의 연결을 지원하여 사용자 네트워크의 밀리초 단위 지연 모니터링이 가능하다.
- 사용자 개인의 네트워크 데이터 분석과 시각화는 안전하고 효율적인 네트워크 관리를 위한 새로운 접근 방식을 제시한다.

## GeekNews 요약
- 로컬 게이트웨이 환경 전용 **트래픽 분석/시각화 대시보드**
- 네트워크 접속 서비스나 프록시 구독 없이 사용자 자신의 네트워크 데이터만 수집
- **WebSocket 실시간 수집**으로 밀리초 단위 지연 모니터링, WS 미연결 시 HTTP 폴링으로 자동 폴백
- 30분 / 1시간 / 24시간 **다차원 트래픽 추세 분석** 지원
- **도메인/IP/프록시 노드별 분석** 제공
  - 도메인별 트래픽, 연관 IP, 연결 수 확인
  - IP에 대한 ASN, 지리 위치, 연관 도메인 표시
  - 프록시 노드별 트래픽 분포와 연결 수 통계
- **Clash / Mihomo**(WebSocket 실시간)와 **Surge v5+**(HTTP 폴링) 게이트웨이 연결 지원
- 여러 **OpenClash 백엔드 인스턴스 동시 모니터링** 가능(Multi-Backend)
- **Agent 배포 모드** 지원으로, 중앙 패널 하나에 다수 원격 기기(OpenWrt, Linux, macOS)가 로컬 게이트웨이 데이터를 수집/보고하며 패널은 게이트웨이에 직접 연결하지 않음
- 기본 저장은 **SQLite**, 대용량/장기 집계가 필요하면 **ClickHouse 이중 기록** 선택 가능
  - CH 쓰기 실패 임계치 초과 시 자동으로 SQLite 폴백, 복구 시 재전환
  - 이중 기록 → 읽기 전환 → 이력 이관 → CH-only의 단계적 마이그레이션 경로 제공
- **PWA 설치**, Light / Dark / System **다크 모드**, 영어/중국어 **다국어 전환** 지원
- Nginx/Cloudflare Tunnel 리버스 프록시 예시 제공, Docker 이미지는 **linux/amd64/arm64** 멀티 아키텍처 지원
- MIT 라이선스

## 원문
- [원문](https://github.com/foru17/neko-master)
- [GeekNews 토론](https://news.hada.io/topic?id=31816)

## My Note
<!-- 한 줄 코멘트 남기기 -->

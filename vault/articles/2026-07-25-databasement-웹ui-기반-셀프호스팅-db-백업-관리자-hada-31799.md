---
category: AI
collected_at: '2026-07-25T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31799
id: hada-31799
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: 4.693
recommended_on: '2026-07-26'
source: geeknews
tags:
- AI
- Other
- github.com/David-Crty
title: databasement - 웹UI 기반 셀프호스팅 DB 백업 관리자
url: https://github.com/David-Crty/databasement
---

## TL;DR
- databasement는 다양한 데이터베이스의 백업 및 복원 기능을 제공하는 웹 UI 기반의 셀프 호스팅 DB 관리자이다.
- 이 시스템은 SSH 터널과 원격 에이전트를 통해 보안성을 높이며, 자동 백업과 멀티 압축 옵션을 지원한다.
- 사용자와 기업은 강화된 데이터 보호 및 관리 효율성을 통해 보다 안전한 데이터 환경을 구축할 수 있다.

## GeekNews 요약
- 여러 종류의 DB를 단일 웹 UI에서 **백업, 복원, 스케줄링**하는 셀프 호스팅 관리자
- MySQL/PostgreSQL/MariaDB/MSSQL/MongoDB/SQLite/Firebird/Redis/Valkey 지원
- **SSH 터널**: bastion/jump 서버를 경유해 사설망 내 DB에 비밀번호 또는 키 기반 인증으로 접속
- **원격 에이전트**: 인바운드 포트 없이 HTTPS로 아웃바운드 연결, 방화벽/격리 네트워크에서 로컬 덤프 후 스토리지로 업로드
- **자동 백업**: 일간/주간 예약, 단순 시간 기반(일수) 또는 **GFS(grandfather-father-son)** 보존 정책 제공
- 멀티 압축 옵션: gzip, zstd(20–40% 향상된 압축률), 민감 데이터용 **AES-256 암호화** 제공
- **교차 서버 복원**: 프로덕션 스냅샷을 스테이징 등 호환 서버로 복원, **예약 복원**은 최신 완료 스냅샷 재생 방식으로 대상 DB 정기 갱신(예: 매일 밤 prod → staging)
- **내장 데이터 브라우저** 제공: 내장 Adminer로 MySQL/PostgreSQL/SQLite 조회(admin 활성화, 역할 기반 제한)
- 유연한 저장 옵션: 로컬, **S3 호환 스토리지**(AWS S3, MinIO 등), Azure Blob, Samba/SMB, SFTP/FTP 지원
- **실시간 모니터링**: 상세 작업 로그 추적, 실패 시 Email/Slack/Discord/Telegram/Pushover/Webhook 알림 가능
- **멀티테넌트 조직** 지원: 격리된 워크스페이스, 역할 기반 접근 제어, OAuth/SSO(Google/GitHub/GitLab/OpenID Connect), 2단계 인증 옵션 가능
- **REST API**와 **MCP 서버** 제공: 스크립트/CI/CD 연동 및 Claude Code/Cursor 등 AI 어시스턴트를 통한 자연어 백업 관리
- 심플한 배포 옵션: 웹 서버/큐 워커/스케줄러가 내장된 **단일 Docker 컨테이너**로 배포 됨
- MIT 라이선스 / PHP 기반

## 원문
- [원문](https://github.com/David-Crty/databasement)
- [GeekNews 토론](https://news.hada.io/topic?id=31799)

## My Note
<!-- 한 줄 코멘트 남기기 -->

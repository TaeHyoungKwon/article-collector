---
category: Other
collected_at: '2026-07-29T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31930
id: hada-31930
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- github.com/oblien
title: Openship - 내장 CI/CD를 갖춘 셀프 호스팅 배포 플랫폼
url: https://github.com/oblien/openship
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 저장소를 지정하면 **빌드 → 실행 → 라우팅 → TLS 종료**까지 한 번에 처리하는 오픈소스 배포 플랫폼
- 설정 파일 없이 `package.json`, lockfile, 프레임워크 설정을 읽어 **스택과 빌드/시작 명령 자동 감지**
- **Push-to-deploy** 지원해서 GitHub webhook이 추적 브랜치 push마다 파이프라인 재실행, monorepo는 실제 변경된 서비스만 재빌드
- 실행 방식은 **데스크탑 앱**(로컬 control plane, 공개 노출 없음), **셀프 호스트 서버**(`openship up`으로 compose 모드), **Openship Cloud** 중 선택
- **Desktop app/Web dashboard/CLI** 세 인터페이스가 동일 백엔드를 제어하며, 자동화용 **MCP endpoint와 REST API** 제공
- 데이터베이스, 도메인/SSL, CDN, 내장 SMTP, 백업, 실시간 모니터링까지 **한 곳에서 통합 관리**
- 실시간 빌드 로그/컨테이너 메트릭 스트리밍, 클라우드 auto-scaling 및 self-hosted 다중 노드 대응, 표준 Docker 컨테이너 기반이라 프로바이더 간 이동이 자유로움
- 다중 노드 클러스터, 로드 밸런싱 UI, private networking, 비주얼 CI/CD 파이프라인도 추가할 예정
- Apache 2.0 라이선스

## 원문
- [원문](https://github.com/oblien/openship)
- [GeekNews 토론](https://news.hada.io/topic?id=31930)

## My Note
<!-- 한 줄 코멘트 남기기 -->

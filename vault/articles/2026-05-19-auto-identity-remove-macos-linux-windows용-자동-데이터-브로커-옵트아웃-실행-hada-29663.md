---
category: Other
collected_at: '2026-05-19T23:38:35+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29663
id: hada-29663
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/stephenlthorn
title: auto-identity-remove - macOS, Linux, Windows용 자동 데이터 브로커 옵트아웃 실행기
url: https://github.com/stephenlthorn/auto-identity-remove
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **auto-identity-remove**는 이름과 지역 정보로 데이터 브로커 사이트를 검색하고 옵트아웃 양식을 자동 제출해, 매월 **500개 이상**의 사람 검색 사이트와 데이터 브로커 데이터베이스에서 개인 정보를 제거하도록 돕는 도구임
- 실행 흐름은 브로커별 검색, 특정 프로필 목록 탐지, 옵트아웃 양식 제출, 필요한 경우 CAPTCHA 처리, 최근 완료된 항목 건너뛰기, 결과 알림, 수동 처리가 필요한 사이트 브라우저 열기로 구성됨
- **상태 추적**은 `state.json`에 마지막 성공 시점과 실행 이력을 저장하며, 기본 재확인 주기는 **90일**이라 완료된 옵트아웃을 매번 다시 제출하지 않음
- CAPTCHA가 있는 양식은 [CapSolver](https://capsolver.com)를 통해 처리할 수 있고, 비용은 대략 **풀이당 $0.001**이며, 설정하지 않으면 해당 사이트는 수동 처리 목록으로 넘어감
- 요구 사항은 **Node.js 18+**, macOS·Linux·Windows, [Playwright](https://playwright.dev) 브라우저이며, `setup.js`가 개인 정보 입력, 별칭, CapSolver 키, 일회성 계정, 알림, 월간 스케줄 등록을 안내함
- 월간 작업은 매월 1일 오전 9시에 실행되도록 등록되며, 플랫폼에 따라 **launchd**, **systemd**, crontab, schtasks를 자동 감지해 사용함
- Docker 실행도 지원하며 공식 Playwright 이미지를 사용해 Chromium과 시스템 의존성이 포함되고, 컨테이너 간 완료 이력을 유지하려면 `state.json`을 마운트해야 함
- 알림은 macOS의 **iMessage** 결과 요약을 지원하고, 헤드리스나 Docker 환경에서는 `notify.webhook`으로 ntfy.sh, Slack incoming webhook, Discord webhook에 `{"text": "<summary>"}`를 POST할 수 있음
- 브로커 지원은 2단계로 나뉘며, [STATUS.md](https://github.com/stephenlthorn/STATUS.md)에 정리된 **명시적 브로커 42개**는 개별 셀렉터로 매핑되고, 약 **490개**는 Do Not Sell 버튼, OneTrust·TrustArc·Osano, 일반 양식, DSAR 링크 탐색을 순서대로 시도하는 휴리스틱 방식임
- `✅ Submitted`는 브로커가 양식을 접수했다는 뜻일 뿐 삭제 보장은 아니며, `node watcher.js --verify`는 기록된 성공 항목을 다시 검색해 `VERIFIED CLEAR`, `STILL LISTED`, `UNVERIFIABLE`로 분류함
- 지원되는 대표 자동 처리 대상에는 Spokeo, WhitePages, FastPeopleSearch, TruePeopleSearch, BeenVerified, Radaris, Acxiom, LexisNexis, ZoomInfo, Clearbit 등이 포함되고, Google Results About You와 Google Outdated Content는 수동 처리로 열림
- 비미국 사용자는 국가 코드, Province/Region, Postal code, 원문 전화번호 저장, 국가 선택 필드 입력을 지원하지만, Spokeo·WhitePages·FastPeopleSearch 등 **US-only** 브로커는 설정 국가가 `US`가 아니면 자동으로 건너뜀
- `--dry-run`은 사이트 탐색과 양식 채우기만 수행하고 제출하지 않으며, 실험 기능인 `--pollute N`은 `acceptsBogus: true`로 표시된 일부 브로커에 가짜 기록을 제출하지만 약관 위반과 법적 위험 가능성이 명시돼 기본적으로 꺼져 있음
- 개인 정보가 담긴 `config.json`, 옵트아웃 이력 `state.json`, 실행 로그는 gitignore 대상이며, 저장소 라이선스는 **MIT**임

## 원문
- [원문](https://github.com/stephenlthorn/auto-identity-remove)
- [GeekNews 토론](https://news.hada.io/topic?id=29663)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-08-09T22:54:39+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32300
id: hada-32300
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- github.com/taevel02
title: 'Show GN: Sift - 원클릭 복구를 지원하는 Rust 기반 로컬 파일 자동 정리 CLI'
url: https://github.com/taevel02/Sift
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Hazel을 아시나요? 맥에서 Hazel을 오래 썼지만 GUI가 무겁고 터미널 전용 환경이나 리눅스 서버에서 쓰지 못하는 아쉬움이 있었습니다. 그렇다고 쉘 스크립트나 Cron을 짜서 돌리기엔 정규식 하나만 틀려도 디렉터리 전체가 날아갈 수 있는 위험이 있지요.

이 문제를 해결하려고 터미널 중심의 속도와 100% 파일 안전성에 집중한 Rust 기반 헤드리스 CLI 도구 Sift를 만들었습니다. Rust로 개발해서 굉장히 가볍고 빠릅니다.

**1. 원클릭 복구 (Undo)**  
모든 이동, 휴지통, 압축 작업은 `~/.config/sift/history.json` 트랜잭션으로 남습니다. `sift undo` 명령으로 이전 상태로 원복하고 파일 mtime을 갱신해 연쇄 재감지를 막습니다.

**2. 시뮬레이션 (Dry-run Default)**  
기본 실행 시 디스크를 수정하지 않고 적용될 룰만 미리 표시합니다. 실제 파일 조작은 -x 플래그를 붙여야 실행됩니다.

**3. 100% 로컬 오프라인 (Zero Telemetry)**  
외부 네트워크 호출이나 데이터 수집, 텔레메트리가 일절 없습니다. 보안에 신경쓰시는 분들에게는 최상의 사용자 경험입니다.

**4. 메타데이터 필터 & 동적 템플릿**  
확장자 외에도 사진 EXIF(카메라 모델), 음원 ID3(가수/앨범), macOS Finder 컬러 태그를 감지합니다. `~/Pictures/{year}/{month}` 형태로 디렉터리를 동적 생성하며 정리합니다.

**5. 실시간 TUI 모니터링 & macOS 백그라운드 데몬**  
`sift watch` 명령으로 터미널 실시간 대시보드를 띄우거나 `sift daemon`으로 macOS launchd 데몬에 등록해 백그라운드 자동화를 수행합니다.

**6. 킬러 5대 레시피 탑재**  
제가 자주 사용하는 5대 킬러 레시피를 탑재했습니다. 직접 만들어 사용할 수도 있고, 직접 정리 규칙을 손쉽게 작성할 수 있습니다.

규칙 구문이나 백그라운드 데몬 관련 피드백, 기여를 언제든 환영합니다.

## 원문
- [원문](https://github.com/taevel02/Sift)
- [GeekNews 토론](https://news.hada.io/topic?id=32300)

## My Note
<!-- 한 줄 코멘트 남기기 -->

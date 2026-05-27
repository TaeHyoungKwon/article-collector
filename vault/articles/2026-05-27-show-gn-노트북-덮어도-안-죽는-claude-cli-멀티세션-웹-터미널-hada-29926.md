---
category: AI
collected_at: '2026-05-27T19:39:16+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29926
id: hada-29926
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/kimtaeyeong1229
title: 'Show GN: 노트북 덮어도 안 죽는 Claude CLI 멀티세션 웹 터미널'
url: https://github.com/kimtaeyeong1229/claude-web-terminal
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
브라우저 탭으로 **여러 Claude CLI 세션을 한 번에 굴리는** 웹 터미널을 만들었습니다.

세션은 서버에 PTY 로 떠 있고 브라우저는 그 화면을 보여줄 뿐이라서, 브라우저를 닫아도 노트북을 덮어도 작업이 계속됩니다. PC 를 끄고 켜도 자동 `--resume` 으로 세션이 복원됩니다.

### 주요 특징

- **멀티세션** — 탭/사이드바 UI 로 N 개의 Claude CLI 를 한 화면에서 전환·관리
- **세션 영속화** — `~/.claude-web-terminal/sessions.json` 에 자동 저장, 서버/PC 재시작 시 자동 복원
- **Docker 컨테이너** — 호스트뿐 아니라 실행 중인 컨테이너 안의 폴더를 골라 그 안에서 Claude 실행 (`docker exec -it -w <path> <container> claude`)
- **외부 Claude 프로세스 감지** — 이미 떠있는 다른 터미널의 claude 에 연결 (Linux `/proc`)
- **재접속 시 스크롤백 복원** — 200KB 버퍼
- **단일 파일 프론트** — Vanilla HTML/CSS/JS, XTerm.js + 약 2,400 줄
- **단일 파일 백엔드** — Python aiohttp + PTY + WebSocket, 약 500 줄

### 스택

- 백엔드: Python 3.10+ / aiohttp / PTY / WebSocket
- 프론트: Vanilla HTML·CSS·JS, XTerm.js 5.5, FitAddon, WebLinksAddon
- 인증: 없음 — 127.0.0.1 바인딩 권장 (LAN 노출 시 reverse proxy + basic auth)

### 자동 실행

- macOS: LaunchAgent plist (README 에 템플릿 포함)
- Linux: systemd user service + `loginctl enable-linger`

### 한 줄 설치

```bash  
git clone <https://github.com/kimtaeyeong1229/claude-web-terminal>  
cd claude-web-terminal && pip install -r requirements.txt  
python3 server.py --host 127.0.0.1 --port 8080  
```

브라우저에서 `http://127.0.0.1:8080`.

### 만든 동기

- Claude CLI 가 좋아서 자주 쓰는데 터미널 창 N 개 띄우기가 번거로움
- 노트북 덮으면 죽거나, ssh 끊기면 세션 끊기는 게 싫음 → 서버 사이드 PTY 로 분리
- 도커 환경에 들어가서 claude 띄우려고 `docker exec -it` 하는 절차가 매번 귀찮음 → UI 에 통합

### 한계

- 인증 없음 — 로컬/신뢰 네트워크 전제
- 외부 프로세스 감지는 Linux 만 (macOS 는 `/proc` 없음)
- 멀티유저/계정 분리 없음 — 단일 사용자 도구

피드백/이슈 환영합니다.

## 원문
- [원문](https://github.com/kimtaeyeong1229/claude-web-terminal)
- [GeekNews 토론](https://news.hada.io/topic?id=29926)

## My Note
<!-- 한 줄 코멘트 남기기 -->

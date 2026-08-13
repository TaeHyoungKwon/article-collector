---
category: AI
collected_at: '2026-08-12T23:56:52+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32436
id: hada-32436
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: -993.307
recommended_on: '2026-08-12'
source: geeknews
tags:
- AI
- Other
- github.com/cpprhtn
title: 'Show GN: LiteDeck – EC2부터 홈서버까지, SSH 포트 하나로 Claude·Codex와 함께 개발 및 모니터링하기'
url: https://github.com/cpprhtn/LiteDeck
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
파일 하나 고치자고 서버에 `vscode-server`를 올립니다. 관리 UI 하나 쓰자고  
패키지를 깔고 포트를 열고, 클라우드면 보안 그룹까지 건드립니다. 요즘은 AI까지  
붙이려고 서버에 Claude Code나 Codex CLI를 깝니다. 그렇게 깔아둔 것들은 나중에  
그것대로 관리 대상이 되고요. **애초에 뭘 깔 수 없거나, 깔면 안 되는 서버도  
많습니다.**

그게 싫어서 만들었습니다.

**서버에는 아무것도 설치하지 않습니다.** 에이전트도, 데몬도, 패키지도,  
`vscode-server`도, Claude도 Codex도 깔지 않습니다. 이미 열려 있는 **SSH 포트  
하나**만 씁니다. 포트를 새로 열지 않으니 클라우드면 보안 그룹도 그대로입니다.

그 상태로 **내 PC의 Claude Code나 Codex CLI가 이 앱을 거쳐** 서버를 조회하고  
파일을 고칩니다. 서버에 Node도 Python도 없는데 Claude가 그 서버의 nginx 설정을  
고치는 식입니다. AI는 GUI와 **같은 어댑터·같은 SSH 연결·같은 Command Log**를  
씁니다. AI 전용 경로가 따로 없습니다.

**전권을 주는 건 아닙니다.** 기본은 전부 꺼져 있고, 켜도 이렇습니다:

- 파일 변경은 **서버에 지금 들어 있는 내용과의 diff**를 띄워 승인을 받습니다  
  (AI가 가질 수 없는 정보라서 사람이 봐야 하는 화면입니다)
- 바꾼 파일은 **되돌릴 수 있습니다**
- Command Log에 **어느 줄이 AI 때문인지** 표시됩니다
- **임의 명령 실행과 삭제는 아예 제공하지 않습니다**
- MCP 엔드포인트는 **`127.0.0.1`에만** 열립니다. tailnet에도 안 올라갑니다

정리하면 **AI는 내 PC에서 돌고, 서버로 가는 것은 평소의 SSH 세션 하나**입니다.  
서버에 AI 도구를 못 깔거나 깔면 안 되는 곳에서도 그대로 됩니다.

**편집기도 양쪽 어디에도 필요 없습니다.** 서버에 `vi`나 VS Code가 없어도 되고,  
**내 PC에 VS Code가 없어도 됩니다.** 편집기가 앱 안에 들어 있습니다(CodeMirror,  
문법 24종). 터미널에 `code .`이나 `vi foo.conf`를 치면 **그 줄이 서버로 가기 전에  
앱이 가로채서** 파일 탭을 엽니다. 서버는 이 기능이 있는지도 모릅니다. 저장할 때는  
서버 현재 내용과의 diff를 먼저 보여주고, 임시 파일에 쓴 뒤 `rename`으로  
갈아끼웁니다 — 저장이 중간에 끊겨도 원본이 반토막 나지 않습니다.

**양쪽 다 OS를 가리지 않습니다.**

서버 쪽은 SSH가 열려 있으면 같습니다 — AWS 같은 클라우드 인스턴스, VPS,  
Proxmox VM, 사내 서버, 홈서버. 오토스케일링으로 사라질 인스턴스에 관리  
에이전트를 깔 이유도, 그것 때문에 AMI를 다시 구울 이유도 없습니다.

클라이언트 쪽도 **macOS·Windows·Ubuntu에서 같은 앱이 돕니다.** 런타임을 따로  
깔 필요가 없습니다 — JVM도, Node도, 번들된 Chromium도 없습니다.

사실 이건 **서버 쪽과 같은 원칙**입니다. 서버에서는 **이미 있는 명령**을 쓰고,  
내 PC에서는 **이미 있는 웹뷰**를 씁니다(WebView2 / WebKitGTK / WKWebView).  
Go로 만들어 OS마다 정적 바이너리 하나가 나오고, 화면은 OS가 이미 가진 것으로  
그립니다. 다운로드가 5MB대인 이유이자, Electron이 아닌 이유입니다.

**모니터링과 운용** — CPU·메모리·디스크·로드, systemd 유닛 시작/중지/재시작과  
실시간 로그, 프로세스 테이블(트리 보기·종료), 열린 포트와 sshd 설정 점검,  
Docker/Podman(Compose 프로젝트 단위 조작), 지금 이 서버에 누가 SSH로 붙어 있는지.  
Windows 서버는 PowerShell 어댑터로 같은 일을 합니다.

**실행하는 모든 명령이 화면에 보입니다.** 운영 서버를 만지는 GUI는 결국  
"믿어달라"고 요구하는 셈이라, 방금 무엇을 실행했는지 그대로 보여주는 쪽을  
골랐습니다. 비밀번호는 stdin으로 가서 명령줄에는 안 남습니다.

**앞으로 할 것**

- **리소스 대시보드 탭** — 그라파나·프로메테우스로 보던 서버 자원 그래프를 심플하게나마 제공할 계획입니다.
- **NVIDIA GPU 추적** — `nvidia-smi`가 있는 서버의 사용률·VRAM·온도·점유  
  프로세스. 내장 GPU는 아직 고려하고 있지 않습니다.
- **2.0.0 — UI/UX 개편** — 지금 화면은 기능을 붙여가며 만든 것이라,  
  실제로 써본 경험과 받은 피드백을 모아 한 번 크게 갈아엎을 계획입니다

Go + Wails + React. 다운로드 4.8~9.8MB. Apache-2.0.

**검증 범위를 문서에 그대로 적어뒀습니다.** macOS·Windows·Ubuntu 24.04.4에서  
확인했고, 아직 컨테이너에서만 확인한 것도 목록으로 남겨뒀습니다. 서명이 없어서  
첫 실행에 Gatekeeper/SmartScreen 경고가 뜹니다(넘기는 방법은 문서에).

**기여와 이슈, 피드백은 언제나 환영합니다.**

[Github/LiteDeck](https://github.com/cpprhtn/LiteDeck)

## 원문
- [원문](https://github.com/cpprhtn/LiteDeck)
- [GeekNews 토론](https://news.hada.io/topic?id=32436)

## My Note
<!-- 한 줄 코멘트 남기기 -->

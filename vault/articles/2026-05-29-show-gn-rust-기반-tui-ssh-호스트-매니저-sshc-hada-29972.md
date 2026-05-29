---
category: Other
collected_at: '2026-05-29T08:55:41+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29972
id: hada-29972
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/hang-in
title: 'Show GN: Rust 기반 TUI SSH 호스트 매니저, sshc'
url: https://github.com/hang-in/sshc
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요.

터미널에서 가볍고 안전하게 호스트를 찾아 접속할 수 있는  
**작은 Rust 기반 TUI 도구, `sshc`** 를 공유합니다.\*\*

**GitHub 저장소:** <https://github.com/hang-in/sshc>

---

#### 주요 핵심 기능 및 아키텍처

`sshc`는 **"사용자가 직접 작성한 설정 파일은 절대 건드리지 않는다"** 는 철학 하에 설계되었습니다.

**인라인 모드 (`sshc`)** 화면 전환 없이 셸 프롬프트 바로 아래에 picker를 띄웁니다. (스크롤백을 해치지 않고 Enter 한 번으로 빠른 접속)  
**관리 모드 (`sshc -m`)** 전체 화면 TUI를 통해 호스트 추가, 삭제, 즐겨찾기, 태그 편집을 지원합니다. (`$EDITOR` 연동 및 직관적인 호스트 관리)  
**안전한 격리 구조** 새 호스트는 오직 `~/.ssh/config.d/sshc.conf`에만 기록됩니다. (기존 `~/.ssh/config` 파일은 `Include` 한 줄만 추가하여 안전하게 보호)  
**다양한 플랫폼 지원** macOS, Linux(빌드 필요)는 물론 **네이티브 Windows 빌드(v0.7+)** 까지 지원합니다. (WSL2 사용자는 물론 Windows OpenSSH 환경까지 완벽 대응)

---

#### 왜 `fzf` 스니펫이나 다른 도구 대신 `sshc`인가요?

1. **지능형 우선순위와 태그 시스템:**  
   관리 모드에서 자주 쓰는 서버에 핀(`f`)을 꽂아두거나 최근 접속한 이력이 있으면 인라인 모드에서 자동으로 최상단에 노출됩니다. `# @tags: prod, staging`과 같은 주석 기반 태그를 지원하여 `@prod` 검색만으로 운영 서버들만 가려낼 수 있습니다.
2. **환경 진단 도구 (`sshc --doctor`):**  
   인프라가 가끔 먹통이 될 때, 네트워크 호출을 최소화하면서 `~/.ssh` 권한 상태, `ssh-agent`의 파이프 연결 상태(`SSH_AUTH_SOCK` 등)를 정밀 진단해 주는 든든한 조력자 역할을 합니다.
3. **바퀴를 다시 발명하지 않는 안전함:**  
   파이썬 기반의 일부 도구들처럼 기존 설정 파일을 통째로 파싱해서 구조를 깨뜨리지 않습니다. 단순 텍스트 매칭으로 `Include` 구문을 놓치는 `fzf` 스크립트와 달리, `ssh -G` 매커니즘을 존중하며 시스템과 완벽히 공존합니다.

---

#### 빠른 설치 및 시작

**macOS / Linux (Homebrew):**

```
brew install hang-in/tap/sshc  
sshc
```

**Windows (PowerShell):**

```
irm [https://github.com/hang-in/sshc/…](https://github.com/hang-in/sshc/releases/latest/download/sshc-installer.ps1) | iex
```

터미널을 떠나고 싶지 않은 엔지니어의 효율적인 워크플로우를 위해 빌드되었습니다. 이제 "그 서버 alias 이름이 뭐였더라?" 하고 cat ~/.ssh/config를 치는 수고를 내려놓으세요.

오픈소스 프로젝트인 만큼 이슈 제보나 Pull Request는 언제나 대환영입니다. (24시간 이내 답변을 목표로 달리고 있습니다!) 마음에 드셨다면 깃허브에 ⭐️**Star** 하나씩 부탁드립니다. 감사합니다!

## 원문
- [원문](https://github.com/hang-in/sshc)
- [GeekNews 토론](https://news.hada.io/topic?id=29972)

## My Note
<!-- 한 줄 코멘트 남기기 -->

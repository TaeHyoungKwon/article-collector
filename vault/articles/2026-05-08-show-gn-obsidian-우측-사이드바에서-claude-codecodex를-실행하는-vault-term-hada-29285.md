---
category: Dev Tools
collected_at: '2026-05-08T10:21:46+09:00'
geeknews_comments: 1
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29285
id: hada-29285
matched_keywords:
- Claude Code
- Codex
read: false
recommend_score: -994.406
recommended_on: '2026-05-08'
source: geeknews
tags:
- Dev Tools
- github.com/obst2580
title: 'Show GN: Obsidian 우측 사이드바에서 Claude Code,Codex를 실행하는 Vault Terminal 플러그인을 만들었습니다'
url: https://github.com/obst2580/obsidian-powershell
---

## TL;DR
- 이 글은 Obsidian에서 Claude Code와 Codex를 실행할 수 있는 Vault Terminal 플러그인의 개발에 대해 다룬다.
- Vault Terminal 플러그인은 Obsidian 우측 사이드바에서 PowerShell, zsh, bash 등 다양한 CLI 도구를 사용할 수 있게 한다.
- 이 플러그인은 사용자에게 Obsidian 내에서 더 효율적인 작업 환경을 제공하며 CLI 도구와의 통합을 가능하게 한다.

## GeekNews 요약
Obsidian에는 기존 터미널 플러그인도 있지만, 제 Windows 환경에서는 Claude Code/Codex 같은 agent CLI를 쓰기에 PTY 동작, 스크롤, 색상, 특수 입력 처리에서 아쉬움이 있었습니다.

그래서 Obsidian 우측 사이드바에 실제 터미널을 띄우고, 현재 볼트 경로를 작업 디렉터리로 사용하는 Vault Terminal 플러그인을 만들었습니다.

Obsidian 노트에는 프로젝트 문서, 설계 메모, 작업 로그를 열어두고, 우측 터미널에서는 claude, codex, git, npm 같은 CLI를 바로 실행하는 흐름을 목표로 했습니다. Claude Code나 Codex CLI가 같은 볼트 안의 AGENTS.md, CLAUDE.md, 프로젝트 노트, 소스 파일을 기준으로 작업할 수 있습니다.

주요 기능은 다음과 같습니다.

Obsidian 우측 사이드바에서 터미널 실행  
현재 볼트 경로를 기준으로 PowerShell, zsh, bash 실행  
Claude Code, Codex CLI, git, npm, Python 같은 CLI 도구 실행  
Windows/macOS 릴리스 ZIP 제공  
Windows 기본 winpty 지원, 필요 시 ConPTY 전환  
Obsidian 라이트/다크 테마에 맞춘 터미널 색상  
Claude Code 멀티라인 입력을 위한 Shift+Enter 처리  
긴 출력 확인을 위한 scrollback 및 강제 스크롤  
TLS inspection proxy / 사용자 지정 CA 환경 설정 지원  
아직 초기 베타입니다. 현재는 Obsidian Community Plugin 방식보다는 GitHub Release ZIP을 받아 볼트별로 설치하는 방식입니다. Node.js가 시스템에 설치되어 있어야 하고, Claude Code/Codex CLI도 VS Code extension이 아니라 터미널 명령으로 실행 가능한 상태여야 합니다.

GitHub:  
<https://github.com/obst2580/obsidian-powershell>

Release:  
<https://github.com/obst2580/obsidian-powershell/releases>

Windows/macOS 환경에서 Claude Code, Codex CLI 같은 agent CLI를 Obsidian과 함께 쓰는 분들의 피드백을 받고 싶습니다.

## 원문
- [원문](https://github.com/obst2580/obsidian-powershell)
- [GeekNews 토론](https://news.hada.io/topic?id=29285)

## My Note
<!-- 한 줄 코멘트 남기기 -->

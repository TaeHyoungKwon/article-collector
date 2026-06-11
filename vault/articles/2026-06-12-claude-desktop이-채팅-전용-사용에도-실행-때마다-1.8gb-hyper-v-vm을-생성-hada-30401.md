---
category: AI
collected_at: '2026-06-12T02:35:13+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30401
id: hada-30401
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/anthropics
title: Claude Desktop이 채팅 전용 사용에도 실행 때마다 1.8GB Hyper-V VM을 생성
url: https://github.com/anthropics/claude-code/issues/29045
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Claude Desktop Windows** 앱이 채팅만 사용할 때도 실행마다 Hyper-V VM을 띄우고, Task Manager에서 **Vmmem**이 약 1,796~1,846MB RAM을 사용하는 현상
- 재현 조건은 Windows 11에서 **VirtualMachinePlatform**을 켠 상태로 Claude Desktop을 설치하고, Cowork/agent mode를 한 번 사용한 뒤 앱을 다시 열거나 재부팅하는 절차
- 보고 환경은 Windows 11 Pro 25H2 Build 26200.7840, Razer Blade 15 Base Model Late 2020, i7-10750H, 16GB RAM, 2026-02-26 기준 Claude Desktop 최신 버전
- Hyper-V, WSL, Docker, Windows Sandbox는 비활성화되어 있고 Core Isolation / Memory Integrity도 꺼져 있으며, `wsl --shutdown`은 “not installed”, `Get-VM`은 실패, Docker 프로세스는 발견되지 않음
- 실행 때마다 Claude Desktop이 RPC interface event를 통해 **vmcompute**를 트리거하고, `vmwp.exe` 프로세스가 VM을 호스팅하며, 부모 프로세스는 `services.exe`로 확인됨
- Hyper-V Compute Admin 로그에 `"The specified property query is invalid: The virtual machine or container JSON document is invalid. (0xC037010D, 'Invalid JSON document '$'')"` 오류가 부팅과 앱 실행 때 반복됨
- `%APPDATA%\Claude\local-agent-mode-sessions\`에서 이전 Cowork 세션의 오래된 세션 파일 2,689개가 발견됐고, 파일 삭제와 `vmcompute`/`vmwp` 종료 뒤에도 Claude Desktop 재실행 시 VM과 1.8GB Vmmem 프로세스가 즉시 다시 생성됨
- 16GB 시스템에서 유휴 메모리 사용량이 약 50%에서 62%로 증가하고, 일반 앱 부하와 함께 70~75%까지 올라가 시스템 둔화와 매 실행 후 VM 프로세스 수동 종료가 필요해짐
- 우회책은 `Disable-WindowsOptionalFeature -Online -FeatureName "VirtualMachinePlatform" -NoRestart`로 VirtualMachinePlatform을 끄는 방법이며, 이 경우 VM 실행은 막지만 Cowork 기능도 비활성화됨
- 다른 우회책은 `Stop-Process -Name vmwp -Force`와 `Stop-Process -Name vmcompute -Force`로 VM 프로세스를 매번 종료하는 방법이며, 종료 후에도 채팅 기능은 정상 동작함
- 요청된 동작은 Cowork 또는 agent mode가 실제로 요청될 때만 VM/container 인프라를 초기화하고, 세션 종료 후 오래된 세션 데이터를 자동 정리하며, VM 인프라가 없거나 불필요할 때 채팅 전용 모드로 처리하는 방식임

## 원문
- [원문](https://github.com/anthropics/claude-code/issues/29045)
- [GeekNews 토론](https://news.hada.io/topic?id=30401)

## My Note
<!-- 한 줄 코멘트 남기기 -->

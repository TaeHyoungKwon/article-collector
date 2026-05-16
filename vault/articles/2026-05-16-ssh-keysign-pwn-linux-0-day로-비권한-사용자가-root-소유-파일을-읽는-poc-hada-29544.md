---
category: AI
collected_at: '2026-05-16T09:12:41+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29544
id: hada-29544
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/0xdeadbeefnetwork
title: ssh-keysign-pwn - Linux 0-day로 비권한 사용자가 root 소유 파일을 읽는 PoC
url: https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **ssh-keysign-pwn**은 비권한 사용자가 root 소유 파일을 읽을 수 있게 하는 Linux 취약점 PoC로, `31e62c2ebbfd` 이전 커널이 대상이라고 밝힘
- 핵심 버그는 `__ptrace_may_access()`가 `task->mm == NULL`일 때 **dumpable 검사**를 건너뛰고, `do_exit()`가 `exit_mm()`을 `exit_files()`보다 먼저 실행해 파일 디스크립터가 열린 채 남는 창이 생기는 구조임
- 이 창에서 호출자의 uid가 대상 프로세스와 일치하면 **`pidfd_getfd(2)`** 가 성공해, 종료 중인 프로세스의 열린 파일 디스크립터를 가져올 수 있음
- `sshkeysign_pwn`은 `/etc/ssh/ssh_host_{ecdsa,ed25519,rsa}_key`를 가져오며, `ssh-keysign.c`가 0600 권한의 키를 연 뒤 `permanently_set_uid()` 전에 `EnableSSHKeysign=no`로 종료하면서 열린 fd를 남기는 흐름을 이용함
- `chage_pwn`은 `/etc/shadow`를 가져오며, `chage -l <user>`가 `spw_open(O_RDONLY)` 후 `setreuid(ruid, ruid)`로 권한을 완전히 내려놓는 흐름에서 종료 레이스를 노림
- 실행은 `make` 후 `./sshkeysign_pwn`으로 호스트 키를, `./chage_pwn root`로 `/etc/shadow` 내용을 표준 출력에 출력하는 방식이며, 100~2000회 스폰 안에 적중한다고 밝힘
- 확인된 환경은 **Raspberry Pi OS Bookworm 6.12.75**, Debian 13, Ubuntu 22.04 / 24.04 / 26.04, Arch, CentOS 9임
- 제어된 대상 PoC로 `vuln_target.c`는 `/etc/shadow`를 연 뒤 권한을 내리고, `exploit_vuln_target.c`는 살아 있는 동안의 `EPERM`과 `SIGKILL` 이후 fd 탈취를 보여줌
- 취약점은 Qualys가 보고했고 Linus가 2026-05-14에 수정했으며, Jann Horn은 2020년 10월에 [FD 탈취 형태](https://lore.kernel.org/all/20201016230915.1972840-1-jannh@google.com/)를 짚었다고 밝힘
- README는 NVD 항목으로 `https://nvd.nist.gov/vuln/detail/CVE-2026-46333`을 제시함

## 원문
- [원문](https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn/)
- [GeekNews 토론](https://news.hada.io/topic?id=29544)

## My Note
<!-- 한 줄 코멘트 남기기 -->

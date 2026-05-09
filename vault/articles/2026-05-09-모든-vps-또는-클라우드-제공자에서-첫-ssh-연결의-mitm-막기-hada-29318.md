---
category: AI
collected_at: '2026-05-09T15:02:06+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29318
id: hada-29318
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- joachimschipper.nl
title: 모든 VPS 또는 클라우드 제공자에서 첫 SSH 연결의 MITM 막기
url: https://www.joachimschipper.nl/Stop%20MITM%20on%20the%20first%20SSH%20connection,%20on%20any%20VPS%20or%20cloud%20provider.html
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- [ssh-init-vm](https://github.com/JoachimSchipper/ssh-init-vm/blob/main/ssh-init-vm)은 새 VM의 첫 SSH 접속에서 **중간자 공격**을 막기 위해 cloud-init으로 임시 SSH 호스트 개인키를 주입하고, 장기 호스트 키를 생성·가져오는 동안만 신뢰하게 함
- Hetzner Cloud처럼 전용 접속 보호 기능이 없는 VPS나 클라우드에서도 동작하며, 필요한 것은 널리 지원되는 **cloud-init**뿐임
- 일반적인 **Trust On First Use**에서 `ssh`의 “The authenticity of host [...] can't be established” 질문에 `yes`를 입력하면, 공격자가 트래픽을 프록시하거나 사용자의 VM처럼 보이는 머신을 제공할 수 있음
- 장기 SSH 호스트 개인키를 cloud-init userdata에 직접 넣으면 첫 접속 인증에는 도움이 되지만, 메타데이터 서비스·SSRF·클라우드 제공자 시스템·관리자 워크스테이션을 통해 **민감한 키 자료**가 노출될 수 있음
- ssh-init-vm은 임시 키를 임시 디렉터리에 두고 `~/.ssh/known_hosts`에 넣지 않으며, VM 출력물을 그대로 저장하지 않고 OpenSSH의 **호스트 키 순환**에 의존해 장기 키를 기록함

---

## 원문
- [원문](https://www.joachimschipper.nl/Stop%20MITM%20on%20the%20first%20SSH%20connection,%20on%20any%20VPS%20or%20cloud%20provider.html)
- [GeekNews 토론](https://news.hada.io/topic?id=29318)

## My Note
<!-- 한 줄 코멘트 남기기 -->

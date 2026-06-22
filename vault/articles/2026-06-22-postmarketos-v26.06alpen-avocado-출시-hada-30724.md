---
category: AI
collected_at: '2026-06-22T19:01:24+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30724
id: hada-30724
matched_keywords:
- AI
- RAG
read: false
recommend_score: 4.901
recommended_on: '2026-06-22'
source: geeknews
tags:
- AI
- Other
- postmarketos.org
title: postmarketOS v26.06(Alpen Avocado) 출시
url: https://postmarketos.org/blog/2026/06/21/v26.06-release/
---

## TL;DR
- postmarketOS v26.06(Alpen Avocado)는 Linux 기반 모바일 운영체제의 최신 출시를 다룬다.
- Alpine Linux 3.24를 기반으로 하며, 다수의 모바일 UI 업데이트와 새로운 기능들이 추가되었다.
- 이 릴리스는 사용자에게 향후 지원 중단 예정인 기능들에 대한 경고와 개선된 사용자 경험을 제공한다.

## GeekNews 요약
- **Linux 애호가**를 주 대상으로 하며, Android나 iOS 수준의 완성도를 기대하는 사용자에게는 아직 맞지 않는 릴리스
- **Alpine Linux 3.24**를 대상으로 하며, GNOME 50, KDE Plasma Mobile 6.6.5, Phosh 0.55.0으로 모바일 UI 버전 갱신
- 기존 설치 업그레이드 후 권장 수동 작업은 SXMO 사용자가 아니면 [input 그룹에서 제거](https://postmarketos.org/devel/2026/06/12/input-group-removal/), [ffmpegthumbnailer 제거](https://postmarketos.org/edge/2025/12/13/ffmpeg-to-gst-thumbnailers/), 커널 cmdline 사용자 설정을 `/etc/kernel-cmdline.d/`로 마이그레이션
- 커널 cmdline의 기존 방식은 당분간 지원되지만 **지원 중단 경고**가 표시되는 상태
- 새 설치의 기본 권한 상승 도구가 **doas**에서 [sudo-rs](https://postmarketos.org/edge/2026/03/18/sudo-rs-instead-of-doas/)로 변경
- 부팅 화면이 [pbsplash에서 Plymouth](https://postmarketos.org/edge/2026/04/30/Switching-from-pbsplash-to-Plymouth/)로 전환되며, ESC 또는 휴대폰 전원 버튼으로 부팅 로그 표시, 잘못 표시되는 기기에서 splash 화면 회전 가능
- 진동이 동작하는 기기는 부팅 시 **진동** 가능, initramfs 모듈이 없거나 진동할 수 없는 기기에서는 동작 없음
- Phosh는 기존 postmarketOS tweaks 앱의 관련 기능을 **Phosh Mobile Settings**에 통합하고, display manager를 tinydm에서 greetd와 phrog로 전환
- Plasma desktop의 systemd 변형은 **sddm** 대신 plasma-login-manager 사용, postmarketOS에서 Plasma와 OpenRC 조합은 더 이상 권장되지 않으며 향후 비활성화 예정
- [Plasma Bigscreen](https://plasma-bigscreen.org/)은 Plasma 6 비호환으로 v24.06 이후 비활성화됐지만 v26.06에서 다시 사용 가능
- ModemManager 업그레이드로 **cell broadcast** 같은 새 기능 추가
- `linux-postmarketos-{mainline,stable,lts}` generic kernel packages가 v26.06에 포함되며, v26.06 지원 기간 동안 업그레이드 및 최신 상태 유지
- testing 카테고리 기기는 **254개**이며, ASUS MeMO Pad 7, Microsoft Surface RT, NVIDIA Tegra ARMv7, Samsung Chromebook, Xiaomi Mi Pad 5 Pro는 커널이 너무 오래됐거나 유지보수되지 않아 community에서 testing으로 이동
- 새 community 기기에는 Google Asurada Chromebook, Google Cherry Chromebook, Google Corsola Chromebook, Radxa Dragon Q6A, PINE64 PineNote 포함
- 미해결 이슈에는 일부 사용자의 재플래시 후 `pmOS_root` 99% 사용, Phosh 시작 시 `/dev/loop1p2` 프롬프트, Fairphone 5 밝기 조절 아티팩트, Fairphone 3 과도한 오디오 볼륨, Librem 5 splash 화면 없음, PinePhone DTMF 톤 동작 중단 포함 {p:99}

## 원문
- [원문](https://postmarketos.org/blog/2026/06/21/v26.06-release/)
- [GeekNews 토론](https://news.hada.io/topic?id=30724)

## My Note
<!-- 한 줄 코멘트 남기기 -->

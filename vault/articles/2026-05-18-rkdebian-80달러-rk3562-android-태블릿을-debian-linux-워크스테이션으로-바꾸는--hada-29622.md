---
category: AI
collected_at: '2026-05-18T16:36:28+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29622
id: hada-29622
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-05-18'
source: geeknews
tags:
- AI
- Other
- github.com/tech4bot
title: rkdebian - 80달러 RK3562 Android 태블릿을 Debian Linux 워크스테이션으로 바꾸는 빌드 시스템
url: https://github.com/tech4bot/rk3562deb
---

## TL;DR
- **rkdebian**은 Rockchip RK3562 기반 Doogee U10 태블릿을 Debian Linux 워크스테이션으로 변환하는 빌드 시스템이다.
- 이 시스템은 SD 카드를 통해 부팅할 수 있으며, 부팅 후 내부 기본 Android 환경으로 복귀할 수 있어 안전하게 사용할 수 있다.
- 독자는 가성비 높은 태블릿을 활용해 Debian 환경을 구축할 수 있는 방법을 알게 되어, 자신의 작업 환경을 다양화할 수 있다.

## GeekNews 요약
- **rkdebian**은 Rockchip RK3562 기반 **Doogee U10** Android 태블릿용으로 부팅 가능한 Debian 12 Bookworm 이미지를 만드는 빌드 시스템임
- 현재 공개 프리릴리스 빌드는 2026년 5월 14일자이며, [릴리스 페이지](https://github.com/tech4bot/rk3562deb/releases/tag/prerelease-14052026)와 [rk3562-debian.img.xz](https://github.com/tech4bot/rk3562deb/releases/download/prerelease-14052026/rk3562-debian.img.xz) 직접 다운로드, [YouTube 데모](https://youtu.be/DbX13_mahKc?si=Ba9u2xqAmoXM7nYb)가 제공됨
- 이미지는 **SD 카드**에 기록해 부팅하며, SD 카드를 제거하면 내부 eMMC의 기본 Android로 돌아가므로 부트로더 언락이나 내부 저장소 변경이 필요 없음
- 대상 하드웨어는 **Doogee U10**으로, RK3562 4× Cortex-A53 2.0GHz, 4GB LPDDR4, 128GB eMMC, 10.1인치 1280×800 DSI 패널, RK817 PMIC 구성을 사용함
- 디스플레이, 10점 멀티터치, Wi-Fi, Bluetooth, 스피커, 마이크, 배터리/충전, SD 카드 부팅, USB OTG, 가속도계, 후면 LED 손전등, 전원 버튼 동작, 잠금화면 회전 유지가 동작함
- **3D 가속**은 Panfrost 기반으로 OpenGL ES가 동작하는 부분 지원 상태이며, 전면 `s5k5e8`·후면 `s5k4h5yb` 카메라는 파이프라인과 미리보기·캡처가 동작하지만 색상 보정에는 추가 ISP 캘리브레이션이 필요함
- RK3562의 단일 **NPU 코어**를 사용해 Rockchip RKLLM 스택 기반 로컬 LLM 추론을 지원하며, [airockchip/rknn-llm](https://github.com/airockchip/rknn-llm)과 [airockchip/rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2)를 사용함
- 태블릿에서 측정한 NPU 경로 기준으로 `Qwen3-0.6B_W8A8_RK3562_opt0`은 warm-run 평균 생성 4.92 tok/s, `Qwen2.5-1.5B-Instruct_W8A8_RK3562`는 2.18 tok/s였고, `Qwen3-0.6B`가 이 RK3562 태블릿에서 더 빠름
- 기본 앱으로 **Firefox ESR**, Chromium, FreeTube, Drawing, Snapshot, Dolphin, Plasma Discover, Okular, Gedit, Pavucontrol, Terminal이 포함되며 Flatpak과 Flathub가 기본 활성화됨
- 빌드는 x86-64 Linux 호스트에서 수행하며 Debian/Ubuntu가 권장되고, `./build.sh all`로 U-Boot, Linux 커널, Debian rootfs, 플래시 가능한 SD 카드 이미지를 한 번에 생성함
- 빌드 옵션은 Phosh UI 세션, `mali` 또는 `panfrost` GPU 스택, Wayland/X11 표시 서버, CPU 거버너, rootfs 재생성, 이미지 최소화, FreeTube 사전 설치 여부 등을 조정할 수 있음
- Debian 실행 후에는 SD 카드를 다시 플래시하지 않고 `output/update/update.tar.gz`를 태블릿의 `/home/chaos/update/` 또는 `/update/pending/`에 넣어 다음 재부팅 때 **OTA 업데이트**를 적용할 수 있음
- 기본 계정은 `chaos/chaos`와 `root/root`이며, 첫 부팅 후 `passwd`와 `sudo passwd root`로 비밀번호를 변경하라는 안내가 포함됨
- Linux 커널은 rockchip-linux `develop-6.1` 계열 6.1.x, U-Boot는 Firefly `rk356x/firefly-5.10`, Debian은 arm64 Bookworm을 사용하며, 프로젝트 자체 라이선스는 **MIT License**임

## 원문
- [원문](https://github.com/tech4bot/rk3562deb)
- [GeekNews 토론](https://news.hada.io/topic?id=29622)

## My Note
<!-- 한 줄 코멘트 남기기 -->

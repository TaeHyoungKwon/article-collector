---
category: Other
collected_at: '2026-06-04T00:34:26+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30148
id: hada-30148
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/c0dejedi
title: nbd-vram - Linux에서 NVIDIA GPU VRAM을 스왑 공간으로 사용하는 도구
url: https://github.com/c0dejedi/nbd-vram
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **nbd-vram**은 Linux에서 NVIDIA GPU의 유휴 VRAM을 높은 우선순위의 스왑 공간으로 쓰게 해주는 작은 데몬임
- 납땜 메모리라 업그레이드가 어렵고 내장 AMD/ATI GPU가 화면 출력을 맡는 **하이브리드 그래픽 노트북**에서, 놀고 있는 NVIDIA VRAM을 메모리 압박 완화에 활용함
- 테스트 환경은 AMD/ATI + RTX 3070 Laptop, RAM 16GB, VRAM 8GB, NVIDIA driver 580.159.03, kernel 6.17, Pop!\_OS이며, VRAM 7GB를 스왑으로 할당해 zram·SSD 스왑까지 합쳐 약 46GB의 주소 지정 가능한 메모리를 구성함
- 동작 순서는 RAM이 먼저 차고, 그다음 **VRAM**이 PCIe를 통해 넘친 페이지를 흡수하며, 이후 zram이 CPU로 압축하고, 마지막에 SSD를 사용하는 구조임
- 데몬은 CUDA driver API로 VRAM을 할당하고, Unix socket 위의 **NBD(Network Block Device)** 프로토콜로 블록 장치를 제공하며, 커널의 내장 `nbd` 드라이버가 `/dev/nbdX`로 노출해 일반 스왑 장치처럼 사용함
- 데이터 경로는 kernel swap subsystem → `/dev/nbdX` → nbd kernel driver → Unix socket → nbd-vram daemon → `cuMemcpyHtoD/DtoH` → GPU VRAM으로 이어짐
- 별도 커널 모듈이나 NVIDIA 커널 심볼이 필요 없어서, 커널·드라이버 업데이트 뒤에도 재빌드 없이 유지될 수 있음
- NVIDIA P2P API 방식은 consumer GeForce GPU에서 `nvidia_p2p_get_pages_persistent`가 `EINVAL`을 반환하고, BAR1 직접 `ioremap_wc` 방식도 약 16MiB의 디스플레이 프레임버퍼 외 영역 읽기가 0을 반환해 실패함
- **CUDA 복사 경로**인 `cuMemcpyHtoD`와 `cuMemcpyDtoH`는 특별한 권한 없이 CUDA GPU에서 동작하므로, NBD 접근이 P2P·BAR1 제약을 우회함
- 요구사항은 CUDA 지원 NVIDIA GPU, `libcuda.so.1`이 있는 NVIDIA 드라이버, Linux kernel 3.0+의 nbd 모듈, `nbd-client`, `gcc`, `make`이며 CUDA toolkit은 필요 없음
- 설치 후 `vram-swap-nbd` systemd 서비스가 부팅 시 자동 실행되며, `/etc/systemd/system/vram-swap-nbd.service`의 `VRAM_SETUP_SIZE_MB`와 `VRAM_SWAP_PRIORITY`로 사용할 VRAM 상한과 스왑 우선순위를 조정함
- 데몬은 요청한 VRAM 크기를 먼저 시도하고 GPU 메모리가 부족하면 512MiB 단위로 줄여 할당하므로, `VRAM_SETUP_SIZE_MB`는 필수 크기가 아니라 상한으로 동작함
- 전원 인식 관리를 켜면 AC 전원 해제나 배터리 임계값 이하에서 서비스가 자동 중지되고, 전원이 복구되면 다시 시작되며, 수동 `systemctl stop`은 덮어쓰지 않음
- RTX 3070 Laptop 벤치마크에서 순차 처리량과 지속 랜덤 I/O는 NVMe가 더 빠르지만, 4K 읽기 1 request/sec 지연 시간은 VRAM이 평균 335us로 NVMe 9.05ms보다 27배 빠름
- **MIT 라이선스**로 제공되며, 저장소는 스모크 테스트용 `test-nbd.sh`, 전체 파티션 검사용 `test-fill.sh`, 처리량·IOPS·지연 시간 벤치마크 스크립트를 함께 제공함

## 원문
- [원문](https://github.com/c0dejedi/nbd-vram)
- [GeekNews 토론](https://news.hada.io/topic?id=30148)

## My Note
<!-- 한 줄 코멘트 남기기 -->

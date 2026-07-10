---
category: AI
collected_at: '2026-07-10T07:34:58+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31276
id: hada-31276
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- neil.computer
title: Synology, QNAP, TrueNAS 없이 최소 ZFS NAS 구축하기 (2024)
url: https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- GUI가 필요 없는 기본 NAS라면 **ZFS 데이터셋**을 만들고 Samba로 공유하는 조합만으로 충분히 단순한 네트워크 스토리지를 구성할 수 있음
- 예시 환경은 Debian 12 Bookworm, OpenZFS zfs-2.1.1, **RAIDZ1**, ECC RDIMM 16GB RAM, 4×4TB NVMe SSD이며 암호화와 백업 전략은 범위에서 제외됨
- ZFS는 풀과 파일시스템 구성을 디스크에 저장하므로 OS가 망가져도 다른 머신에서 `zfs import`로 데이터를 다시 가져올 수 있음
- 디스크는 `/dev/nvme1` 같은 순서 의존 이름보다 `/dev/disk/by-id` 또는 `/etc/zfs/vdev_id.conf`의 **별칭**으로 지정하는 편이 안전함
- 실제 네트워크 공유는 Samba가 담당하며, 일반 문서 공유와 macOS **Time Machine** 공유를 `docs`, `backups` 데이터셋으로 나눠 구성함

---

## 원문
- [원문](https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/)
- [GeekNews 토론](https://news.hada.io/topic?id=31276)

## My Note
<!-- 한 줄 코멘트 남기기 -->

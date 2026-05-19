---
category: AI
collected_at: '2026-05-19T09:58:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29646
id: hada-29646
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- discuss.haiku-os.org
title: Haiku OS가 이제 M1 Mac에서 실행됨
url: https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Haiku arm64 포트**가 최신 야간 빌드에서 데스크톱까지 부팅되며, hrev59669 이미지는 QEMU에서 동작함
- QEMU 실행에는 **Tianocore EFI**와 CPU 선택의 호환성이 중요하며, Debian에서는 `--cpu cortex-a76` 지정으로 해결됨
- 작은 수정으로 **UTM 부팅**도 가능해졌지만, 마우스 움직임이 느리고 끊겨 실제 사용성은 아직 낮음
- arm64 야간 이미지는 **unbootstrapped** 상태라 `git`, `gcc`, 개발 패키지가 없고, OpenSSL 부재로 패키지 설치도 막힐 수 있음
- 호스트와 게스트 간 파일 전달은 **FAT32 디스크 이미지**로 우회 가능하며, x86\_64나 Linux에서 `.hpkg` 크로스 빌드 가능성이 거론됨

---

## 원문
- [원문](https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2)
- [GeekNews 토론](https://news.hada.io/topic?id=29646)

## My Note
<!-- 한 줄 코멘트 남기기 -->

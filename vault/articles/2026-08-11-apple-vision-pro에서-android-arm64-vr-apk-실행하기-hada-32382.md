---
category: Other
collected_at: '2026-08-11T11:25:28+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32382
id: hada-32382
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/shinyquagsire23
title: Apple Vision Pro에서 Android ARM64 VR APK 실행하기
url: https://github.com/shinyquagsire23/Klepton
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Klepton**은 JIT 없이 Android ARM64 VR APK를 Apple Vision Pro와 macOS에서 실행하는 런타임
- `klepton-ld`가 Android `.so`를 Apple의 `.dylib`·`.framework`로 변환하고, **Bionic·NDK·JNI·OVRP 호환 계층**을 Klepton 런타임에 연결함
- 그래픽은 **GLES 3.2를 ANGLE GLES 3.0**, Vulkan을 MoltenVK로 변환해 Metal 백엔드에서 처리하며, visionOS 기능은 Compositor Services·ARKit 등과 연동함
- macOS가 문맥 전환 시 `x18`을 0으로 만드는 문제를 피하기 위해 `klepton-ld`가 모든 `x18` 사용을 라이브러리별 **TLS 슬롯**으로 패치함
- **Beat Saber**는 macOS와 visionOS에서 사소한 그래픽 문제와 함께 작동하지만, Steam VR Link와 범용성·빌드 도구 개선은 아직 개발 중이며 LuaJIT·V8 기반 앱은 JIT가 필요할 수 있음

---

## 원문
- [원문](https://github.com/shinyquagsire23/Klepton)
- [GeekNews 토론](https://news.hada.io/topic?id=32382)

## My Note
<!-- 한 줄 코멘트 남기기 -->

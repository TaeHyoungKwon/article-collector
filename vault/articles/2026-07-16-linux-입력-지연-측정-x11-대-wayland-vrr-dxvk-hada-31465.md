---
category: Other
collected_at: '2026-07-16T00:36:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31465
id: hada-31465
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- marco-nett.de
title: 'Linux 입력 지연 측정: X11 대 Wayland, VRR, DXVK'
url: https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 500Hz 디스플레이에서 클릭부터 화면 밝기 변화까지 측정한 결과, X11·VRR·dxvk-low-latency를 모두 적용해도 기본 Wayland보다 **종단 간 지연 중앙값**이 0.72ms 낮아지는 데 그침
- 네이티브 Wayland는 X11보다 **0.14~0.22ms** 느린 반면, XWayland는 네이티브 Wayland 대비 최대 **3.13ms**를 추가해 훨씬 큰 차이를 만듦
- **가변 주사율(VRR)** 은 모든 비교에서 지연을 0.26~0.45ms 줄였고, p5~p95 분포 폭도 2.6~3.0ms에서 2.1~2.2ms로 좁힘
- **dxvk-low-latency**는 프레임 제한 시 0.10~0.29ms, 제한 해제 시 0.84ms를 줄였지만, 후자에서는 GPU 사용률을 100% 대신 95~97%로 유지하면서 FPS가 715에서 670으로 감소함
- 결과는 안정적인 FPS와 CPU 병목이라는 **최적 조건** 및 특정 하드웨어·소프트웨어 조합에서 나온 것으로, 실제 플레이에서는 VRR의 지터 감소와 프레임 페이서의 렌더 큐 억제가 중앙값 이상의 차이를 만들 수 있음

---

## 원문
- [원문](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/)
- [GeekNews 토론](https://news.hada.io/topic?id=31465)

## My Note
<!-- 한 줄 코멘트 남기기 -->

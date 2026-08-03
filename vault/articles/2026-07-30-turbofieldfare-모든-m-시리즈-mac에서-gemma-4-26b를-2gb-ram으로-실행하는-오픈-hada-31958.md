---
category: AI
collected_at: '2026-07-30T03:32:03+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31958
id: hada-31958
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-08-03'
source: geeknews
tags:
- AI
- Other
- github.com/drumih
title: TurboFieldfare - 모든 M 시리즈 Mac에서 Gemma 4 26B를 2GB RAM으로 실행하는 오픈소스 엔진
url: https://github.com/drumih/turbo-fieldfare
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **TurboFieldfare**는 전체 14.3GB 모델을 메모리에 올리지 않고 Gemma 4 26B-A4B를 약 2GB의 메모리로 실행해, 8GB Apple Silicon Mac에서도 로컬 추론이 가능함
- 1.35GB 공유 코어와 FP16 KV 캐시만 상주시킨 뒤 토큰마다 필요한 **MoE 전문가 가중치**를 SSD에서 스트리밍하며, 16슬롯 LFU 캐시와 병렬 `pread`로 입출력을 제한함
- Gemma 4 26B-A4B는 토큰당 약 3.88B 파라미터를 활성화하며, 측정된 디코딩 속도는 8GB M2 MacBook Air에서 **5.1~6.3 tok/s**, 24GB M5 Pro에서 31~35 tok/s임
- Swift 6.2와 Metal 4로 구현된 전용 런타임이며, 네이티브 Mac 앱·CLI·설치 도구·실험적 **OpenAI 호환 서버**를 동일한 `.gturbo` 모델 디렉터리 위에서 제공함
- 현재 범위는 macOS 26 이상과 최소 8GB RAM을 갖춘 Apple Silicon Mac의 **텍스트 전용 추론**으로 한정되며, 이미지·음성·영상과 원격 서버 인증·TLS는 지원하지 않음

---

## 원문
- [원문](https://github.com/drumih/turbo-fieldfare)
- [GeekNews 토론](https://news.hada.io/topic?id=31958)

## My Note
<!-- 한 줄 코멘트 남기기 -->

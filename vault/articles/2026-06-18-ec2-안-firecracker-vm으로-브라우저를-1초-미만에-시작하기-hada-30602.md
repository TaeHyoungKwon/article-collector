---
category: Other
collected_at: '2026-06-18T12:49:46+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30602
id: hada-30602
matched_keywords: []
read: false
recommend_score: 1.307
source: geeknews
tags:
- Other
- browser-use.com
title: EC2 안 Firecracker VM으로 브라우저를 1초 미만에 시작하기
url: https://browser-use.com/posts/firecracker-browser-infra
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Browser Use Cloud는 브라우저 세션마다 **개별 Firecracker VM**을 쓰면서 새 세션 시작 시간을 1초 미만으로 낮추고 비용을 브라우저 시간당 $0.06에서 **$0.02**로 줄임
- 이전 Unikraft 구조는 유휴 비용에는 유리했지만, 트래픽 급증 때 사람이 용량을 조정해야 해 부하 테스트 중 프로덕션이 **45분간 중단**됨
- 새 구조는 자체 **control plane**이 브라우저 플릿을 실시간으로 감시해 EC2 호스트 배치, 확장, 드레이닝을 CloudWatch보다 더 세밀하게 결정함
- 정규 EC2 위에서 Firecracker를 실행하는 **중첩 가상화**를 택한 대신, 2MB 메모리 페이지, `userfaultfd`, vCPU 고정, real-time priority, headless Chromium 패치로 병목을 줄임
- VM cold start는 400ms 미만이고, 10,000세션 스트레스 테스트에서 공개 API 기준 브라우저 생성 지연은 p50 825ms, p99 1.35초였으며 모든 브라우저가 성공적으로 시작됨

---

## 원문
- [원문](https://browser-use.com/posts/firecracker-browser-infra)
- [GeekNews 토론](https://news.hada.io/topic?id=30602)

## My Note
<!-- 한 줄 코멘트 남기기 -->

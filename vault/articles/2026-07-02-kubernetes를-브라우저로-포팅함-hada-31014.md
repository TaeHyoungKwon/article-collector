---
category: AI
collected_at: '2026-07-02T02:40:59+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31014
id: hada-31014
matched_keywords:
- LLM
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- ngrok.com
title: Kubernetes를 브라우저로 포팅함
url: https://ngrok.com/blog/i-ported-kubernetes-to-the-browser
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **webernetes**는 Kubernetes 일부를 TypeScript로 옮겨 브라우저 안에서 클러스터를 실행하게 만든 프로젝트로, 2개월 동안 552개 커밋·629개 파일·거의 10만 줄 규모로 만들어짐
- WebAssembly로 Kubernetes를 그대로 컴파일한 방식이 아니라, **kubelet 일부**, 여러 컨트롤러, 브라우저 기반 CNI와 컨테이너 런타임, 클러스터 조작 API를 새로 구현함
- 실제 이미지 레지스트리에서 이미지를 가져오지 않고 TypeScript API로 이미지를 정의하며, 목표는 프로덕션 배포판이 아니라 **인터랙티브 Kubernetes 콘텐츠** 제작임
- 코드 대부분은 LLM이 작성했지만 모든 줄을 사람이 리뷰했고, k3s와 같은 테스트를 실행하는 **204개 통합 테스트**와 Kubernetes Go 코드베이스에서 포팅한 1,855개 단위 테스트로 검증함
- LLM은 포팅 중 축약, 임의 헬퍼 생성, 테스트 누락을 반복했으며, 빠른 코드 생성의 이점을 얻으려면 **리뷰와 테스트**를 함께 적용해야 함

---

## 원문
- [원문](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser)
- [GeekNews 토론](https://news.hada.io/topic?id=31014)

## My Note
<!-- 한 줄 코멘트 남기기 -->

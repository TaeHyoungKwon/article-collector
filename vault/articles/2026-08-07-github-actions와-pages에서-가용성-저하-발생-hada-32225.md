---
category: Other
collected_at: '2026-08-07T09:39:43+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32225
id: hada-32225
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- githubstatus.com
title: GitHub Actions와 Pages에서 가용성 저하 발생
url: https://www.githubstatus.com/incidents/qcvjkzcs7j74
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 2026년 8월 6일 GitHub Actions에서 시작된 장애가 **Pages·Copilot·GitHub Enterprise Importer** 등으로 확산됐으며, 이튿날 완화 조치 후 안정성 모니터링 단계로 전환됨
- 워크플로가 시작되지 않거나 실행 중 실패했고, **Actions REST API 오류**와 예상치 못한 속도 제한, 웹훅 지연, 작업 대기가 함께 발생함
- 복구 과정에서 웹훅 처리량은 약 **15%**, 대기 작업 성공률은 한때 30~40%까지 떨어졌으며, 러너가 사라진 작업을 반복해서 할당받는 문제로 원인이 좁혀짐
- GitHub-hosted와 self-hosted runner가 모두 영향을 받았지만, 수정 배포 후 실행 중인 워크플로 성공률이 **97%에서 99%로 상승**하고 시스템 전체 대기열도 소진됨
- 웹훅 기반 Actions와 Pages, Copilot은 처리량을 회복했으나 **GitHub Enterprise Importer 마이그레이션**은 예방 차원에서 계속 중단됨

---

## 원문
- [원문](https://www.githubstatus.com/incidents/qcvjkzcs7j74)
- [GeekNews 토론](https://news.hada.io/topic?id=32225)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-07-27T09:35:02+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31846
id: hada-31846
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- slack.engineering
title: 'Shipyard: Slack의 차세대 EC2 플랫폼 구축기'
url: https://slack.engineering/shipyard-how-we-built-slacks-next-generation-ec2-platform/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Slack은 장기 실행 EC2를 계속 수정하던 기존 방식에서 **불변 AMI 기반 교체 배포**로 전환해, 컨테이너로 옮기기 어려운 워크로드에도 현대적인 배포 방식을 적용함
- 공통 기반 이미지인 **slack-zero** 위에 서비스별 이미지를 쌓고, 무거운 구성은 이미지 베이킹에서 처리하며 환경별 비밀정보와 메타데이터만 부팅 시 적용함
- 배포 오케스트레이터 **Gondola**는 AMI와 버전이 지정된 Chef 아티팩트를 하나의 배포 단위로 관리하고, 지표 기반 단계적 배포·중단·자동 롤백을 수행함
- **Peekaboo**는 전체 EC2 인벤토리를 거의 실시간으로 제공하고, **The Reaper**는 오염되거나 수명이 지난 인스턴스를 속도 제한과 일시정지 장치 아래 교체함
- 단기 실행 서비스에는 효과적이지만 데이터 노드, GitHub Enterprise, Atlassian JIRA처럼 빠르게 교체할 수 없는 **장기 실행 인스턴스**에는 별도의 패치 방식과 배포 실행기가 필요함

---

## 원문
- [원문](https://slack.engineering/shipyard-how-we-built-slacks-next-generation-ec2-platform/)
- [GeekNews 토론](https://news.hada.io/topic?id=31846)

## My Note
<!-- 한 줄 코멘트 남기기 -->

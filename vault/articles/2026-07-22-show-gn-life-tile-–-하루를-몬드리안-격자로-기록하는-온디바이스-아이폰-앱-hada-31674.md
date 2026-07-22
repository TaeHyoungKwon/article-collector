---
category: Dev Tools
collected_at: '2026-07-22T09:01:56+09:00'
geeknews_comments: 1
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=31674
id: hada-31674
matched_keywords:
- Claude Code
read: false
recommend_score: 3.817
source: geeknews
tags:
- Dev Tools
- Other
- apps.apple.com
title: 'Show GN: Life Tile – 하루를 몬드리안 격자로 기록하는 온디바이스 아이폰 앱'
url: https://apps.apple.com/app/life-tile/id6767332648
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
프론트엔드 개발자. 이전에 Claude Code로 웹 앱은 만들어 봤지만 네이티브 앱은 처음.  
올 4월부터 약 3개월간 개발 후 출시. 아이폰용으로 만들어진 시간·위치 기록 앱

왜 만들었나

- 오래 쓰던 Life Cycle이 업데이트가 멈춘 지 오래됨
- Reddit을 보니 대안을 찾는 사람이 꽤 있었고, 직접 더 나은 걸 만들어보기로 함

가장 어려웠던 것: iOS 백그라운드 위치 추적

- 여행지, 공항, 대형 쇼핑몰, 장소 밀집 지역에서는 감지가 흔들림
- 짧은 방문은 누락, 인접한 장소는 하나로 병합되기도 함
- 결국 iOS 위치 추적 정확도만으로는 "완전 자동"이 불가능하다는 결론
- 방향 전환: 완벽한 자동화 대신, 잘못 잡힌 기록을 사용자가 쉽게 고칠 수 있게 설계.

온디바이스로 만든 건 오히려 편했다

- 모든 데이터를 기기에만 저장(SwiftData), 서버 없음. 프라이버시 때문에 선택한 구조
- 부수 효과로 백엔드가 없으니 개발이 훨씬 단순. 서버 운영 비용·인증·동기화 서버 모두 불필요.
- iCloud 동기화는 사용자 본인 기기 간에만 선택적으로 동작
- 사용패턴 분석을 위해서 TelemetryDeck으로 익명 데이터 수집.

Claude Code 활용

- 특별한 에이전트 하네스 없이 기본 기능만 사용. 주로 Opus로 작업
- 상세 로그를 분석하는 skill을 추가해 위치 추적 디버깅에 활용
- 앱스토어 홍보 스크린샷은 Claude Design으로 생성
- 경쟁 앱 조사, 앱스토어 등록, 출시 후 홍보 전략 등 개발 외에도 도움을 많이 받음.

비용 공개

- 정기: 도메인(Route 53) 연 $15, Apple Developer Program 연 $99
- 한시적: Claude Code Max ×5, 개발 집중한 4~5월 2개월간 $220 (이후 Pro로 전환), Arc Timeline 4 구독(경쟁 앱 리서치용) 월 ₩6,600
- 수익 모델은 구독 없는 일시불. 일주일 무료 사용 제공.

남은 생각

- 네이티브 앱 특유의 제약(백그라운드 정책, 권한, 배터리)은 웹과 또 달라서, 그 부분을 이해하고 기획하는 게 핵심이었음
- Claude Code가 구현을 대신해 줘도, 어떤 예외 케이스를 어떻게 다룰지 정의하는 건 결국 사람의 몫
- 각 커뮤니티가 신규 계정의 홍보성 글을 막아두고 있어서, 출시 직전에 계정만 만들면 늦음. 미리 가입하고 커뮤니티에 참여해두는 준비가 필요
  - Product Hunt: [위상을 많이 잃었지만](https://news.hada.io/topic?id=23331) 검색 결과에 노출되므로 등록
  - Show HN: 신규 유저 급증으로 현재 일시 제한 중
  - Reddit: 서브레딧마다 정책이 다름. r/iOSApps는 로컬 카르마 10 이상부터 글 작성 가능
  - GeekNews: 가입 후 일주일이 지나야 뉴스 링크 등록 가능

## 원문
- [원문](https://apps.apple.com/app/life-tile/id6767332648)
- [GeekNews 토론](https://news.hada.io/topic?id=31674)

## My Note
<!-- 한 줄 코멘트 남기기 -->

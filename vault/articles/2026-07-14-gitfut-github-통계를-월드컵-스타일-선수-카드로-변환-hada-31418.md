---
category: AI
collected_at: '2026-07-14T09:31:01+09:00'
geeknews_comments: 2
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31418
id: hada-31418
matched_keywords:
- AI
read: false
recommend_score: 3.023
recommended_on: '2026-07-17'
source: geeknews
tags:
- AI
- Other
- github.com/Younesfdj
title: GitFut - GitHub 통계를 월드컵 스타일 선수 카드로 변환
url: https://github.com/Younesfdj/gitfut
---

## TL;DR
- GitFut는 GitHub 프로필의 활동을 분석해 축구 선수 카드 형식으로 시각화하는 서비스이다.
- GitHub 활동에 기반한 축구 능력치를 6가지 신호로 변환하여 선수 카드를 생성하며, 이는 실시간으로 업데이트된다.
- 개발자들은 자신의 GitHub 통계를 카드 형태로 공유할 수 있어, 포트폴리오와 README를 통해 시각적으로 매력적인 정보를 제공할 수 있다.

## GeekNews 요약
- GitHub 프로필의 활동을 분석해 **99점 만점**짜리 축구 선수 카드를 생성해줌
- GitHub 에서 여섯 가지 신호를 읽어 축구 능력치로 변환하고 6단계의 등급으로 각각의 디자인 적용
  - **PAC / Pace**: 최근 1년 커밋 수
  - **SHO / Shooting**: 저장소가 받은 전체 Star 수
  - **PAS / Passing**: Pull Request와 팔로워 수
  - **DRI / Dribbling**: 사용 언어 다양성
  - **DEF / Defending**: 코드 리뷰와 이슈 활동
  - **PHY / Physical**: 전체 기간의 기여 활동
- 등급은 **Bronze / Silver / Gold / In-Form / TOTY / Icon**
  - 일반 통계만으로 얻을 수 있는 종합 점수는 **최대 88점**으로 제한
  - 90점대는 오랜 활동 기간과 영향력을 요구하므로, 한 해 동안 활동량이 높았다는 이유만으로 Icon이 되지는 않음
- 능력치 분포를 분석해 **포지션과 플레이 유형**도 자동으로 결정
  - Shooting이 두드러지면 득점형 공격수
  - Defending과 Passing이 높으면 후방 플레이메이커로 분류
- 생성된 카드는 GitHub 통계가 바뀌면 다시 평가되는 **실시간 이미지 URL**로 제공됨
  - `gitfut.com/<username>.png`: README나 포트폴리오에 삽입할 카드 이미지
  - `gitfut.com/<username>`: 전체 스카우팅 보고서
  - `?country=XX`: 카드의 국가 국기 직접 지정
- GitHub 프로필 README에는 다음과 같이 삽입 가능  
  `[![My GitFut card](https://gitfut.com/YOUR_USERNAME.png)](https://gitfut.com/YOUR_USERNAME)`
- Next.js / TypeScript / Tailwind / Redis로 구현
- MIT 라이선스

## 원문
- [원문](https://github.com/Younesfdj/gitfut)
- [GeekNews 토론](https://news.hada.io/topic?id=31418)

## My Note
<!-- 한 줄 코멘트 남기기 -->

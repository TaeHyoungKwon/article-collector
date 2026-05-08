---
collected_at: '2026-05-08T07:33:21+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29273
id: hada-29273
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- openrss.org
title: YouTube, 당신의 RSS 피드가 고장났습니다
url: https://openrss.org/blog/youtube-your-feeds-are-broken
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **YouTube 채널 RSS 피드**는 피드 리더에서 사용할 수 있지만, 일부 사용자에게는 예고 없이 조용해지거나 사라졌고 공지·오류 메시지·설명도 없었음
- YouTube 채널 페이지에는 피드 리더 구독 링크나 **add feed** 버튼이 보이지 않아, 사용자가 `channel/UC4a-GbYw7vOacCHmFo40b9g` 같은 식별자로 직접 피드를 구성해야 함
- YouTube가 짧은 영상 기능을 확장하면서 원하지 않는 **Shorts**가 RSS 피드에 섞이고, 긴 형식 영상을 팔로우하려는 피드 리더 사용 목적과 맞지 않음
- 대형 플랫폼들은 시간이 지나며 피드를 덜 보이게 만들고 사용하기 어렵게 만들며, RSS는 플랫폼의 **알고리듬** 없이 사용자가 보는 콘텐츠와 시점을 통제하게 해줌
- RSS는 Google의 피드 리더 종료와 소셜 미디어 타임라인 확산 이후에도 유지됐고, YouTube 피드가 제대로 작동하지 않으면 **Open RSS**가 YouTube용 피드를 대신 제공하려는 시도를 계속할 수밖에 없음

---

## YouTube 피드의 신뢰성과 접근성 문제

- YouTube 채널별 피드는 피드 리더에서 사용할 수 있지만, 일부 사용자에게는 예고 없이 조용해지거나 완전히 사라지는 문제가 [발생](https://www.reddit.com/r/rss/comments/1aduw8j/did_youtube_killed_its_rss_feature_or_is_there_an/)해 왔음
- 피드가 없어졌다는 [사례](https://reddit.com/r/rss/comments/1rgvzbj/did_youtube_remove_their_rss_feeds/)에는 공지, 오류 메시지, 설명이 없는 상태가 포함됨
- 일부 장애는 너무 오래 지속돼 YouTube가 RSS 기능을 [중단한 것 아니냐](https://sh.itjust.works/post/56041755)는 의심으로 이어짐
- 버그일 가능성이 크지만, YouTube 규모의 플랫폼에서 이런 문제가 방치되면 단순한 실수보다 **우선순위에서 밀린 선택**처럼 보임

## 피드 링크가 드러나지 않는 구조

- YouTube 채널 페이지에는 피드 리더로 구독할 수 있는 링크나 **add feed** 버튼이 제공되지 않음
- 사용자는 `channel/UC4a-GbYw7vOacCHmFo40b9g` 같은 채널 식별자 형태에서 직접 피드를 구성해야 함
- 이런 식별자는 기억하기 어렵고 사람을 위한 설계로 보이지 않음
- 초기 웹에서는 피드가 중요한 기능으로 취급됐고, 사이트 상단에 피드 링크가 눈에 띄게 표시되던 관행과 대비됨
- YouTube는 한 번의 클릭으로 피드 리더 구독을 가능하게 할 인프라와 기회가 있지만, 이를 표면화하지 않음

## Shorts가 RSS 피드에 섞이는 문제

- YouTube가 TikTok과 유사한 짧은 영상 중심 기능을 확장하는 과정에서, 원하지 않는 사용자 피드에도 **Shorts**가 나타남
- 피드 리더 구독은 의도적인 선택이므로, 특정 채널의 긴 형식·고품질 영상 콘텐츠를 팔로우하려는 경우 해당 콘텐츠만 기대하게 됨
- Shorts는 무한 스크롤을 위한 충동적 콘텐츠로 여겨지며, 피드 리더의 사용 목적과 맞지 않음
- 긴 영상과 Shorts를 같은 피드에 섞는 방식은 단순한 불편을 넘어, 피드가 무엇을 위해 존재하는지에 대한 근본적 오해로 이어짐
- YouTube가 Shorts 전략을 추진하더라도, 모든 사용자가 그 흐름에 끌려갈 필요는 없음

## 더 큰 웹 플랫폼 흐름

- YouTube만의 문제가 아니라, 대형 플랫폼들이 시간이 지나며 피드를 덜 보이게 만들고 사용하기 어렵게 만드는 더 넓은 흐름의 일부로 다뤄짐
- 피드 리더에서 쓸 수 있는 피드는 로그인하거나 플랫폼을 계속 확인하지 않아도 좋아하는 콘텐츠를 따라갈 수 있게 함
- 피드는 사용자가 보는 것과 시점을 플랫폼이 정하는 **알고리듬**을 제거하고, 사용자에게 통제권을 돌려줌
- 이런 구조는 참여 지표와 광고 수익을 중시하는 플랫폼에는 불리하게 작용할 수 있음
- YouTube는 여전히 피드 리더에서 사용할 수 있는 피드를 제공하는 몇 안 되는 플랫폼 중 하나로 평가되지만, 존재를 잊게 만들려는 듯한 태도도 함께 드러남

## RSS의 지속성과 Open RSS의 대응

- 피드 리더에서 사용하는 기술은 이를 무의미하게 만들려던 여러 플랫폼보다 오래 살아남았음
- RSS는 Google이 자체 피드 리더를 종료하면서 관련 기술 채택을 약화시켰다는 [비판](https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds) 이후에도 살아남음
- 소셜 미디어 타임라인의 확산과 팟캐스트 업계의 폐쇄적 생태계 시도 속에서도 RSS는 계속 유지됨
- YouTube가 피드를 제공한다면 실제로 작동하게 만들어야 하며, 그렇지 않다면 Open RSS가 YouTube용 피드를 [대신 제공하려는 시도](https://openrss.org/feeds/youtube)를 계속할 수밖에 없음

## 원문
- [원문](https://openrss.org/blog/youtube-your-feeds-are-broken)
- [GeekNews 토론](https://news.hada.io/topic?id=29273)

## My Note
<!-- 한 줄 코멘트 남기기 -->

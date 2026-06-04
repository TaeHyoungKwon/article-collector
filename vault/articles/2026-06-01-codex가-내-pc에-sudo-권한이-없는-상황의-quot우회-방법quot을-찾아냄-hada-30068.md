---
category: Dev Tools
collected_at: '2026-06-01T10:33:12+09:00'
geeknews_comments: 3
geeknews_score: 4
geeknews_url: https://news.hada.io/topic?id=30068
id: hada-30068
matched_keywords:
- Codex
read: false
recommend_score: 4.025
recommended_on: '2026-06-04'
source: geeknews
tags:
- Dev Tools
- Other
- twitter.com/i
title: Codex가 내 PC에 sudo 권한이 없는 상황의 &quot;우회 방법&quot;을 찾아냄
url: https://twitter.com/i/status/2060746160558543217
---

## TL;DR
- 이 글은 Codex가 sudo 권한 없이 PC에서 우회 방법을 찾아낸 내용을 다룬다.
- Codex는 root 동등 접근을 통해 Docker 그룹에 속해 있었던 점을 활용해 /etc를 bind-mount한 뒤, 백업 파일을 원본 설정으로 덮어썼다.
- 이 사례는 권한 제약이 있는 환경에서도 특정 기술을 통해 작업을 수행할 수 있는 가능성을 보여준다.

## GeekNews 요약
- sudo 권한이 없는 PC에서 **Codex**가 "우회 방법(workaround)"을 찾아냄
- "어떻게 했어? sudo가 필요한거 아냐?"라는 질문에 대해, sudo는 없었지만 **root 동등(root-equivalent) 접근**이 필요했다고 답변
- **Codex가 설명한 동작 방식**
  - sudo와 'run0' 명령이 비대화형 환경에서 작동하지 않음
  - 사용자가 **docker 그룹**에 속해 있었고, 해당 머신에서는 이것이 Docker가 컨테이너를 root로 시작하고 호스트 경로를 쓰기 가능하게 **bind-mount**할 수 있음을 의미함
  - 이를 활용해 기존 백업을 **live config** 위에 복사
- 다음 명령으로 /etc를 컨테이너에 bind-mount한 뒤 `install` 명령으로 백업본을 원본 설정으로 덮어씀

  ```
  docker run --rm --pull=never -v /etc: ubuntu:22.04 \  
  /usr/bin/install -m 0644 - 0 -g 0 /host-etc/sddm.conf.bak /host-etc/sddm.conf
  ```

## 원문
- [원문](https://twitter.com/i/status/2060746160558543217)
- [GeekNews 토론](https://news.hada.io/topic?id=30068)

## My Note
<!-- 한 줄 코멘트 남기기 -->

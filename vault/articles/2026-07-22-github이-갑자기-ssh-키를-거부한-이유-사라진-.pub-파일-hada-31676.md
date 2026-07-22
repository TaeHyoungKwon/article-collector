---
category: Other
collected_at: '2026-07-22T09:06:53+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31676
id: hada-31676
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- thorsell.io
title: 'GitHub이 갑자기 SSH 키를 거부한 이유: 사라진 .pub 파일'
url: https://thorsell.io/2026/07/21/github-ssh-keys.html
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 변경하지 않은 노트북에서 GitHub의 `git pull`이 갑자기 실패했지만, 개인 키에 대응하는 **`.pub` 파일을 생성**하자 다시 인증됨
- `.pub` 파일이 있으면 OpenSSH는 공개 키를 먼저 제시해 승인을 받은 뒤 서명하고, 없으면 **서명된 인증 요청을 즉시 전송**함
- 두 흐름 모두 **RFC 4252**에 부합하고 일반적인 `sshd`도 허용하지만, 당시 GitHub SSH 프런트엔드는 직접 서명된 요청을 받아들이지 않는 것으로 보였음
- 12차례 통제 시험에서 `.pub` 파일이 없던 6회는 모두 거부됐고, 파일이 있던 6회는 모두 성공함
- 서버 배너 변화로 **서버 측 소프트웨어 변경 가능성**을 추정할 수 있지만, 정확한 원인은 확인되지 않아 대응 공개 키 파일을 함께 유지하는 것이 안전함

---

## 원문
- [원문](https://thorsell.io/2026/07/21/github-ssh-keys.html)
- [GeekNews 토론](https://news.hada.io/topic?id=31676)

## My Note
<!-- 한 줄 코멘트 남기기 -->

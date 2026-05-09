---
category: AI
collected_at: '2026-05-08T09:08:18+09:00'
geeknews_comments: 2
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29275
id: hada-29275
matched_keywords:
- AI
- RAG
read: false
recommend_score: -994.572
recommended_on: '2026-05-08'
source: geeknews
tags:
- AI
- openwall.com
title: 'Dirty Frag: 범용 Linux LPE(로컬 권한 상승) 취약점'
url: https://www.openwall.com/lists/oss-security/2026/05/07/8
---
********
## TL;DR
- 이 글은 **Dirty Frag**라는 범용 Linux 로컬 권한 상승 취약점에 대해 설명한다.
- 이 취약점은 **결정론적 로직 버그**로 인해 높은 성공률을 가지며, 패치가 아직 제공되지 않는다.
- 독자는 주요 Linux 배포판의 취약점을 인식하고 임시 완화책을 적용해야 할 필요성을 알게 된다.

## GeekNews 요약
- **Dirty Frag**는 **주요 Linux 배포판 전반에서 root 권한 획득을 가능하게 하는 범용 로컬 권한 상승 취약점**으로, 책임 있는 공개 일정과 엠바고가 깨져 **패치와 CVE가 아직 없음**
- Dirty Pipe, Copy Fail과 같은 버그 클래스의 확장으로, **결정론적 로직 버그**이기 때문에 레이스 컨디션이 불필요하고 성공률이 매우 높음
- 취약점의 유효 수명은 약 **9년**이며, Ubuntu, RHEL, Fedora, openSUSE 등 주요 배포판에서 테스트 완료
- 기존 Copy Fail 완화 조치(algif\_aead 블랙리스트)를 적용한 시스템에서도 여전히 **Dirty Frag에 취약**함
- 임시 완화책으로 배포판 패치가 나오기 전까지 취약점이 발생하는 **esp4**, **esp6**, **rxrpc** 모듈 제거 권고

---

## 원문
- [원문](https://www.openwall.com/lists/oss-security/2026/05/07/8)
- [GeekNews 토론](https://news.hada.io/topic?id=29275)

## My Note
<!-- 한 줄 코멘트 남기기 -->

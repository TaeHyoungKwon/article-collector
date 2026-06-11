---
category: AI
collected_at: '2026-06-10T21:46:16+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30360
id: hada-30360
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.307
recommended_on: '2026-06-10'
source: geeknews
tags:
- AI
- Other
- slopguard.app
title: 'Show GN: SlopGuard – AI 슬롭 PR/이슈를 점수 매겨 격리하는 GitHub 앱 (자동으로 안 닫음)'
url: https://slopguard.app
---

## TL;DR
- SlopGuard는 GitHub에서 AI가 생성한 저품질 PR/이슈를 점수화하여 격리하는 앱이다.
- 이 앱은 PR과 이슈에 대해 0~100점으로 평가하고, 메인테이너가 직접 결정을 내리도록 설계되어 있다.
- 오픈소스 메인테이너들은 저품질 기여자와의 소통을 유지하면서 효율성을 높일 수 있는 유용한 도구를 확보하게 된다.

## GeekNews 요약
오픈소스 메인테이너들이 AI가 생성한 저품질 PR/이슈에 시달리는 게 요즘 흔한 문제입니다. 처음 30초는 그럴듯해 보여서 안 볼 수도 없고, 일일이 거르다 보면 시간이 갈려나갑니다. 그렇다고 패턴만 보고 막 닫으면 진짜 첫 기여자를 내칠 위험이 있고요.

SlopGuard는 GitHub 앱입니다. 한 번 클릭으로 설치(Action YAML 불필요)하면 들어오는 PR과 이슈를 0~100점으로 점수화하고, 출처 특징을 태깅한 뒤 임계값을 넘으면 slop-quarantine 라벨과 근거 코멘트를 답니다. 절대 자동으로 닫지 않습니다. 격리 해제/거부 같은 결정은 메인테이너가 /slop approve, /slop reject 코멘트로 직접 합니다.

무료(호스팅) 티어는 휴리스틱 전용입니다. LLM 키가 필요 없고, 공개한 평가셋에서 정밀도 100%, 재현율 92%가 나옵니다(평가셋이 작다는 점은 솔직히 밝힙니다, 방법론은 레포에 공개). 유료 티어는 LLM 판정을 더해 미묘한 케이스까지 잡습니다.

소스 공개(MIT + Commons Clause)라 직접 읽고 자기 용도로 셀프호스팅할 수 있습니다.

소스: <https://github.com/Blue-B/slopguard>

## 원문
- [원문](https://slopguard.app)
- [GeekNews 토론](https://news.hada.io/topic?id=30360)

## My Note
<!-- 한 줄 코멘트 남기기 -->

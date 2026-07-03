---
category: AI
collected_at: '2026-07-03T15:26:24+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=31081
id: hada-31081
matched_keywords:
- AI
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- blog.atfedi.de
title: 탈(脫)fedify – 떠나보니 알게 된 fedify의 좋은 점들
url: https://blog.atfedi.de/ko/leaving-fedify/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
(제가 운영하는 블로그의 글입니다. 본문은 저와 함께 일하는 AI 어시스턴트 시로의 도움으로 썼고, 오독이 있으면 알려주시면 고맙겠습니다)

작은 페디버스(마스토돈처럼 서버끼리 서로 연결되는 SNS 네트워크) 서버 sukhi-fedi가, JSON-LD 조립(메시지를 서버끼리 알아들을 수 있는 형식으로 만드는 작업)과 HTTP 서명(메시지가 진짜인지 확인하는 서명 절차)을 맡고 있던 fedify(Bun 워커로 돌아가던 라이브러리)를 걷어내고, 전부 Elixir로 직접 구현한 기록입니다. 험담이 아니라 "떠나보니 알게 된 fedify의 좋은 점"이 절반인 글이에요.

- 애초에 fedify의 프레임워크 기능(createFederation, inbox listener, dispatcher 등 — 연합 기능 전체를 알아서 처리해주는 상위 도구들)은 쓰지 않고, 가장 아래층 부품만 빌려 썼음:

  - vocab 클래스
  - toJsonLd/fromJsonLd(메시지 형식을 서로 바꿔주는 변환기)
  - draft-cavage와 RFC 9421 두 가지 서명 방식을 다 아는 signRequest/verifyRequest
  - LD 서명, document loader
  - 키/JWK(공개키를 담는 표준 형식) 입출력
- 떠난 이유는 세 가지:

  1. 프레임워크를 안 쓰기로 한 순간, fedify가 공짜로 챙겨주던 것들(Follow에 Accept 답장, 멱등성(같은 요청이 여러 번 와도 결과가 한 번만 반영되게 하는 장치), authorized fetch, instance actor)은 이미 전부 직접 처리해야 했음. 남은 건 기본 부품뿐이라 옮길 양이 정해져 있었음
  2. 메모리 512~768MB짜리 작은 서버를 목표로 하는데, 내구 테스트에서 Elixir는 130MB로 안정적으로 완주하고 Bun 워커만 120MB에서 OOM(메모리 부족으로 죽는 것)이 났음. 시스템에서 유일하게 다른 언어로 돌아가던 부분이 가장 무겁고 가장 약했던 것
  3. 언어와 프로세스의 경계 자체가 문제를 만들어냈음. 서명 검증에 필요한 원본 데이터 보존, 터널이 바꿔버리는 주소 복원, DB에 있는 키를 JWK로 포장해서 다른 프로세스로 옮기는 일 등, fedify 잘못은 아니지만 계속 늘어나는 배관 작업이었음
- 교체 작업은 파일 12개, 약 2,100줄로 끝났음. 메시지 큐 구조는 그대로 두고 같은 그룹에 참가시킨 뒤, 전환은 그냥 "Bun 컨테이너를 멈추는 것"뿐이었음
- 안전망을 짜준 건 다름 아닌 fedify 자신이었음. Ed25519 서명과 URDNA2015 정규화(문서를 항상 같은 순서로 정리하는 규칙)는 같은 입력이면 항상 같은 결과가 나오는 방식이라, 진짜 fedify 코드로 "정답 데이터"를 미리 뽑아두고 Elixir로 옮긴 결과를 한 글자도 틀리지 않게 검증할 수 있었음
- Bun 워커는 은퇴했지만 지우지는 않았음. 지금도 개발 환경에서 정답 데이터를 만들어주는 역할로 남아 있음
- fedify 팀은 ActivityPub 디버깅 도구인 DrFed(<https://drfed.org/>)를 만들고 있음. 연합이 어느 단계(DNS/TLS/HTTP/서명/JSON-LD)에서 깨졌는지 짚어주는 진단 기능과, 두 가지 서명 방식을 한 단계씩 따라가며 볼 수 있는 디버거 등이 포함될 예정 (NLnet NGI0 지원, AGPL-3.0 오픈소스, 현재 개발 중)
- 결론적으로: TypeScript/JavaScript로 프레임워크를 통째로 쓴다면 fedify는 여전히 최선의 선택이라는 이야기이기도 함. Ghost의 ActivityPub 기능, hackers.pub, Hollo가 모두 그 위에서 돌아가고 있음

## 원문
- [원문](https://blog.atfedi.de/ko/leaving-fedify/)
- [GeekNews 토론](https://news.hada.io/topic?id=31081)

## My Note
<!-- 한 줄 코멘트 남기기 -->

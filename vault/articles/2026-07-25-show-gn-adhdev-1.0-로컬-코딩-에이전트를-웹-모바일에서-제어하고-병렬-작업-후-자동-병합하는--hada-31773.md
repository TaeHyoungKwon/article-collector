---
category: AI
collected_at: '2026-07-25T00:43:04+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31773
id: hada-31773
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 6.693
source: geeknews
tags:
- AI
- Other
- adhf.dev
title: 'Show GN: ADHDev 1.0 - 로컬 코딩 에이전트를 웹/모바일에서 제어하고 병렬 작업 후 자동 병합하는 도구'
url: https://adhf.dev
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요, ADHDev 만든 개발자입니다. 스탠드얼론 에디션은 AGPL로 공개했고, 클라우드 버전으로 운영비를 벌 생각입니다.

Claude Code, Codex 같은 터미널 에이전트를 머신 두세 대에서 돌리다 보니 두 가지가 계속 발목을 잡았습니다. 어느 세션이 끝났는지, 멈췄는지, 승인을 기다리는지 터미널을 왔다갔다 하며 확인하는 것. 그리고 여러 개가 동시에 끝났을 때의 머지 지옥이요.

그래서 이미 쓰고 있는 에이전트들에 붙는 데몬과 웹 대시보드를 만들었습니다. 브라우저에서 태스크를 큐에 넣으면 격리된 git 워크트리로 분배되고(머신이 여러 대면 머신 간에도), 작업이 끝나면 Refinery라고 부르는 파이프라인이 저장소의 자체 검증(빌드/테스트/린트)을 돌리고 패치 동등성을 확인한 뒤 main에 fast-forward로 병합하고 워크트리까지 정리합니다. force-push는 절대 안 하고, 애매하면 병합하지 않고 저한테 되돌립니다.

디테일 몇 가지. 승인 요청은 폰 푸시로 와서 원탭으로 처리합니다. 실제로 핫스팟 켜고 노트북은 가방에 넣은 채 폰으로만 승인하고 지시하면서 돌아다닌 적이 많은데, WebRTC P2P에 TURN 폴백이라 포트포워딩이나 VPN 설정이 아예 없습니다. 스크린샷을 채팅에 붙여넣으면 다른 머신 터미널 에이전트의 컨텍스트로 그대로 들어갑니다. MAGI라는 교차검증 모드도 있습니다. 같은 읽기 전용 질문을 다른 머신·모델 리플리카들에 보내고 어디서 의견이 갈리는지 보여주는 건데, 같은 머신에서 나온 합의는 두 번 세지 않고 할인합니다.

채팅·명령·스크린샷은 브라우저와 데몬이 직접 주고받고, 서버는 인증·시그널링과 경량 세션 상태만 다룹니다. 코드는 서버를 안 거칩니다.

이 프로젝트 자체를 이걸로 개발하고 있습니다. 최근 7개 태스크짜리 프로토콜 마이그레이션을 맥과 윈도우 워커가 나눠서 작성했고 전부 Refinery로 병합됐습니다.

한계도 적자면, 단일 머신 도구보다는 셋업이 무겁습니다. 그리고 머지는 의도적으로 순수 git ff-only입니다. 애매한 상황에서 똑똑한 척 하지 않고 멈춰서 물어보는 쪽을 택했습니다.

GitHub: <https://github.com/vilmire/adhdev> / 문서: <https://docs.adhf.dev>

## 원문
- [원문](https://adhf.dev)
- [GeekNews 토론](https://news.hada.io/topic?id=31773)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-18T01:46:32+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30581
id: hada-30581
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- drive-game.pages.dev
title: 'Show GN: Nürburgring Drive - Fable 5로 만든 웹 기반 드라이빙 게임'
url: https://drive-game.pages.dev
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
웹브라우저에서 바로 할 수 있는 뉘르부르크링 1인칭 드라이빙 게임을 만들었습니다. 설치 없이 바로 운전할 수 있습니다.  
모바일에서는 가로 모드로 하면 전체화면으로 플레이 가능합니다

url: <https://drive-game.pages.dev>  
GitHub: <https://github.com/esc5221/drive-game>

slowroads.io 같은 게임을 좋아하는데, 좀 더 실제 서킷이랑 진짜 차에 맞춘, 레이싱 dna가 있는 버전이 있으면 좋겠다 싶어서 만들었습니다. 아케이드보다는 심 쪽을 지향해서 생각보다 어려울 수 있는데, 키보드로 레이싱 게임 해보신 분들은 할만하실겁니다.

작동하는 버전의 코드는 Claude Fable 5가 다 짰고, 이후 기능 수정 / 튜닝이랑 감 잡는 부분만 손봤습니다. 한 줄 프롬프트로 게임 뚝딱 만드는 게 유행인데, 물리나 사운드처럼 손이 많이 가는 부분을 AI로 어디까지 파볼 수 있나 궁금해서 거기에 집중했습니다.

만들면서 통한 방식은 "그럴듯하게"가 아니라 측정 가능한 목표와 검증 방법을 같이 준 거였습니다.

- 물리: 차마다 실제 제로백·최고속도를 주고 방정식으로 역산하게 한 뒤, 헤드리스 테스트로 측정하면서 수치가 맞을 때까지 반복
- 사운드: 실제 온보드 녹음을 스펙트로그램으로 분석하고, 합성음을 오프라인 렌더해서 같은 방식으로 A/B 비교하며 파라미터를 맞춤

기술 요약:

- 차량 물리는 자체 구현(게임엔진 안 씀): 240Hz 고정 스텝 강체, 레이캐스트 서스펜션, Pacejka 복합 슬립 타이어, 클러치 런치 모델, 공력, 노면별·날씨별 접지력, TC/ABS
- 차량 5종(아반떼 N, 992 GT3 / GT3 RS, 카트, F1), 각각 실제 제로백·최고속도에 맞춰 튜닝
- 엔진음은 녹음 샘플이 아니라 합성(AudioWorklet) — 엔진·배기·변속·타이어·브레이크 등이 전부 따로 켜고 끄는 레이어
- 트랙은 실제 오픈스트리트맵(OSM) 지오메트리 — 20.7km 노르트슐라이페 + Spa + 연습 서킷, SRTM 고도
- 렌더링은 Three.js, 단일 코드베이스로 웹(Vite) + 안드로이드(Capacitor)

이 게임을 만든 전체 세션도 그대로 공개해뒀습니다. Fable과 처음부터 주고받은 대화를 볼 수 있고, 한국어 원문에 영어 토글이 붙어 있습니다. 중간에 보시면 fable 모델이 제한되어서.. 이후에는 opus로 사용하는것도 볼수있습니다  
<https://drive-game.pages.dev/making>

이정도 퀄리티를 단시간에 AI모델들이 구현해주는걸 못봤었는데 , 확실히 Fable이 체감이 되게 좋았던거같습니다.

## 원문
- [원문](https://drive-game.pages.dev)
- [GeekNews 토론](https://news.hada.io/topic?id=30581)

## My Note
<!-- 한 줄 코멘트 남기기 -->

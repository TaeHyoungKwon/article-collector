---
category: Dev Tools
collected_at: '2026-07-21T00:24:29+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31622
id: hada-31622
matched_keywords:
- Claude Code
read: false
recommend_score: 2.693
source: geeknews
tags:
- Dev Tools
- Other
- github.com/itdar
title: 'Show GN: newsline – Claude Code 기다리는 동안 상태줄에서 읽는 한 줄 뉴스'
url: https://github.com/itdar/newsline
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Claude Code에 긴 작업을 시키면 `esc to interrupt`를 멍하니 보는 시간이 쌓입니다.  
딴 일 하기엔 짧고 가만히 있기엔 긴 그 시간에, 세션 하단 상태줄에서 뉴스 헤드라인을  
한 줄씩 읽으면 어떨까 싶어서 만들었습니다.

#### 무엇을 하나

- 기존 상태줄(HUD) *아래 줄*에 지역 맞춤 헤드라인이 6초마다 회전 표시됩니다. 기존  
  상태줄은 그대로 유지됩니다.
- 단순 번역이 아니라 *그 지역의 실제 현지 매체*에서 가져옵니다. 한국이면 연합뉴스,  
  일본이면 NHK, 프랑스면 Le Monde, 독일이면 Tagesschau/Spiegel, 스페인이면 El País,  
  브라질이면 G1, 영어권이면 BBC/NPR 식으로요. 해당 매체가 죽거나 막히면 Google News  
  로케일 피드로 자동 폴백합니다. 지금은 위 매체들 기준이고, 앞으로 더 다양한 플랫폼과  
  기사가 섞여 점점 풍부해질 예정입니다.
- 헤드라인은 OSC 8 하이퍼링크라 대부분의 터미널에서 바로 클릭해 기사로 이동합니다.
- 한국어 포함 8개 언어, 분야(topic: 테크/비즈니스/스포츠 등) 선택 가능.
- 헤드라인 색상과 회전 주기(기본 6초)도 설정에서 원하는 대로 조정할 수 있습니다.

#### 왜 / 기존과 뭐가 다른가

상태줄에 정보를 붙이는 도구는 많지만, 대부분 기존 상태줄을 교체합니다. newsline은  
교체가 아니라 *한 줄을 덧붙이는* 방식이라 이미 쓰던 HUD/statusline과 같이 씁니다.  
그리고 언어 코드에 아무 뉴스나 붙이는 게 아니라, 로케일별로 신뢰도 높은 자국 매체를  
1순위로 두고(엣지 서비스가 지역·분야별로 신선한 소스를 골라줌) 폴백만 Google News를  
씁니다.  
그리고 상태줄은 Claude Code가 매우 자주 호출하기 때문에 절대 네트워크를 기다리면  
안 됩니다. 그래서:

1. 백그라운드에서 RSS를 로컬로 가져오고 (python3 표준 라이브러리만, 의존성 없음)
2. 헤드라인 N개를 캐시에 저장한 뒤
3. 상태줄 호출 시엔 캐시에서 즉시 렌더하고 벽시계 기준으로 회전시킵니다.  
   갱신은 single-flight 락이 걸린 백그라운드 프로세스가 담당해서 중복 실행이 없습니다.

#### 사용해보기 (가입·이메일 불필요)

> curl -fsSL <https://raw.githubusercontent.com/itdar/newsline/master/install.sh> | sh

npm(`npm i -g newsline-cli && newsline init`), Homebrew, Claude Code 플러그인  
마켓플레이스(`/plugin marketplace add itdar/newsline`)로도 설치됩니다. 다음 메시지  
전송 시점부터 표시되고 재시작이 필요 없습니다. `newsline uninstall`로 이전 상태줄이  
완전히 복원됩니다.

#### 프라이버시

수집·표시는 전부 로컬입니다. 외부로 나가는 건 지역 소스 선정을 위한 대략적 컨텍스트  
(언어·국가·분야 등, 트래킹 ID 없음)뿐입니다. `~/.config/newsline/config.json`에  
`"api": "off"`와 `"endpoint": "off"`를 넣으면 완전 로컬 모드가 되어 뉴스 피드 외  
어디에도 접속하지 않습니다.

GitHub: <https://github.com/itdar/newsline>  
어떤 뉴스 소스나 분야가 더 필요한지 피드백 특히 환영합니다.

## 원문
- [원문](https://github.com/itdar/newsline)
- [GeekNews 토론](https://news.hada.io/topic?id=31622)

## My Note
<!-- 한 줄 코멘트 남기기 -->

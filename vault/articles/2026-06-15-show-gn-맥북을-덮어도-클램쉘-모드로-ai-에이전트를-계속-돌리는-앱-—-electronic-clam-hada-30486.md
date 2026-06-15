---
category: AI
collected_at: '2026-06-15T09:09:29+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30486
id: hada-30486
matched_keywords:
- AI
- Claude Code
- Codex
read: false
recommend_score: 7.386
source: geeknews
tags:
- AI
- Other
- github.com/jadhvank
title: 'Show GN: 맥북을 덮어도 클램쉘 모드로 AI 에이전트를 계속 돌리는 앱 — Electronic Clam'
url: https://github.com/jadhvank/eclam
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. 맥북을 덮어도(클램쉘 모드) AI 에이전트가 멈추지 않고 계속 돌아가게 하는  
macOS 메뉴바 앱을 만들어 공유합니다.

최근 'AI 코딩 열풍에 노트북을 닫지 못한 채 이동하는 개발자들'(이른바  
'노트북 열고 걷기' 밈) 같은 뉴스들이 나왔습니다.  
(<https://www.donga.com/news/Economy/article/all/20260513/133913987/3>)

딱 제 얘기였습니다. 이동 중에 에이전트한테 작업을 시켜놓고 자리를 떠야 할 때가 있는데,  
맥북을 덮으면 잠들어 작업이 끊기곤 했습니다.  
그 기사에선 "Caffeinate 쓰면 되지 않냐"고도  
하는데, 실제로 caffeinate를 걸어도 외장 화면 없이 덮개를 닫으면 클램쉘로 잠들어버리죠.  
그렇다고 늘 켜두자니 *프로세스가 떠 있는지*만 볼 뿐이라, 일이 끝나도 계속 깨어서 발열과  
방전을 부릅니다. 기존 '커피류(?)' 앱들이 막아주지 못하거나, 막아줘도 조금 아쉬웠습니다.

그래서 직접 만들었습니다.

- **덮개를 닫아도 안 잠재우기** — 토글 하나. 터미널 명령도, 인증을 다시 할 필요도 없습니다.
- **과열·방전 방지** — 배터리와 온도를 지켜보다가 설정값을 넘으면 작업을 쉬게 해서  
  맥북이 가방 안에서 타거나 방전되는 걸 막습니다. 외장화면 없이 덮개 닫으면 더 깐깐하게,  
  Desktop 모드면 느슨하게 — 상태에 따라 기준이 바뀝니다.
- **프로세스가 아니라 작업을 감지** — 에이전트 작업이 진작 끝났는데 계속 클램쉘이면  
  그것대로 배터리 낭비에 발열입니다. *실제로 작업 중인지*를 감지해서, 일이 끝나면 알아서  
  유휴로 넘어갑니다 (Strict). 프로세스 살아있는 한 깨워두는 Lax 모드도 있습니다.
- **기본 에이전트 5종 인식** — Claude Code · Codex · Cursor · opencode · Antigravity.  
  다른 에이전트도 glob 패턴이나 선언 파일 하나로 직접 추가 가능합니다.
- **원격 작업 인지** — SSH·화면 공유·Tailscale로 접속 중이면 잠들지 않아 원격 작업이 끊기지 않습니다.
- **보안** — 감지는 transcript 파일의 *수정 시각*만 읽습니다. 내용은 읽지 않습니다.

그 외 CLI, 이름 붙인 세션, Telegram 알림(선택), 종료 시 sleep 복원 3중 안전장치도 있습니다.

기술 스택은 외부 의존성 없이 Swift + AppKit, 전원 제어는 IOKit SPI  
(`IOPMSetSystemPowerSetting`), 권한은 SMAppService 데몬으로 helper 하나를 사용합니다.  
Developer ID로 서명되어 있습니다. Apple Silicon · macOS 13+ (Ventura) 전용입니다.

아직 개발 단계라 거친 부분이 있습니다.  
무료 오픈소스이고, 써보시고 피드백 주시면 정말 감사하겠습니다 🙏  
"이 에이전트도 인식됐으면" 하는 게 있으면 알려주세요.

## 원문
- [원문](https://github.com/jadhvank/eclam)
- [GeekNews 토론](https://news.hada.io/topic?id=30486)

## My Note
<!-- 한 줄 코멘트 남기기 -->

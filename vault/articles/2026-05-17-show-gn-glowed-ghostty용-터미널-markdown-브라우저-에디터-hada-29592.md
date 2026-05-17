---
category: AI
collected_at: '2026-05-17T23:47:45+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=29592
id: hada-29592
matched_keywords:
- AI
- LLM
- RAG
- Codex
read: false
recommend_score: 9.099
source: geeknews
tags:
- AI
- Other
- github.com/khw1031
title: 'Show GN: glowed - Ghostty용 터미널 Markdown 브라우저/에디터'
url: https://github.com/khw1031/glowed
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
glowed는 Ghostty 터미널에서 프로젝트 안의 Markdown 문서를 검색, 미리보기, 편집하는 TUI 도구입니다.

개인적으로 지식 관리 시스템 안의 `.md` 파일을 터미널 안에서 빠르게 탐색하고, 필요한 부분은 LLM CLI로 넘기는 흐름이 필요해서 만들었습니다. 특히 터미널만 열어놓고 문서를 빠르게 탐색하고 보고 싶은 욕구에서 바이브 코딩으로 이틀 정도 시간을 들여 만들어봤습니다.

설치는 Homebrew tap으로 할 수 있습니다.

```
brew install khw1031/tap/glowed
```

사용 예시는 다음과 같습니다.

```
 cd my-project  
 glowed  
  
 # 또는 특정 파일 바로 열기  
 glowed ./docs/note.md
```

현재 지원하는 기능은 다음과 같습니다.

- project root 아래 .md 파일 스캔
- 파일명, frontmatter, tag: / tags: 검색
- Glamour 기반 Markdown preview
- raw Markdown edit mode
- 저장 시 backup + atomic write
- undo/redo
- mouse click/wheel/drag 기반 selection
- source selection mode에서 원본 Markdown을 path metadata와 함께 복사
- footer action bar
- 설정 가능한 keymap
- 외부 LLM CLI session launcher
  - claude, codex, aider, 또는 직접 만든 wrapper script 등 PATH에서 실행 가능한 CLI를 설정 가능

LLM 쪽은 glowed가 API key나 OAuth를 직접 다루지 않고, 사용자가 이미 로그인해 둔 CLI를 새 Ghostty split/session에서 여는 방식입니다.

현재 한계도 명확합니다. (개인 사용 용도로 개인 환경에 맞춰서 바이브 코딩 되었습니다...)

- macOS + Ghostty 기준으로 만들었습니다.
- iTerm2, Terminal.app, WezTerm, Kitty, tmux, SSH, Linux terminal 등에서는 아직 충분히 테스트하지 않았습니다.
- mouse tracking, drag selection, cursor/key sequence, Ghostty split 실행은 환경 영향을 많이 받을 수 있습니다.
- preview 화면에서 선택한 rendered text를 원본 Markdown line/column으로 정확히 역매핑하지는 않습니다. 원본 Markdown 복사는 edit mode나 source selection mode를 사용해야 합니다.
- 아직 초기 MVP라 중요한 문서는 git 같은 version control과 함께 쓰는 것을 권장합니다.

개발 과정도 README에 적어두었습니다. 현재 구현은 Codex GPT-5.5, pi agent coding harness, local TODO.md planning file을 사용해 만들었습니다.

이 프로젝트에서는 AI 시대에 맞는 새로운 오픈소스 관리 방식도 실험해보고 있습니다.

기존처럼 모든 개선을 upstream PR로 모으는 방식보다는, 사용자가 자신의 workflow에 맞게 자유롭게 수정하고, 각자의 Homebrew tap으로 배포하는 방식을 우선 권장합니다.

예를 들어 같은 glowed formula 이름이라도 Homebrew tap namespace가 다르면 각각 배포할 수 있습니다.

```
  brew install khw1031/tap/glowed  
  brew install someone/tap/glowed
```

즉, 사용자는 someone/tap/glowed처럼 자신의 버전을 만들어 자유롭게 사용하고 배포할 수 있습니다. 필요하다면 binary 이름도 glowed로 유지하거나, 여러 버전과 공존하도록 glowed-someone처럼 바꿀 수 있습니다.

수정한 버전을 공개하신다면 GitHub issue의 Distribution registration으로 알려주시면 좋겠습니다. 승인 요청은 아니고, 어떤 버전이 있는지 공유하는 용도입니다. AI agent나 coding harness로 수정했다면 어떤 agent/model/method를 썼는지도 함께 적는 것을 권장합니다. 제가 살펴보고 필요하다고 판단한 아이디어나 변경점은 직접 이 저장소에 반영할 수 있습니다. 그렇기 때문에 자유롭게 사용할 수 있는 LICENSE로 재배포되어야 합니다.

---

P.S.

덧붙여, 현재 새로운 기회를 찾고 있습니다. FE 개발자로 일해왔고, 에이전트를 활용한 AI Transformation과 개발/비개발 워크플로우 개선에 관심이 많습니다. 회사 내부에서 에이전트 기반 워크플로우를 구성해 업무 효율을 높인 경험도 있습니다. 관련 기회가 있다면 GitHub 프로필로 편하게 연락주세요 :)

## 원문
- [원문](https://github.com/khw1031/glowed)
- [GeekNews 토론](https://news.hada.io/topic?id=29592)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: AI
collected_at: '2026-06-04T14:43:56+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30170
id: hada-30170
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/kirinonakar
title: 'Show GN: TxtAIEditor - AI 에이전트와 Markdown/html 미리보기를 탑재한 Windows 텍스트 에디터'
url: https://github.com/kirinonakar/TxtAIEditor
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
TxtAIEditor는 .NET 10.0 및 WinUI 3의 강력한 윈도우 네이티브 성능 위에, WebView2 기반의 커스텀 코어를 융합하여 유연한 렌더링 기능을 결합한 프리미엄 데스크톱 에디터입니다.마크다운 작성, AI 협업, 간단한 CSV 편집까지 개발자와 파워 유저에게 필요한 유용한 기능들을 유기적으로 통합했습니다.

🌟 핵심 기능

1. 가상화 에디터 코어 (대용량 파일 지원)  
   초고속 파일 편집: 가상 스크롤(Virtual Scrolling) 기술을 적용하여 200MB가 넘는 로그 파일, 장편소설, 소스 코드도 지연(Lag) 없이 즉시 열고 매끄럽게 편집할 수 있습니다.  
   최적화된 렌더링: 화면에 보이는 뷰포트 영역과 최소한의 버퍼 영역만 DOM으로 렌더링하여 메모리 사용량을 낮추고 반응 속도를 극대화했습니다.  
   코드 하이라이팅 및 자동완성: Markdown, C#, JavaScript, Python, LaTeX 등 다양한 언어의 구문 강조를 지원하며, Enter나 Tab 키로 즉시 삽입 가능한 인텔리전트 자동완성 및 커스텀 스니펫 기능을 제공합니다.
2. 인터랙티브 CSV 테이블 모드  
   스프레드시트 뷰 변환: .csv 파일을 열면 단순 텍스트가 아닌, 사용하기 편리하고 반응성이 뛰어난 그리드(Grid) 형태의 UI로 자동 변환하여 보여줍니다.  
   엑셀처럼 셀 사이를 자유롭게 이동하며 편집할 수 있습니다.  
   다중 선택 및 열 크기 조절: Ctrl, Shift 키와 마우스 드래그를 활용한 행/열 다중 선택을 지원하며, 경계선을 드래그해 실시간으로 열 너비를 조절할 수 있습니다.
3. AI 어시스턴트, 에이전트 연동  
   다양한 Provider 지원: OpenAI, Gemini, OpenRouter뿐만 아니라 로컬에서 구동하는 LM Studio 엔드포인트까지 자유롭게 연결할 수 있습니다.  
   안전한 키 관리: 민감한 API 키는 윈도우 네이티브 기능인 Windows 자격 증명 관리자(Credential Manager)에 안전하게 암호화되어 저장됩니다.  
   프롬프트 탭 및 프리셋: 최대 4개의 독립된 프롬프트 지시어 탭을 띄워 현재 파일 컨텍스트를 첨부해 질문할 수 있으며, 자주 쓰는 프롬프트 템플릿을 프리셋으로 관리할 수 있습니다.  
   맥락 맞춤형 액션: 드래그한 코드나 텍스트를 대상으로 코드 구조나 마크다운 포맷을 유지한 채 번역, 설명, 리팩토링, 요약 등의 작업을 빠르게 수행합니다.  
   AI 에이전트: AI 에이전트를 탑재하여 복잡한 작업이 가능하며 웹검색, 웹페이지 보기 기능을 지원하여 최신 정보를 참고한 편집이 가능합니다.
4. 사생활 보호를 위한 암호화 노트 (Encrypted Notes)  
   독자 규격의 암호화 노트를 지원하여 개인적인 메모를 안전하게 보관할 수 있습니다.  
   철저한 디스크 보안: 암호화된 탭은 열 때 비밀번호 입력을 요구하며, 편집 후 저장 시 평문이 디스크에 유출되지 않도록 다시 암호화되어 저장됩니다. 암호화된 탭에는 별도의 잠금 아이콘이 표시됩니다.
5. 개발 편의 기능 집약  
   내장 터미널: PowerShell, CMD, Git Bash, WSL 등 다양한 셸 프로필을 에디터 하단에 바로 띄울 수 있으며, 현재 작업 공간과 디렉터리가 자동으로 동기화됩니다.  
   Git 패널: 변경 사항 추적, 스테이징, 커밋 및 원격 저장소 푸시(Push)와 커밋 히스토리 그래프 뷰어를 기본 내장하고 있습니다.  
   스마트 아웃라인 (TOC): 마크다운 헤더 구조 파악은 물론, C#, Python, JS/TS, Go 등의 소스 코드 내 클래스 및 메서드 구조를 분석해 클릭 시 해당 위치로 즉시 이동하는 인터랙티브 아웃라인을 생성해 줍니다.  
   프리미엄 UI/UX: 윈도우 네이티브 Mica 백드롭 테마(다크/라이트 모드)와 조절 가능한 멀티 패널 스플리터, 언제나 위에 고정할 수 있는 스티키 노트 모드를 지원합니다.

Windows 환경에서 가볍고 강력하면서도 편리한 AI 메모장/에디터 쉘이 필요하셨던 분들께 좋은 선택지가 되었으면 합니다.  
사용해 보시고 피드백 남겨주시면 정말 감사하겠습니다!

GitHub 레포지토리 (다운로드 및 소스코드): <https://github.com/kirinonakar/TxtAIEditor>

개인 홈페이지 (다른 개발 앱들도 구경해 보세요!): <https://kirinonakar.github.io/>

## 원문
- [원문](https://github.com/kirinonakar/TxtAIEditor)
- [GeekNews 토론](https://news.hada.io/topic?id=30170)

## My Note
<!-- 한 줄 코멘트 남기기 -->

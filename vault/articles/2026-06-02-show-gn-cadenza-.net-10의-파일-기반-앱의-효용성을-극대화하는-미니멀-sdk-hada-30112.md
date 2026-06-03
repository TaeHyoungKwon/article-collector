---
category: AI
collected_at: '2026-06-02T14:48:18+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30112
id: hada-30112
matched_keywords:
- AI
- Codex
read: false
recommend_score: 4.693
recommended_on: '2026-06-03'
source: geeknews
tags:
- AI
- Other
- github.com/rkttu
title: 'Show GN: Cadenza: .NET 10의 파일 기반 앱의 효용성을 극대화하는 미니멀 SDK'
url: https://github.com/rkttu/cadenza
---

## TL;DR
- Cadenza는 .NET 10+ 파일 기반 앱을 위한 간편한 스크립팅 SDK로, 코드 작성과 실행을 쉽게 할 수 있도록 돕는다.
- 이 SDK는 콘솔 스크립트, 웹 API 등 다섯 가지 타입을 제공하며, 특히 맞춤형 AI 에이전트를 개발할 수 있는 기능이 강조된다.
- Cadenza는 추가 라이센스 없이 VS Code 환경에서 사용 가능해, 개발자들이 보다 쉽게 AI 및 클라우드 기반 솔루션을 다룰 수 있는 기회를 제공한다.

## GeekNews 요약
Cadenza는 .NET 10+ file-based 앱을 위한 단일 파일 스크립팅 SDK 묶음으로. .NET 10 SDK 최신 버전만 설치하면 곧바로 코드를 작성하고 실행할 수 있도록 설계되어있습니다. 익숙하지 않으신 분을 위하 부연 설명을 하자면, Python 기준으로 uv가 PEP 723 경험을 제공하는 것과 비슷한 것으로 볼 수 있습니다.

Cadenza로 개발하면 크게 다음의 다섯 가지 타입의 SDK 중 하나를 고를 수 있습니다.

- Cadenza: 콘솔 스크립트, CLI 유틸리티
- Cadenza.Worker: 백그라운드 서비스, 데몬
- Cadenza.Web: 웹 API, Minimal API 스크립트
- Cadenza.Mcp: Claude / Cursor / VS Code AI 에이전트용 MCP 서버
- Cadenza.Agent: 로컬 AI 에이전트 (MEAI 기반)

웹 API를 비롯한 여러 기본 기능을 제공하지만 가장 강조하고 싶은 것은 Agent 개발입니다. 예를 들어 커스텀 AI 에이전트를 만들기 위해 다음과 같이 코드를 작성하여 실행하고, 개별 실행 파일 혹은 Docker 컨테이너 이미지로 빌드할 수 있는 기능을 제공합니다.

```
ServedModelName = "custom-codex-agent";  
SystemPrompt("You are a helpful assistant with read-only filesystem access.");  
  
Tool("read_file", "Read a UTF-8 text file from disk",  
    (string path) => ReadText(path));  
  
Tool("list_files", "List files matching a glob pattern (e.g., **/*.cs)",  
    (string pattern) => Glob(pattern).ToArray());  
  
UseOllama("llama3.2");  
  
await Run();
```

그리고 이렇게 만든 AI 에이전트를 아래와 같은 별도의 설정 파일을 만들고 CODEX\_HOME 환경 변수에 대체하면 AI 에이전트 구성을 커스터마이징할 수 있는 창구가 열리게 됩니다.

```
model          = "cadenza-codex-openrouter"  
model_provider = "cadenza"  
model_catalog_json = "{catalogPath}"  
  
[model_providers.cadenza]  
name     = "Cadenza.Agent (OpenRouter-backed)"  
base_url = "http://localhost:8080/v1";  
wire_api = "responses"  
env_key  = "CADENZA_API_KEY"  
stream_idle_timeout_ms = 300000
```

아울러 Cadenza 기반 스크립트 작성은 VS Code의 [C# 기본 익스텐션 (Dev Kit 아님)](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp), 혹은 타 VS Code 호환 에디터용 [C# 기본 익스텐션](https://open-vsx.org/extension/dotnetdev-kr-custom/csharp) 만 있으면 바로 쓸 수 있도록 되어있어 Visual Studio 라이선스가 불필요합니다.

많이 사용해보시고 피드백 주시면 감사하겠습니다!

## 원문
- [원문](https://github.com/rkttu/cadenza)
- [GeekNews 토론](https://news.hada.io/topic?id=30112)

## My Note
<!-- 한 줄 코멘트 남기기 -->

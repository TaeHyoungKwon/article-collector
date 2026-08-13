---
category: AI
collected_at: '2026-08-13T10:30:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32455
id: hada-32455
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 8.693
source: geeknews
tags:
- AI
- Other
- unsloth.ai
title: Unsloth Desktop - 로컬 AI 모델 실행/학습/에이전트를 하나로 묶은 오픈소스 앱
url: https://unsloth.ai/docs/desktop
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 빠른 파인튜닝 도구 **Unsloth**가 Desktop 버전을 출시
- LLM뿐 아니라 **diffusion 이미지/비디오, embedding, vision, TTS/STT** 모델을 실행/학습하며, **GGUF/MLX/safetensors** 포맷 지원
- 맥/윈/리눅스/WSL 지원. NVIDIA/AMD/Mac GPU에서 학습 가능
- Claude Code/Codex/Hermes/OpenClaw/OpenCode를 `unsloth start claude` 명령 하나로 **로컬 LLM에 연결**, `--as-subagent` 옵션으로 기존 모델은 유지한 채 로컬 모델을 서브에이전트로 사용 가능
- MCP 연결과 **Bash/Python 샌드박스 실행**을 지원하며, 실패를 자동 감지/수정/재시도하는 **self-healing tool call**로 도구 호출 정확도 최대 50% 향상
- LoRA/QLoRA/전체 파인튜닝/사전학습/RL을 지원하며 500개 이상 모델을 **2배 빠른 학습, 70% 적은 VRAM**으로 처리. **MoE는 최대 12배 빠르고**, GRPO/FP8/vision RL은 VRAM 80% 절감
- **PDF/CSV/DOCX에서 데이터셋 자동 생성**(Data Recipes) 후 노드 기반 UI에서 편집, 학습 결과는 **GGUF/16-bit safetensors** 등으로 내보내기 지원
- **OpenAI/Anthropic 호환 API**로 로컬 모델을 서빙하고, 무료 **Cloudflare HTTPS 터널**(`--secure`)로 휴대폰 등 외부 기기에서 접속 가능
- 무제한 **웹 검색과 Deep Research** 내장. 계획 수립 후 출처를 인용한 상세 리포트 생성. OpenAI/Anthropic/Ollama/vLLM 등 클라우드/외부 서버 모델도 같은 UI에서 혼용
- Kimi K3, Gemma 4, DeepSeek-V4, GLM-5.2, Qwen3.6, MiniMax M3 등을 지원하며 Qwen3.8 등 신모델의 **Day Zero 지원**을 지향
- **텔레메트리 없이 완전 오프라인 실행**이 가능하고 파일/인터넷/도구 실행 권한을 사용자가 직접 제어할 수 있음
- 코어는 Apache 2.0, Studio UI 등 일부 컴포넌트는 AGPL-3.0 듀얼 라이선스

## 원문
- [원문](https://unsloth.ai/docs/desktop)
- [GeekNews 토론](https://news.hada.io/topic?id=32455)

## My Note
<!-- 한 줄 코멘트 남기기 -->

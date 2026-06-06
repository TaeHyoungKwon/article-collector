---
category: AI
collected_at: '2026-06-05T21:35:30+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30207
id: hada-30207
matched_keywords:
- AI
- Claude Code
read: false
recommend_score: -995.099
recommended_on: '2026-06-05'
source: geeknews
tags:
- AI
- Other
- github.com/anthropics
title: Defending Code Reference Harness - AI 기반 취약점 발견과 수정용 Anthropic 오픈소스 프레임워크
url: https://github.com/anthropics/defending-code-reference-harness
---

## TL;DR
- **Defending Code Reference Harness**는 AI 기반으로 취약점을 발견하고 수정하는 자율 파이프라인을 제공하는 오픈소스 프레임워크이다.
- 이 프로젝트는 Docker와 ASAN을 사용하여 C/C++ 메모리 취약점을 탐색하며, 기존 코드를 맞춤화하는 방식으로 다양한 코드베이스에 적용가능하다.
- 독자는 이 프레임워크를 통해 자율적인 보안 작업 흐름을 구축하고, 취약점 관리와 패치 자동화를 통해 보안 성능을 개선할 수 있다.

## GeekNews 요약
- **Defending Code Reference Harness**는 Claude로 자율 취약점 발견과 수정을 수행하기 위한 참조 구현이며, 여러 조직의 보안팀과 협업하며 얻은 학습을 바탕으로 구성한 프로젝트임
- 이 저장소는 제품이 아니라 **참조 구현**이며, 현재 유지보수되지 않고 기여도 받지 않는 상태임
- Anthropic은 관리형 대안으로 [**Claude Security**](https://claude.com/product/claude-security)를 제공하며, 여러 프로젝트의 소스 코드에서 취약점을 찾고 수정하며 triage, fix validation, rapid fix generation 수명주기를 관리할 수 있음
- Claude Code용 skills는 `/quickstart`, `/threat-model`, `/vuln-scan`, `/triage`, `/patch`, `/customize`를 제공하며, 대화형 범위 설정, 스캔, triage, 패치 작업을 지원함
- `harness/`는 **recon → find → verify → report → patch** 흐름의 자율 참조 파이프라인이며, Docker와 ASAN을 사용해 C/C++ 메모리 취약점 탐색에 맞춰져 있음
- 참조 파이프라인의 일반 구조, 프롬프트, 샌드박싱 방식은 재사용할 수 있지만, 모든 코드베이스에서 바로 동작하지 않으며 `/customize`로 언어, 탐지기, 취약점 종류에 맞게 포팅해야 함
- `/quickstart`, `/threat-model`, `/vuln-scan`, `/triage`와 정적 결과에 대한 `/patch`는 파일 읽기·쓰기만 수행하며, Claude Code에서 각 도구 사용을 검토하고 승인하면 샌드박스 없이 실행 가능함
- 자율 참조 파이프라인과 파이프라인 결과에 대한 `/patch`는 대상 코드를 실행하므로, 명시적으로 우회하지 않는 한 **gVisor 샌드박스** 밖에서는 실행을 거부함
- 파이프라인 실행에는 `scripts/setup_sandbox.sh`로 gVisor와 에이전트 이미지를 준비해야 하며, Docker와 `ANTHROPIC_API_KEY` 또는 `CLAUDE_CODE_OAUTH_TOKEN` 환경 변수가 필요함
- 실행 단계는 빌드, recon, find, verify, dedupe, report, patch로 나뉘며, find 에이전트는 격리 컨테이너에서 malformed input을 만들고 ASAN 바이너리가 3회 중 3회 크래시할 때까지 탐색함
- verify 단계는 별도 grader 에이전트가 새로운 컨테이너에서 proof of concept만 넘겨받아 크래시를 재현하고, dedupe 단계는 새 버그·기존 버그의 더 나은 예·중복 여부를 판정함
- report 단계는 primitive class, reachability, escalation path, severity를 포함한 구조화된 exploitability analysis를 작성하고, patch 단계는 수정안을 만든 뒤 빌드, 원래 proof of concept의 비크래시, 테스트 통과, 우회 가능성 재탐색을 확인함
- 초기 사용 흐름은 Day 1에 threat model과 정적 scan·triage·candidate patch를 만들고, Day 2에 C/C++ 라이브러리에서 실행 검증된 findings를 생성한 뒤, Days 3-5에 자체 대상용 `targets/<your-service>/`를 만드는 방식임
- 자체 스택으로 포팅할 때는 finding 신호, proof of concept 형태, 빌드·실행 방식을 정의해야 하며, C/C++ 참조는 ASAN crash signature, crashing input file, clang+ASAN 기반 Dockerfile을 기준으로 삼음
- 자율 triage와 patching은 아직 열린 문제이며, `/patch`의 검증 전략이 기준을 높이지만 severity와 우선순위는 환경별 판단이고 검증된 패치가 항상 upstream 가능하지는 않다는 제약이 있음

## 원문
- [원문](https://github.com/anthropics/defending-code-reference-harness)
- [GeekNews 토론](https://news.hada.io/topic?id=30207)

## My Note
<!-- 한 줄 코멘트 남기기 -->

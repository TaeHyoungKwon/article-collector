---
category: AI
collected_at: '2026-05-18T13:52:04+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29618
id: hada-29618
matched_keywords:
- AI
- LLM
read: false
recommend_score: 4.693
source: geeknews
tags:
- AI
- Other
- github.com/bssm-oss
title: 'Show GN: CodeRabbit 유료 PR 리뷰를 GitHub Actions + Gemma로 무료 대체하기'
url: https://github.com/bssm-oss/gemmaci
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
GemmaCI라는 오픈소스 프로젝트를 만들었습니다.

한 줄로 설명하면, CodeRabbit 같은 AI PR 리뷰어를 GitHub Actions 안에서 무료로 돌려보자는 프로젝트입니다.

CodeRabbit은 좋은 도구지만, private repo에서 본격적으로 PR review를 쓰려면 유료 플랜이 필요합니다. 공식 문서 기준 Free 플랜은 PR summarization 중심이고, PR review는 Pro 이상에서 제공됩니다. Pro는 연간 결제 기준 $24/mo/user, 월결제 기준 $30/mo/user입니다.

그래서 “작은 팀, 학생 프로젝트, 개인 사이드프로젝트에서 CodeRabbit의 핵심 경험을 무료로 대체할 수 없을까?”라는 생각으로 만들었습니다.

GemmaCI는 GitHub Actions에서 Ollama + Gemma 모델을 실행해서 PR diff를 리뷰합니다.

현재 되는 기능은 다음과 같습니다.

- PR summary comment 생성
- 변경된 라인에 inline review comment 작성
- high / critical finding 발견 시 CI check 실패
- evidence, confidence, recommendation 기반 리뷰 출력
- Ollama / model cache로 cold start 비용 절감
- workflow 파일 하나만 추가해서 사용
- PR diff, model output, artifact를 모두 untrusted data로 보는 보안 모델

중요하게 본 부분은 “무료”와 “보안”입니다.

단순히 LLM에게 diff를 던지고 댓글을 달게 하는 것이 아니라, 모델 output을 schema 검증하고, 실제 changed line에 근거가 있는 finding만 게시합니다.

또한 기본적으로 pull\_request\_target을 쓰지 않습니다. PR 작성자가 바꾼 workflow나 script가 write 권한으로 실행되는 위험을 피하기 위해서입니다. publish 단계에서도 trusted base branch code만 실행하고, artifact와 model output은 다시 검증합니다.

실제 GitHub Actions runner에서 smoke PR을 열어 검증했습니다.

검증된 항목:

- GitHub-hosted runner에서 workflow 실행
- Ollama 설치 및 Gemma 모델 리뷰 job 실행
- PR summary comment 게시
- 변경 라인 inline comment 게시
- high severity finding 감지 시 check 실패

테스트 PR에서는 일부러 unsafeDivide 함수를 넣었고, GemmaCI가 “0 나눗셈 검증 누락”을 high severity finding으로 잡아 inline comment를 남겼습니다.

아직 CodeRabbit을 1:1로 완전히 대체하는 수준은 아닙니다. 큰 모델을 쓰는 SaaS 리뷰어만큼의 품질이나 통합 기능을 기대하면 안 됩니다.

대신 목표는 명확합니다.

“돈 내기 애매한 작은 repo에서도, workflow 파일 하나로 무료 AI PR 리뷰를 붙일 수 있게 하자.”

GitHub:  
<https://github.com/bssm-oss/gemmaci>

피드백, 이슈, PR 환영합니다.

## 원문
- [원문](https://github.com/bssm-oss/gemmaci)
- [GeekNews 토론](https://news.hada.io/topic?id=29618)

## My Note
<!-- 한 줄 코멘트 남기기 -->

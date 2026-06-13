---
category: Other
collected_at: '2026-06-13T20:05:45+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30457
id: hada-30457
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- coopi.neocities.org
title: Nix Flakes와 그에 대응하는 Guix 기능들
url: https://coopi.neocities.org/posts/nix-flakes-vs-guix#guix-purity-by-design_6eece251b1ca
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Nix Flakes**는 프로젝트 의존성, 잠금, 출력 스키마, 개발 환경을 `flake.nix`와 `flake.lock` 중심으로 묶고, Guix는 channels, manifests, `guix describe`, `guix shell`, `operating-system` 같은 직교 도구 조합으로 같은 종류의 기능을 제공함
- **Flakes**는 프로젝트별 `inputs`와 자동 `flake.lock`으로 의존성을 고정하고, Guix는 사용자별 `guix describe`와 프로젝트에 커밋을 적은 `channels.scm`, `guix time-machine`으로 재현 가능한 환경을 구성함
- **순수성**은 Flakes에서 restricted evaluation으로 강제되고, Guix에서는 Scheme 모듈 구조와 명시적 입력, 격리된 빌드 컨테이너를 통해 설계상 달성됨
- **출력 구조**는 Flakes가 `packages`, `devShells`, `nixosConfigurations` 같은 표준 attrset을 제공하는 반면, Guix는 `<package>`, manifest, `operating-system`, service 같은 투명한 Scheme 레코드와 파일을 각 명령이 직접 소비함
- **선택 기준**은 단일 진입점과 표준 스키마를 선호하면 Flakes가 맞고, 작고 독립적인 도구를 조합하는 방식을 선호하면 Guix가 더 잘 맞음

---

## 원문
- [원문](https://coopi.neocities.org/posts/nix-flakes-vs-guix#guix-purity-by-design_6eece251b1ca)
- [GeekNews 토론](https://news.hada.io/topic?id=30457)

## My Note
<!-- 한 줄 코멘트 남기기 -->

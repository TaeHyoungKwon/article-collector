---
category: AI
collected_at: '2026-06-08T22:46:59+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30287
id: hada-30287
matched_keywords:
- AI
read: false
recommend_score: 3.099
source: geeknews
tags:
- AI
- Other
- github.com/PerryTS
title: TypeScript를 LLVM 기계어로 직접 컴파일, &quot;Perry&quot; 네이티브 컴파일러
url: https://github.com/PerryTS/perry
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
기존의 TypeScript 개발 패러다임은 고수준 추상화인 TS 코드를 JavaScript로 트랜스파일한 뒤, V8이나 JavaScriptCore 같은 무거운 JIT 런타임 엔진(Node.js, Bun, Deno 등) 위에서 구동하는 방식이 당연시되어 왔습니다.

최근 오픈소스 트랙에 등장한 Perry는 이러한 전통적인 런타임 모델을 완전히 걷어내고, TypeScript 코드를 standalone 네이티브 바이너리로 직접 컴파일하는 것을 목표로 하는 Rust 기반의 Native-First 컴파일러입니다.

---

💡 핵심 아키텍처 및 특징

- No Runtime (런타임 제로): V8 엔진이나 Electron, JVM 같은 무거운 중간 계층 없이, SWC로 TS 코드를 파싱하고 LLVM 인프라를 통해 타겟 플랫폼의 머신 코드로 직접 빌드합니다.
- 크로스 플랫폼 원소스 빌드: 하나의 TypeScript 코드베이스로 macOS, iOS, Android, Linux, Windows를 모두 지원하는 바이너리를 생성합니다.
- True TypeScript Support: AssemblyScript처럼 'TS와 유사한 별도 언어'가 아닌, Strict Mode를 기반으로 하는 온전한 TypeScript 생태계 지원을 지향합니다.
- 초경량 UI 프레임워크 호환: 단 몇 MB 수준의 바이너리 용량과 0ms에 가까운 sub-second 콜드 스타트를 자랑합니다. SwiftUI, GTK4, WinUI 같은 플랫폼 네이티브 GUI 결합은 물론, 자체 React 렌더러를 통한 JSX 작성도 가능합니다.

---

🛠️ 개발 현황 및 한계 (Hacker News 피드백 반영)  
최근 HN 등지에서 뜨거운 감자로 떠오른 프로젝트인 만큼, 프로덕션 레벨로 가기 위한 과제들도 명확히 논의되고 있습니다.

- 동적 JS 특성 제한: 객체에 런타임에 임의로 필드/메서드를 주입하거나 프로토타입을 변형하는 식의 동적 자바스크립트 스타일은 정적 컴파일 특성상 지원하지 않으며, 엄격하고 결정론적인(Deterministic) TS 서브셋을 기반으로 동작합니다.
- Node.js 내장 모듈 에뮬레이션: 현재 hyper, rustls, tokio 등 Rust 생태계를 기반으로 Node.js의 HTTP 표준 라이브러리를 고스란히 에뮬레이션하고 있습니다. Fastify 등 일부 모듈 컴파일에 성공하며 빠르게 발전 중이지만, Express처럼 동적 임포트가 얽힌 복잡한 생태계 라이브러리들과의 100% 호환성은 아직 알파 단계의 해결 과제입니다.

---

```
# 사용법은 극도로 심플합니다  
$ perry compile src/main.ts -o myapp  
$ ./myapp  # 의존성 없는 순수 네이티브 바이너리 실행
```

---

웹 생태계에 갇혀있던 TypeScript를 시스템 프로그래밍과 초경량 네이티브 앱 영역으로 확장하려는 시도로서, 고성능 시스템 아키텍처나 LLVM 컴파일러 파이프라인에 관심이 많으신 분들이 흥미롭게 지켜볼 만한 프로젝트입니다.

GitHub: <https://github.com/PerryTS/perry>

## 원문
- [원문](https://github.com/PerryTS/perry)
- [GeekNews 토론](https://news.hada.io/topic?id=30287)

## My Note
<!-- 한 줄 코멘트 남기기 -->

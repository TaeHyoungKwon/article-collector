---
category: Other
collected_at: '2026-07-30T18:29:54+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31984
id: hada-31984
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/clroot
title: 'Show GN: prewire - 런타임 컨테이너 없이 빌드 타임에 연결하는 TypeScript 프론트엔드 DI'
url: https://github.com/clroot/prewire
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. TypeScript 프론트엔드용 빌드 타임 DI 라이브러리 **prewire**를 만들었습니다.

이 라이브러리를 만들게 된 계기는 제가 관리하는 프론트엔드 모노레포의 구조였습니다.

여러 사업의 프론트엔드가 하나의 core/kit 코드를 공유하고 있는데, 현재 앱들은 Next.js를 사용하고 있습니다. 앞으로 일부 사업에서는 TanStack Router를 사용해 보고 싶었지만, 그렇다고 공유 코어가 `next/navigation`이나 `@tanstack/react-router`에 직접 의존하게 만들고 싶지는 않았습니다.

사업마다 다른 구현을 선택하면서도 공유 코어는 수정하지 않는 구조가 필요했습니다.

prewire에서는 공유 코드가 먼저 port와 token을 선언합니다.

```
export interface RouterPort {  
  href(to: string): string  
  push(to: string): void  
}  
  
export const ROUTER = new InjectionToken<RouterPort>('router')
```

각 앱은 자신이 사용하는 프레임워크로 이 port를 구현합니다.

```
export const tanstackRouter = injectable(  
  { logger: LOGGER },  
  ({ logger }): RouterPort => ({  
    href: (to) => to,  
    push: (to) => {  
      logger.info(`navigate → ${to}`)  
      throw redirect({ to })  
    },  
  }),  
  { provides: ROUTER },  
)
```

공유 코드를 포함한 소비자 쪽에서는 구현이 어디서 왔는지 알 필요 없이 같은 경로만 import합니다.

```
import { router } from '#prewire'
```

`prewire codegen`이 앱과 공유 패키지의 `injectable()` 선언을 정적으로 분석해 의존성 순서대로 평범한 TypeScript composition root를 생성합니다.

```
export const logger = consoleLoggerBinding.factory({})  
export const router = tanstackRouterBinding.factory({ logger })
```

런타임 컨테이너나 `reflect-metadata`, decorator는 사용하지 않습니다. 누락된 binding, 순환 의존성, 중복 binding 같은 문제는 실행 중이 아니라 코드 생성 단계에서 빌드 에러로 처리합니다. 생성된 코드는 직접 읽을 수 있고, 필요하면 떼어내 수동 composition root로 사용할 수도 있습니다.

공유 패키지의 구현을 앱이 아무렇게나 덮어쓰지 못하도록 override도 기본적으로 닫혀 있습니다. 공유 코드가 `default: true`를 지정한 binding만 앱에서 교체할 수 있습니다. Kotlin의 `open`과 비슷한 의도입니다.

`environment` 축도 별도로 두었습니다. `live/test`, `server/client`, 또는 사업 앱 이름처럼 사용자가 원하는 기준으로 서로 다른 root를 만들 수 있습니다. 예를 들어 서버 전용 binding은 클라이언트 root에서 단순히 실행되지 않는 정도가 아니라, 생성된 코드에 import 자체가 포함되지 않습니다.

현재 저장소의 예제에는 하나의 공유 kit를 다음 세 앱이 서로 다르게 연결하는 구성이 들어 있습니다.

- Next.js
- TanStack Start
- React Router

빌드 연동은 Vite·webpack·rspack용 unplugin과 Next.js용 `withPrewire()`를 제공하고 있습니다.

다만 아직 실제 제품 코드에 도입한 상태는 아닙니다. 먼저 별도의 라이브러리와 예제로 설계를 검증하고 공개한 단계입니다. 현재 npm에 `0.1.1`로 배포되어 있으며, 초기 0.x 버전이라 API는 변경될 수 있습니다.

또한 단일 앱, 단일 환경에서 binding이 몇 개 없는 경우에는 prewire를 사용할 이유가 크지 않습니다. 그런 프로젝트라면 composition root 한 파일을 직접 작성하는 편이 더 단순합니다. 같은 공유 코드를 여러 앱·환경·테스트 구성에서 다르게 연결해야 할 때를 주된 대상으로 생각하고 있습니다.

저는 주로 백엔드를 개발해 왔고, 프론트엔드 모노레포를 관리하면서 이 문제를 DI와 빌드 타임 코드 생성으로 풀었습니다. 그래서 해법 자체가 꽤 백엔드스럽다는 생각도 듭니다.

프론트엔드를 전문적으로 다루는 분들은 여러 앱이 공유 코어를 사용하면서 라우터처럼 프레임워크별 구현만 달라지는 문제를 보통 어떻게 해결하는지 궁금합니다. prewire 같은 빌드 타임 DI가 적절해 보이는지, 더 단순하거나 프론트엔드 생태계에 익숙한 접근이 있다면 의견을 듣고 싶습니다.

GitHub: <https://github.com/clroot/prewire>  
npm: <https://www.npmjs.com/package/@prewire/core>

MIT 라이선스입니다. 초기 단계라 설계와 API에 대한 비판적인 피드백도 환영합니다.

## 원문
- [원문](https://github.com/clroot/prewire)
- [GeekNews 토론](https://news.hada.io/topic?id=31984)

## My Note
<!-- 한 줄 코멘트 남기기 -->

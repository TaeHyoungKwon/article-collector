---
category: AI
collected_at: '2026-08-14T16:42:19+09:00'
geeknews_comments: 1
geeknews_score: 6
geeknews_url: https://news.hada.io/topic?id=32492
id: hada-32492
matched_keywords:
- AI
- LLM
- Claude Code
- Codex
read: false
recommend_score: 10.154
recommended_on: '2026-08-14'
source: geeknews
tags:
- AI
- Other
- blog.modelcontextprotocol.io
title: MCP가 Stateless해짐
url: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
최근 <https://news.hada.io/topic?id=32203> 를 읽고 찾아보다가 MCP에 큰 변경사항이 있었다는걸 알게되어 공유합니다.

---

- MCP `2026-07-28`은 출시 이후 가장 큰 규모의 스펙 변경으로, 프로토콜 코어를 **stateful한 양방향 연결 구조에서 stateless한 request/response 구조로 전환**함
- 기존의 `initialize` handshake와 `Mcp-Session-Id`가 제거되어 각 요청이 독립적으로 처리되며, remote MCP 서버를 일반적인 HTTP 서비스처럼 여러 인스턴스로 수평 확장하기 쉬워짐
- 서버가 클라이언트에게 추가 입력을 요청하는 흐름은 **Multi Round-Trip Requests(MRTR)** 로 재설계되고, `Mcp-Method`, `Mcp-Name`, cache metadata, Trace Context 등이 추가되어 routing·caching·observability도 개선됨
- MCP Apps와 Tasks를 시작으로 **Extensions가 정식 1급 개념**이 되어, 새로운 기능을 MCP core와 독립적으로 개발하고 버전 관리할 수 있게 됨
- Roots, Sampling, Logging은 deprecated 되었으며, Tool schema는 전체 JSON Schema 2020-12를 지원함
- 이번 버전부터 정식 deprecation policy도 도입되어 기능을 제거하려면 최소 12개월의 deprecated 기간을 거쳐야 함

#### Stateful에서 Stateless 프로토콜로 전환

- 기존 MCP에서는 먼저 `initialize`를 호출해 protocol version, capabilities, client 정보를 교환하고 서버가 `Mcp-Session-Id`를 발급했음
- 이후 모든 요청이 해당 session ID를 사용했기 때문에 여러 MCP 서버 인스턴스를 운영하려면 sticky session이나 shared session store 같은 추가 구성이 필요할 수 있었음
- `2026-07-28`에서는 `initialize` / `initialized` handshake와 `Mcp-Session-Id`가 모두 제거됨
- protocol version, client identity, capabilities 등 요청을 처리하는 데 필요한 정보가 요청 자체에 포함되어, 어떤 MCP 서버 인스턴스가 요청을 받아도 독립적으로 처리할 수 있음
- 서버의 capabilities를 미리 확인해야 하는 경우에는 새로운 `server/discover` RPC를 선택적으로 사용할 수 있음
- 결과적으로 remote MCP 서버를 일반적인 HTTP 서비스처럼 round-robin load balancer 뒤에 두고 운영할 수 있게 됨

#### Stateless여도 애플리케이션 상태는 유지할 수 있음

- protocol-level session이 사라졌다고 해서 MCP 서버가 상태를 유지할 수 없는 것은 아님
- 브라우저 세션이나 장바구니처럼 여러 tool call 사이에서 상태가 필요한 경우 `browser_id`, `basket_id` 같은 명시적인 handle을 반환하고 이후 tool argument로 다시 전달하는 방식을 권장함
- 기존에는 transport의 session 내부에 숨겨져 있던 상태가 model에게 명시적으로 보이게 되며, model이 여러 tool 사이에서 handle을 전달하거나 조합할 수도 있음

#### Multi Round-Trip Requests(MRTR)

- Stateless 구조에서는 서버가 persistent connection을 통해 client에게 역방향 요청을 보내는 기존 방식도 변경할 필요가 있었음
- 이를 위해 **Multi Round-Trip Requests(MRTR)** 가 도입됨
- 예를 들어 tool 실행 중 `"파일 3개를 삭제할까요?"` 같은 사용자 확인이 필요한 경우 서버는 연결을 계속 열어두는 대신 `input_required` 결과를 반환함
- Client가 사용자 입력을 받은 뒤 `inputResponses`와 서버가 전달한 `requestState`를 포함해 원래 요청을 다시 호출함
- 필요한 상태가 요청 안에 포함되므로 최초 요청과 재요청을 서로 다른 MCP 서버 인스턴스가 처리해도 됨
- Server-initiated request도 반드시 현재 처리 중인 client request에서 시작되어야 하므로, 서버가 아무런 사용자 요청 없이 갑자기 elicitation을 발생시키는 것은 허용되지 않음

#### Routing, Caching, Tracing 개선

- Streamable HTTP 요청에 `Mcp-Method`, `Mcp-Name` header가 추가됨
- 예를 들어 gateway가 JSON body를 직접 파싱하지 않고도 `tools/call`, 특정 tool 이름 등을 header만 보고 routing, authorization, rate limiting에 사용할 수 있음
- Header와 실제 JSON body의 method/name이 일치하지 않으면 서버가 요청을 거부하도록 해 header spoofing을 방지함
- `tools/list`, `resources/list`, `resources/read` 등의 결과에는 `ttlMs`, `cacheScope`가 추가되어 client가 결과를 얼마나 오래 cache할 수 있는지 알 수 있음
- Tool 목록도 deterministic한 순서를 유지하도록 권장되어 tool definition 순서가 불필요하게 바뀌면서 LLM prompt cache가 깨지는 문제를 줄임
- `_meta`를 통한 W3C Trace Context 전달도 표준화되어 host → MCP client → MCP server → downstream service까지 하나의 distributed trace로 연결할 수 있음

#### Extensions가 정식 1급 개념으로 변경

- 기존에도 Extensions 개념은 있었지만 공식적인 관리·버전 정책은 부족했음
- 새 스펙에서는 extension마다 reverse-DNS 형식의 ID와 독립적인 버전, repository, maintainer를 가질 수 있도록 정식 framework가 추가됨
- Client와 server는 capabilities의 `extensions` map을 통해 서로 지원하는 extension을 확인함
- 새로운 기능을 MCP core release에 바로 넣지 않고 extension으로 먼저 실험하고 독립적으로 발전시킬 수 있게 됨

#### MCP Apps

- 공식 extension 중 하나로, MCP 서버가 단순 text/JSON 결과뿐 아니라 **interactive HTML UI**를 제공할 수 있게 함
- Tool이 사용할 UI template을 미리 선언하면 host가 이를 prefetch·cache·검토한 뒤 sandboxed iframe 안에서 렌더링함
- Dashboard, chart, form, interactive control 같은 UI를 MCP tool 결과와 함께 제공할 수 있음
- UI에서 발생한 동작도 기존 MCP JSON-RPC와 동일한 audit·consent 흐름을 거치도록 설계됨

#### Tasks

- `2025-11-25`에서 experimental core 기능이었던 Tasks는 별도의 `io.modelcontextprotocol/tasks` extension으로 이동함
- 오래 걸리는 tool 작업의 경우 서버가 즉시 결과를 반환하는 대신 task handle을 반환할 수 있음
- 이후 client가 `tasks/get`, `tasks/update`, `tasks/cancel`을 사용해 작업 상태를 조회하거나 입력을 추가하고 취소할 수 있음
- Task 생성 여부는 client가 지정하는 것이 아니라, client가 Tasks 지원 여부를 알리면 server가 해당 tool call을 task로 실행할지 결정함
- Session이 사라지면서 task 목록을 안전하게 scope하기 어려워져 기존 `tasks/list`는 제거됨

#### Authorization 강화

- OAuth 2.0 / OpenID Connect 실제 배포 환경에 맞추기 위한 여러 보안 개선이 포함됨
- Authorization response의 `iss`를 검증해 authorization-server mix-up 공격을 방지함
- Dynamic Client Registration 시 desktop/CLI client가 `"web"` application으로 잘못 처리되어 localhost redirect URI가 거부되는 문제를 줄이기 위해 `application_type`을 명시함
- 발급받은 client credential은 해당 authorization server의 issuer에 bind되어 다른 issuer에서 재사용할 수 없음
- Refresh token, step-up authorization의 scope 처리, `.well-known` discovery 규칙 등도 명확해짐
- 최종 스펙에서는 Dynamic Client Registration(DCR) 자체도 deprecated되고 Client ID Metadata Documents(CIMD)를 사용하는 방향으로 이동함

#### Roots, Sampling, Logging Deprecated

- 세 가지 기존 core 기능이 deprecated 상태로 전환됨
- Roots 대신 tool parameter, resource URI, server configuration 등을 사용하는 방향을 권장함
- Sampling 대신 MCP server가 필요한 LLM provider API와 직접 통합하는 방식을 권장함
- Logging은 stdio의 경우 `stderr`, structured observability는 OpenTelemetry 사용을 권장함
- 즉 MCP 자체에서 별도의 범용 기능을 계속 확장하기보다 이미 존재하는 표준이나 명시적인 tool primitive를 활용하는 방향으로 core의 역할을 줄이고 있음

#### JSON Schema 2020-12 지원

- Tool의 `inputSchema`, `outputSchema`가 전체 JSON Schema 2020-12를 지원함
- `oneOf`, `anyOf`, `allOf`, conditional, `$ref`, `$defs` 등을 사용할 수 있어 복잡한 tool input/output 구조를 표현하기 쉬워짐
- `inputSchema`의 root는 계속 object여야 하지만 `outputSchema`에는 같은 제한이 없으며, `structuredContent`도 object뿐 아니라 임의의 JSON 값을 반환할 수 있음
- 외부 `$ref`를 자동으로 가져오는 것은 SSRF 등의 위험이 있어 금지되며 schema depth와 validation time에도 제한을 둘 것을 권장함

#### Formal Deprecation Policy

- 기능 lifecycle을 `Active → Deprecated → Removed`로 공식화함
- Deprecated된 기능은 최소 12개월 동안 유지되어야 하며, 실제 제거에도 별도의 SEP가 필요함
- Extensions framework와 함께 MCP core를 안정적으로 유지하면서 새로운 기능은 별도로 빠르게 발전시킬 수 있는 구조를 만드는 것이 목적임

#### 전체적으로

- 이번 변경의 핵심은 MCP를 **특수한 stateful agent protocol에서 일반적인 Web/HTTP 인프라와 잘 맞는 stateless protocol로 바꾸는 것**에 가까움
- Connection이나 session 안에 숨겨져 있던 상태를 request metadata나 명시적인 handle로 옮기고, 복잡한 기능은 Extensions로 분리함
- 덕분에 remote MCP 서버를 load balancer, API gateway, cache, OpenTelemetry 같은 기존 인프라와 훨씬 자연스럽게 결합할 수 있게 됨
- 기존 `2025-11-25` 구현에서 session이나 기존 Tasks API에 의존하고 있다면 migration이 필요한 breaking release임

---

본문에 있는 내용은 아닌데 참고차 추가로 덧붙입니다.

#### Claude / Codex에는 바로 적용되는가?

- MCP 스펙이 새로 출시됐다고 Claude나 Codex에 자동으로 적용되는 것은 아니며, **Claude Code / Codex CLI 같은 MCP client가 새 프로토콜을 직접 구현해야 함**
- 모델 자체가 바뀌는 문제라기보다, 모델을 감싸는 MCP client 구현의 문제임

#### Codex

- Codex CLI는 `0.147.0`부터 MCP `2026-07-28` 지원이 구현되어 있음
- 다만 아직 기본 활성화된 기능은 아니며 `mcp_2026_07_28` feature flag를 켜야 사용할 수 있음

```
[features]  
mcp_2026_07_28 = true
```

- 또는 `codex --enable mcp_2026_07_28`로 실행 가능
- Modern MCP의 `server/discover` 등을 지원하면서, 새 프로토콜을 지원하지 않는 서버에는 기존 `initialize` 기반 Legacy MCP로 fallback하도록 구현되어 있음
- 따라서 **Codex에서는 지금 바로 새 MCP를 실험할 수 있지만 아직 기본값은 아님**

#### Claude Code

- Claude Code에도 이미 MCP `2026-07-28` migration 작업이 들어가고 있음
- 현재 버전에서는 먼저 `server/discover`와 `MCP-Protocol-Version: 2026-07-28`을 사용해 Modern MCP 서버인지 확인하는 동작이 관찰됨
- Modern MCP가 아니면 기존 `initialize` 기반 프로토콜로 fallback함
- 따라서 Claude Code도 새 스펙을 전혀 지원하지 않는 상태는 아니지만, **Codex처럼 전체 `2026-07-28` 지원이 명확하게 GA로 발표된 상태인지는 아직 불분명함**

#### MCP 서버도 새 스펙을 지원해야 함

- Client만 업데이트된다고 새 기능을 모두 사용할 수 있는 것은 아님
- MCP 서버 역시 `2026-07-28`을 지원해야 Stateless transport, MRTR, cache metadata 등의 새 기능을 실제로 사용할 수 있음
- 당분간은 Client와 Server가 Legacy / Modern MCP를 동시에 지원하고 negotiation을 통해 점진적으로 migration하는 형태가 될 가능성이 높음

#### 기존 MCP 서버는 그대로 사용 가능

- 최신 Codex나 Claude Code에서 기존 MCP 서버를 연결해도 바로 깨지는 것은 아님
- Client가 Modern MCP 지원 여부를 확인한 뒤 지원하지 않는 서버라면 기존 Legacy MCP 방식으로 fallback함
- 따라서 현재 사용 중인 MCP 서버를 당장 전부 수정할 필요는 없음

#### 실제 체감 변화

- 기존 Legacy MCP 서버를 그대로 사용한다면 최신 Claude/Codex를 사용해도 동작 방식에는 큰 차이가 없음
- Client와 Server 양쪽 모두 `2026-07-28`을 지원할 때 비로소 다음과 같은 새 구조의 이점을 얻을 수 있음
  - `initialize` / `Mcp-Session-Id` 제거
  - Stateless request 처리
  - 일반적인 round-robin load balancing
  - MRTR 기반 추가 입력 요청
  - Tool / Resource cache metadata
  - `Mcp-Method`, `Mcp-Name` 기반 gateway routing
  - 새로운 Extensions 구조

#### Tool contract 갱신 문제는 별개

- MCP `2026-07-28`은 `tools/list`, `ttlMs`, `listChanged`, `subscriptions/listen` 등을 통해 **동적으로 변경되는 tool catalog를 처리할 기반**을 크게 개선함
- 하지만 MCP client가 변경된 tool schema를 다시 받아온 뒤, 현재 Claude/Codex 모델 세션의 tool definition까지 즉시 갱신할지는 각 host 구현에 달려 있음
- 즉 새 스펙이 tool contract freezing 문제를 해결할 프로토콜 기반은 제공하지만, 실제 동작은 Claude Code / Codex의 구현이 따라줘야 함

#### 현재 상태 요약

- MCP `2026-07-28`: 정식 출시됨
- Codex CLI: 지원 구현 완료, 현재 opt-in
- Claude Code: Modern MCP negotiation 지원이 이미 들어가고 있으며 migration 진행 중
- 기존 MCP 서버: 계속 사용 가능
- 새 Stateless / MRTR 등의 기능: **Client와 Server 양쪽 모두 새 스펙을 지원해야 사용 가능**

## 원문
- [원문](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [GeekNews 토론](https://news.hada.io/topic?id=32492)

## My Note
<!-- 한 줄 코멘트 남기기 -->

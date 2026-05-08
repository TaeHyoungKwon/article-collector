---
collected_at: '2026-05-08T11:03:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29288
id: hada-29288
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- hacks.mozilla.org
title: Claude Mythos Preview로 Firefox를 강화한 비하인드 스토리
url: https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Mozilla는 모델 성능 향상과 **하네스(harness)** 개선으로 AI 생성 보안 보고서의 신호를 높이고 잡음을 줄여, Firefox에서 실제 보안 버그를 대규모로 찾는 파이프라인을 구축함
- Firefox [150 release](https://www.firefox.com/en-US/firefox/150.0/releasenotes/)에서는 **Claude Mythos Preview**가 식별한 271개 버그가 수정됐고, [149.0.2](https://www.firefox.com/en-US/firefox/149.0.2/releasenotes/), [150.0.1](https://www.firefox.com/en-US/firefox/150.0.1/releasenotes/), [150.0.2](https://www.firefox.com/en-US/firefox/150.0.2/releasenotes/)에도 관련 수정이 포함됨
- 공개된 대표 버그에는 JIT의 WebAssembly GC 구조체 초기화 제거로 인한 가짜 객체 원시 기능, IPC 경합 조건을 통한 부모 프로세스 UAF, NaN 역직렬화 문제, XSLT의 20년 된 rehash 버그, `rowspan=0`을 이용한 16비트 레이아웃 bitfield overflow 등이 들어감
- 공개된 버그 상당수는 **샌드박스 탈출**이며, 손상된 콘텐츠 프로세스가 권한 있는 부모 프로세스로 권한을 올리는 상황을 전제로 해 퍼징만으로 찾기 어려운 공격 표면을 AI 분석이 더 포괄적으로 다룸
- Mozilla는 기존 퍼징 인프라 위에 agentic 하네스를 얹어 재현되지 않는 추측을 버리고 테스트케이스로 가설을 검증했으며, 앞으로 패치가 tree에 들어올 때 스캔하도록 **지속적 통합**에 통합할 계획임

---

## AI 모델로 드러난 Firefox 보안 버그의 변화

- 몇 달 전까지만 해도 오픈소스 프로젝트에 들어오는 AI 생성 보안 버그 보고서는 그럴듯하지만 틀린 경우가 많아 유지보수자에게 **비대칭 비용**을 만들었음
- Firefox에서는 짧은 기간 동안 상황이 크게 바뀌었고, 모델 성능 향상과 모델을 **하네스(harness)** 로 조종·확장·결합해 신호를 늘리고 잡음을 걸러내는 기법 개선이 핵심 이유였음
- Mozilla는 보통 보안 권고와 수정 배포 후에도 상세 버그 보고서를 몇 달간 비공개로 유지하지만, 이번에는 생태계 전반의 긴급성과 관심을 고려해 일부 보고서를 공개하기로 결정함
- 공개된 보고서는 브라우저 여러 하위 시스템에서 고른 것이며 선정은 어느 정도 임의적이지만, 보고서의 깊이와 다양성은 방어자들이 이 기법을 적용해야 할 필요성을 보여줌

## 공개된 대표 버그

- [2024918](https://bugzilla.mozilla.org/show_bug.cgi?id=2024918)
  - 잘못된 동등성 검사 때문에 JIT가 살아 있는 WebAssembly GC 구조체 초기화를 최적화로 제거했고, 내부·외부 연구자의 광범위한 퍼징을 거친 코드에서 잠재적 임의 읽기·쓰기와 연결되는 **가짜 객체 원시 기능**을 만들 수 있었음
- [2024437](https://bugzilla.mozilla.org/show_bug.cgi?id=2024437)
  - `<legend>` 요소의 15년 된 버그로, 재귀 스택 깊이 제한, expando 속성, cycle collection 등 브라우저의 서로 떨어진 영역에 있는 엣지 케이스를 정교하게 조합해 유발됨
- [2021894](https://bugzilla.mozilla.org/show_bug.cgi?id=2021894)
  - IPC 경합 조건을 안정적으로 악용해 손상된 콘텐츠 프로세스가 부모 프로세스의 IndexedDB 참조 카운트를 조작하고, UAF와 잠재적 **샌드박스 탈출**을 일으킬 수 있었음
- [2022034](https://bugzilla.mozilla.org/show_bug.cgi?id=2022034)
  - 원시 NaN이 IPC 경계를 넘으며 태그된 JS 객체 포인터처럼 보일 수 있어, double 역직렬화가 부모 프로세스 가짜 객체 원시 기능과 샌드박스 탈출로 이어질 수 있었음
- [2024653](https://bugzilla.mozilla.org/show_bug.cgi?id=2024653)
  - 중첩 이벤트 루프, `pagehide` 리스너, 가비지 컬렉션을 엮은 복잡한 테스트케이스로 `<object>` 요소의 속성 setter에서 UAF를 유발함
- [2022733](https://bugzilla.mozilla.org/show_bug.cgi?id=2022733)
  - WebTransport에 수천 개의 인증서 해시를 밀어 넣어 참조 카운트가 많은 복사 루프의 경합 조건을 늘리고, 손상된 콘텐츠 프로세스에서 IPC를 통해 부모 UAF를 유발함
- [2023958](https://bugzilla.mozilla.org/show_bug.cgi?id=2023958)
  - glibc DNS 함수 호출을 가로채 악성 DNS 서버를 시뮬레이션하고, UDP에서 TCP로 넘어가는 fallback 엣지 케이스를 재현해 HTTPS RR 및 ECH 파싱 중 버퍼 초과 읽기와 부모 프로세스 스택 메모리 누수를 유발함
- [2025977](https://bugzilla.mozilla.org/show_bug.cgi?id=2025977)
  - 재진입 `key()` 호출이 해시 테이블 rehash를 일으켜 backing store를 해제하지만 원시 엔트리 포인터가 계속 사용되는 20년 된 XSLT 버그였으며, 수정된 여러 sec-high XSLT 문제 중 하나였음
- [2027298](https://bugzilla.mozilla.org/show_bug.cgi?id=2027298)
  - 컬러 피커를 패치해 자동화하기 어려운 사용자 선택을 시뮬레이션한 뒤, 동기 입력 이벤트로 중첩 이벤트 루프를 돌려 actor teardown에 재진입하고 callback이 풀리는 중 해제되게 해 콘텐츠 프로세스 UAF를 유발함
- [2023817](https://bugzilla.mozilla.org/show_bug.cgi?id=2023817)
  - 손상된 콘텐츠 프로세스가 임의의 배경화면 이미지를 부모 프로세스에서 디코딩하도록 보낼 수 있었고, 가상의 이미지 디코더 취약점과 결합하면 샌드박스 탈출로 이어질 수 있었음
  - 부모 프로세스에서 입력의 신뢰 수준을 판단하는 자동화하기 어려운 추론이 필요했음
- [2029813](https://bugzilla.mozilla.org/show_bug.cgi?id=2029813)
  - Firefox 95의 세밀한 샌드박싱 기술인 [RLBox](https://blog.mozilla.org/attack-and-defense/2021/12/06/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/)에서, 신뢰할 수 없는 쪽에서 신뢰하는 쪽으로 값을 복사하는 검증 로직의 틈을 이용해 샌드박스를 우회함
- [2026305](https://bugzilla.mozilla.org/show_bug.cgi?id=2026305)
  - HTML 테이블의 특수한 `rowspan=0` 의미를 이용하는 매우 작은 테스트케이스로, `>65535`개 행을 추가해 clamping을 우회하고 16비트 레이아웃 bitfield를 overflow했으며 수년간 퍼저에 잡히지 않았음

## 샌드박스 탈출과 방어 계층

- 공개된 버그 중 상당수는 **샌드박스 탈출**이며, Firefox 전체 체인 침해로 이어지려면 다른 익스플로잇과 결합되어야 함
- 이런 보고서는 사이트 콘텐츠를 렌더링하는 샌드박스 프로세스가 별도 버그로 이미 손상되어 있고, 공격자 제어 기계어 코드가 권한 있는 부모 프로세스로 권한을 올리려는 상황을 전제로 함
- 샌드박스 탈출을 만들 때 모델은 수정된 코드가 샌드박스 프로세스 안에서만 실행되는 한 Firefox 소스 코드를 패치할 수 있음
- 이 유형의 버그는 퍼징으로 찾기 어렵고, Mozilla는 [스냅샷을 이용한 IPC 퍼징](https://blog.mozilla.org/attack-and-defense/2024/06/24/ipc-fuzzing-with-snapshots/) 같은 기법을 개발해 왔지만, AI 분석이 이 중요한 표면을 훨씬 포괄적으로 다룰 수 있었음
- 모델이 찾지 못한 부분도 중요했음
  - 최근 몇 년간 보안 연구자들은 권한 있는 부모 프로세스에서 prototype pollution을 유발해 프로세스 샌드박스를 탈출하는 보고서를 여러 건 보냈음
  - Mozilla는 문제를 하나씩 고치는 대신, 기본적으로 prototype을 freeze하는 [아키텍처 변경](https://bugzilla.mozilla.org/show_bug.cgi?id=1771084)을 적용함
  - 하네스 로그에서는 이 탈출 경로를 시도했지만 설계로 막힌 흔적이 많이 보였고, 이전 강화 작업의 직접적인 효과가 확인됨

## 하네스로 보안 강화 파이프라인 구축

- Mozilla는 지난 몇 년간 GPT 4나 Sonnet 3.5 같은 모델로 고위험 코드를 정적 분석하는 LLM 코드 감사 실험을 내부에서 진행했음
- 초기 실험은 가능성을 보였지만, **거짓 양성** 비율이 높아 규모를 키우기 어려웠음
- 보안 문제를 안정적으로 감지하는 agentic 하네스의 등장으로 상황이 바뀜
  - 실제 버그를 찾을 수 있음
  - 재현되지 않는 추측을 버릴 수 있음
  - 적절한 인터페이스와 지시가 있으면 재현 가능한 테스트케이스를 만들고 실행해 코드 버그 가설을 동적으로 검증할 수 있음
- Mozilla는 2월 [Anthropic이 보낸](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/) 초기 이슈를 수정한 뒤, [기존 퍼징 인프라](https://hacks.mozilla.org/2021/02/browser-fuzzing-at-mozilla/) 위에 자체 하네스를 구축함
- 초기에는 Claude Opus 4.6으로 샌드박스 탈출을 찾도록 작은 규모의 실험을 시작했음
  - 이 모델만으로도 멀티프로세스 브라우저 엔진 코드에 대한 복잡한 추론이 필요한, 이전에 알려지지 않은 취약점을 상당수 식별함
  - 처음에는 터미널에서 과정을 직접 지켜보며 실시간으로 프롬프트와 로직을 조정함
  - 작동이 안정된 뒤에는 여러 ephemeral VM으로 작업을 병렬화하고, 각 VM이 특정 대상 파일에서 버그를 찾은 뒤 결과를 bucket에 기록하도록 함
- 발견 하위 시스템만으로는 충분하지 않았음
  - 무엇을 찾을지, 어디를 볼지, 결과물을 어떻게 처리할지를 포함해 전체 **보안 버그 수명주기**와 통합해야 했음
  - 기존 이슈와의 중복 제거, 버그 추적, triage, 수정 배포까지 포함됨
  - 모델은 하네스를 움직이는 핵심 원시 요소지만, 규모 있게 유용하게 만들려면 전체 파이프라인이 필요함
- 하네스는 프로젝트 간 재사용 가능성이 있지만, 파이프라인은 코드베이스의 의미, 도구, 프로세스에 따라 프로젝트별로 달라짐
- Firefox 엔지니어들이 들어오는 버그를 처리하는 과정과 밀접한 피드백 루프를 두고 상당한 반복 작업이 필요했음

## Claude Mythos Preview와 모델 교체 효과

- 엔드투엔드 파이프라인이 갖춰지면 새 모델이 나올 때 다른 모델로 바꾸는 일은 간단해짐
- Mozilla는 공개 모델로도 여러 심각한 버그를 찾았고, 이 파이프라인 덕분에 Claude Mythos Preview 평가 기회를 얻었을 때 바로 활용할 수 있었음
- 모델 업그레이드는 파이프라인 전체의 효과를 높였음
  - 잠재 버그를 더 잘 찾음
  - 버그를 입증하는 개념증명 테스트케이스를 더 잘 만듦
  - 병리와 영향을 더 잘 정리함
- Firefox [150 release](https://www.firefox.com/en-US/firefox/150.0/releasenotes/)에서 Claude Mythos Preview가 식별한 271개 버그를 수정한 것 외에도, [149.0.2](https://www.firefox.com/en-US/firefox/149.0.2/releasenotes/), [150.0.1](https://www.firefox.com/en-US/firefox/150.0.1/releasenotes/), [150.0.2](https://www.firefox.com/en-US/firefox/150.0.2/releasenotes/)에도 관련 수정이 포함됨
- 내부적으로는 다른 방법으로도 버그를 계속 찾고 있으며, 다른 프로젝트들과 비슷하게 최근 몇 달간 외부 보고도 크게 늘었음
- 모든 버그는 제대로 고치려면 세심한 주의가 필요했고, 전례 없는 규모를 따라잡기 위해 지난 몇 달간 많은 작업과 긴 근무가 이어졌음
- 100명 넘는 사람이 가장 안전한 Firefox를 배포하기 위한 코드 기여에 참여했으며, 패치 작성·리뷰 외에도 파이프라인 구축·확장, triage, 수정 테스트, 각 버그의 릴리스 프로세스 관리가 함께 이루어졌음

## 핵심 교훈

- 소프트웨어를 만드는 누구나 지금 현대적 모델과 하네스를 사용해 버그를 찾고 코드를 강화할 수 있음
- 간단한 프롬프트에서 시작해 관찰하고 반복할 수 있음
  - 초기 프롬프트는 [이 영상](https://youtu.be/1sd26pWhfmg?si=tRU14Bpc4MwTeMAT&t=316)에 나온 방식과 크게 다르지 않았음
  - 반복을 거치며 파이프라인 최적화와 확장을 위한 orchestration과 도구가 많이 추가됐지만, 내부 루프의 핵심은 “이 코드 부분에 버그가 있으니 찾아서 테스트케이스를 만들어라”였음
- Firefox의 잠재 버그를 모두 바닥낸 상태는 아니지만, 현재 궤적에는 만족하고 있음
- 현재 스캔은 대체로 사람의 판단과 자동 신호를 섞어 지정한 특정 코드 영역, 즉 파일과 함수에 집중됨
- 가까운 미래에는 이 분석을 지속적 통합 시스템에 통합해 패치가 tree에 들어올 때 스캔할 계획임
- 모델은 제공되는 문맥 형식에 유연하게 대응하며, 패치 기반 스캔이 파일 기반 스캔만큼 또는 그보다 더 잘 작동할 것으로 예상됨
- 현재 시점은 위험하지만 기회도 크며, 인터넷을 안전하게 만들기 위해 함께 움직여야 함

## 자주 묻는 질문

- ### “271개 버그”와 보안 권고 숫자가 다른 이유

  - [보안 권고 웹페이지](https://www.mozilla.org/en-US/security/advisories/mfsa2026-30/#CVE-2026-6784)에서는 내부 보고 버그를 여러 개의 버그가 아래에 묶인 “rollup” CVE로 그룹화함
  - 웹페이지는 CVE 할당의 정식 위치인 [foundation-security-advisories](https://github.com/mozilla/foundation-security-advisories) 저장소의 [yaml](https://github.com/mozilla/foundation-security-advisories/blob/dcb9392460ff2026f02ca45d37142c4cad17eb83/announce/2026/mfsa2026-30.yml#L236-L262)에서 만들어짐
  - 일부 브라우저는 내부 발견 이슈에 CVE 식별자를 만들지 않지만, Mozilla는 가능한 투명하게 정보를 제공하기 위해 이를 공개함
  - Firefox 150에는 내부 rollup이 3개 있었음
    - CVE-2026-6784: 154개 버그
    - CVE-2026-6785: 55개 버그
    - CVE-2026-6786: 107개 버그
  - 세 내부 rollup의 합은 316개로, Claude Mythos Preview로 찾았다고 발표한 271개보다 많음
  - 이유는 Mozilla 보안팀이 매일 Firefox를 공격하며 새 버그를 찾고, 그 방법이 퍼징 시스템, 수동 검사, 여러 모델을 활용한 새로운 agentic 파이프라인의 조합이기 때문임
  - 4월 릴리스에서 총 423개의 보안 버그가 수정됨
    - 2주 전 발표한 271개 버그
    - 외부 보고 버그 41개
    - 나머지 111개는 내부 발견이며 대략 세 부류로 나뉨
      - Claude Mythos Preview를 사용한 이 파이프라인으로 찾았지만 Firefox 150이 아닌 다른 릴리스에서 수정된 버그
      - 다른 모델을 사용한 이 파이프라인으로 찾은 버그
      - 퍼징 같은 다른 기법으로 찾은 버그
  - Anthropic에는 이번 최신 작업과 별개로 CVE 3개가 직접 크레딧됨
    - CVE-2026-6746
    - CVE-2026-6757
    - CVE-2026-6758
  - 이들은 몇 달 전 Anthropic Frontier Red Team이 [Mozilla에 보낸](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/) 버그 수정이며, 일반 절차에 따라 각각 고유 CVE가 할당됨
- ### 보안 심각도 등급의 의미

  - Mozilla는 버그의 긴급도를 나타내기 위해 [security severity ratings](https://wiki.mozilla.org/Security_Severity_Ratings/Client)를 critical부터 low까지 적용함
  - sec-critical과 sec-high는 웹페이지 방문 같은 일반 사용자 행동으로 유발될 수 있는 취약점에 부여됨
  - sec-critical과 sec-high 사이에 기술적 차이는 없지만, sec-critical은 공개적으로 공개됐거나 실제 공격에 악용된 것으로 알려진 이슈에만 사용됨
  - sec-moderate는 원래 sec-high로 평가될 취약점이지만 피해자에게 비정상적이고 복잡한 단계가 필요한 경우에 부여됨
  - sec-low는 안전한 crash처럼 사용자 피해와 거리가 먼 성가신 버그에 부여됨
  - Firefox 150에서 발표한 271개 버그의 등급은 다음과 같음
    - sec-high 180개
    - sec-moderate 80개
    - sec-low 11개
  - Mozilla는 critical/high 버그를 가장 중요하게 보지만, 정확성 문제 수정과 심층 방어를 위해 moderate와 low 보안 버그도 우선순위에 올리는 것이 일반적임
- ### sec-high 또는 sec-critical과 실제 익스플로잇의 차이

  - sec-high 또는 sec-critical 버그가 곧 실용적 익스플로잇이라는 뜻은 아님
  - 대부분의 경우 하나의 critical/high 버그만으로 Firefox를 침해하기에는 충분하지 않음
  - Firefox는 심층 방어 아키텍처를 갖고 있어, 예를 들어 JIT 버그를 악용해도 샌드박스되고 사이트별로 분리된 프로세스에서 원격 코드 실행을 얻는 수준임
  - 실제 공격자는 일반적으로 여러 익스플로잇을 체인으로 묶어 하나 이상의 샌드박싱 계층과 ASLR 같은 OS 수준 완화를 거쳐 권한을 올려야 함
  - Mozilla는 일반적으로 버그가 실제 공격자에게 사용될 수 있는지 확인하기 위해 익스플로잇을 만들지 않음
  - sec-high 분류는 AddressSanitizer가 보고하는 use-after-free나 out-of-bounds 메모리 문제 같은 예측 가능한 crash 증상에 기반함
  - 위협 모델은 충분한 노력이 있으면 이런 버그가 악용 가능할 수 있다고 가정함
  - 이 방식은 악용 가능성 분석에서 거짓 음성 위험을 줄이고, 더 많은 취약점을 찾고 고치는 데 자원을 집중하게 해줌

## 원문
- [원문](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)
- [GeekNews 토론](https://news.hada.io/topic?id=29288)

## My Note
<!-- 한 줄 코멘트 남기기 -->

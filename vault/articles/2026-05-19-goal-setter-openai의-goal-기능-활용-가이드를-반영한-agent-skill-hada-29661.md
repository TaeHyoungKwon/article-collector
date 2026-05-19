---
category: AI
collected_at: '2026-05-19T23:34:35+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29661
id: hada-29661
matched_keywords:
- AI
- Codex
read: false
recommend_score: 4.693
recommended_on: '2026-05-19'
source: geeknews
tags:
- AI
- Other
- github.com/computerphilosopher
title: 'goal-setter: OpenAI의 goal 기능 활용 가이드를 반영한 agent skill'
url: https://github.com/computerphilosopher/agent-skills/blob/main/skills/goal-setter/SKILL.md
---

## TL;DR
- 이 글은 OpenAI의 Codex의 Goal 기능을 활용하여 목표 설정을 효율화하는 Agent Skill인 Goal Setter에 대해 설명한다.
- Goal Setter는 사용자의 요구 사항을 조사하여 명확한 목표를 만들고 이를 바탕으로 실행 가능한 마크다운 파일을 생성한다.
- 잘 정의된 목표 설정은 에이전트의 수행 비용을 절감하고 프로젝트 관리의 효율성을 높이는 데 기여할 수 있다.

## GeekNews 요약
Codex에 Goal 기능이 생기면서 긴 작업을 끝날 때까지 계속 맡길 수 있게 됐습니다. 다만 Goal은 조금만 의도가 어긋나도 토큰과 시간이 크게 낭비될 수 있습니다.

Goal Setter는 goal을 작성하기 위해 필요한 요소를 사용자와의 인터뷰를 통해 확인합니다.

- 정확히 어떤 상태가 완료인지
- 하지 말아야 할 일은 무엇인지
- 성공 여부를 어떤 evidence로 판단할지
- 막혔을 때 어디서 멈추고 무엇을 보고해야 하는지

인터뷰에서 확인할 내용은 OpenAI에서 발표한 사용 팁을 기반으로, Codex의 skill-creator 스킬을 통해 작성했습니다.  
(참고: <https://news.hada.io/topic?id=29639>)

인터뷰가 끝나면 프로젝트 루트에 `goals/<goal-name>.md` 파일을 생성합니다. 문서 내용이 마음에 들지 않으면 다시 수정을 요구할 수 있습니다.

문서의 내용이 요구사항을 충족하면 생성된 마크다운을 통해 goal을 실행합니다.

```
/goal @goals/<goal-name>.md
```

### 장점

- Goal에 사용할 프롬프트를 OpenAI가 공개한 기준에 맞게 구체적으로 작성할 수 있습니다.
- 에이전트와 리뷰를 반복하면서 마음에 들때까지 수정할 수 있습니다. (Goal은 장시간 많은 토큰을 태우며 실행되기 때문에 프롬프트를 잘 작성하는 것의 이득이 큼)
- Goal의 내용이 파일로 남기 때문에, git에 추가해서 내역 관리를 쉽게 할 수 있습니다.

### 설치 방법

Codex에서 skill-installer 스킬을 사용해 설치할 수 있습니다.

```
Use $skill-installer to install https://github.com/computerphilosopher/agent-skills/…
```

## 원문
- [원문](https://github.com/computerphilosopher/agent-skills/blob/main/skills/goal-setter/SKILL.md)
- [GeekNews 토론](https://news.hada.io/topic?id=29661)

## My Note
<!-- 한 줄 코멘트 남기기 -->

---
category: Other
collected_at: '2026-06-21T23:38:28+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30689
id: hada-30689
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- date-light.flyingsquirrel.me
title: 'Show GN: date-light — 3.11KB TypeScript 날짜 유틸리티 라이브러리'
url: https://date-light.flyingsquirrel.me/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
날짜 라이브러리를 넣고 싶은데, locale/timezone/duration/plugin까지 전부 필요한 건 아닐 때가 있다.

date-light는 이 문제를 푸는 작은 날짜 유틸리티 라이브러리다. 웹/앱에서 자주 쓰는 날짜 작업만 골라서 39개 함수로 제공한다. 런타임 의존성은 없고, TypeScript 타입과 ESM/CJS 엔트리포인트를 포함한다.

```
import { addDays, differenceInDays, format, startOfWeek } from "date-light";  
  
const launch = new Date(2026, 5, 30, 14, 30);  
const reminder = addDays(launch, -7);  
  
format(launch, "yyyy-MM-dd HH:mm"); // "2026-06-30 14:30"  
format(startOfWeek(launch), "yyyy-MM-dd"); // "2026-06-29"  
differenceInDays(launch, reminder); // 7
```

#### 무엇을 제공하는지

format, parseISO, parse

addDays, addMonths, addYears, addHours, subDays, subMonths...

differenceInDays, differenceInMonths, differenceInYears

isBefore, isAfter, isEqual, isSameDay, isSameMonth

isWeekend, isLeapYear, isValid, getDaysInMonth

startOfDay, endOfWeek, startOfMonth, endOfYear 등

입력 Date는 변경하지 않는다. 모든 함수는 새 Date를 반환하거나 값을 계산한다.

#### 왜 만들었는지

대부분의 앱은 날짜 라이브러리의 아주 작은 부분만 쓴다.

날짜를 포맷하고, ISO 문자열을 파싱하고, 며칠 더하고, 두 날짜 차이를 구하고, 주/월/년의 시작과 끝으로 맞추는 정도다.

date-light는 이 범위만 작게 가져가자는 쪽이다. date-fns와 비슷한 사용감을 유지하되, 자주 쓰는 유틸만 묶었다.

#### 의도적으로 없는 것

locale, timezone DB, duration 객체, 플러그인, 체이닝 API는 없다.

이런 기능이 필요하면 Intl, Temporal, Luxon, date-fns가 더 맞다. date-light는 일반적인 앱 날짜 처리만 작게 가져가고 싶을 때 쓰는 도구다.

#### 크기

39개 함수 기준 약 3.11KB minzipped.

문서의 번들 사이즈 비교 기준으로는 date-fns에서 비슷한 20개 함수를 가져오는 경우보다 약 5.9배 작다.

> GitHub: <https://github.com/flyingsquirrel0419/date-light>  
> npm: npm install date-light  
> docs/playground: <https://date-light.flyingsquirrel.me/>

## 원문
- [원문](https://date-light.flyingsquirrel.me/)
- [GeekNews 토론](https://news.hada.io/topic?id=30689)

## My Note
<!-- 한 줄 코멘트 남기기 -->

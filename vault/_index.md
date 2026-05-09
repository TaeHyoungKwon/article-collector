---
title: Articles Index
tags: [_meta]
---
********
# 📚 Articles Index

> Dataview plugin이 설치돼 있어야 카테고리별 표가 보입니다.
> Settings → Community plugins → Browse → "Dataview" 설치 후 활성화.

## 추천된 글 (최근순)

```dataview
TABLE WITHOUT ID
  file.link AS "Title",
  category,
  recommend_score,
  recommended_on,
  read
FROM "articles"
WHERE recommended_on != null
SORT recommended_on DESC, recommend_score DESC
```

## 카테고리별

### AI

```dataview
TABLE WITHOUT ID
  file.link AS "Title",
  recommend_score,
  geeknews_score,
  recommended_on,
  read
FROM "articles"
WHERE category = "AI"
SORT recommend_score DESC
```

### Dev Tools

```dataview
TABLE WITHOUT ID
  file.link AS "Title",
  recommend_score,
  geeknews_score,
  recommended_on,
  read
FROM "articles"
WHERE category = "Dev Tools"
SORT recommend_score DESC
```

### Backend

```dataview
TABLE WITHOUT ID
  file.link AS "Title",
  recommend_score,
  geeknews_score,
  recommended_on,
  read
FROM "articles"
WHERE category = "Backend"
SORT recommend_score DESC
```

### Other

```dataview
TABLE WITHOUT ID
  file.link AS "Title",
  recommend_score,
  geeknews_score,
  recommended_on,
  read
FROM "articles"
WHERE category = "Other"
SORT recommend_score DESC
```

## 아직 안 읽은 추천 글

```dataview
TABLE WITHOUT ID
  file.link AS "Title",
  category,
  recommended_on
FROM "articles"
WHERE recommended_on != null AND read = false
SORT recommended_on DESC
```

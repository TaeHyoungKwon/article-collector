---
category: Other
collected_at: '2026-08-17T09:30:03+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32568
id: hada-32568
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/TheRealYT
title: git-knife - Git 커밋 메타데이터를 표처럼 편집하는 데스크톱 GUI
url: https://github.com/TheRealYT/git-knife
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Git 커밋의 **메시지, 작성자/커미터 이름·이메일, 작성일/커밋일**을 표 형태 GUI에서 직접 수정하는 도구
- GitKraken/Sublime Merge/Fork 같은 GUI는 reword/reorder는 잘 지원하지만 **임의 커밋의 날짜나 committer 정보 변경**은 제한적이며,  
  이를 지원하는 `git-filter-repo`나 `git commit-tree`는 CLI 중심이라는 틈을 겨냥함
- Git 자체를 재구현하지 않고 시스템의 `git` CLI와 `git commit-tree`를 사용해 커밋을 다시 생성함
  - 기존 커밋의 tree를 그대로 재사용하기 때문에 히스토리를 수정해도 **파일 내용 자체는 변경하지 않음**
- 저장소를 열고 원하는 로컬 브랜치를 checkout하지 않은 채 ref로 직접 편집하므로 **현재 working tree를 건드리지 않음**
- 여러 커밋의 메시지/이름/이메일을 한꺼번에 바꾸는 **Bulk Find & Replace**를 지원하며 일반 문자열과 Regex 모두 사용 가능
  - 오래된 이메일 주소를 전체 히스토리에서 새 주소로 교체하는 식의 작업에 활용 가능
- 실제 적용 전에 모든 변경 사항을 old → new 형태로 미리 확인할 수 있고, 이미 원격에 push된 히스토리를 건드리면 별도 경고를 표시
- 변경 적용 전마다 `refs/knife-backup/...`에 **자동 백업 ref**를 생성해 GUI에서 원클릭 복구하거나 Git CLI로 되돌릴 수 있음
- Signed Commit도 감지해 히스토리 재작성으로 **GPG/SSH 서명이 사라질 커밋을 경고**하고, 설정된 키를 이용해 다시 서명하는 옵션을 제공
- git-knife 자체는 **로컬 브랜치만 수정하며 remote에 접속하거나 push하지 않음**. 재작성한 히스토리의 push는 사용자가 직접 수행해야 함
- 기존에 push된 커밋을 변경하면 이후 모든 커밋 hash도 달라지므로 `git push --force-with-lease`가 필요하며, **공유된 히스토리 재작성할때는 팀원과 조율 필요**
- 현재 MVP에서는 non-merge commit만 편집할 수 있으며 **reorder/squash/drop, merge commit 재작성, staging/branch/remote 관리**는 아직 지원하지 않음
- Tauri v2 기반 데스크톱 앱으로 맥/윈도우/리눅스 지원

## 원문
- [원문](https://github.com/TheRealYT/git-knife)
- [GeekNews 토론](https://news.hada.io/topic?id=32568)

## My Note
<!-- 한 줄 코멘트 남기기 -->

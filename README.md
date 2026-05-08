# article-collector

태형님 학습용 아티클 수집/추천 파이프라인.

매일 아침 GeekNews RSS를 수집해 LLM 3줄 요약을 붙이고, Obsidian vault(`vault/`)에 markdown으로 저장한 뒤, 키워드/점수 기반 top 10을 Gmail로 발송한다. 읽고 `## My Note`에 코멘트를 남기면 다음날 추천 알고리즘이 그 시그널을 학습한다.

## 구성

```
src/        # 파이프라인 코드 (Python)
vault/      # Obsidian vault root (articles/ 안에 글 저장)
.github/    # 매일 아침 cron 워크플로
tests/      # pytest
```

## 핵심 결정

- 소스: GeekNews (https://news.hada.io/rss). 이후 확장.
- 요약: GeekNews 자체 한국어 요약 보존 + 최상단에 GitHub Models(`openai/gpt-4o-mini`) 3줄 요약.
- 본문: 외부 원문 본문은 수집하지 않음 (요약만).
- 추천 점수 v0: GeekNews 점수 + 매칭 키워드 + 다양성 - 중복 페널티.
- 학습 시그널: frontmatter `read: true` 또는 `## My Note` 섹션 비어있지 않음.

## 실행 환경

GitHub Actions cron — UTC 23:00 (KST 08:00). 코드와 vault가 같은 repo에 있어 워크플로가 vault를 직접 commit & push한다.

## 로컬에서 한 번 돌리기

```bash
# 1. 의존성 설치 (uv 필수)
uv sync

# 2. 환경변수 준비
cp .env.example .env
# .env 열어서 GITHUB_MODELS_TOKEN, GMAIL_*, OBSIDIAN_VAULT_NAME 채우기

# 3. dry-run (메일 발송 없이 dryrun_mail.html만 생성, 비용·시간 검증용)
uv run python -m src.main --dry-run -v

# 4. 실제 실행 (메일까지 발송)
uv run python -m src.main -v

# 테스트
uv run pytest -v
```

## Gmail 앱 비밀번호 발급

1. Google 계정에 2단계 인증을 켠다 — https://myaccount.google.com/security
2. 앱 비밀번호 페이지로 이동 — https://myaccount.google.com/apppasswords
3. 앱 이름 임의로(예: `article-collector`) 입력 → 생성된 16자 비밀번호를 `GMAIL_APP_PASSWORD`에 넣는다.

> 일반 계정 비밀번호로는 SMTP 로그인이 안 된다 (Google이 차단함).

## Obsidian 연동

1. Obsidian을 열고 vault 폴더로 이 repo의 `vault/`를 추가한다.
2. 추가 시 부여한 vault 이름(예: `articles-vault`)을 `OBSIDIAN_VAULT_NAME`에 적는다.
3. 메일에 `obsidian://open?vault=...&file=articles/...md` 링크가 포함되며, 클릭하면 해당 노트가 바로 열린다.
4. **Dataview plugin 설치**: Settings → Community plugins → Browse → `Dataview` 검색 → Install → Enable.
   - 활성화 후 `vault/_index.md` 노트를 열면 카테고리별 표 + "추천된 글" + "아직 안 읽은 추천 글" 표가 자동으로 채워진다.
   - 인덱스는 매 실행마다 자동 갱신되므로 직접 편집할 필요 없음.

## GitHub 운영 (cron)

워크플로(`.github/workflows/daily.yml`)가 KST 08:00에 자동 실행된다. 동작에 필요한 secret을
**Settings → Secrets and variables → Actions**에 등록한다:

| Secret | 필수 | 설명 |
|---|---|---|
| `GMAIL_USER` | ✓ | 발신/수신 Gmail 주소 |
| `GMAIL_APP_PASSWORD` | ✓ | 위에서 발급한 16자 앱 비밀번호 |
| `RECIPIENT_EMAIL` | ✗ | 미지정 시 GMAIL_USER로 자기 자신에게 발송 |
| `OBSIDIAN_VAULT_NAME` | ✗ | 메일에 obsidian://open 링크 추가 |
| `KEYWORDS` | ✗ | 콤마 구분 키워드 override |

> LLM 요약은 GitHub Models를 사용하며, Actions에서는 워크플로 자체에 부여된
> `GITHUB_TOKEN` (with `permissions: models: read`)을 그대로 활용한다 —
> 별도 secret 등록 불필요.

수동 실행: **Actions → daily-collect → Run workflow** (체크박스로 dry-run 가능).

## KPI

`src/feedback.py`가 매 실행 종료 시 다음 지표를 로깅한다.

- **read_rate** = 읽은 글 / 추천된 글
- **comment_rate_among_read** = 코멘트 남긴 글 / 읽은 글  ← 핵심 KPI
- **keyword_lift(kw)** = 그 키워드 글의 engagement 비율 (가중치 튜닝의 입력)

## 추천 알고리즘 튜닝

`src/score.py`의 상수를 조정하면 된다.

```python
KEYWORD_WEIGHT = 2.0
GEEKNEWS_SCORE_WEIGHT = 1.0
COMMENT_WEIGHT = 0.3
ALREADY_RECOMMENDED_PENALTY = 1000.0
```

시그널이 충분히 쌓이면(예: 추천 누적 200건 이상) feedback 데이터를 입력으로 키워드별 가중치를 자동 학습하는 v1으로 진화시킬 예정.

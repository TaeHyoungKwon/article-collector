from __future__ import annotations

import logging
import os
import smtplib
import urllib.parse
from collections.abc import Iterable
from datetime import date
from email.message import EmailMessage

from jinja2 import Environment, select_autoescape

from src.models import Article

logger = logging.getLogger(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head><meta charset="utf-8"><title>오늘의 아티클</title></head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
             max-width:680px;margin:0 auto;padding:24px;color:#222;line-height:1.55;">
  <h1 style="font-size:20px;border-bottom:1px solid #eee;padding-bottom:8px;">
    오늘의 아티클 추천 — {{ on_date }}
  </h1>
  <p style="color:#666;font-size:13px;">
    GeekNews 기반 top {{ articles|length }}. 읽고 Obsidian의 <code>## My Note</code>에 한 줄 남겨주세요.
  </p>
  {% for a in articles %}
  <div style="margin:24px 0;padding:16px;border:1px solid #e5e5e5;border-radius:8px;">
    <div style="font-size:12px;color:#888;margin-bottom:6px;">
      #{{ loop.index }}
      {% if a.matched_keywords %}· {{ a.matched_keywords | join(', ') }}{% endif %}
      {% if a.tags %}· {{ a.tags | join(', ') }}{% endif %}
      · GN점수 {{ a.geeknews_score }} · 댓글 {{ a.geeknews_comments }}
      · 추천점수 {{ a.recommend_score }}
    </div>
    <a href="{{ a.url }}" style="font-size:17px;font-weight:600;color:#0a58ca;text-decoration:none;">
      {{ a.title }}
    </a>
    {% if a.tldr %}
    <ul style="margin:12px 0 12px 20px;padding:0;">
      {% for line in a.tldr %}
      <li style="margin-bottom:4px;">{{ line }}</li>
      {% endfor %}
    </ul>
    {% endif %}
    <div style="font-size:12px;color:#888;">
      <a href="{{ a.geeknews_url }}" style="color:#666;">GeekNews 토론</a>
      {% if obsidian_uri_for(a) %}
      · <a href="{{ obsidian_uri_for(a) }}" style="color:#666;">Obsidian에서 열기</a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
  <p style="color:#aaa;font-size:11px;margin-top:32px;">
    article-collector · 자동 발송
  </p>
</body>
</html>
"""


def render_email_html(
    articles: Iterable[Article],
    on_date: date,
    obsidian_vault_name: str | None = None,
) -> str:
    env = Environment(autoescape=select_autoescape(["html", "xml"]))
    template = env.from_string(EMAIL_TEMPLATE)

    def obsidian_uri_for(a: Article) -> str:
        if not obsidian_vault_name:
            return ""
        params = urllib.parse.urlencode(
            {"vault": obsidian_vault_name, "file": f"articles/{a.filename()}"}
        )
        return f"obsidian://open?{params}"

    return template.render(
        articles=list(articles),
        on_date=on_date.isoformat(),
        obsidian_uri_for=obsidian_uri_for,
    )


def send_email(
    subject: str,
    html_body: str,
    to_addr: str | None = None,
    from_addr: str | None = None,
    app_password: str | None = None,
) -> None:
    user = (from_addr or os.environ["GMAIL_USER"]).strip()
    # Gmail displays app passwords as "xxxx xxxx xxxx xxxx" — users often paste
    # them with regular or non-breaking spaces. Strip every whitespace char
    # (str.split() catches NBSP \xa0 too) so SMTP auth doesn't choke.
    raw_password = app_password or os.environ["GMAIL_APP_PASSWORD"]
    password = "".join(raw_password.split())
    recipient = (to_addr or os.environ.get("RECIPIENT_EMAIL") or user).strip()

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = recipient
    msg.set_content("HTML 메일 클라이언트로 열어주세요.")
    msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)
    logger.info("email sent to %s (subject=%r)", recipient, subject)

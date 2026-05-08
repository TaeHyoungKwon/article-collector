from __future__ import annotations

import argparse
import logging
import os
import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

from src.fetch import fetch_articles
from src.feedback import collect_feedback
from src.mailer import render_email_html, send_email
from src.score import configured_keywords, mark_recommended, score_articles, top_n
from src.summarize import summarize_articles
from src.vault import existing_ids, iter_articles, save_article

logger = logging.getLogger("article_collector")


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    _configure_logging(args.verbose)
    load_dotenv()

    repo_root = Path(__file__).resolve().parent.parent
    vault_root = repo_root / "vault"
    today = date.today()

    logger.info("article-collector run on %s (vault=%s, dry_run=%s)", today, vault_root, args.dry_run)

    seen = existing_ids(vault_root)
    logger.info("vault already has %d articles", len(seen))

    new_articles = fetch_articles(skip_ids=seen)
    logger.info("fetched %d new articles", len(new_articles))

    # Save new articles immediately without TL;DR — we only spend LLM calls on the
    # articles that survive ranking, not all 50 fetched (rate-limit + cost friendly).
    if new_articles:
        for a in new_articles:
            save_article(a, vault_root)
        logger.info("saved %d new articles to vault (no LLM yet)", len(new_articles))

    if args.collect_only:
        logger.info("collect-only mode: skipping score/summarize/mail")
        return 0

    all_articles = list(iter_articles(vault_root))
    logger.info("scoring %d total articles", len(all_articles))
    score_articles(all_articles, keywords=configured_keywords())

    selection = top_n(all_articles, n=args.top_n)
    logger.info(
        "top %d selected (scores: %s)",
        len(selection),
        [a.recommend_score for a in selection],
    )

    if not selection:
        logger.warning("no articles to recommend; exiting")
        return 0

    # Only summarize the articles we're actually going to recommend.
    needs_tldr = [a for a in selection if not a.tldr]
    if needs_tldr:
        logger.info("summarizing %d selected articles via GitHub Models", len(needs_tldr))
        summarize_articles(needs_tldr)

    html = render_email_html(
        selection,
        today,
        obsidian_vault_name=os.environ.get("OBSIDIAN_VAULT_NAME"),
    )
    subject = f"오늘의 아티클 추천 — {today.isoformat()}"

    if args.dry_run:
        out = repo_root / "dryrun_mail.html"
        out.write_text(html, encoding="utf-8")
        logger.info("dry-run: HTML written to %s (no email sent)", out)
    else:
        send_email(subject, html)

    mark_recommended(selection, today)
    for a in selection:
        save_article(a, vault_root)

    report = collect_feedback(vault_root)
    logger.info(
        "KPI snapshot — recommended=%d, read=%d, commented=%d, comment_rate=%.0f%%",
        report.total_recommended,
        report.total_read,
        report.total_commented,
        report.comment_rate_among_read * 100,
    )
    return 0


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="article-collector daily pipeline")
    p.add_argument("--dry-run", action="store_true", help="render mail to file, skip SMTP")
    p.add_argument(
        "--collect-only",
        action="store_true",
        help="fetch + save new articles only (no scoring, no LLM, no email)",
    )
    p.add_argument("--top-n", type=int, default=10, help="how many articles to recommend (default: 10)")
    p.add_argument("-v", "--verbose", action="store_true", help="DEBUG level logging")
    return p.parse_args(argv)


def _configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == "__main__":
    sys.exit(main())

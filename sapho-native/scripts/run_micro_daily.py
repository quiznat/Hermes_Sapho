from __future__ import annotations

import argparse
from typing import Any

from common import (
    ARTICLES_DIR,
    article_artifact_publication_current,
    article_file,
    article_ready_for_pm_on_date,
    assert_unique_canonical_records,
    daily_dir,
    load_article_records,
    read_markdown,
    timestamp_for_date,
    write_article_markdown,
)
from micro_common import (
    bullet_lines,
    clean_loose_text,
    daily_stage_path,
    package_markdown,
    parse_pass_block,
    read_job,
    run_loose_agent,
    summary_section,
    summary_title,
)

DEFAULT_CLUSTER_SIZE = 4
DEFAULT_CLUSTER_TIMEOUT_SECONDS = 300
DEFAULT_DAILY_SYNTHESIS_TIMEOUT_SECONDS = 1800
DEFAULT_DAILY_GATE_TIMEOUT_SECONDS = 600


def ready_articles_for_date(replay_date: str) -> list[tuple[dict, str]]:
    items: list[tuple[dict, str]] = []
    for article_path in sorted(ARTICLES_DIR.glob("*/article.md")):
        meta, body = read_markdown(article_path)
        if not article_ready_for_pm_on_date(meta, replay_date):
            continue
        items.append((meta, body))
    return items


def article_ledger(items: list[tuple[dict, str]]) -> str:
    lines: list[str] = []
    for meta, body in items:
        title = summary_title(body, meta.get("source_title") or meta["article_id"])
        thesis = summary_section(body, "Core Thesis")
        why = summary_section(body, "Why It Matters")
        key_findings = bullet_lines(summary_section(body, "Key Findings"))
        lines.append(f"- {title}")
        if thesis:
            lines.append(f"  Thesis: {thesis}")
        if why:
            lines.append(f"  Why: {why}")
        for finding in key_findings[:2]:
            lines.append(f"  Finding: {finding}")
    return "\n".join(lines)


def chunked(items: list[tuple[dict[str, Any], str]], size: int) -> list[list[tuple[dict[str, Any], str]]]:
    if size <= 0:
        raise ValueError("invalid_cluster_size")
    return [items[idx : idx + size] for idx in range(0, len(items), size)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-date", required=True)
    parser.add_argument("--synthesist-agent", default="synthesist")
    parser.add_argument("--cluster-size", type=int, default=DEFAULT_CLUSTER_SIZE)
    parser.add_argument("--cluster-timeout", type=int, default=DEFAULT_CLUSTER_TIMEOUT_SECONDS)
    parser.add_argument("--daily-timeout", type=int, default=DEFAULT_DAILY_SYNTHESIS_TIMEOUT_SECONDS)
    parser.add_argument("--gate-timeout", type=int, default=DEFAULT_DAILY_GATE_TIMEOUT_SECONDS)
    # Conclave is a gate, not a configured OpenClaw persona id in this runtime.
    # Execute the gate as an orchestrator review job.
    parser.add_argument("--conclave-agent", default="orchestrator")
    args = parser.parse_args()

    items = ready_articles_for_date(args.replay_date)
    if not items:
        raise ValueError("no_ready_articles_for_date")
    ready_ids = {str(meta.get("article_id") or "").strip() for meta, _body in items}
    publication_records = [
        record
        for record in load_article_records()
        if str(record.get("publication_status") or "") == "published" or str(record.get("article_id") or "") in ready_ids
    ]
    assert_unique_canonical_records(publication_records, context=f"micro-daily:{args.replay_date}")

    day_dir = daily_dir(args.replay_date)
    day_dir.mkdir(parents=True, exist_ok=True)
    clusters = chunked(items, args.cluster_size)
    cluster_notes: list[str] = []
    for index, cluster_items in enumerate(clusters, start=1):
        cluster_prompt = (
            f"{read_job('daily-cluster.md')}\n\n"
            f"Replay date: {args.replay_date}\n"
            f"Cluster: {index}/{len(clusters)}\n"
            f"Article count: {len(cluster_items)}\n\n"
            "Article ledger:\n\n"
            f"{article_ledger(cluster_items)}\n"
        )
        cluster_text = run_loose_agent(
            args.synthesist_agent,
            cluster_prompt,
            timeout=args.cluster_timeout,
            thinking="off",
        )
        daily_stage_path(args.replay_date, f"cluster-{index:02d}").write_text(
            clean_loose_text(cluster_text) + "\n",
            encoding="utf-8",
        )
        cluster_notes.append(clean_loose_text(cluster_text))

    cluster_dossier = "\n\n".join(
        f"### Cluster {index}\n\n{note}" for index, note in enumerate(cluster_notes, start=1)
    )

    technical_prompt = (
        f"{read_job('daily-technical.md')}\n\n"
        f"Replay date: {args.replay_date}\n"
        f"Article count: {len(items)}\n\n"
        f"Cluster count: {len(cluster_notes)}\n\n"
        "Cluster notes:\n\n"
        f"{cluster_dossier}\n"
    )
    technical_text = run_loose_agent(args.synthesist_agent, technical_prompt, timeout=args.daily_timeout, thinking="off")
    daily_stage_path(args.replay_date, "technical").write_text(clean_loose_text(technical_text) + "\n", encoding="utf-8")

    executive_prompt = (
        f"{read_job('daily-executive.md')}\n\n"
        f"Replay date: {args.replay_date}\n"
        f"Article count: {len(items)}\n\n"
        f"Cluster count: {len(cluster_notes)}\n\n"
        "Cluster notes:\n\n"
        f"{cluster_dossier}\n"
    )
    executive_text = run_loose_agent(args.synthesist_agent, executive_prompt, timeout=args.daily_timeout, thinking="off")
    daily_stage_path(args.replay_date, "executive").write_text(clean_loose_text(executive_text) + "\n", encoding="utf-8")

    gate_prompt = (
        f"{read_job('conclave-gate.md')}\n\n"
        f"Replay date: {args.replay_date}\n"
        f"Article count: {len(items)}\n\n"
        "Technical Daily:\n\n"
        f"{clean_loose_text(technical_text)}\n\n"
        "Executive Brief:\n\n"
        f"{clean_loose_text(executive_text)}\n"
    )
    gate_text = run_loose_agent(args.conclave_agent, gate_prompt, timeout=args.gate_timeout, thinking="off")
    daily_stage_path(args.replay_date, "conclave", ".txt").write_text(clean_loose_text(gate_text) + "\n", encoding="utf-8")
    verdict, _rationale = parse_pass_block(gate_text)

    generated_at = timestamp_for_date(args.replay_date)
    technical_body = clean_loose_text(technical_text)
    executive_body = clean_loose_text(executive_text)
    package_markdown(
        {
            "version": "technical-executive-report.v1",
            "date": args.replay_date,
            "generated_at_utc": generated_at,
            "mode": "agent",
            "status": "published" if verdict == "pass" else "blocked",
        },
        technical_body,
        day_dir / "technical-executive-report.md",
    )
    package_markdown(
        {
            "version": "executive-brief.v1",
            "date": args.replay_date,
            "generated_at_utc": generated_at,
            "mode": "agent",
            "status": "published" if verdict == "pass" else "blocked",
        },
        executive_body,
        day_dir / "executive-brief.md",
    )
    package_markdown(
        {
            "version": "daily.v1",
            "date": args.replay_date,
            "generated_at_utc": generated_at,
            "mode": "agent",
            "status": "published" if verdict == "pass" else "blocked",
        },
        technical_body,
        day_dir / "daily.md",
    )
    package_markdown(
        {
            "version": "conclave.v1",
            "date": args.replay_date,
            "generated_at_utc": generated_at,
            "verdict": verdict,
            "mode": "agent",
        },
        clean_loose_text(gate_text),
        day_dir / "conclave.md",
    )
    publish_body = (
        "# Publish Receipt\n\n"
        f"- date: {args.replay_date}\n"
        f"- verdict: {verdict}\n"
        f"- article_count: {len(items)}\n"
    )
    package_markdown(
        {
            "version": "publish-receipt.v1",
            "date": args.replay_date,
            "published_at_utc": generated_at,
            "verdict": verdict,
            "article_count": len(items),
        },
        publish_body,
        day_dir / "publish.md",
    )

    if verdict != "pass":
        raise RuntimeError("conclave_blocked")

    for meta, body in items:
        article_meta, article_body = read_markdown(article_file(meta["article_id"]))
        if not article_artifact_publication_current(article_meta):
            raise RuntimeError(f"artifact_not_published:{meta['article_id']}")
        article_meta["publication_status"] = "published"
        article_meta["published_in_daily"] = args.replay_date
        write_article_markdown(article_file(meta["article_id"]), article_meta, article_body)

    from render_site import render_site as _render_site
    _render_site()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

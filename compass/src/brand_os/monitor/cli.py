"""Monitor CLI commands."""
from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from brand_os.cli_utils import emit

monitor_app = typer.Typer(help="Brand monitoring commands.")
console = Console()


@monitor_app.command("report")
def report(
    brand: str = typer.Option(..., "--brand", "-b", help="Brand name"),
    period: str = typer.Option("7d", "--period", "-p", help="Time period"),
    send: bool = typer.Option(False, "--send", help="Send via email"),
    to: list[str] = typer.Option([], "--to", "-t", help="Email recipients"),
    output: Path | None = typer.Option(None, "--output", "-o", help="Output file"),
    format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown, html, json, yaml"),
) -> None:
    """Generate a brand report."""
    from brand_os.monitor.emailer import send_report
    from brand_os.monitor.reports import (
        format_report_html,
        format_report_markdown,
        generate_report,
    )

    console.print(f"Generating report for {brand} (period: {period})...")

    report_obj = generate_report(brand, period=period)

    if send and to:
        result = send_report(report_obj, to=to)
        if result.get("success"):
            console.print(f"[green]Report sent to: {', '.join(to)}[/green]")
        else:
            console.print(f"[red]Failed to send: {result.get('error')}[/red]")

    # Format output
    if format == "markdown":
        formatted = format_report_markdown(report_obj)
    elif format == "html":
        formatted = format_report_html(report_obj)
    elif format in ("json", "yaml"):
        if output:
            output.write_text(emit(report_obj.model_dump(), format))
            console.print(f"Report saved to: {output}")
            return
        else:
            emit(report_obj.model_dump(), format)
            return
    else:
        formatted = format_report_markdown(report_obj)

    if output:
        output.write_text(formatted)
        console.print(f"Report saved to: {output}")
    else:
        console.print(formatted)


@monitor_app.command("analyze")
def analyze(
    brand: str = typer.Option(..., "--brand", "-b", help="Brand name"),
    period: str = typer.Option("7d", "--period", "-p", help="Time period"),
    format: str = typer.Option("table", "--format", "-f", help="Output format"),
) -> None:
    """Analyze brand signals and performance."""
    from brand_os.signals.history import get_signal_count, query_signals
    from brand_os.signals.relevance import filter_signals
    from brand_os.core.brands import load_brand_config

    config = load_brand_config(brand)
    signals = query_signals(brand, since=period, limit=200)

    console.print(f"[bold]Signal Analysis for {brand}[/bold]")
    console.print(f"Period: {period}")
    console.print(f"Total signals in history: {get_signal_count(brand)}")
    console.print(f"Signals in period: {len(signals)}")

    # Filter relevant signals
    relevant = filter_signals(
        signals,
        keywords=config.get("keywords", []),
        competitors=config.get("competitors", []),
        min_score=0.3,
    )

    console.print(f"Relevant signals: {len(relevant)}")

    if relevant:
        console.print("\n[bold]Top Signals:[/bold]")
        for signal in relevant[:10]:
            score = signal.get("relevance_score", 0)
            headline = signal.get("headline", signal.get("title", ""))[:60]
            console.print(f"  [{score:.2f}] {headline}")

    # Try to load learnings
    try:
        from brand_os.eval.learnings import get_learnings
        learnings = get_learnings(brand)
        if learnings:
            console.print("\n[bold]Content Learnings:[/bold]")
            for dim in learnings.get("weak_dimensions", [])[:3]:
                console.print(f"  - Weak: {dim}")
            for rec in learnings.get("recommendations", [])[:3]:
                console.print(f"  - Rec: {rec}")
    except Exception:
        pass

    # Queue status
    try:
        from brand_os.publish.queue import get_queue
        pending = len(get_queue(brand, status="pending"))
        posted = len(get_queue(brand, status="posted"))
        console.print(f"\n[bold]Content Queue:[/bold]")
        console.print(f"  Pending: {pending}")
        console.print(f"  Posted: {posted}")
    except Exception:
        pass

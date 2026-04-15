"""Signals CLI commands."""
from __future__ import annotations

import typer
from rich.console import Console

from brand_os.cli_utils import emit

signals_app = typer.Typer(help="Signal monitoring commands.")
console = Console()


@signals_app.command("fetch")
def fetch(
    brand: str = typer.Option(..., "--brand", "-b", help="Brand name"),
    source: str = typer.Option("google_news", "--source", "-s", help="Signal source"),
    query: str | None = typer.Option(None, "--query", "-q", help="Custom search query"),
    limit: int = typer.Option(20, "--limit", "-l", help="Max signals to fetch"),
    save: bool = typer.Option(True, "--save/--no-save", help="Save to history"),
    format: str = typer.Option("json", "--format", "-f", help="Output format"),
) -> None:
    """Fetch signals from a source."""
    from brand_os.core.brands import load_brand_config
    from brand_os.signals.history import append_signals
    from brand_os.signals.providers.google_news import fetch_google_news

    config = load_brand_config(brand)

    # Build query from brand keywords if not provided
    if not query:
        keywords = config.get("keywords", [])
        name = config.get("name", brand)
        query = f"{name} OR " + " OR ".join(keywords[:5]) if keywords else name

    console.print(f"Fetching signals for: {query}")

    if source == "google_news":
        signals = fetch_google_news(query, limit=limit)
    else:
        console.print(f"[red]Unknown source: {source}[/red]")
        raise typer.Exit(1)

    console.print(f"Found {len(signals)} signals")

    if save and signals:
        count = append_signals(brand, signals)
        console.print(f"Saved {count} new signals to history")

    emit(signals, format)


@signals_app.command("filter")
def filter_cmd(
    brand: str = typer.Option(..., "--brand", "-b", help="Brand name"),
    min_score: float = typer.Option(0.1, "--min-score", "-m", help="Minimum relevance score"),
    format: str = typer.Option("json", "--format", "-f", help="Output format"),
) -> None:
    """Filter signals by relevance."""
    from brand_os.core.brands import load_brand_config
    from brand_os.signals.history import query_signals
    from brand_os.signals.relevance import filter_signals

    config = load_brand_config(brand)

    # Get recent signals
    signals = query_signals(brand, limit=200)
    console.print(f"Loaded {len(signals)} signals from history")

    # Filter by relevance
    filtered = filter_signals(
        signals,
        keywords=config.get("keywords", []),
        competitors=config.get("competitors", []),
        stop_phrases=config.get("stop_phrases", []),
        min_score=min_score,
    )

    console.print(f"Filtered to {len(filtered)} relevant signals")

    emit(filtered, format)


@signals_app.command("history")
def history(
    brand: str = typer.Option(..., "--brand", "-b", help="Brand name"),
    query: str | None = typer.Option(None, "--query", "-q", help="Search query"),
    since: str | None = typer.Option(None, "--since", "-s", help="Date filter (ISO or '7d')"),
    limit: int = typer.Option(50, "--limit", "-l", help="Max results"),
    format: str = typer.Option("json", "--format", "-f", help="Output format"),
) -> None:
    """Query signal history."""
    from brand_os.signals.history import get_signal_count, query_signals

    total = get_signal_count(brand)
    console.print(f"Total signals in history: {total}")

    signals = query_signals(brand, query=query, since=since, limit=limit)
    console.print(f"Returning {len(signals)} signals")

    emit(signals, format)


@signals_app.command("discover-subreddits")
def discover_subreddits(
    query: str | None = typer.Option(None, "--query", "-q", help="Search query"),
    brand: str | None = typer.Option(None, "--brand", "-b", help="Discover for brand"),
    industry: str | None = typer.Option(None, "--industry", "-i", help="Industry/sector"),
    limit: int = typer.Option(15, "--limit", "-l", help="Max results"),
) -> None:
    """Discover relevant subreddits.

    Examples:
        agentcy-compass signals discover-subreddits --query "AI startup"
        agentcy-compass signals discover-subreddits --brand acme
        agentcy-compass signals discover-subreddits --industry "B2B SaaS" --query "automation"
    """
    from rich.table import Table
    from brand_os.signals.sources.reddit_discover import SubredditDiscovery

    discovery = SubredditDiscovery()

    if brand:
        # Load brand config and discover
        from brand_os.core.config import load_brand_config
        config = load_brand_config(brand) or {}

        console.print(f"[bold]Discovering subreddits for brand: {brand}[/bold]\n")

        results = discovery.discover_for_brand(
            brand_name=config.get("name", brand),
            industry=industry or config.get("industry"),
            keywords=config.get("keywords", []),
            target_audience=config.get("target_audience"),
            use_llm=True,
        )
    elif query:
        console.print(f"[bold]Searching subreddits for: {query}[/bold]\n")
        results = discovery.search(query, limit=limit)
    elif industry:
        console.print(f"[bold]Searching subreddits for industry: {industry}[/bold]\n")
        results = discovery.search(industry, limit=limit)
    else:
        console.print("[red]Provide --query, --brand, or --industry[/red]")
        raise typer.Exit(1)

    if not results:
        console.print("[yellow]No subreddits found[/yellow]")
        return

    table = Table(title=f"Discovered Subreddits ({len(results)})")
    table.add_column("Subreddit", style="cyan")
    table.add_column("Subscribers", justify="right")
    table.add_column("Active", justify="right")
    table.add_column("Score", justify="right")
    table.add_column("Description")

    for sub in results[:limit]:
        table.add_row(
            f"r/{sub.name}",
            f"{sub.subscribers:,}",
            f"{sub.active_users:,}" if sub.active_users else "-",
            f"{sub.relevance_score:.2f}" if sub.relevance_score else "-",
            (sub.description or sub.title)[:50] + "..." if len(sub.description or sub.title) > 50 else (sub.description or sub.title),
        )

    console.print(table)

    # Show as YAML for easy copy to brand.yml
    console.print("\n[dim]Add to brand.yml:[/dim]")
    console.print("subreddits:")
    for sub in results[:10]:
        console.print(f"  - {sub.name}")

"""agentcy — dispatcher CLI.

Each subcommand delegates to its member binary via subprocess,
passing all arguments through verbatim. JSON output, exit codes,
and signals are forwarded unchanged.

Pipeline:
    agentcy vox export <persona> --to voice-pack.v1 --json
    agentcy compass plan --brand <id> --json
    agentcy echo run --files docs/ --brief brief.v1.json --json
    agentcy loom run social.post --brand <id> --json
    agentcy pulse adapt --run-result run.json --sidecar s.json --json
    agentcy pulse calibrate --forecast f.json --performance p.json
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="agentcy",
    help="Agent CLI suite — vox | compass | echo | loom | pulse",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()
err = Console(stderr=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run(bin_name: str, args: list[str]) -> None:
    """Resolve bin, exec, forward exit code."""
    resolved = shutil.which(bin_name)
    if not resolved:
        err.print(f"[red]error:[/red] '{bin_name}' not found — run: uv sync --all-extras")
        raise typer.Exit(2)
    result = subprocess.run([resolved, *args])
    raise typer.Exit(result.returncode)


def _loom_bin() -> str | None:
    """Resolve the loom entry point.

    Priority:
    1. agentcy-loom in PATH (global install)
    2. loom/runtime/bin/loom.js relative to monorepo root (local dev)
    """
    if found := shutil.which("agentcy-loom"):
        return found
    root = Path(__file__).parent.parent.parent  # src/agentcy/cli.py → agentcy root
    local = root / "loom" / "runtime" / "bin" / "loom.js"
    if local.exists():
        return str(local)
    return None


def _loom_command(args: list[str]) -> list[str]:
    node = shutil.which("node")
    if not node:
        err.print("[red]error:[/red] 'node' not found — install Node.js")
        raise typer.Exit(2)

    bin_path = _loom_bin()
    if not bin_path:
        err.print("[red]error:[/red] loom not found — run: cd loom/runtime && pnpm install")
        raise typer.Exit(2)

    if bin_path.endswith(".js"):
        return [node, bin_path, *args]
    return [bin_path, *args]


def _run_node(args: list[str]) -> None:
    """Invoke loom via its packaged command or local JS entry point."""
    result = subprocess.run(_loom_command(args))
    raise typer.Exit(result.returncode)


def _probe_member(command: list[str]) -> bool:
    """Return True when a lightweight health probe exits successfully."""
    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


# ---------------------------------------------------------------------------
# Subcommands — each is a transparent pass-through
# ---------------------------------------------------------------------------

_PASS = {"allow_extra_args": True, "ignore_unknown_options": True}


@app.command(
    "vox",
    context_settings=_PASS,
    help="Persona management — create, test, optimize, export",
)
def vox(ctx: typer.Context) -> None:
    _run("agentcy-vox", ctx.args)


@app.command(
    "compass",
    context_settings=_PASS,
    help="Brand ops — signals, planning, production, loop",
)
def compass(ctx: typer.Context) -> None:
    _run("agentcy-compass", ctx.args)


@app.command(
    "echo",
    context_settings=_PASS,
    help="Swarm prediction — docs + requirement → forecast",
)
def echo(ctx: typer.Context) -> None:
    _run("agentcy-echo", ctx.args)


@app.command(
    "loom",
    context_settings=_PASS,
    help="Comms runtime — brief → draft → render → publish",
)
def loom(ctx: typer.Context) -> None:
    _run_node(ctx.args)


@app.command(
    "pulse",
    context_settings=_PASS,
    help="Measurement + calibration — run_result → performance",
)
def pulse(ctx: typer.Context) -> None:
    _run("agentcy-pulse", ctx.args)


# ---------------------------------------------------------------------------
# doctor — check all members are installed and reachable
# ---------------------------------------------------------------------------

@app.command("doctor")
def doctor(
    json_out: Annotated[bool, typer.Option("--json", help="Machine-readable output")] = False,
) -> None:
    """Check that all member CLIs are installed and healthy."""
    node = shutil.which("node")
    members = [
        ("vox", "agentcy-vox", "python", ["agentcy-vox", "--version"]),
        ("compass", "agentcy-compass", "python", ["agentcy-compass", "--help"]),
        ("echo", "agentcy-echo", "python", ["agentcy-echo", "--help"]),
        ("loom", "agentcy-loom", "node", None),
        ("pulse", "agentcy-pulse", "python", ["agentcy-pulse", "doctor"]),
    ]

    results: dict[str, dict] = {}
    all_ok = True

    for name, bin_name, runtime, probe_command in members:
        if runtime == "node":
            resolved = _loom_bin()
            found = resolved is not None and node is not None
            reachable = found and _probe_member(_loom_command(["help", "--json"]))
        else:
            resolved = shutil.which(bin_name)
            found = resolved is not None
            reachable = (
                found
                and probe_command is not None
                and _probe_member([resolved, *probe_command[1:]])
            )

        if not found or not reachable:
            all_ok = False
        results[name] = {
            "bin": bin_name,
            "found": found,
            "reachable": reachable,
            "runtime": runtime,
        }

    if json_out:
        print(json.dumps({
            "status": "ok" if all_ok else "error",
            "command": "doctor",
            "data": results,
        }))
        raise typer.Exit(0 if all_ok else 1)

    table = Table(title="agentcy doctor")
    table.add_column("member")
    table.add_column("bin")
    table.add_column("status")
    for name, info in results.items():
        if not info["found"]:
            status = "[red]missing[/red]"
        elif info["reachable"]:
            status = "[green]ok[/green]"
        else:
            status = "[yellow]broken[/yellow]"
        table.add_row(name, info["bin"], status)
    console.print(table)
    raise typer.Exit(0 if all_ok else 1)


# ---------------------------------------------------------------------------
# version
# ---------------------------------------------------------------------------

@app.command("version")
def version() -> None:
    """Print suite version."""
    from agentcy import __version__
    console.print(f"agentcy {__version__}")

# Tool Stack Consolidation Plan

## Architecture

```
cli-prsna → brand-os → cli-phantom → cli-metrics
(voice)     (strategy)  (execute/publish)  (measure/retrain)
```

| Tool | Role | Status |
|---|---|---|
| cli-prsna | Voice/persona layer — drift detection, fidelity scores, versioned personas | Complete, standalone |
| brand-os | Strategy + governance — signals, briefs, policy gating, audit trail | Merge cli-agency in |
| cli-phantom | Execution + publishing — render, adapt, publish, resumable runs | Production, daily use |
| cli-metrics | Analytics feedback — platform engagement, performance → learning tracker | Missing, needs building |

---

## cli-agency → brand-os (merge)

Absorb cli-agency into brand-os. Both Python, same stack (Typer, Pydantic, uv).

**What moves in:**
- `agency/stages/` → `brand-os/pipeline/` (research, strategy, creative, activation)
- `agency/core/llm.py` → consolidate with brand-os LLM interface
- `agency/core/mcp.py` → hold, add later if needed
- `agency/schemas/` → merge with brand-os Pydantic models

**What gets dropped:**
- `agency/plugins/` (social/SEO) — phantom does this better
- `agency/core/store.py` (JSON persistence) — brand-os uses SQLite
- MCP server — not needed yet, add later when phantom needs programmatic calls

**brand-os after merge:**
```
brand-os/
├── core/        # policy engine, decision log, learning tracker (unchanged)
├── signals/     # RSS/Reddit ingestion (unchanged)
├── pipeline/    # cli-agency stages land here
├── brands/      # YAML configs (unchanged)
└── cli.py       # unified CLI
```

**Archive:** cli-agency

---

## cli-prsna integration (no merge, contract only)

cli-prsna stays standalone. Define one export contract:

- `prsna export --format phantom` → voice config consumed by brand.yml
- phantom uses prsna persona as copy generation constraints
- prsna learning loop ingests phantom published post outcomes to detect voice drift

---

## brand-os → cli-phantom contract

**brand-os outputs:** `brief.json`
```json
{
  "brand": "...",
  "signal": { "source": "...", "content": "..." },
  "strategy": { "angle": "...", "cta": "...", "platforms": [] },
  "policy": { "verdict": "approved|escalate|deny", "confidence": 0.0 },
  "creative": { "copy": "...", "tone": "..." }
}
```

**cli-phantom outputs:** `run.json` (outcome fed back to brand-os decision log)
```json
{
  "run_id": "...",
  "brief_id": "...",
  "status": "published|failed|skipped",
  "platforms": [],
  "published_at": "..."
}
```

This feedback loop powers brand-os's learning tracker — approval rates, confidence calibration, auto-tuning.

---

## What each needs before shippable

**brand-os:**
- [ ] Merge cli-agency pipeline stages
- [ ] Define and output brief.json schema
- [ ] At least one working execution handler (currently all stubbed)

**cli-phantom:**
- [ ] Accept brief.json as input (currently drafts from brand.yml only)
- [ ] Write run.json outcome for brand-os to ingest
- [ ] blog.post and outreach workflows (beyond social.post)

**cli-prsna:**
- [ ] `prsna export --format phantom` command
- [ ] Document voice config schema

**Shared:**
- [ ] Document brief.json and run.json schemas
- [ ] One example brand config working across all three
- [ ] Setup guide covering the full stack

---

## Open source framing

**brand-os** — brand strategy + governance layer. Audience: developers, brand strategists.

**cli-phantom** — brand communications runtime. Audience: operators running daily publishing.

**cli-prsna** — persona engineering toolkit. Audience: developers building AI agents with consistent voice.

Together: a self-improving brand publishing system with human-set guardrails. Three focused tools, clean interfaces, not one monolith.

---

## Missing: cli-metrics (analytics feedback)

The learning loop in brand-os is blind without performance data. Currently calibrates on human approvals only — weak signal.

**What it does:**
- Pulls engagement data from platforms (Twitter, LinkedIn, Instagram) after publish
- Maps performance back to the brief that generated the content
- Feeds results into brand-os learning tracker (impressions, clicks, reach, follows)
- Detects what works — voice, angle, platform, timing — and surfaces tuning recommendations
- Feeds drift signals back to cli-prsna (is the persona performing?)

**The loop it closes:**
```
publish → measure → retrain prsna persona → better strategy → better content
```

Without it: `signal → strategy → publish → silence`

**Gap severity:**

| Gap | Severity |
|---|---|
| Analytics feedback (cli-metrics) | Critical — learning tracker blind without it |
| Scheduler/trigger | Medium — brand-os loop daemon exists but stubbed |
| Multi-brand management | Medium — needed for productization |
| Web UI | Low — CLI fine for personal use |

**What it needs:**
- [ ] Platform API integrations (Twitter analytics, LinkedIn insights)
- [ ] Map post ID → brief_id via phantom's run.json
- [ ] Write performance.json consumed by brand-os learning tracker
- [ ] Drift signal export for cli-prsna

---

## What to archive

- `cli-agency/` — absorbed into brand-os
- `brand-os/produce/`, `brand-os/publish/`, `brand-os/persona/`, `brand-os/eval/`, `brand-os/intel/` — shells, replaced by pipeline/ merge

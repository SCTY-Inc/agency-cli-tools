# agentcy recap

Date: 2026-04-20

Note: literal repo directory renames to the `agentcy-*` names landed on 2026-04-12. Historical mentions of `cli-prsna`, `brand-os`, `cli-mirofish`, `cli-phantom`, and `cli-metrics` below refer to former directory names unless explicitly called out.

Current live note (2026-04-20): the active monorepo members are `protocols`, `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-pulse`. Earlier planning references to a separate `agentcy-lab` are now superseded by the live `agentcy-pulse` calibration/study surfaces. The root `agentcy` operator layer now exposes `doctor`, `pipeline run`, `pipeline update`, and `pipeline study`; preview bundles land in module-first folders, can use stable names via `--pipeline-id`, and record honest preview-only Pulse state instead of pretending canonical `performance.v1` exists.

## Goal

Unify the current repo family into a clearer modular system that can be used:
- standalone
- chained together by file/protocol handoffs
- optionally bundled later

The goal is **not** to merge everything into one monolith.

## Chosen family names

Current target family in lowercase kebab-case:

- `agentcy-protocols`
- `agentcy-vox`
- `agentcy-compass`
- `agentcy-echo`
- `agentcy-loom`
- `agentcy-pulse`

## Current repo directories after rename

- `protocols` (shared schema/example/adapter authority, plus narrow shared JSON/LLM helper utilities)
- `agentcy-vox` (formerly `cli-prsna`)
- `agentcy-compass` (formerly `brand-os`)
- `agentcy-echo` (formerly `cli-mirofish`)
- `agentcy-loom` (formerly `cli-phantom` / Loom runtime)
- `agentcy-pulse` (formerly `cli-metrics`; now also carries the bounded study/calibration work that earlier planning described as `agentcy-lab`)

## Current operator surface

The root dispatcher now acts as the bounded control plane over the canonical module writers:
- `agentcy catalog --json` describes suite/member ownership, install profiles, and positioning metadata in one root envelope
- `agentcy quickstart --profile ... --json` prints the smallest install path for a chosen suite profile
- `agentcy member <member> --json ...` normalizes member responses behind one root envelope even when native member JSON differs
- `agentcy pipeline run --mode preview` writes one module-first bundle under `artifacts/pipelines/<pipeline_id>/`
- `--pipeline-id` allows stable operator folders such as `artifacts/pipelines/givecare-launch-01/`
- root `--provider` / `--model` overrides still forward to members that honor `LLM_PROVIDER` / `CLAUDE_MODEL`, and compatible Compass runs also receive `BRANDOPS_LLM_PROVIDER` / `BRANDOPS_LLM_MODEL`
- preview mode writes `pulse/preview.json` when Loom only produced a dry run, instead of fabricating canonical measurement output

Repo-local operator evidence now includes:
- `agentcy-echo` run-local `eval/run_eval.v1.json` and `logs/llm_telemetry.jsonl`
- auto-written `bundle_manifest.json` and `reports/operator_report.md` at the pipeline root
- clean full Echo CLI exits via the non-interactive `--no-wait` simulation path

## Module roles

### `agentcy-vox`
Persona / tone / drift / voice-pack layer.

Owns:
- personas
- voice rules
- drift checks
- voice learnings

Does not own:
- strategy
- publishing
- analytics

Operator note:
- `agentcy-vox test --difficulty ... --save-report` now writes repo-local eval artifacts under `~/.prsna/evals/`
- `agentcy-vox evals --latest|--compare` reopens those saved reports for operator review without widening canonical protocols

### `agentcy-compass`
Strategy / policy / briefs / decisioning layer.

Owns:
- signals
- policy decisions
- briefs
- approvals/escalations

Does not own:
- final rendering
- publishing runtime
- persona internals

Operator note:
- `agentcy-compass catalog --json` exposes its preferred boundaries machine-readably
- compatible Compass data commands now support both global `--json` preference and `--json-envelope` normalized success envelopes

### `agentcy-echo`
Foresight / scenario simulation / predicted reaction layer.

Owns:
- simulation runs
- forecasts
- scenario artifacts
- snapshots/reports

Does not own:
- canonical strategy
- publishing
- actual performance analytics

### `agentcy-loom`
Execution / render / review / publish runtime.

Owns:
- runs
- artifacts
- review state
- publish outcomes

Does not own:
- strategy
- persona evolution
- analytics

### `agentcy-pulse`
Analytics / attribution / calibration / study layer.

Owns:
- performance snapshots
- attribution records
- performance summaries
- calibration reports
- repo-local study synthesis that can combine canonical artifacts with echo/vox sidecars

Does not own:
- publishing
- strategy authoring
- persona authoring

Historical note: earlier planning used a separate `agentcy-lab` for eval/autoresearch ideas. In the live monorepo, the bounded calibration/study slice currently lives under `agentcy-pulse` instead.

## High-level flow

```text
protocols define the shared contracts

agentcy-vox -> agentcy-compass -> agentcy-echo
                     |                |
                     |                v
                     +------------> agentcy-loom -> agentcy-pulse
                                              ^            |
                                              |------------|
                                               learnings / feedback
```

More concretely:
- `protocols` defines the shared family artifact contracts
- `vox` exports voice constraints
- `compass` creates briefs
- `echo` pressure-tests scenarios/messages and can emit repo-local run-shape eval sidecars
- `loom` executes and publishes from the canonical brief
- `pulse` measures reality and can synthesize repo-local study output from canonical artifacts plus echo/vox sidecars

## Core architecture rules

### 1. Protocol first, not language first
Do **not** start by rewriting everything to TypeScript or Python.

The true unifier should be:
- artifact schemas
- lineage IDs
- CLI conventions
- skills/prompts

### 2. One writer per state object
Each major artifact should have exactly one owner.

Target ownership:
- `voice_pack.v1` -> `agentcy-vox`
- `brief.v1` -> `agentcy-compass`
- `scenario_pack.v1` -> `agentcy-compass` or umbrella orchestration
- `forecast.v1` -> `agentcy-echo`
- `run_result.v1` -> `agentcy-loom`
- `performance.v1` -> `agentcy-pulse`

The literal repo directory rename has now landed.

- repo directories now use the `agentcy-*` names
- older protocol artifacts and historical notes may still carry pre-rename repo identifiers until a deliberate writer-contract normalization pass lands
- `writer.module` remains on the family module name track throughout

### 3. MCP is not the first integration layer
If needed later, MCP should be a facade over the stack.

The first shared thing should be:
- shared protocol
- shared lineage
- shared CLI conventions

### 4. Keep the stack polyglot for now
Recommended default:
- `agentcy-vox` -> Python
- `agentcy-compass` -> Python
- `agentcy-echo` -> Python
- `agentcy-loom` -> TypeScript
- `agentcy-pulse` -> Python
- `protocols` -> schema/docs/adapters, language-agnostic by design

## Important repo-specific observations

### `brand-os` / future `agentcy-compass`
The old consolidation doc is directionally right but stale.

Important reality:
- a lot of `cli-agency` planning logic is already partially mirrored inside `brand-os`
- `brand-os` still overlaps with persona / produce / publish / eval responsibilities
- it needs narrowing, not just more merging

### `cli-mirofish` / future `agentcy-echo`
Best framed as a distinct **foresight** module, not “just another content tool.”

Also note:
- it is heavy
- it is a separate architecture
- it is AGPL-licensed
- that argues for loose coupling, not deep merging

### `cli-phantom` / future `agentcy-loom`
Already closest to the desired agent-friendly runtime surface.

### `cli-prsna` / future `agentcy-vox`
Should stay standalone and own the voice/persona layer.

## Shared artifacts to define next

Minimal target set:
- `voice_pack.v1`
- `brief.v1`
- `scenario_pack.v1`
- `forecast.v1`
- `run_result.v1`
- `performance.v1`

And lineage IDs like:
- `brand_id`
- `voice_pack_id`
- `brief_id`
- `scenario_id`
- `forecast_id`
- `run_id`
- `performance_id`

## What not to do yet

Do **not** do these first:
- massive repo renames
- language rewrites
- one giant umbrella CLI
- MCP-first integration
- a giant extension project
- a monorepo migration
- building a huge board system if this stays one-off

## Practical pi/Codex strategy

Since this may be closer to a one-off / occasional effort, the recommended lightweight setup is:

### Minimal durable artifacts
Create only:
- `AGENTCY_STACK.md`
- `AGENTCY_PROGRESS.md`
- one prompt template like `/continue-agentcy`
- maybe one umbrella skill later

### Lean continuation pattern
Use a bounded session loop:
1. read recap / stack / progress docs
2. pick the next smallest high-value task
3. make one bounded change
4. verify it
5. update progress doc
6. stop at blocker or after 1-3 meaningful deltas

This is more idiomatic than trying to create one giant autonomous loop for a one-off.

## pi packages worth using instead of building everything yourself

The most useful external leverage found during this session:

### `pi-web-access`
GitHub: https://github.com/nicobailon/pi-web-access

Best immediate leverage:
- web search
- content fetching
- GitHub cloning
- PDF / YouTube / video analysis

### `pi-subagents`
GitHub: https://github.com/nicobailon/pi-subagents

Best for:
- delegation
- chains
- parallel repo inspection
- background runs

### `pi-messenger`
GitHub: https://github.com/nicobailon/pi-messenger

Only needed if you want:
- multiple terminals
- multi-agent coordination
- file reservations / worker mesh

### `pi-mcp-adapter`
GitHub: https://github.com/nicobailon/pi-mcp-adapter

Only needed if you already have useful MCP servers to connect.

### Recommended install order
Start with:

```bash
pi install npm:pi-web-access
pi install npm:pi-subagents
```

Then only add if needed:

```bash
pi install npm:pi-messenger
pi install npm:pi-mcp-adapter
```

## Recommended next steps

### Lowest-friction next steps
1. Write `AGENTCY_STACK.md`
2. Write `AGENTCY_PROGRESS.md`
3. Define the six shared artifact names at a doc level
4. Do one vertical slice on paper:
   - `vox -> compass -> echo -> loom -> pulse`

### First real implementation targets
Good first concrete work:
1. make `agentcy-vox` export a real `voice_pack`
2. narrow `agentcy-compass` to briefs/policy/strategy ownership
3. define `brief -> forecast -> run_result` handoff
4. leave `pulse` as a later module

## Suggested restart prompt

When restarting, use something close to:

> Read `AGENTCY_RECAP.md`. Treat the current live monorepo as:
> `protocols`, `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-pulse`.
> Do not propose language rewrites or a monolith. Protocol first.
> Keep canonical schemas narrow, keep richer eval/study data repo-local when possible, and identify the next smallest high-value task to clarify roles, boundaries, or protocol handoffs.

## Session bottom line

The main conclusion of this session:

- the family naming is now clear
- the architecture should stay modular
- the first shared thing should be protocol, not MCP
- the stack should remain polyglot for now
- `agentcy-echo` is a real foresight/simulation layer
- `agentcy-pulse` is the live bounded calibration/study layer; richer eval/study data should stay repo-local unless a canonical seam truly needs widening
- for near-term leverage, use `pi-web-access` + `pi-subagents` instead of building custom infrastructure first

# `agentcy-compass` boundary drift review against `brief.v1` ownership — 2026-04-14

Date: 2026-04-14  
Scope: bounded family review for `task-4`  
Primary repo under review: `agentcy-compass/`  
Supporting source-material repo: `cli-agency/`

## Purpose

This review inspects `agentcy-compass/` as a current family repo and `cli-agency/` as supporting source material only.

It answers five bounded questions:

1. What is the literal repo-directory truth today versus the still-locked historical writer naming?
2. Which over-boundary surfaces still make `agentcy-compass` broader than the future `agentcy-compass` module shape?
3. Which `cli-agency` surfaces should be kept, narrowed, treated as reference-only, or archived?
4. What dirty-state evidence exists right now?
5. What are the next smallest repo-local narrowing or doc-clarification tasks, without reopening merger or rename theater?

## Executive summary

`agentcy-compass/` is the live family repo directory today, but the canonical `brief.v1` writer contract is still intentionally mixed:

```json
{
  "repo": "brand-os",
  "module": "agentcy-compass"
}
```

That mixed writer contract is not the problem by itself. It is already locked by family protocol artifacts and tests.

The real drift problem is boundary drift inside the repo:

- package/import/CLI surfaces still ship as `brand-os` / `brand_os` / `brandos`
- the top-level command tree and source tree still expose broader-than-compass surfaces such as `persona`, `produce`, `eval`, `publish`, `queue`, `monitor`, and `server`
- selective `cli-agency` re-home work is real, but it is partial and should stay framed as narrow planning-source reuse rather than merger authority

`cli-agency/` should therefore remain a support/reference repo, not a second authority for `brief.v1` and not a family root.

## Current truth: repo directory versus writer contract

### Literal repo-directory truth

Current workspace evidence shows:

- family repo directory: `agentcy-compass/`
- supporting repo directory: `cli-agency/`
- `agentcy-compass` has active local changes
- `cli-agency` also has active local changes

Relevant current-surface evidence:

- `agentcy-compass/pyproject.toml` still ships distribution `brand-os`
- `agentcy-compass/pyproject.toml` still ships import root `brand_os`
- `agentcy-compass/pyproject.toml` still exposes installed CLI `brandos`
- `cli-agency/pyproject.toml` still ships distribution `agency`
- `cli-agency/pyproject.toml` still exposes installed CLI `agency`

### Historical writer naming that remains intentionally locked

Canonical family protocol evidence still requires:

- `brief.v1.writer.repo = "brand-os"`
- `brief.v1.writer.module = "agentcy-compass"`

Primary proof:

- `protocols/lineage-rules.md`
- `protocols/examples/brief.v1.rich.json`
- `protocols/tests/test_canonical_writer_module_references.py`
- `agentcy-compass/tests/plan/test_brief_v1.py`

### Conclusion

The repo-directory rename to `agentcy-compass/` has already happened, but the protocol writer contract has not been normalized to the new directory name. That is currently intentional family control-plane behavior, not accidental leakage.

So this task should not treat the writer contract itself as drift to “fix.”

## Dirty-state evidence

### `agentcy-compass`

Observed on 2026-04-14:

```text
## main...origin/main [ahead 11]
 M .gitignore
 M docs/packaged-install-help-proof-2026-04-12.md
 M pyproject.toml
?? docs/cli-surface-proof-2026-04-12.md
?? tests/core/test_cli_surface_compat.py
?? uv.lock
```

Interpretation:

- the repo is in active local motion
- current package/CLI evidence is itself being refined
- any review claim should distinguish current dirty-state proof work from stable historical loop-10 conclusions

### `cli-agency`

Observed on 2026-04-14:

```text
## main...origin/main [ahead 4]
 M .gitignore
 M docs/re-home-candidate-scorecard-2026-04-12.md
?? CODEMAP.md
```

Interpretation:

- this supporting repo also has active local doc/inventory churn
- its classification should still stay narrow because it is not a family module and not the canonical `brief.v1` writer

## `brief.v1` ownership: what is settled versus what is not

### Settled

These points are already settled and should not be reopened in this task:

- `agentcy-compass` is the current family repo directory for the compass module
- canonical `brief.v1` ownership remains with `brand-os` as `writer.repo`
- canonical module identity remains `agentcy-compass` as `writer.module`
- `cli-agency` must not appear as `brief.v1` writer, alternate writer, or protocol authority

### Not settled

These points are still unresolved and are the actual review surface:

- how much of the repo should remain under the current broad `brand-os` CLI/product surface
- which broad repo groups are still outside future compass ownership
- which `cli-agency` planning concepts are still worth referencing versus fully leaving behind
- how to narrate repo-directory truth without implying repo/package/import/CLI/runtime rename readiness

## Main over-boundary surfaces still present in `agentcy-compass`

The biggest issue is not just naming drift. It is that the repo still exposes a broader product boundary than the strategy/policy/briefing layer described in `_agentcy-docs/AGENTCY_RECAP.md`.

## Boundary inventory from current source tree and CLI

Evidence from `agentcy-compass/src/brand_os/cli.py` and the top-level source tree shows the repo still exposes:

- `persona`
- `intel`
- `signals`
- `plan`
- `produce`
- `eval`
- `publish`
- `queue`
- `monitor`
- `loop`
- `decision`
- `policy`
- `learn`
- `brand`
- `config`
- repo-local server/API surfaces under `src/brand_os/server`

Top-level source directories observed now:

- `src/brand_os/persona`
- `src/brand_os/produce`
- `src/brand_os/eval`
- `src/brand_os/publish`
- `src/brand_os/monitor`
- `src/brand_os/server`
- plus the more compass-shaped `signals`, `plan`, `core`, and workflow/decision surfaces

## Boundary classification

| Surface in `agentcy-compass` | Current role | Boundary status | Why it matters |
| --- | --- | --- | --- |
| `plan`, `signals`, `policy`, `decision`, `learn` | Closest to strategy/policy/brief ownership | keep | These are the strongest current evidence for compass-shaped ownership. |
| `persona/` and `persona` CLI | overlaps voice/persona territory | narrow later | This exceeds future compass scope and collides conceptually with `agentcy-vox`. |
| `produce/` | overlaps execution/content generation | narrow later | This leans toward downstream runtime/output ownership rather than pure brief authorship. |
| `eval/` | overlaps shared eval plane and downstream quality checks | narrow later | Evaluation may belong partly in `agentcy-lab` or downstream repo-local seams, not necessarily compass core. |
| `publish/`, `queue/`, `monitor/` | overlaps publish/runtime/ops ownership | narrow later | These are the clearest over-boundary runtime surfaces relative to future `agentcy-compass`. |
| `server/` | broader integration/runtime surface | reference-only until justified | This is not needed to prove canonical `brief.v1` ownership. |
| `brand-os` / `brand_os` / `brandos` package/import/CLI surfaces | naming and operator compatibility surfaces | keep as current truth, do not rewrite here | They are real current surfaces, but this task is about drift classification, not migration execution. |

## Most important over-boundary conclusion

The strongest over-boundary surfaces still present in `agentcy-compass` are:

1. persona-facing surfaces
2. production/evaluation surfaces
3. publish/queue/monitor runtime surfaces
4. server/API surfaces

These are the surfaces that make the repo broader than a clean strategy/policy/briefing module.

They are more important than the mixed writer naming when discussing boundary drift.

## `cli-agency` overlap: what remains useful and how to classify it

`cli-agency` should be treated as supporting source material only.

The strongest bounded value still present in `cli-agency` is the research/strategy seam:

- `agency/schemas/research.py`
- `agency/schemas/strategy.py`
- `agency/stages/research.py`
- `agency/stages/strategy.py`

Those files still provide useful source concepts for:

- research insights
- assumptions
- source provenance
- narrowed competitor context
- positioning
- audience framing
- messaging pillars
- proof points
- risks

The rest of the repo is mostly runtime scaffolding, persistence, plugins, or interactive workflow that should not be re-centered in the family.

## `cli-agency` surface classification

| `cli-agency` surface | Classification | Why |
| --- | --- | --- |
| `agency/schemas/research.py` | keep/narrow | Best current typed source material for research inputs that can strengthen `brief.v1` planning. |
| `agency/schemas/strategy.py` | keep/narrow | Best current typed source material for positioning, audience, pillars, proof, and risks. |
| `agency/stages/research.py` | reference-only | Prompt/flow ideas are useful, but runtime search wiring should not be re-homed wholesale. |
| `agency/stages/strategy.py` | reference-only | Stage framing is useful, but it should remain source material rather than direct authority. |
| `agency/cli.py` non-interactive stage sequencing | reference-only | Helpful for understanding thin pipeline seams, but not a family contract. |
| `agency/schemas/creative.py` and `agency/stages/creative.py` | archive candidate for this boundary question | Too close to downstream content generation, not needed for bounded compass review. |
| `agency/schemas/activation.py` and `agency/stages/activation.py` | archive candidate for this boundary question | Too close to execution/runtime planning rather than canonical brief ownership. |
| `agency/core/store.py` | archive candidate | `.agency/` persistence is implementation detail and not family protocol authority. |
| `agency/core/mcp.py` | archive candidate | Family docs explicitly defer MCP-first integration. |
| `agency/plugins/*` | archive candidate | Plugin/runtime surfaces are not the smallest useful seam for compass narrowing. |
| interactive/session commands and resume flow | archive candidate | Useful locally in `cli-agency`, but not part of bounded family ownership for `brief.v1`. |

## Important nuance on `cli-agency`

This review does not claim `cli-agency` should be deleted. It only classifies its family relevance:

- keep/narrow for a very small research/strategy concept set
- reference-only for prompt/stage framing
- archive candidate relative to Agentcy family ownership for the rest

That keeps `cli-agency` from regaining conceptual authority over `agentcy-compass`.

## Evidence of already-bounded re-home work inside `agentcy-compass`

`agentcy-compass/src/brand_os/plan/stages/strategy.py` already states that it selectively re-homes only the smallest durable strategy concepts from `cli-agency`:

- positioning
- audience framing
- messaging pillars
- proof points
- risks

That is the right posture.

It shows the overlap is currently best understood as:

- narrow concept reuse for planning
- not a broad merger
- not a second writer
- not proof that all `cli-agency` pipeline/runtime surfaces belong in `agentcy-compass`

## Review findings

### Finding 1: current repo truth and writer truth are different, and that is intentional

The directory is `agentcy-compass/`, but canonical `brief.v1` artifacts still use `writer.repo = "brand-os"`. This is a control-plane choice, not necessarily a defect.

### Finding 2: the main drift problem is boundary breadth, not just old names

The repo still exposes several broad operational surfaces beyond strategy/policy/brief authorship. That is the main boundary drift.

### Finding 3: `cli-agency` overlap is now mostly conceptual, not canonical-authority leakage

Current docs and protocol tests already keep `cli-agency` out of canonical `brief.v1` ownership. The remaining overlap is source-material and narrative gravity, not active writer leakage.

### Finding 4: `cli-agency` should remain narrow source material, not merger center

The strongest family-valuable surfaces are still research/strategy schemas and stage ideas. Store, MCP, plugins, interactive state, creative, and activation surfaces should stay out of the bounded compass core.

## Next smallest tasks only

The next acceptable tasks should stay repo-local to `agentcy-compass` or family-doc-local. They should not reopen a broad merge or rename wave.

### Smallest repo-local narrowing tasks

1. **`agentcy-compass` boundary scorecard refresh**  
   Update or add one repo-local scorecard that classifies current top-level command groups and directories as:
   - compass-core
   - over-boundary but tolerated for now
   - likely future handoff/reference-only

2. **CLI scope clarification doc**  
   Add a small doc mapping current `brandos` command groups to future module ownership intent without changing command names or code behavior.

3. **Planning seam proof note**  
   Add a narrow doc that links the existing `plan` stage shapes in `agentcy-compass` to the exact `cli-agency` source concepts they intentionally reuse, so future workers do not over-read the overlap as merger authority.

### Smallest family-doc clarification tasks

4. **Current-directory versus writer-contract note**  
   Add a small clarification to family docs that `agentcy-compass/` is the current repo directory while `brief.v1.writer.repo` remains intentionally locked to `brand-os` until a deliberate writer-contract normalization pass lands.

5. **Historical-source authority note for `cli-agency`**  
   Add or strengthen one cross-link from `CONSOLIDATION.md` or companion docs pointing readers to the newer bounded scorecards whenever they encounter old absorb/merge language.

## Explicit non-recommendations

This review does not recommend:

- renaming package/import/CLI surfaces now
- changing `brief.v1.writer.repo` now
- pulling `agency/core/store.py`, plugin surfaces, or MCP surfaces into `agentcy-compass`
- reopening `cli-agency -> brand-os` as a broad merge branch
- turning this task into runtime rewiring across multiple repos

## Bottom line

`agentcy-compass` already holds the canonical `brief.v1` writer contract at the protocol layer, but it is still broader than future compass ownership at the repo boundary layer.

The key drift to review is therefore:

- not whether `brief.v1` has the right writer contract
- but whether the repo still exposes too many non-compass surfaces

And the right posture toward `cli-agency` is:

- narrow planning-source material: yes
- reference implementation: sometimes
- family root or alternate authority: no
- broad merge target: no

## Citation index

- Control plane: `_agentcy-docs/AGENTCY_RECAP.md`, `_agentcy-docs/AGENTCY_STACK.md`, `_agentcy-docs/AGENTCY_PROGRESS.md`, `_agentcy-docs/CONSOLIDATION.md`
- Prior family evidence: `_agentcy-docs/family-workspace-reality-scan-2026-04-14.md`, `_agentcy-docs/family-naming-writer-protocol-drift-2026-04-14.md`
- `agentcy-compass` repo-local docs: `agentcy-compass/CLAUDE.md`, `agentcy-compass/docs/ownership-scorecard-2026-04-12.md`, `agentcy-compass/docs/rename-blocker-profile-2026-04-12.md`
- `agentcy-compass` source evidence: `agentcy-compass/pyproject.toml`, `agentcy-compass/src/brand_os/cli.py`, `agentcy-compass/src/brand_os/plan/stages/strategy.py`, `agentcy-compass/tests/plan/test_brief_v1.py`
- `cli-agency` repo-local docs: `cli-agency/CLAUDE.md`, `cli-agency/docs/re-home-candidate-scorecard-2026-04-12.md`, `cli-agency/docs/historical-ownership-authority-collisions-2026-04-12.md`
- `cli-agency` source evidence: `cli-agency/pyproject.toml`, `cli-agency/agency/schemas/research.py`, `cli-agency/agency/schemas/strategy.py`, `cli-agency/agency/stages/research.py`, `cli-agency/agency/stages/strategy.py`
- Protocol ownership proof: `protocols/lineage-rules.md`, `protocols/examples/brief.v1.rich.json`, `protocols/tests/test_canonical_writer_module_references.py`

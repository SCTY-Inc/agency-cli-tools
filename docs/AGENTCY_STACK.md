# AGENTCY_STACK

Last updated: 2026-04-20

Note: literal repo directory renames to the `agentcy-*` names landed on 2026-04-12. Older loop notes below intentionally preserve pre-rename names where they describe historical proof work. The current bounded synthesis is the 2026-04-14 family checkpoint; mixed writer contracts remain intentionally locked even though live repo directories are now `agentcy-*`. Historical `agentcy-lab` mentions below are superseded by the current live monorepo, where bounded calibration/study work now sits under `agentcy-pulse`.

## Canonical docs

Use these in this order:

1. `AGENTCY_RECAP.md` — current canonical architecture, naming, module boundaries
2. `CONSOLIDATION.md` — original consolidation plan and concrete handoff seed
3. `AGENTCY_PROGRESS.md` — live execution ledger for the current loop

When `CONSOLIDATION.md` and `AGENTCY_RECAP.md` differ, prefer the recap.
Use the consolidation doc as historical context and a source of concrete contract ideas, not as the final authority.

## Current family vs supporting surfaces

### Current live monorepo modules

| Current repo | Module | Role now |
| --- | --- | --- |
| `protocols` | `agentcy-protocols` | parent protocol authority for schemas, examples, lineage rules, and thin handoff adapters |
| `agentcy-compass` | `agentcy-compass` | strategy / policy / brief layer |
| `agentcy-echo` | `agentcy-echo` | foresight / forecast layer |
| `agentcy-loom` | `agentcy-loom` | execution / review / publish runtime |
| `agentcy-pulse` | `agentcy-pulse` | analytics / attribution / feedback + repo-local study layer |
| `agentcy-vox` | `agentcy-vox` | voice / persona / drift layer |

The current operator layer at the monorepo root is `agentcy`, which now provides `doctor`, `pipeline run`, `pipeline update`, and `pipeline study` over the member CLIs without changing the canonical protocol writers. Preview bundles are module-first (`vox/`, `compass/`, `echo/`, `loom/`, `pulse/`, `reports/`), can use stable names via `--pipeline-id`, and can forward compatible root `--provider` / `--model` choices into Compass as `BRANDOPS_LLM_PROVIDER` / `BRANDOPS_LLM_MODEL`.

### Supporting / control-plane surfaces

| Surface | Role now |
| --- | --- |
| `cli-agency` | supporting source-material repo to narrow/re-home, primarily toward `agentcy-compass`; not a current family product module or canonical artifact writer |

## Architecture rules

1. **Protocol first.** Shared artifacts, lineage IDs, CLI conventions, and handoffs matter more than language convergence.
2. **One writer per artifact.** Each major artifact should have one clear owner.
3. **One repo per implementation task by default.** Cross-repo tasks should usually be docs, protocol, or thin adapter work.
4. **No giant rename or monolith pass first.** Defer broad renames, umbrella CLIs, monorepo work, and deep merges.
5. **Polyglot is fine for now.** Keep each repo idiomatic in its own stack.
6. **Bounded breadth/depth loops.** Use parallel recon for breadth, then narrow depth work in one repo or one protocol surface.

## Target artifacts and owners

| Artifact | Likely owner |
| --- | --- |
| `voice_pack.v1` | `agentcy-vox` |
| `brief.v1` | `agentcy-compass` |
| `scenario_pack.v1` | `agentcy-compass` or orchestration layer |
| `forecast.v1` | `agentcy-echo` |
| `run_result.v1` | `agentcy-loom` |
| `performance.v1` | `agentcy-pulse` |

## Family checkpoints

The current bounded family synthesis is `family-deep-review-checkpoint-2026-04-14.md`.

The active repo-local control-plane slice beneath that synthesis remains `family-loop-12-checkpoint-2026-04-12.md` for the bounded `agentcy-pulse` repo-birth proof.

`family-loop-6-checkpoint-2026-04-12.md` remains the completed seam-proof checkpoint for the bounded canonical published `run_result.v1 -> performance.v1` slice.

The prior slice checkpoint `family-checkpoint-2026-04-12.md` remains the historical gate that locked artifact ownership and the first bounded implementation wave.

`family-loop-4-checkpoint-2026-04-12.md` is now superseded historical context, not an active branch.

`family-loop-5-checkpoint-2026-04-12.md` remains the locked protocol baseline for the bounded `run_result.v1 -> performance.v1` slice.

Loop 7 is the completed bounded rename-readiness and canonical naming alignment wave. It remains docs, audit, and validation evidence only; literal repo renames remain deferred.

Loop 8 is the completed bounded `cli-phantom` / `agentcy-loom` package and CLI alias-readiness slice. It remains the locked single-repo proof surface for package metadata, CLI alias policy, and packaged install/help readiness only.

Loop 9 is the completed bounded `cli-prsna` / `agentcy-vox` package and CLI alias-readiness slice. It remains the locked single-repo proof surface for the `prsna` package target, the explicit `persona`-first CLI policy, and packaged install/help readiness only.

Loop 10 is the completed bounded `brand-os` / `agentcy-compass` blocker-reduction slice. It remains the locked single-repo proof surface for separating naming drift from boundary/ownership drift, keeping `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }` locked, and recording unresolved-before-rename evidence without authorizing any rename or migration claim.

Loop 11 is the completed bounded `cli-mirofish` / `agentcy-echo` attribution-preserving compatibility slice. It remains the locked single-repo planning and proof-boundary surface for package/distribution, import-root, and CLI compatibility around the current `mirofish-backend`, `app`, and `mirofish` surfaces while keeping `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }` locked.

Loop 12 remains the active bounded `cli-metrics` / `agentcy-pulse` repo-birth slice underneath the 2026-04-14 checkpoint. Its live repo-directory reality is now `agentcy-pulse`, while the mixed writer contract remains intentionally locked as `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }`.

### Locked ownership decisions

| Artifact | Canonical writer repo | Family module |
| --- | --- | --- |
| `voice_pack.v1` | `cli-prsna` | `agentcy-vox` |
| `brief.v1` | `brand-os` | `agentcy-compass` |
| `forecast.v1` | `cli-mirofish` | `agentcy-echo` |
| `run_result.v1` | `cli-phantom` | `agentcy-loom` |
| `performance.v1` | `cli-metrics` | `agentcy-pulse` |

### Completed first slice

The first real implementation slice is complete:

`voice_pack.v1 -> brief.v1`

Interpretation:
- `cli-prsna` is the writer for the canonical voice artifact
- `brand-os` is the writer for the canonical brief artifact
- parent-level family docs own schemas, lineage notes, example payloads, and ownership notes

### Completed second slice

The second bounded implementation slice is complete:

`brief.v1 -> run_result.v1`

Interpretation:
- `brand-os` remains the canonical writer for `brief.v1`
- `cli-phantom` / `agentcy-loom` is the canonical writer for `run_result.v1`
- parent-level family docs own the schema, lineage rules, examples, and thin handoff expectations that made this slice verifiable

### Completed third slice

The third bounded implementation slice is complete:

`brief.v1 -> forecast.v1`

Interpretation:
- `brand-os` remains the canonical writer for `brief.v1`
- `cli-mirofish` / future `agentcy-echo` is the canonical writer for `forecast.v1`
- parent-level family docs own the schema, lineage rules, examples, ownership notes, and thin handoff expectations that made this slice verifiable
- canonical family-owned `forecast.v1` export remains intentionally limited to completed forecasts, with failed or partial MiroFish outcomes staying repo-local for now
- lineage persistence from imported `brief.v1` inputs into stable `cli-mirofish` run artifacts is now part of the proven seam

### Completed fifth slice

The fifth bounded implementation slice is now proven at the family control-plane level:

`cli-metrics` readiness -> future `agentcy-pulse` -> `performance.v1`

Interpretation:
- loop 4 (`cli-agency` narrowing -> `brand-os` / future `agentcy-compass`) remains superseded historical context, not an active branch to reopen
- `cli-metrics` is still absent or not implementation-ready as a working family repo, and loop 5 proved that the family can still lock the measurement path without repo bootstrap
- the strongest upstream seam for loop 5 is canonical published `run_result.v1` from `cli-phantom` / `agentcy-loom`
- `protocols/examples/run_result.v1.published.json` is the sole canonical source fixture for the first pulse seam
- the smallest viable first `performance.v1` remains a narrow measurement snapshot for published `social.post` outcomes only, carrying canonical lineage and publish locators
- loop 5 is now evidenced by four landed pieces: the readiness scan, the minimal `performance.v1` contract, the loom seam proof, and the thin family validation pass
- loop 5 keeps `agentcy-pulse` measurement-only and does not pull strategy, publish, persona, or generic runtime ownership into analytics
- canonical artifacts, examples, and tests for loop 5 exclude tokens, auth material, secrets, and audience-level or user-level PII

### Completed sixth slice

The sixth bounded implementation slice is now evidenced at the family control-plane level as the seam-proof follow-up to loop 5:

`agentcy-pulse` thin fixture or tiny adapter seam for canonical published `run_result.v1 -> performance.v1`

Interpretation:
- loop 5 remains the locked protocol baseline and should not be reopened as a schema redesign or repo-bootstrap wave
- loop 6 proved the family can land a family-owned seam without a `cli-metrics` repo bootstrap and without creating a second authority for canonical fixtures
- `cli-metrics` remains absent or not implementation-ready as a working family repo, so the seam stays fixture-only or tiny-adapter-only
- `protocols/examples/run_result.v1.published.json` remains the sole canonical source fixture the seam may read from
- the loop-6 output target remains canonical `performance.v1`, deterministically emitted from that canonical published input plus only the narrow sidecar measurement envelope
- the family now has direct proof via a tiny adapter and parent-level canonical-fixture validation covering deterministic fixture-path loading, golden output parity, lineage/publish-locator preservation, privacy bounds, and bounded rejection cases
- any future repo-local mirror fixture, including a `cli-phantom` convenience copy, is optional, non-canonical, and non-blocking

### Completed seventh slice

The seventh bounded control-plane slice is complete:

`rename-readiness and canonical naming alignment audit`

Interpretation:
- loop 7 remains the locked family audit wave for naming readiness across repo, package, import, CLI, docs, writer-field, fixture, and runtime-prefix surfaces
- loop 7 does not authorize literal repo renames and should not be reopened as a broad implementation branch
- the completed result is the merged readiness summary plus the shared audit template and family matrix
- the key invariant remains locked: `writer.module` may carry the future family module name, while `writer.repo` stays on the preserved historical lineage ID for each canonical artifact writer
- future follow-up work should stay surface-specific and repo-specific rather than collapsing back into a family-wide rename campaign
- future `agentcy-pulse` work should still use `cli-metrics-birth-contract-2026-04-12.md` as the minimum naming-readiness contract before any repo/package/import/CLI surface is created

### Completed eighth slice

The eighth bounded control-plane slice is now complete:

`cli-phantom` / `agentcy-loom` package and CLI alias-readiness proof

Interpretation:
- loop 8 is a narrow single-repo follow-up to loop 7, not a new family-wide rename wave
- the target repo remains `cli-phantom`, with future family module `agentcy-loom`
- the active proof surface is limited to package metadata, the explicit `loom-runtime` / `loom` alias policy, and packaged install/help readiness
- the acceptance bar is an honest packaged operator path, including installable-binary/help readiness rather than source-first `npx tsx src/cli.ts ...` assumptions alone
- canonical artifact ownership remains unchanged, with `run_result.v1.writer = { repo: "cli-phantom", module: "agentcy-loom" }`
- loop 8 must not turn into literal repo renames, umbrella CLI work, MCP-first integration, runtime-prefix migration, broad runtime unification, monolith moves, or cosmetic churn outside the package/CLI proof surface
- loop 7 remains the completed readiness audit baseline that loop 8 depends on; it should not be rewritten as if the proof had landed before the bounded external package/help verification actually did
- bounded proof is now present: `cli-phantom/docs/packaged-install-help-proof-2026-04-12.md` records `npm pack`, local tarball install, and successful external `loom --help` / `loom help --json` execution without claiming a repo rename or an `agentcy-loom` binary

### Loop-7 merged readiness summary

The loop-7 control plane now has enough evidence to summarize rename-readiness without authorizing any literal rename.

| Repo | Artifact-writer status | Repo rename status | Package / import / CLI status | Smallest next control-plane action |
| --- | --- | --- | --- | --- |
| `cli-prsna` | aligned now (`cli-prsna` / `agentcy-vox`) | deferred | not ready; `prsna` + `persona` + `prsna` import remain live surfaces | choose future package/bin targets and alias policy before any rename proposal |
| `brand-os` | aligned now (`brand-os` / `agentcy-compass`) | deferred | not ready; boundary drift plus `brand-os` / `brand_os` / `brandos` and runtime-prefix surfaces remain blockers | narrow repo boundary first and keep runtime/env migration separate |
| `cli-mirofish` | aligned now (`cli-mirofish` / `agentcy-echo`) | deferred | not ready; MiroFish lineage, AGPL constraints, `mirofish-backend`, `mirofish`, and `app` remain blockers | define attribution-preserving compatibility policy before public rename work |
| `cli-phantom` | aligned now (`cli-phantom` / `agentcy-loom`) | deferred | partially aligned but not rename-ready; Loom-shaped runtime surfaces exist and bounded external packaged `loom` help proof now exists, but repo identity remains mixed and no `agentcy-loom` binary claim is proven | keep `loom-runtime` transitional, keep `loom` as the verified installed alias, and do not inflate the proof into a repo/package rename claim |
| `cli-metrics` / `agentcy-pulse` | aligned at protocol and bounded repo-birth layer (`cli-metrics` / `agentcy-pulse`) | not rename-ready; repo birth landed under current contract | bounded birth surfaces now proven as `agentcy-pulse` package / `agentcy_pulse` import / `agentcy-pulse` CLI only | keep loop 12 narrow: record the landed birth names and proof boundary, preserve `writer.repo = "cli-metrics"`, and defer live analytics, broader abstractions, and rename claims |

Family-level interpretation:
- every active family artifact is already aligned on the mixed writer contract
- no repo is honestly rename-ready across repo, package, import, CLI, and runtime surfaces together
- repo renames remain deferred until the smaller surface-specific blockers are resolved and verified
- package/distribution, import-path, CLI-binary, and runtime-prefix readiness must stay separate in future tasks

### Completed ninth slice

The ninth bounded control-plane slice is now complete:

`cli-prsna` / `agentcy-vox` package and CLI alias-readiness proof

Interpretation:
- loop 9 is a narrow single-repo follow-up to loop 7, not a new family-wide rename wave
- the target repo remains `cli-prsna`, with future family module `agentcy-vox`
- the active proof surface is limited to the `prsna` package/distribution, the explicit `persona`-first CLI policy, and packaged install/help readiness
- the acceptance bar is an honest packaged operator path from outside the repo root, including installable-binary/help readiness rather than source-first assumptions alone
- canonical artifact ownership remains unchanged, with `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`
- loop 9 must not turn into literal repo renames, umbrella CLI work, MCP-first integration, import-path rewrites, broad runtime unification, monolith moves, or cosmetic churn outside the package/CLI proof surface
- loop 7 remains the completed readiness audit baseline that loop 9 depends on; it should not be rewritten as if `cli-prsna` package/bin proof had landed before the bounded external package/help verification actually did
- bounded proof is now present: `cli-prsna/docs/packaged-install-help-proof-2026-04-12.md` records `uv build`, external wheel install, successful `persona --help`, `persona --version`, `persona export --list`, and an unchanged `import prsna` smoke test from outside the repo root
- the loop-9 proof is intentionally limited to the currently shipped `persona` installed CLI; it does not claim a new installed alias such as `agentcy-vox` or `vox`

### Completed eleventh slice

The eleventh bounded control-plane slice is now complete:

`cli-mirofish` / `agentcy-echo` attribution-preserving package/import/bin compatibility planning

Interpretation:
- loop 11 remains the locked single-repo compatibility-planning baseline for current `mirofish-backend`, `app`, and `mirofish` surfaces
- the landed family evidence is still current-surface-only, preserves upstream MiroFish lineage and AGPL-aware attribution, and keeps the generic `app` import root recorded as a real blocker
- canonical artifact ownership remains unchanged, with `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`
- loop 11 does not justify literal repo renames, package/distribution rename execution, import-path rewrites, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, or cosmetic churn outside the compatibility-planning surface

### Active twelfth slice

The twelfth bounded control-plane slice is now active:

`cli-metrics` / `agentcy-pulse` first minimal repo-birth proof

Interpretation:
- loop 12 is a narrow single-repo follow-up to loop 11, not a new family-wide rename wave
- the target repo remains `cli-metrics`, with future family module `agentcy-pulse`
- the landed birth surfaces are now explicit: package/distribution `agentcy-pulse`, import root `agentcy_pulse`, and CLI binary `agentcy-pulse`
- canonical artifact ownership remains unchanged, with `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }`
- the active proof boundary is intentionally limited to `uv sync`, `uv run agentcy-pulse --help`, `uv run python -c "import agentcy_pulse"`, and one family-fixture seam check only
- loop 12 must not turn into live analytics integration, warehouse/event abstraction work, broader metrics architecture, non-`social.post` analytics expansion, literal repo renames, umbrella CLI work, MCP-first integration, runtime unification, monolith moves, or cosmetic churn outside the minimal birth surface
- loop 7 remains the completed naming-readiness baseline and loop 5 plus loop 6 remain the locked protocol and seam baselines; they should not be rewritten as if loop 12 changed ownership or widened the proven seam

### Explicit deferrals

Still explicitly deferred during and after loop 12:
- literal family repo renames
- package/distribution rename execution
- umbrella CLI work
- MCP-first integration
- import-path rewrites
- broad runtime unification
- runtime-wide cleanup outside the current compatibility-planning slice
- monolith moves or deep repo merges
- heavy `cli-metrics` repo bootstrap
- live analytics platform integrations
- broad metric abstractions beyond published `social.post`
- unnecessary code churn undertaken only to cosmetically align names before compatibility readiness is proven

Why:
- they matter to the long-term family boundary map
- they are not required to complete the bounded rename-readiness and canonical naming alignment follow-up for `cli-mirofish`
- implementation should stay bounded and protocol-first rather than expanding into rename theatre, import rewrites, runtime rewrites, or a metrics monolith

## Operating loop

### Outer loop: Pi Messenger Crew

Run Pi from `/Users/amadad/projects` when you want family-wide orchestration.

1. Read `CONSOLIDATION.md`, `AGENTCY_RECAP.md`, `AGENTCY_STACK.md`, and `AGENTCY_PROGRESS.md`
2. Use `pi_messenger({ action: "plan", ... })` to create a dependency-aware task graph
3. Run `pi_messenger({ action: "work", autonomous: true })` for parallel worker waves
4. Let review gate every completed task
5. Update `AGENTCY_PROGRESS.md`

### Inner loop: pi-subagents

Use subagents for bounded bursts inside the broader loop:

- family-wide recon across 2-4 repos
- protocol and handoff synthesis
- repo-specific scout -> planner -> reviewer chains

Do not use nested fan-out casually. Keep subagent bursts short and scoped.

## Task taxonomy

Prefer task titles with explicit scope:

- `[family]` docs, protocol, ownership, lineage, schema work
- `[brand-os]` repo-local work for future `agentcy-compass`
- `[cli-prsna]` repo-local work for future `agentcy-vox`
- `[cli-mirofish]` repo-local work for future `agentcy-echo`
- `[cli-phantom]` repo-local work for future `agentcy-loom`
- `[cli-metrics]` repo-local work for future `agentcy-pulse`
- `[integration]` thin handoff or adapter tasks spanning a small number of repos

## Guardrails for workers

- Reserve exact files or tight directories, not whole repos, unless necessary.
- Default to one repo per worker task.
- If a task spans repos, keep it documentation-, schema-, or adapter-focused.
- If a task changes command surfaces, verify installability, output behavior, and safe approval boundaries.
- Avoid MCP-first integration and avoid inventing a giant shared runtime before the handoffs are real.

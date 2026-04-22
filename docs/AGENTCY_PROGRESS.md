# AGENTCY_PROGRESS

Updated: 2026-04-20

Note: literal repo directory renames to the `agentcy-*` names landed on 2026-04-12. Historical loop entries below intentionally preserve pre-rename repo names where they describe the evidence as it was produced. The 2026-04-14 family checkpoint is the current bounded synthesis; mixed writer contracts remain intentionally locked. Historical `agentcy-lab` mentions below are now superseded by the live monorepo shape, where bounded calibration/study work lives under `agentcy-pulse`.

## Current phase

The current bounded synthesis is `_agentcy-docs/family-deep-review-checkpoint-2026-04-14.md`.

Current live six-module monorepo set:
- `protocols`
- `agentcy-compass`
- `agentcy-echo`
- `agentcy-loom`
- `agentcy-pulse`
- `agentcy-vox`

Supporting/control-plane surfaces that must be narrated separately:
- `cli-agency` as supporting source material, not a family product module or canonical artifact writer

Current family readout:
- live monorepo members are now `protocols`, `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-pulse`
- mixed writer contracts remain intentionally locked for the five canonical artifacts even though the package/bin layer is `agentcy-*`
- the root `agentcy` dispatcher now exposes `doctor`, `pipeline run`, `pipeline update`, and `pipeline study` as the operator entry surface
- `agentcy pipeline run --mode preview` now writes a module-first repo-local bundle (`vox/`, `compass/`, `echo/`, `loom/`, `pulse/`, `reports/`) plus `bundle_manifest.json` and an auto-generated operator report
- root pipeline bundles can now use stable named folders via `--pipeline-id`, so operator runs can land at paths like `artifacts/pipelines/givecare-launch-01/`
- `agentcy-echo` now has a deterministic `--smoke` path plus repo-local `run_eval` and `llm_telemetry` artifacts for fast e2e proof without widening canonical protocols
- full echo CLI automation now exits cleanly instead of lingering in command-waiting mode, and the single-platform scripts emit action logs again for downstream timeline/report assembly
- `agentcy-vox` and `agentcy-pulse` now use repo-local eval/study artifacts (`evals --compare`, `study`, manifest/echo-run discovery) instead of widening the canonical family schemas
- `agentcy-compass` remains the highest boundary-risk hotspot

Loop 12 still remains the active repo-local control-plane slice for the bounded `cli-metrics` / `agentcy-pulse` first minimal repo-birth wave beneath this checkpoint:
- canonical artifact ownership remains unchanged, with `performance.v1` still owned by `cli-metrics` / `agentcy-pulse`
- `writer.module` may remain on the family-name track where already locked, while `writer.repo` must still reflect preserved writer history
- the live repo-directory reality is `agentcy-pulse`, while the bounded proof surface remains install/help/import plus one family-fixture seam check only
- pulse follow-ups must stay clear of literal repo renames, live analytics expansion, warehouse/event abstractions, umbrella CLI work, MCP-first integration, import-path rewrites outside the bounded birth surface, broad runtime unification, and unnecessary churn

## Done

- Installed Pi packages needed for this workflow:
  - `pi-web-access`
  - `pi-subagents`
  - `pi-messenger`
- Added parent-level Pi Messenger defaults for `/Users/amadad/projects`
- Added project-level Crew config and Agentcy-specific crew agent overrides
- Added project subagents for breadth recon, planning, implementation, and review
- Added `/continue-agentcy` prompt template
- Created `AGENTCY_STACK.md` and this progress log
- Landed the root dispatcher operator layer in `src/agentcy/cli.py` with `doctor`, `pipeline run`, `pipeline update`, and `pipeline study`
- Added bounded repo-local analysis surfaces without widening canonical protocols:
  - `agentcy-echo run --smoke` + `run_eval.v1.json` + `logs/llm_telemetry.jsonl`
  - `agentcy-vox evals --compare`
  - `agentcy-pulse study` with pipeline-manifest and echo-run auto-discovery
- Hardened the operator happy path:
  - root pipeline bundles are now module-first and emit one operator report automatically
  - full echo CLI runs now pass `--no-wait` to the simulation subprocess
  - Compass stage outputs are normalized before Pydantic validation so near-schema LLM output no longer crashes the stage immediately
  - Compass can now use local `claude-cli` / `CLAUDE_MODEL` for planning runs, which avoids the Gemini 429 fallback path on operator E2Es
- Historical note: the earlier `agentcy-lab` calibration/eval concept is now effectively absorbed into the live `agentcy-pulse` repo-local study/calibration layer

## Working assumptions

- `AGENTCY_RECAP.md` is the current canonical architecture doc.
- `CONSOLIDATION.md` is historical context plus concrete contract seed material, not the final authority.
- `_agentcy-docs/family-deep-review-checkpoint-2026-04-14.md` is the current bounded synthesis for present family state.
- `cli-agency` is supporting source material to narrow/re-home, not the permanent center of the family.
- `protocols` is the family protocol authority, not an extra family product module.
- The family should stay modular and protocol-first.
- Mixed writer contracts are currently intentional protocol truth, not by themselves a defect to normalize.

## Next queue

1. Use `_agentcy-docs/family-deep-review-checkpoint-2026-04-14.md` as the current bounded synthesis for the post-review family state.
2. Keep the highest-value family follow-ups doc/protocol-local first:
   - normalize present-tense control-plane narration so live repo directories are consistently described as `agentcy-*`
   - fix stale renamed-path references in parent-level docs/tests such as remaining `brand-os/...` path assumptions
   - publish or strengthen one authority note that keeps `cli-agency` as supporting source material and `protocols` as parent protocol authority rather than extra family modules
3. Keep `agentcy-compass` as the highest boundary-risk hotspot and limit the next repo-local work to scorecards or CLI-scope maps that classify current surfaces without changing command behavior.
4. Keep `agentcy-echo` bounded to compatibility/attribution/dependency-proof follow-ups only:
   - preserve explicit MiroFish + AGPL lineage
   - keep `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`
   - treat optional simulation-runtime proof and family path-narration cleanup as the next blockers, not import rewrites or rename execution
5. Keep `agentcy-loom`, `agentcy-vox`, and `agentcy-pulse` on docs-first clarification follow-ups:
   - `agentcy-loom`: refresh packaged-help proof wording so current repo path, preserved writer repo, and live package/bin surfaces are clearly separated
   - `agentcy-vox`: clarify family-level narration instead of starting package/import/CLI rename work
   - `agentcy-pulse`: record live `agentcy-pulse/` repo reality in loop-12 family docs while preserving `writer.repo = "cli-metrics"`
6. Treat the historical `agentcy-lab` concept as absorbed into the live `agentcy-pulse` calibration/study layer; no separate lab follow-up is active unless another stable protocol-backed seam later justifies a new bounded module.
7. Keep the following explicitly deferred:
   - literal family repo renames
   - umbrella CLI work
   - MCP-first integration
   - import-path rewrites
   - broad runtime unification
   - runtime-prefix migration work before inventory is complete
   - monolith moves or deep repo merges
   - large boundary rewrites
   - broad analytics expansion beyond the current pulse seam
   - package renames or public-surface rewrites undertaken only for cosmetic alignment

## Active questions / blockers

- No blocking gap remains for the current family checkpoint itself; the open work is follow-up clarification, not a second synthesis pass.
- For `agentcy-compass`, what is the smallest scorecard or CLI-scope map that classifies over-boundary surfaces without changing behavior?
- For `agentcy-echo`, what is the smallest honest current-surface proof path across package `mirofish-backend`, import root `app`, CLI `mirofish`, and explicit upstream MiroFish attribution without widening scope into import rewrites or rename execution?
- Which parent-level docs/tests still carry stale renamed-path assumptions such as `brand-os/...` despite live `agentcy-*` repo directories?
- For later pulse follow-up, can family docs keep live `agentcy-pulse/` repo reality explicit while preserving `performance.v1.writer.repo = "cli-metrics"` and the current privacy/scope bounds?

## Operator notes

### Default control-plane cwd

Run Pi from:

`/Users/amadad/projects`

That keeps the family docs and the cross-repo Crew state in one place.

### Default loop entrypoint

Use:

`/continue-agentcy`

Optional focus examples:

- `/continue-agentcy first breadth scan`
- `/continue-agentcy close loop-4 and open loop-5`
- `/continue-agentcy focus on cli-metrics readiness and performance.v1`

### Expected behavior

- Pi Messenger drives the continuous outer loop.
- pi-subagents handles bounded breadth/depth bursts.
- `AGENTCY_PROGRESS.md` should be updated whenever a meaningful architecture, protocol, or implementation milestone lands.

## Session log

### 2026-04-22 — recovered smoke/eval/study surfaces from mixed local state

- Recovered and shipped the durable parts of a mixed local stash instead of leaving them hidden behind a clean worktree.
- `agentcy-echo` now keeps its deterministic smoke-mode path, split graph retrieval/report support modules, and the supporting test coverage in the live repo.
- `agentcy-vox` now keeps structured eval tiers plus saved eval-report inspection (`evals --latest`, `evals --compare`) in the live repo.
- `agentcy-compass` now keeps stage normalization, Claude CLI provider support, and explicit unsupported optional surfaces in the live repo.
- Generated `artifacts/**` outputs and other low-signal leftovers were intentionally discarded rather than restored.

### 2026-04-18 — root operator layer and repo-local eval loops landed

- Added a real root `agentcy` operator surface with member env forwarding, richer `doctor` output, persisted pipeline manifests, `pipeline run`, `pipeline update`, and `pipeline study`.
- Added bounded repo-local eval/report surfaces instead of widening canonical family artifacts:
  - `agentcy-echo`: `run_eval.v1.json`, `--smoke`, and per-run `logs/llm_telemetry.jsonl`
  - `agentcy-vox`: saved eval reports plus `evals --compare`
  - `agentcy-pulse`: `study`, plus forecast/eval discovery from pipeline manifests or echo run dirs
- Preserved the current protocol decision: canonical schemas/examples stay narrow; richer analysis remains repo-local sidecars and manifests.

### 2026-04-12 — loop bootstrap

- Re-anchored the setup around `CONSOLIDATION.md -> AGENTCY_RECAP.md`
- Shifted the operating model from generic CLI harmonization to recap-grounded family orchestration
- Set up the family control loop at the parent projects level
- Left the next meaningful task as a fresh breadth scan plus first vertical-slice selection

### 2026-04-12 — breadth scan scorecards landed

- Added `brand-os/docs/ownership-scorecard-2026-04-12.md` to capture current `brand-os` boundaries, keep/narrow recommendations, and the thinnest likely `brief.v1` emit seam.
- Added `cli-prsna/docs/voice-pack-v1-scorecard.md` to capture the current Persona/export surface and the thinnest canonical `voice_pack.v1` writer path.
- Added `cli-mirofish/docs/forecast-v1-deferral-scorecard.md` to inventory current run/report artifacts and record why `forecast.v1` stays out of the first slice.
- Added `cli-phantom/docs/agentcy-loom-breadth-scan-2026-04-12.md` to capture current runtime artifact types, run-state boundaries, and the likely future `brief.v1 -> run_result.v1` seams.
- Added `cli-agency/docs/re-home-candidate-scorecard-2026-04-12.md` to capture the smallest research/strategy concepts worth re-homing into `brand-os` and the store/plugin/MCP surfaces to leave behind.

### 2026-04-12 — family checkpoint locked

- Added `family-checkpoint-2026-04-12.md` as the explicit family checkpoint artifact consolidating the five repo-local scans.
- Locked one-writer-per-artifact decisions across the family and made the next implementation wave contingent on that checkpoint rather than planner prose alone.
- Chose `voice_pack.v1 -> brief.v1` as the first implementation slice.
- Recorded explicit first-slice deferrals for `cli-mirofish` / `forecast.v1`, `cli-phantom` / `run_result.v1`, and `cli-metrics` / `performance.v1`.
- Updated `AGENTCY_STACK.md` and this progress log so the active queue now points to schema/examples first, then repo-local writer tasks.

### 2026-04-12 — canonical first-slice protocol artifacts published

- Added `protocols/voice_pack.v1.schema.json` as the family-owned canonical JSON Schema for the `cli-prsna` / `agentcy-vox` voice artifact.
- Added `protocols/brief.v1.schema.json` as the family-owned canonical JSON Schema for the `brand-os` / `agentcy-compass` brief artifact.
- Added `protocols/lineage-rules.md` to lock authoritative lineage semantics for `brand_id`, `voice_pack_id`, and `brief_id`, plus the parent-authority and repo-local mirroring rules.
- Added canonical minimal and richer example payloads under `protocols/examples/` for both artifact types.
- Verified all new JSON artifacts parse cleanly and that the examples satisfy the first-slice lineage invariants.

### 2026-04-12 — thin `voice_pack.v1 -> brief.v1` handoff validation landed

- Added `protocols/tests/test_voice_pack_to_brief_v1.py` as the parent-level thin integration check for the first real family slice.
- Validated `cli-prsna` rich fixture export output against `protocols/voice_pack.v1.schema.json` and canonical writer ownership.
- Validated `brand-os` brief emission built from that exported `voice_pack.v1` artifact against `protocols/brief.v1.schema.json` and the lineage invariants in `protocols/lineage-rules.md`.
- Recorded concrete evidence by re-running the repo-local writer tests plus the new parent-level handoff test:
  - `cli-prsna/.venv/bin/python -m pytest protocols/tests/test_voice_pack_to_brief_v1.py`
  - `cli-prsna/.venv/bin/python -m pytest cli-prsna/tests/test_exporters.py`
  - `cd brand-os && PYTHONPATH=src ../cli-prsna/.venv/bin/python -m pytest tests/plan/test_brief_v1.py`
- The first slice is now complete and the active roadmap moves to the bounded `brief.v1 -> run_result.v1` loop.
- `cli-phantom` / `agentcy-loom` remains the canonical writer for `run_result.v1`.
- Keep loop-2 scoped to protocol artifacts plus a thin loom handoff, not umbrella CLI work, MCP-first integration, or broad runtime unification.

### 2026-04-12 — thin `brief.v1 -> run_result.v1` dry-run handoff validated

- Added `protocols/tests/test_brief_to_run_result_v1.py` as the parent-level thin integration check for the second family slice.
- Proved `cli-phantom` can ingest the canonical parent `brief.v1` example, advance through review, and emit canonical `run_result.v1` on dry-run publish without adding any umbrella cross-repo tooling.
- Validated the emitted `run_result.v1` against `protocols/run_result.v1.schema.json` and checked lineage continuity for `brand_id`, `brief_id`, `source_voice_pack_id`, `campaign_id`, and `signal_id`.
- Recorded concrete verification evidence for the bounded handoff and its repo-local seams:
  - `cli-prsna/.venv/bin/python -m pytest protocols/tests/test_brief_to_run_result_v1.py protocols/tests/test_run_result_v1_protocol.py protocols/tests/test_voice_pack_to_brief_v1.py`
  - `cd brand-os && PYTHONPATH=src ../cli-prsna/.venv/bin/python -m pytest tests/plan/test_brief_v1.py`
  - `cd cli-phantom/runtime && npm test`
- The second bounded slice is now proven at the family protocol layer: `brand-os` remains the canonical brief writer and `cli-phantom` remains the canonical `run_result.v1` writer.

### 2026-04-12 — canonical `brief.v1 -> forecast.v1` handoff validated

- Added `protocols/tests/test_brief_to_forecast_v1.py` as the parent-level thin integration check for the third family slice.
- Proved `cli-mirofish` can take the canonical parent `brief.v1` example through its documented `runs export ... --artifact forecast_v1` seam and emit canonical `forecast.v1` without adding any umbrella cross-repo runtime.
- Validated the emitted `forecast.v1` against `protocols/forecast.v1.schema.json` and checked lineage continuity for `brand_id`, `brief_id`, `source_voice_pack_id`, `campaign_id`, and `signal_id`.
- Verified that MiroFish-local provenance IDs (`project_id`, `graph_id`, `simulation_id`, `report_id`) remain distinct from family-owned lineage IDs, and added an optional mirror-backed validation path using `brand-os/tests/fixtures/brief.v1.rich.mirror.json`.
- Recorded concrete verification evidence for the bounded handoff and its repo-local seam coverage:
  - `cd cli-mirofish && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py ../protocols/tests/test_forecast_v1_protocol.py`
  - `cd cli-mirofish && uv run python -m pytest tests/test_cli_artifacts_and_visuals.py -k 'forecast_v1 or import_brief_v1'`
- The third bounded slice is now proven at the family protocol layer: `brand-os` remains the canonical `brief.v1` writer and `cli-mirofish` remains the canonical `forecast.v1` writer.

### 2026-04-12 — loop 4 control-plane re-anchor

- Closed loop 3 in the parent control-plane docs and recorded `brief.v1 -> forecast.v1` as completed rather than active.
- Declared loop 4 active as a bounded `cli-agency` narrowing -> `brand-os` / future `agentcy-compass` wave.
- Added `family-loop-4-checkpoint-2026-04-12.md` to restate that `brand-os` remains the canonical `brief.v1` writer and `cli-agency` is source material, not the family root.
- Re-locked explicit deferrals for giant renames, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, `cli-agency` store/plugin/runtime surfaces, and `cli-metrics` / `performance.v1`.
- Narrowed the next queue to keep/re-home/archive decisions around `cli-agency` research and strategy surfaces instead of a giant merge plan.

### 2026-04-12 — loop 4 brief writer ownership re-validated

- Strengthened `protocols/tests/test_voice_pack_to_brief_v1.py` so the parent family validation now also asserts the canonical `brief.v1` example and the `brand-os` mirror fixture both keep `writer = { repo: "brand-os", module: "agentcy-compass" }`.
- Added an explicit loop-4 lineage rule that `cli-agency` must not appear as a `brief.v1` writer, alternate writer, or protocol authority in canonical artifacts, examples, mirror fixtures, or protocol tests.
- Restated the loop-4 checkpoint language so bounded re-home work does not create a second `brief.v1` writer while `cli-agency` remains source/reference material only.
- Recorded verification evidence for the thin family-level pass:
  - `cd brand-os && PYTHONPATH=src ../cli-prsna/.venv/bin/python -m pytest tests/plan/test_brief_v1.py`
  - `cli-prsna/.venv/bin/python -m pytest protocols/tests/test_voice_pack_to_brief_v1.py`

### 2026-04-12 — cli-agency keep/re-home/archive matrix published

- Upgraded `cli-agency/docs/re-home-candidate-scorecard-2026-04-12.md` from breadth-scan notes into an explicit loop-4 decision matrix for exact `cli-agency` surfaces.
- Marked `agency/schemas/research.py` and `agency/schemas/strategy.py` as the smallest high-value re-home candidates for the `brand-os` plan -> `brief.v1` seam.
- Kept `agency/stages/research.py`, `agency/stages/strategy.py`, and selected `agency/cli.py` non-interactive seams as reference-only source material rather than direct re-home targets.
- Explicitly left `agency/core/store.py`, `agency/core/mcp.py`, `agency/plugins/*`, interactive session commands, creative-generation surfaces, and activation-runtime planning behind for loop 4.
- Named likely destination/archive status in the matrix so downstream repo-local tasks can depend on the classification without reopening the full family breadth scan.

### 2026-04-12 — loop 5 control-plane re-anchor

- Closed loop 4 as superseded historical context in the parent control-plane docs so it no longer appears to be an active parallel branch.
- Declared loop 5 active as the bounded `cli-metrics` readiness -> future `agentcy-pulse` -> `performance.v1` wave.
- Added `family-loop-5-checkpoint-2026-04-12.md` as the new active checkpoint and marked `family-loop-4-checkpoint-2026-04-12.md` as superseded/historical.
- Recorded that `cli-metrics` is still absent or not implementation-ready, so loop 5 starts with readiness scan, protocol definition, seam proof, and validation rather than repo bootstrap.
- Re-locked explicit deferrals for giant renames, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, heavy repo bootstrap, and live analytics integrations.
- Narrowed the next queue to the smallest viable `run_result.v1 -> performance.v1` slice for published `social.post` outcomes only.

### 2026-04-12 — `cli-metrics` absence map and loop-5 readiness scan published

- Added `cli-metrics-absence-map-and-performance-v1-readiness-2026-04-12.md` as the substantive loop-5 family readiness artifact.
- Confirmed `cli-metrics` is currently absent as a working family repo, so loop 5 is not ready for implementation-heavy analytics work or repo bootstrap.
- Recorded canonical published `run_result.v1` from `cli-phantom` / `agentcy-loom` as the usable upstream seam for `performance.v1`, including lineage (`run_id`, `brief_id`, `brand_id`, `source_voice_pack_id`, `campaign_id`, `signal_id`) and publish locators (`platform`, `post_id`, `url`).
- Named likely downstream readers in `brand-os` learning/calibration surfaces and `cli-prsna` drift/learning surfaces while restating that future `agentcy-pulse` stays measurement-only.
- Locked first-wave exclusions for dry-run, failed, blog, outreach, reply, and non-`social.post` analytics, plus all secret-bearing or audience/user-level payloads.
- Restated the smallest next actionable slice as family-owned `performance.v1` schema/examples/lineage plus a docs/test-only loom seam proof, with no `cli-metrics` repo bootstrap yet.

### 2026-04-12 — minimal `performance.v1` contract published

- Added `protocols/performance.v1.schema.json` as the parent-owned canonical schema for aggregate performance snapshots limited to published `social.post` outcomes only.
- Added canonical examples `protocols/examples/performance.v1.minimal.json` and `protocols/examples/performance.v1.rich.json` showing required lineage, publish locators, and intentionally narrow optional metric fields.
- Extended `protocols/lineage-rules.md` to lock `performance_id` semantics, `run_result.v1 -> performance.v1` invariants, writer ownership for future `cli-metrics` / `agentcy-pulse`, and the no tokens, secrets, auth material, audience-level data, or user-level PII rule.
- Added `protocols/tests/test_performance_v1_protocol.py` as the thin family validation proving canonical published `run_result.v1` lineage and publish locators are sufficient upstream input for `performance.v1`.
- Recorded concrete verification evidence for the bounded protocol pass:
  - `cli-prsna/.venv/bin/python -m pytest protocols/tests/test_performance_v1_protocol.py protocols/tests/test_run_result_v1_protocol.py`

### 2026-04-12 — loop 5 evidence merged and next bounded candidate recorded

- Merged the readiness, schema/examples/lineage, loom seam, and family validation results into the parent control-plane docs so loop 5 now reads as proven rather than merely active.
- Restated that `cli-metrics` is still absent or not implementation-ready as a working family repo, so the stale loop-4 branch stays superseded instead of being reopened as a fallback.
- Recorded that docs/schema/examples/tests are already in place for the first `run_result.v1 -> performance.v1` slice and should remain the locked contract surface.
- Named the only acceptable next implementation candidate as a future thin `cli-metrics` fixture or adapter seam, not a full repo bootstrap, live analytics integration pass, or runtime unification effort.

### 2026-04-12 — loop 6 control-plane seam opened and bounded

- Opened `family-loop-6-checkpoint-2026-04-12.md` as the new active checkpoint while keeping `family-loop-5-checkpoint-2026-04-12.md` as the locked protocol baseline.
- Reframed the next wave as a family-owned `agentcy-pulse` seam proof only: fixture-only or tiny-adapter-only for canonical published `run_result.v1 -> performance.v1`.
- Restated that `cli-metrics` remains absent or not implementation-ready, so loop 6 must not turn into repo bootstrap, live analytics integration, umbrella CLI work, MCP-first integration, runtime unification, or monolith moves.
- Locked `protocols/examples/run_result.v1.published.json` as the sole canonical source fixture for the seam and kept any repo-local mirror explicitly optional and non-authoritative.

### 2026-04-12 — loop 6 seam evidence merged and next pulse boundary restated

- Merged the loop-6 seam proof back into the family control-plane docs after the family-owned adapter and canonical-fixture validation landed.
- Recorded that the family has now directly proven the canonical published `run_result.v1 -> performance.v1` seam through a tiny adapter plus parent-level golden-fixture tests.
- Restated that `protocols/examples/run_result.v1.published.json` remains the sole canonical source fixture and that any repo-local mirror stays optional, labeled, and non-authoritative.
- Confirmed loop-5 contract artifacts remain locked, including schema/examples, lineage rules, privacy bounds, and the narrow published-`social.post` scope.
- Recorded the bounded evidence surface: deterministic fixture-path loading, golden-output parity, canonical lineage/publish-locator preservation, aggregate-only sidecar observations, and rejection of dry-run, failed, non-`social.post`, missing-locator, and unmatched-platform inputs.
- Re-locked explicit deferrals for live analytics integrations, broader analytics scope, and heavy `cli-metrics` repo bootstrap so the next pulse boundary stays thinner than a new repo wave.

### 2026-04-12 — loop 7 rename-readiness control-plane wave opened

- Opened `family-loop-7-checkpoint-2026-04-12.md` as the active control-plane checkpoint for bounded rename-readiness and canonical naming alignment work.
- Recorded loop 6 as complete rather than active, so the pulse seam evidence remains locked while naming readiness is audited separately.
- Published the shared family audit template for repo directory name, package/distribution name, import path, CLI binary, docs/install branding, artifact writer fields, fixture/test references, and runtime path/key prefixes.
- Locked the required four-way per-surface classification: current canonical, post-rename target, acceptable legacy alias, and hard blocker.
- Re-stated that literal family repo renames, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, and unnecessary code churn remain deferred during loop 7.
- Clarified the naming invariant that `writer.module` may already carry future family naming while `writer.repo` stays on the preserved historical lineage ID for each canonical artifact writer.

### 2026-04-12 — canonical writer/module validation pass landed for loop 7

- Added `protocols/tests/test_canonical_writer_module_references.py` as the family-level regression test covering the canonical mixed writer contract across schemas, examples, fixture-backed expected output, lineage rules, and family docs.
- Added `family-canonical-writer-module-validation-2026-04-12.md` as the exact fix-or-note artifact for the bounded validation pass across protocols, fixtures, tests, and control-plane docs.
- Confirmed the family-owned protocol layer still keeps preserved historical writer identities as canonical `writer.repo` values while keeping target family names as canonical `writer.module` values.
- Tightened `AGENTCY_RECAP.md` so the recap now explicitly matches the loop-7 naming invariant already recorded in `AGENTCY_STACK.md` and this progress log.
- No stale family-owned protocol examples or tests were found that prematurely implied a literal repo rename.

### 2026-04-12 — loop 7 findings merged into the control plane

- Merged the completed repo-local audits, package/CLI naming check, canonical writer/module validation, and historical ownership-collision check back into the parent control-plane docs.
- Updated the family checkpoint, stack, and rename-readiness matrix to summarize rename-readiness by repo instead of leaving the findings scattered across individual scorecards.
- Recorded the exact blocker profile per repo:
  - `cli-prsna`: public package/import/CLI surfaces still use `prsna` / `persona`, with import-path churn as the heaviest blocker
  - `brand-os`: hardest blocker profile because naming drift overlaps boundary/ownership drift plus runtime/env/data-path prefixes
  - `cli-mirofish`: upstream MiroFish/AGPL lineage, generic `app` import root, and current public package/bin surfaces block a cosmetic rename story
  - `cli-phantom`: Loom-shaped runtime surfaces are ahead of repo identity, but packaged family-name readiness remains unproven
  - future `cli-metrics`: birth-time naming decisions remain the blocker, not implementation polish
- Re-stated the key control-plane rule that repo rename readiness, package/distribution readiness, import-path readiness, CLI-binary readiness, and runtime-prefix readiness must stay separate in future tasks.
- Kept literal repo renames deferred until the documented blockers are resolved with bounded compatibility and verification work.

### 2026-04-12 — future `agentcy-pulse` birth contract published for loop 7

- Added `cli-metrics-birth-contract-2026-04-12.md` as the loop-7 control-plane birth contract for future `cli-metrics` / `agentcy-pulse` naming readiness.
- Recorded repo absence as the primary blocker and explicitly avoided turning the task into a repo-bootstrap or analytics-design wave.
- Locked the minimum required future surfaces to decide at repo birth: repo directory name, package/distribution name, import path if any, CLI naming, docs/install branding, writer-field expectations, repo-local fixture/test mirroring, and validation commands.
- Re-stated that the only acceptable initial pulse scope remains the already-proven canonical published `social.post` `run_result.v1 -> performance.v1` seam.
- Preserved the current mixed writer contract (`writer.repo = cli-metrics`, `writer.module = agentcy-pulse`) as the canonical family baseline unless a later bounded control-plane task changes it intentionally.

### 2026-04-12 — loop 8 control-plane slice opened for `cli-phantom` / `agentcy-loom`

- Added `family-loop-8-checkpoint-2026-04-12.md` as the new active checkpoint for the bounded `cli-phantom` / `agentcy-loom` package and CLI alias-readiness slice.
- Updated `AGENTCY_STACK.md` so loop 7 now reads as completed rename-readiness evidence and loop 8 is the active single-repo proof surface.
- Updated the stack and progress docs to keep the proof target narrow: `cli-phantom` package metadata, explicit `loom-runtime` / `loom` alias policy, and packaged install/help readiness only.
- Re-stated the canonical ownership invariant for the slice: `run_result.v1.writer = { repo: "cli-phantom", module: "agentcy-loom" }`.
- Kept literal repo renames, umbrella CLI work, MCP-first integration, runtime-prefix migration, broad runtime unification, monolith moves, and cosmetic churn explicitly deferred.

### 2026-04-12 — loop 8 packaged install/help proof merged back into the family control plane

- Added `cli-phantom/docs/packaged-install-help-proof-2026-04-12.md` as the repo-local proof record for the bounded external package/install/help check.
- Verified the exact loop-8 command chain from outside the repo root: `npm pack`, local tarball install, `loom --help`, and `loom help --json`.
- Updated `AGENTCY_STACK.md`, `family-loop-8-checkpoint-2026-04-12.md`, and `rename-readiness-matrix-2026-04-12.md` so the family now records the bounded proof without overstating it as a repo rename or an `agentcy-loom` binary claim.
- Re-stated that the verified installed operator-facing binary is still `loom`, `loom-runtime` remains a transitional package alias, and the mixed writer contract stays `writer.repo = "cli-phantom"` plus `writer.module = "agentcy-loom"`.

### 2026-04-12 — loop 9 packaged install/help proof merged back into the family control plane

- Added `cli-prsna/docs/packaged-install-help-proof-2026-04-12.md` as the repo-local proof record for the bounded external package/install/help check.
- Finalized `family-loop-9-checkpoint-2026-04-12.md` and updated `AGENTCY_STACK.md` plus `rename-readiness-matrix-2026-04-12.md` so the family now records the bounded proof without overstating it as a repo rename, import-path rewrite, or a new installed `agentcy-vox` / `vox` alias claim.
- Recorded the exact loop-9 externally verified command surface: `uv build`, external wheel install, `persona --help`, `persona --version`, `persona export --list`, and unchanged `import prsna` from outside the repo root.
- Re-stated that the verified installed operator-facing binary is still `persona`, the packaged/import surface is still `prsna`, and the mixed writer contract stays `writer.repo = "cli-prsna"` plus `writer.module = "agentcy-vox"`.

### 2026-04-12 — loop 10 re-anchored as the active `brand-os` blocker-reduction slice

- Added `family-loop-10-checkpoint-2026-04-12.md` as the new active checkpoint for the bounded `brand-os` / `agentcy-compass` blocker-reduction and rename-readiness decomposition wave.
- Updated `AGENTCY_STACK.md` so loop 10 is explicitly active, loop 9 is preserved as completed evidence, and the mixed writer contract for `brief.v1` remains `writer.repo = "brand-os"` plus `writer.module = "agentcy-compass"`.
- Updated the progress log so the next queue now points to bounded `brand-os` evidence-first follow-ups instead of leaving loop 9 implicitly active.
- Re-stated that package/import/CLI inventory work and runtime/env/data-path inventory work may proceed only as parallel bounded follow-ups, not as import rewrites, runtime migration, umbrella CLI work, MCP-first integration, monolith moves, or large boundary rewrites.

### 2026-04-12 — loop 10 `brand-os` proof merged back into the family matrix

- Updated `family-loop-10-checkpoint-2026-04-12.md` so the active checkpoint now records the landed bounded proof rather than only the slice opening.
- Updated `rename-readiness-matrix-2026-04-12.md` so the family matrix now reflects the exact loop-10 evidence set: current-surface packaged install/help proof on `brand-os` / `brand_os` / `brandos`, mixed runtime/env/data-path inventory, and explicit separation of naming drift from boundary/ownership drift.
- Re-stated at the family layer that canonical ownership stays `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }` and that the landed proof does not authorize literal renames, import-path changes, umbrella CLI work, MCP-first integration, runtime-prefix migration, or large boundary rewrites.
- Closed loop 10 as completed bounded blocker-reduction evidence while preserving loop 9 as completed packaged proof for `cli-prsna`.

### 2026-04-12 — loop 11 re-anchored as the active `cli-mirofish` compatibility-planning slice

- Added `family-loop-11-checkpoint-2026-04-12.md` as the new active checkpoint for the bounded `cli-mirofish` / `agentcy-echo` attribution-preserving package/import/bin compatibility-planning wave.
- Updated `AGENTCY_STACK.md` so loop 11 is explicitly active, loop 10 is preserved as completed evidence, and the mixed writer contract for `forecast.v1` remains `writer.repo = "cli-mirofish"` plus `writer.module = "agentcy-echo"`.
- Updated the progress log and queue so the next control-plane work now points to bounded `cli-mirofish` inventory and alias-policy follow-ups instead of leaving the `brand-os` slice active.
- Re-stated that literal repo renames, package/distribution rename execution, import-path rewrites, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, and cosmetic churn remain explicitly deferred.

### 2026-04-12 — loop 11 repo-local evidence merged back into the family control plane

- Updated `rename-readiness-matrix-2026-04-12.md` and `family-loop-11-checkpoint-2026-04-12.md` so the family now summarizes the landed `cli-mirofish` alias-policy and proof-boundary evidence without overstating readiness.
- Re-stated the attribution-preserving compatibility policy at the family layer: current shipped surfaces remain `cli-mirofish` / `mirofish-backend` / `app` / `mirofish`, while future family framing must keep explicit upstream MiroFish lineage and AGPL-aware history visible.
- Re-stated that canonical ownership remains unchanged, with `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`.
- Recorded the exact blocker/proof split: the generic `app` import root remains a real rename blocker; repo-local build/help/import proof and the narrow `brief.v1 -> forecast.v1` protocol seam are evidenced for current compatibility surfaces only; clean external wheel-install, external installed-binary proof, and external import proof remain blocked by reproduced `camel-oasis==0.2.5` dependency resolution.
- Kept literal renames, package/distribution rename execution, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, import-path rewrites, and cosmetic churn explicitly deferred.

### 2026-04-14 — checkpoint-driven stack/progress docs sync

- Updated `AGENTCY_STACK.md` so the current bounded synthesis now points to `_agentcy-docs/family-deep-review-checkpoint-2026-04-14.md` rather than implying the loop-12 pulse slice is the whole family readout.
- Made the six current family repos explicit in the stack/progress control plane: `agentcy-compass`, `agentcy-echo`, `agentcy-lab`, `agentcy-loom`, `agentcy-pulse`, and `agentcy-vox`.
- Separated supporting/control-plane surfaces from the family set by recording `cli-agency` as supporting source material and `protocols` as parent protocol authority rather than extra family modules.
- Preserved the mixed writer-contract rules, including `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }`, while clarifying live repo-directory reality.
- Kept the update narrow: no rename execution claims, no umbrella CLI narrative, no MCP-first integration, and no broader runtime-unification claim.

### 2026-04-12 — loop 12 pulse repo-birth evidence merged into the family control plane

- Added `family-loop-12-checkpoint-2026-04-12.md` as the new active checkpoint for the bounded first minimal `cli-metrics` / `agentcy-pulse` repo-birth slice.
- Updated `AGENTCY_STACK.md` and this progress log so loop 11 is preserved as completed evidence and loop 12 is recorded as the active pulse slice.
- Recorded the landed birth-name choices explicitly as repo `cli-metrics`, package/distribution `agentcy-pulse`, import root `agentcy_pulse`, and CLI binary `agentcy-pulse`.
- Re-stated that canonical ownership remains unchanged, with `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }`.
- Recorded the exact proof boundary as `cd cli-metrics && uv sync`, `cd cli-metrics && uv run agentcy-pulse --help`, `cd cli-metrics && uv run python -c "import agentcy_pulse"`, and one family-fixture seam check via `cd cli-metrics && uv run pytest`.
- Kept literal renames, live analytics integrations, warehouse/event abstractions, broad metrics architecture, non-`social.post` analytics expansion, umbrella CLI work, MCP-first integration, runtime unification, monolith moves, and cosmetic churn explicitly deferred.

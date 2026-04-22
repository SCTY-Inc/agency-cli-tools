# Solutions Log

## 2026-04-22 — Repo-local smoke, eval, and study workflows were recovered from mixed local state without restoring generated artifacts
- Problem: several real operator-facing improvements were stranded in a mixed local stash alongside disposable generated pipeline artifacts, which left the repo clean only by hiding useful code rather than integrating it.
- Fix: the durable parts were recovered and shipped — Echo smoke mode plus split graph/report helpers and tests, Vox structured eval cases plus saved eval-report workflows, Compass stage normalization / Claude CLI / honest unsupported surfaces, Pulse study-path recovery, and the small shared protocol helper layer — while generated `artifacts/**` outputs and other low-signal leftovers were intentionally discarded.

## 2026-04-22 — Root `agentcy member --json` now normalizes cross-member machine contracts
- Problem: even after tightening Compass, the suite still had real JSON-shape differences across members (`pulse` emitted a normalized envelope, `vox` used raw global JSON, `echo` mixed raw JSON with `success:false` errors, and `loom` wrapped its own command/data shape). That made root-level automation depend on per-member quirks.
- Fix: the root dispatcher now exposes `agentcy member <member> --json ...`, which injects each member's appropriate JSON mode when possible, captures the member output, and returns one root envelope with normalized `member_status`, `member_command`, `result`, and `stderr` fields.

## 2026-04-22 — Compass now exposes explicit boundaries and a better JSON story
- Problem: Compass was the blurriest member in the suite: persona functionality still lived there even though vox owns personas, and its JSON contract lagged behind the rest of the family because many data-producing commands still relied on per-command `-f json` conventions or human-oriented default formats.
- Fix: Compass now exposes `agentcy-compass catalog --json` for an explicit boundary summary, marks the persona surface as deprecated in favor of `agentcy-vox`, accepts a global `--json` preference across compatible data-producing commands, supports `--json-envelope` for normalized Compass-local success payloads, and routes status/progress chatter through stderr-aware helpers so core operator flows stay cleaner for machine composition.

## 2026-04-22 — Root agentcy now exposes consumable suite catalog and install profiles
- Problem: the suite already had good stage ownership and chainable artifacts, but outside operators still had to infer whether it was a drop-in library, which runtimes were required, and how to install only the surfaces they actually needed.
- Fix: the root dispatcher now exposes `agentcy catalog --json` for machine-readable suite/member ownership and packaging metadata plus `agentcy quickstart --profile ... --json` for install-profile guidance, and the root package now ships optional extras that reflect the Python-side install contours (`echo-simulation`, `compass-all`, `full-python`).

## 2026-04-22 — Echo now seeds structured scenario buckets and Pulse scores synthetic-signal quality
- Problem: Echo could simulate from a fairly flat event seed and the downstream repo-local eval only described run shape, which made it harder to tell whether a forecast came from broad, varied synthetic coverage or from a narrow lane that just happened to stay active.
- Fix: Echo simulation-config generation now normalizes taxonomy-driven `scenario_buckets` into aligned `initial_posts` / `scheduled_events`, preserves bucket metadata through publisher assignment, and `run_eval.v1.json` now reports synthetic-signal metrics such as coverage, local diversity, complexity, and heuristic critic rejection rate. Pulse `study` now ingests those metrics and folds them into the guarded-risk verdict alongside the older round/top-agent checks.

## 2026-04-20 — Echo, Compass, and Loom now fail honestly on unsupported or broken paths
- Problem: several cleanup targets still masked failures or implied support where there was none — Compass had fake-success/placeholder autonomous and optional surfaces, Echo still had duplicated broad-fallback report/process handling, and Loom inspect could drop `run_result.v1` assembly failures from its output.
- Fix: Compass now escalates unsupported autonomous actions via `ManualExecutionRequired` and returns explicit unsupported errors for video generation, Reve, MCP, and loop background mode; Echo centralizes report-failure persistence and simulation-runner shutdown/updater helpers while narrowing expected IO/process catches; Loom `inspect run` now surfaces `runResultError` instead of hiding canonical run-result build failures.

## 2026-04-20 — Named preview bundles now land in stable operator folders
- Problem: the new root pipeline bundle layout was useful, but the default random `pipeline_<id>` folder made repeatable operator runs like GiveCare awkward to compare or reopen.
- Fix: `agentcy pipeline run` now supports `--pipeline-id`, so module-first preview bundles can land at stable paths such as `artifacts/pipelines/givecare-launch-01/` while still emitting `manifest.json`, `bundle_manifest.json`, and `reports/operator_report.md`.

## 2026-04-20 — Compass operator runs can use Claude CLI instead of falling back after Gemini rate limits
- Problem: real GiveCare planning runs were degrading to `mock` after Gemini hit provider-side failures, which made the bundle honest but prevented a clean operator path.
- Fix: Compass planning now accepts `claude-cli` as a local provider, honors root pipeline provider/model forwarding through `BRANDOPS_LLM_PROVIDER` and `BRANDOPS_LLM_MODEL`, and the GiveCare preview path now completes with `provider = "claude-cli"` instead of `mock`.

## 2026-04-20 — Compass activation and Echo full-run automation are more tolerant on the operator happy path
- Problem: Compass activation could fail on near-schema numeric fields like `week` and `budget_allocation`, and full Echo CLI runs could linger in command-waiting mode or miss single-platform action logs needed for downstream artifacts.
- Fix: Compass normalization now coerces numeric activation fields before validation, and Echo CLI automation now uses the non-interactive `--no-wait` simulation path while the single-platform runners rebuild action logs from SQLite trace data for downstream timeline/report assembly.

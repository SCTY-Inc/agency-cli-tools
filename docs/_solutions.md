# Solutions Log

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

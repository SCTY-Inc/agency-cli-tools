# Canonical writer/module validation — protocols, fixtures, tests, and family docs

Date: 2026-04-12
Task: `task-9`
Scope: family-owned protocols, examples, tests, and control-plane docs only

## Validation result

The current family control plane remains internally consistent on the key loop-7 naming rule:

- canonical `writer.repo` values still point at the current literal repo names
- canonical `writer.module` values already point at the target family module names
- no family-owned protocol example or test fixture needed a rename-style rewrite

## Canonical writer pairs validated

| Artifact | Canonical `writer.repo` now | Canonical `writer.module` now |
| --- | --- | --- |
| `voice_pack.v1` | `cli-prsna` | `agentcy-vox` |
| `brief.v1` | `brand-os` | `agentcy-compass` |
| `forecast.v1` | `cli-mirofish` | `agentcy-echo` |
| `run_result.v1` | `cli-phantom` | `agentcy-loom` |
| `performance.v1` | `cli-metrics` | `agentcy-pulse` |

## Surfaces checked

- `protocols/*.schema.json`
- `protocols/examples/*.json`
- `protocols/tests/*`
- `protocols/tests/fixtures/run_result_to_performance_v1/*`
- `protocols/lineage-rules.md`
- `AGENTCY_RECAP.md`
- `AGENTCY_STACK.md`
- `AGENTCY_PROGRESS.md`

## Exact fix-or-note list

### Fixes landed in this task

1. Added `protocols/tests/test_canonical_writer_module_references.py` to lock the mixed canonical writer contract across schemas, examples, fixture-backed expected output, lineage rules, and family docs.
2. Added an explicit naming-rule note to `AGENTCY_RECAP.md` so the recap now matches the stronger loop-7 control-plane wording already present in stack/progress docs.
3. Added this validation note so loop-7 has a concrete family-owned audit artifact listing the exact canonical writer pairs and the checked surfaces.

### Notes from the validation pass

1. No stale family-owned protocol examples were found that prematurely switched `writer.repo` to future family names.
2. No stale family-owned protocol examples were found that left `writer.module` on old repo names for the active canonical artifacts.
3. `cli-metrics` remains intentionally mixed at the family layer: `writer.repo = cli-metrics` and `writer.module = agentcy-pulse` stay canonical until a literal repo decision lands.
4. Repo-local naming audits remain out of scope for this task; this pass does not reopen package/import/CLI/runtime rename readiness inside child repos.
5. Family docs should continue treating rename-readiness as validation-only work; no protocol/example/test rewrite should imply a literal repo rename happened.

## Bounded conclusion

The family-owned protocol layer is currently consistent with the loop-7 naming invariant. The only changes needed here were to make the recap explicit and to add a durable regression test plus a validation note. Repo-local rename-readiness questions should continue through the separate audit artifacts rather than by changing canonical writer fields early.

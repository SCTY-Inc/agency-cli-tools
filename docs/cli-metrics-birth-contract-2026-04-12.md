# cli-metrics birth contract for future `agentcy-pulse` rename readiness

Date: 2026-04-12
Repo under audit: future `cli-metrics` / future `agentcy-pulse`
Task: `task-7`
Scope: loop-7 docs/audit/validation only; no repo bootstrap or literal rename authorized
Summary readiness verdict: the primary blocker is simple and explicit — the repo does not exist yet. The minimum honest loop-7 output is a birth contract that fixes the first naming decisions before implementation creates legacy debt, while keeping scope limited to the already-proven canonical published `social.post` `run_result.v1 -> performance.v1` seam.

## Source docs consulted

- `AGENTCY_RECAP.md`
- `AGENTCY_STACK.md`
- `AGENTCY_PROGRESS.md`
- `CONSOLIDATION.md`
- `family-loop-6-checkpoint-2026-04-12.md`
- `family-loop-7-checkpoint-2026-04-12.md`
- `rename-readiness-matrix-2026-04-12.md`
- `cli-metrics-absence-map-and-performance-v1-readiness-2026-04-12.md`
- `protocols/performance.v1.schema.json`
- `protocols/lineage-rules.md`
- `protocols/adapters/run_result_to_performance_v1.py`

## Purpose

Because `cli-metrics` is still absent, loop 7 should not pretend to audit a real package tree, runtime, or CLI that has not been created yet.
Instead, it should publish the smallest birth contract that future implementation must satisfy on day one so the repo is born with family-aligned naming rather than accumulating avoidable legacy debt.

This contract is intentionally narrower than a bootstrap plan.
It does not design a full analytics product.
It only locks the minimum naming-ready surfaces needed for the already-proven first pulse seam:

- canonical published `run_result.v1` input
- narrow `performance.v1` output
- aggregate published `social.post` observations only
- deterministic validation commands

## Primary blocker

The hard blocker is repo absence.

Today there is:
- no `cli-metrics/` directory
- no package manifest
- no import surface
- no repo-local CLI binary
- no repo-local README or install guide
- no repo-local tests

That means loop 7 cannot honestly claim rename readiness for package/import/CLI/runtime surfaces by inspecting implementation.
The only honest output is a pre-implementation contract for what those surfaces must be when the repo is created.

## Naming surface audit

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory name | no repo exists yet; family docs currently refer to future writer repo as `cli-metrics` | prefer choosing the birth name before creation: either create the repo directly as `agentcy-pulse` or create `cli-metrics` only with an explicit future-rename note on day one | if the repo is born as `cli-metrics`, treat that name as the single temporary literal repo alias until a later approved rename | repo absent; the family has not yet decided whether to avoid future repo rename debt by birthing directly at `agentcy-pulse` or to keep the current literal repo placeholder `cli-metrics` |
| Package/distribution name | none yet | choose one family-aligned distribution at repo birth; recommended default is `agentcy-pulse` unless package-registry constraints force another exact spelling | no alias by default; if a temporary `cli-metrics` package is created, document it as transitional immediately | no manifest exists yet, so any new package name chosen casually later would create unnecessary legacy debt |
| Import path | none yet | choose one explicit public import root if a library surface exists; recommended default is `agentcy_pulse` | no alias by default; only add a shim if downstream imports actually exist | no code/package tree exists yet, so import-path choice is still undecided and should be fixed before implementation |
| CLI binary | none yet | choose one canonical operator-facing binary at birth; recommended default is `agentcy-pulse` if a standalone CLI is needed | none by default; if a temporary `cli-metrics` binary is introduced, pair it with an explicit alias/deprecation policy immediately | no CLI exists yet, so the first binary name chosen will set legacy expectations |
| Docs/install branding | family docs already describe the module as future `agentcy-pulse` while noting repo absence | repo README/CLAUDE/install docs should lead with `agentcy-pulse` module identity and explicitly mention any temporary `cli-metrics` repo/package alias if used | `cli-metrics` may appear only as a literal repo/package alias if that is how the repo is born | repo docs do not exist yet, so branding can still be aligned cleanly at birth |
| Artifact writer fields | canonical family contract is already locked: `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }` | unchanged until a literal repo rename actually lands; if the repo is born directly as `agentcy-pulse`, the family must intentionally update the parent protocol contract in a later bounded pass | none beyond the currently locked mixed writer pair | parent protocol artifacts intentionally keep `writer.repo = cli-metrics` today, so runtime implementation must not silently invent a second writer contract |
| Examples/tests/docs | parent canonical examples, tests, and adapter docs already cover the first seam | future repo-local examples/tests/docs should mirror parent canonical fixtures rather than inventing repo-local authority | optional repo-local mirrors are acceptable only if clearly non-canonical and kept in sync with parent fixtures | repo-local docs/tests do not exist yet, so the birth contract must prevent a second authority from emerging |
| Validation commands | current family-owned validation is parent-level only | future repo birth should include one tiny validation path that proves package/import/CLI naming without widening analytics scope | parent-level protocol validation may remain the authority even if repo-local smoke tests are added | no repo-local command surface exists yet, so validation requirements must be declared before implementation |

## Minimum birth contract

When the future repo is created, it should satisfy the following minimum contract and nothing broader unless a later task expands scope deliberately.

### 1. Scope stays on the proven seam

The repo may only claim the bounded first pulse seam:
- input: canonical published `run_result.v1`
- output: canonical `performance.v1`
- workflow: `social.post`
- observations: aggregate metrics only
- source fixture authority: parent `protocols/examples/run_result.v1.published.json`

It must not broaden into:
- live analytics platform integrations
- generic warehouse abstractions
- non-`social.post` workflows
- dry-run, failed, blog, outreach, or reply analytics
- audience/user-level analytics
- strategy, publishing, or persona ownership

### 2. Naming decisions must be made once at birth

Before the first manifest or README lands, choose and document:
- literal repo directory name
- package/distribution name
- import path if a library API exists
- CLI binary name if a CLI exists
- README/install branding
- alias/deprecation policy if any temporary old name is used

The family should prefer birthing these surfaces correctly instead of promising a future cosmetic cleanup.

### 3. Parent protocol authority remains canonical

Until a later bounded control-plane task says otherwise:
- `performance.v1.writer.repo` remains `cli-metrics`
- `performance.v1.writer.module` remains `agentcy-pulse`
- parent schemas/examples/tests remain the canonical contract
- repo-local mirrors are optional and non-authoritative

### 4. Repo-local implementation should start tiny

The future repo, if created, should begin with only:
- one manifest
- one tiny README/install section
- one importable adapter or CLI entrypoint for the published `run_result.v1 -> performance.v1` seam
- one repo-local smoke test or fixture check that mirrors the parent contract

Anything larger should require a new scoped task.

## Canonical surfaces already aligned

- The family already knows the future module name: `agentcy-pulse`.
- The family already locked the first writer contract at the protocol layer:
  - `writer.repo = "cli-metrics"`
  - `writer.module = "agentcy-pulse"`
- The family already proved the seam without a repo bootstrap through:
  - `protocols/performance.v1.schema.json`
  - `protocols/lineage-rules.md`
  - `protocols/adapters/run_result_to_performance_v1.py`
  - parent-level tests and canonical fixtures
- The first acceptable measurement scope is already narrow and explicit: aggregate metrics for published `social.post` outcomes only.

## Safe legacy aliases

Because the repo does not exist yet, the best legacy-alias policy is to avoid creating one unless necessary.

If the repo is born under `cli-metrics`, the following can be treated as bounded temporary aliases only if documented immediately:
- repo directory `cli-metrics`
- package/distribution name `cli-metrics`
- CLI binary `cli-metrics`

Even in that case:
- `agentcy-pulse` should remain the module identity in family docs
- the repo should not create multiple competing package/import/bin names without an explicit compatibility plan
- repo-local fixtures/docs must still point back to the parent protocol contract as the authority

## Hard blockers to literal naming readiness

### 1. No repo exists to audit

This is the primary blocker.
Until a repo exists, rename readiness outside the parent protocol layer is hypothetical.

### 2. Writer fields are intentionally mixed today

The current family contract is deliberately:
- current writer repo name: `cli-metrics`
- future module name: `agentcy-pulse`

A future implementation must honor that contract unless the family explicitly changes it in a bounded control-plane pass.

### 3. Birth-time package/import/CLI choices are still undecided

If the first implementation lands before these names are fixed, the family will create unnecessary legacy debt immediately.
That is exactly what this birth contract is meant to prevent.

### 4. Scope creep remains a larger risk than naming drift

The family already proved a tiny pulse seam.
The bigger risk now is that a new repo accidentally expands into analytics-platform integration or broad product design instead of staying on the narrow published-`social.post` seam.

## Bounded next actions

1. Keep loop 7 at the control-plane level by publishing this birth contract only.
2. If a future repo-creation task is opened, require it to choose repo/package/import/CLI names before landing code.
3. Reuse the parent canonical schema, lineage rules, adapter behavior, and fixtures rather than redesigning them.
4. Add at most one repo-local smoke test mirroring the parent seam if and when the repo is created.
5. If the family chooses to birth the repo directly as `agentcy-pulse`, schedule a separate bounded control-plane task to reconcile `writer.repo` and related parent docs intentionally rather than by drift.

## Explicit non-goals

This birth contract does not authorize:
- creating the `cli-metrics` repo now
- designing a broad analytics architecture
- adding live platform analytics integrations
- adding warehouse/event-stream abstractions
- widening `performance.v1` beyond published `social.post`
- changing the canonical writer contract right now
- broad cross-repo rename churn

## Minimum validation commands for future repo birth

These commands are the minimum future checks that should exist once the repo is created, while the parent family contract remains authoritative.

### Parent contract checks already available now

```bash
cli-prsna/.venv/bin/python -m pytest protocols/tests/test_performance_v1_protocol.py protocols/tests/test_run_result_v1_protocol.py
cli-prsna/.venv/bin/python -m pytest protocols/tests/test_run_result_to_performance_v1_adapter.py
python protocols/adapters/run_result_to_performance_v1.py protocols/tests/fixtures/run_result_to_performance_v1/sidecar.rich.json
```

### Additional minimum repo-birth checks to require later

Assuming the repo is created with a package/import/CLI surface, require only:

```bash
cd <future-pulse-repo> && <package-manager-install-command>
cd <future-pulse-repo> && <chosen-cli-binary> --help
cd <future-pulse-repo> && python -c "import <chosen-import-path>"
cd <future-pulse-repo> && <chosen-test-command-for-one-smoke-test>
```

The exact commands depend on the stack chosen later, but the contract is that install, help, import, and one fixture-backed seam check must all exist.

## Bottom line

`agentcy-pulse` is already real at the family protocol layer, but not yet as a repo.
The honest loop-7 outcome is therefore not a bootstrap — it is a birth contract.
That contract says the next repo must be born with deliberate repo/package/import/CLI naming, must preserve the currently locked mixed writer contract unless intentionally changed later, and must stay tightly scoped to the proven published `social.post` `run_result.v1 -> performance.v1` seam.
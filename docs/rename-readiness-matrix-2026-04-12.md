# Agentcy family rename-readiness matrix

Date: 2026-04-12
Owner: family control plane
Scope: loop 7 family baseline plus loop-8/9 packaged proof updates, completed loop-10 `brand-os` blocker-reduction evidence, completed loop-11 `cli-mirofish` compatibility-planning evidence, and active loop-12 `cli-metrics` repo-birth evidence

This matrix publishes the family-owned current-vs-target naming view for the bounded rename-readiness waves through active loop 12.
It does not authorize literal repo renames.

## Locked naming rule

Across the family, the writer rule stays:

- `writer.module` tracks the future family module name where the family contract already locked it
- `writer.repo` stays the current literal repo name until a literal repo rename actually lands

That means the canonical writer pairs remain intentionally mixed during loop 7, for example:

- `cli-prsna` / `agentcy-vox`
- `brand-os` / `agentcy-compass`
- `cli-mirofish` / `agentcy-echo`
- `cli-phantom` / `agentcy-loom`
- `cli-metrics` / `agentcy-pulse`

## Family naming matrix

| Future module | Current repo directory | Current package / distribution | Current import / module path | Current CLI binary / invocation | README / CLAUDE branding now | Canonical artifact writer now | Fixture / test references now | Runtime path / prefix surfaces now | Post-rename target | Acceptable legacy alias during transition | Hard blocker to calling this surface rename-ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `agentcy-vox` | `cli-prsna` | Python package `prsna` (`cli-prsna/pyproject.toml`) | `prsna` | `persona` | repo/docs still brand as `cli-prsna` / `prsna` | `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }` | parent protocol tests and examples point to `cli-prsna`, plus repo fixtures under `cli-prsna/tests/fixtures/voice_pack` and loop-9 proof notes under `cli-prsna/docs/packaged-install-help-proof-2026-04-12.md` | repo-local persona storage and docs stay on `~/.prsna/...` conventions | repo: `agentcy-vox`; package/import likely `agentcy-vox` / `agentcy_vox`; CLI likely `agentcy-vox` or family-approved alias | `cli-prsna`, `prsna`, and `persona` may remain as compatibility aliases while install/import/CLI migration is proven | bounded packaged proof now exists for `prsna` + installed `persona` only; import-path migration remains deferred and no future-facing installed alias is proven |
| `agentcy-compass` | `brand-os` | Python package `brand-os` | `brand_os` | `brandos` | repo/docs still brand as `brand-os` / `brandos` | `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }` | parent protocol tests, mirror fixtures, downstream seams, and loop-10 proof notes require `brand-os` writer today | current runtime/install surfaces include `brand-os[...]` extras plus mixed `~/.brand-os/...`, `~/.brandos/...`, `BRANDOS_DATA_DIR`, `BRANDOPS_*`, and `brandos.yml` compatibility surfaces | repo: `agentcy-compass`; package/import likely `agentcy-compass` / `agentcy_compass`; CLI likely `agentcy-compass` or approved alias | `brand-os`, `brand_os`, and `brandos` may remain only as bounded compatibility aliases while runtime/env/data-path migration is proven | hardest blocker profile in family: naming drift overlaps ownership drift; bounded proof now exists only for the current `brand-os` / `brand_os` / `brandos` compatibility surfaces, while boundary drift and runtime/env/data-path migration remain unresolved |
| `agentcy-echo` | `cli-mirofish` | Python package `mirofish-backend` | `app` plus repo-local `cli-mirofish` references | `mirofish` | repo/docs and product language still brand as `MiroFish` / `cli-mirofish` | `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }` | canonical examples/tests assert `cli-mirofish` writer and repo paths, while loop-11 repo-local proof docs now live under `cli-mirofish/docs/rename-readiness-scorecard-2026-04-12.md` and `cli-mirofish/docs/packaged-compatibility-proof-boundary-2026-04-12.md` | scripts and services rely on repo-local `scripts/` pathing and MiroFish-named docs/runtime seams | repo: `agentcy-echo`; package/import likely family-aligned later; CLI likely `agentcy-echo` or approved alias | `cli-mirofish`, `mirofish-backend`, `mirofish`, upstream `MiroFish` branding, and internal legacy/runtime identifiers may need to persist as explicit compatibility/reference aliases | upstream coupling and AGPL/history constraints mean package/import/CLI renames cannot be treated as a simple cosmetic pass, and the generic `app` import root remains a distinct blocker rather than a rename-ready alias |
| `agentcy-loom` | `cli-phantom` | Node package `loom-runtime` in `cli-phantom/runtime/package.json` | runtime modules under `src/...`; canonical family writer uses `agentcy-loom` but repo/runtime still say loom/phantom | installed local package binary now proven as `./node_modules/.bin/loom` via external tarball install; source invocation `cd runtime && npx tsx src/cli.ts ...` remains a transitional developer path | `cli-phantom` repo, `Loom Runtime` docs, and `brand.yml` runtime language coexist | `run_result.v1.writer = { repo: "cli-phantom", module: "agentcy-loom" }` | parent protocol tests and runtime fixtures assert `cli-phantom` writer and repo path | `runtime/`, `state/`, `brands/`, and review/publish run-state paths remain loom/phantom-specific | repo: `agentcy-loom`; package likely `agentcy-loom`; import/package/bin naming still to be normalized; CLI likely `agentcy-loom` once packaged, with `loom` preserved as an operator alias candidate | `cli-phantom`, `loom-runtime`, `loom`, and direct `npx tsx src/cli.ts` invocation may remain temporarily | mixed phantom-vs-loom naming across repo, package, and invocation surfaces; bounded packaged help proof now exists, but it does not justify a repo rename or an `agentcy-loom` binary claim |
| `agentcy-pulse` | `cli-metrics` | Python package `agentcy-pulse` in `cli-metrics/pyproject.toml` | `agentcy_pulse` | `agentcy-pulse` | repo-level birth branding now exists only for the minimal pulse slice; broader family branding/readiness remains intentionally unproven | `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }` remains locked at the family protocol layer | parent examples/tests/adapters already reference `cli-metrics` as writer repo and `agentcy-pulse` as module; loop-12 checkpoint now records the landed repo-birth proof boundary | no broader runtime path/prefix surface is proven yet beyond the minimal repo birth and its thin seam wrapper | repo remains `cli-metrics`; package/import/bin birth choices are now landed as `agentcy-pulse` / `agentcy_pulse` / `agentcy-pulse`; any later rename requires a separate bounded task | no broader alias policy is implied yet beyond the landed birth surfaces | bounded repo birth is now proven, but rename readiness, live analytics readiness, runtime-prefix policy, and broader ownership remain explicitly deferred |
| `agentcy-lab` | shared eval/autoresearch layer, no single canonical repo | no single package | no single import path | no single CLI binary | family-only naming in recap/stack docs | no locked production artifact writer; cross-cutting plane only | no canonical production fixtures keyed to one repo | no unified runtime path/prefix surface | family may later publish a concrete repo/package/CLI shape if needed | none yet beyond descriptive family references | intentionally deferred; not part of the current literal rename queue |

## Cross-family interpretation

## Smallest-next-actions summary

### Repo-by-repo control-plane summary

| Repo / future module | Artifact-writer readiness | Repo rename readiness | Package / import / CLI readiness | Exact blocker summary | Smallest next actions |
| --- | --- | --- | --- | --- | --- |
| `cli-prsna` -> `agentcy-vox` | ready now: canonical `voice_pack.v1` already uses `{ repo: "cli-prsna", module: "agentcy-vox" }` | not ready yet | partially proven but not rename-ready: packaged external install/help proof exists for `prsna` + `persona` only | public package `prsna`, import root `prsna`, and binary `persona` are all still real public surfaces; loop 9 proved the current packaged operator path only, while import-path migration remains the heaviest blocker and no new alias is proven | keep `writer.repo` unchanged; record loop-9 proof as `persona`-only packaging evidence; defer import-path changes; choose any future package/bin target before making a rename claim |
| `brand-os` -> `agentcy-compass` | ready now: canonical `brief.v1` already uses `{ repo: "brand-os", module: "agentcy-compass" }` | not ready yet | bounded current-surface proof exists, but rename readiness does not | hardest blocker profile: boundary/ownership drift remains real, while package `brand-os`, import `brand_os`, binary `brandos`, and mixed runtime/env/data-path prefixes are all still live compatibility surfaces | keep `brand-os` as canonical repo writer; treat loop 10 as current-surface proof plus blocker decomposition only; narrow the public repo boundary before any rename; keep runtime/env prefix migration separate; do not convert packaged/help proof into an import-path or repo-rename claim |
| `cli-mirofish` -> `agentcy-echo` | ready now: canonical `forecast.v1` already uses `{ repo: "cli-mirofish", module: "agentcy-echo" }` | not ready yet | active bounded compatibility-planning slice with current-surface proof, but not rename-ready | explicit alias policy now preserves current compatibility surfaces (`cli-mirofish` / `mirofish-backend` / `app` / `mirofish`) plus upstream `MiroFish` attribution; the generic import root `app` remains a deep blocker; repo-local build/help/import and narrow protocol proof now exist only for current surfaces; clean external wheel-install proof remains blocked by `camel-oasis==0.2.5` dependency resolution | preserve explicit MiroFish lineage; keep loop 11 on attribution-preserving package/import/bin compatibility planning; treat `app` as a real import-root blocker; record the current proof boundary as current-surface-only; decide package/import/bin target once before any future rename; do not touch public names until external dependency/install blockers and attribution policy are resolved |
| `cli-phantom` -> `agentcy-loom` | ready now: canonical `run_result.v1` already uses `{ repo: "cli-phantom", module: "agentcy-loom" }` | not ready yet | partially aligned but not rename-ready | runtime package/docs/CLI are Loom-shaped, and bounded external packaged help proof now exists for installed `loom`; repo identity still remains `cli-phantom`, no `agentcy-loom` binary claim is proven, and runtime-prefix migration policy is undefined | keep mixed state explicit; treat `loom-runtime` as transitional and `loom` as the verified installed alias; do not escalate the proof into a repo/package rename claim |
| `cli-metrics` -> `agentcy-pulse` | ready now at protocol and bounded repo-birth layer: canonical `performance.v1` uses `{ repo: "cli-metrics", module: "agentcy-pulse" }` and the minimal repo birth now exists | not rename-ready yet | bounded birth surfaces now proven only for package `agentcy-pulse`, import `agentcy_pulse`, and CLI `agentcy-pulse` | loop 12 proves only install/help/import plus one family-fixture seam check; it does not prove live analytics, broad package/import migration readiness, runtime-prefix policy, or a later repo rename story | keep the loop-12 birth names and proof boundary explicit; preserve the mixed writer contract; open any broader analytics or rename work only via a new bounded control-plane task |

### Public-surface summary across the family

| Surface | Family-wide status | What must happen before this surface can be called rename-ready |
| --- | --- | --- |
| Repo directory name | deferred across the family | keep `writer.repo` on current repo names; inventory repo-path references; prove bounded path updates without hidden assumptions |
| Package / distribution name | not ready in any current repo | choose one target per repo; define compatibility/alias policy; verify install still works |
| Import path | heaviest technical blocker in Python repos | inventory downstream imports; decide whether shims exist; prove at least one import smoke test |
| CLI binary | mixed, but not family-normalized | choose one canonical future binary per repo; keep old binary aliases explicit; verify `--help`, `--json`, and one representative command |
| Docs / install branding | easy to drift, not sufficient on its own | update docs only after package/bin/repo plans are explicit so docs do not imply renames happened early |
| Runtime paths / env / local state prefixes | mostly deferred | treat these as compatibility migrations, not cosmetic renames; inventory persisted keys and env vars before changing anything |

### Ambiguous ownership and authority decisions still open

- `brand-os` remains the main repo-level ambiguity: canonical `brief.v1` ownership is settled, but the repo boundary is still broader than future `agentcy-compass`, still carries residual `cli-agency` narrative gravity, and now has explicit loop-10 evidence showing that naming drift and boundary/ownership drift must be tracked separately.
- `cli-mirofish` keeps an intentional split between family module identity (`agentcy-echo`) and upstream MiroFish lineage; future naming work must preserve attribution rather than pretending the repo is lineage-free.
- `cli-prsna` keeps an intentional split between family module identity (`agentcy-vox`) and current public surfaces (`prsna`, `persona`, `prsna` import); loop 9 now proves the current packaged external operator path for `persona` only, and future work must not collapse package/import/CLI migration into a repo rename claim or pretend a new installed alias already ships.
- `cli-phantom` keeps an intentional split between repo identity (`cli-phantom`) and Loom-shaped runtime/package/docs surfaces; bounded proof now shows `loom-runtime` can be installed locally and exposes installed `loom` help from outside the repo root, but future work still must not inflate that into a repo rename or `agentcy-loom` binary claim.
- `cli-metrics` now exists as the bounded pulse repo-birth surface, but any later repo-rename question remains explicitly deferred behind a separate bounded control-plane task.

### Canonical surfaces already aligned

- Future family module names are already canonical at the artifact level through `writer.module`.
- Parent protocol schemas, examples, and tests already encode the future module names:
  - `agentcy-vox`
  - `agentcy-compass`
  - `agentcy-echo`
  - `agentcy-loom`
  - `agentcy-pulse`
- The family control plane already treats repo-name and module-name alignment as separate questions.

### Surfaces intentionally not yet aligned

- repo directory names
- package / distribution names
- import paths
- installed CLI names
- runtime data paths, env vars, and local state prefixes
- README / CLAUDE branding that still describes current repo identity

These remain current-name-first until a literal rename is justified and verified.

## Active loop-11 family readout for `cli-mirofish`

Loop 11 is the active bounded `cli-mirofish` slice, and the family-level interpretation is now explicit:
- canonical ownership stays `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`
- the active planning surface applies only to the current `mirofish-backend` package/distribution, `app` import root, and `mirofish` installed CLI surfaces
- the repo-local alias policy is attribution-preserving: current names remain acceptable compatibility aliases while future family framing must keep upstream MiroFish fork lineage and AGPL-aware history explicit
- the generic `app` import root is treated as a real blocker that requires compatibility planning, not a cosmetic rename candidate
- the exact loop-11 proof boundary is current-surface-only: repo-local build/help/import and the narrow `brief.v1 -> forecast.v1` protocol seam are proven, while clean external wheel-install, external installed-binary proof, and external import proof remain blocked by reproduced `camel-oasis==0.2.5` dependency resolution
- literal renames, package/distribution rename execution, import-path changes, umbrella CLI work, MCP-first integration, runtime unification, and large rewrites remain explicitly deferred

## Minimal verification evidence before any rename can be called ready

A surface is not rename-ready just because the desired family name is known. The family needs the smallest evidence below.

### 1. Repo directory rename readiness

Required evidence:
- current family docs and repo-local docs agree on the target module mapping
- no canonical artifact changes `writer.repo` early
- parent protocol tests and repo-local tests can be updated in a bounded diff without discovering hidden path assumptions everywhere
- explicit inventory of repo-path references in docs, fixtures, scripts, CI, and task instructions
- a rollback-safe alias or transition note exists for operators

Minimum proof:
- one audited inventory document
- one grep-based reference scan saved in task evidence
- one bounded test pass after updating only path references in a dry-run branch or review plan

### 2. Package / distribution rename readiness

Required evidence:
- current published or local install surface is inventoried
- package rename target is chosen once
- install docs and dependency references are enumerated
- compatibility story is explicit: alias package, major-version break, or unpublished/internal-only move
- editable install and clean install both still work under the proposed naming plan

Minimum proof:
- manifest audit (`pyproject.toml` or `package.json`)
- install command verification from a clean environment or equivalent documented check
- `--help` or package import still works under the migration plan

### 3. Import-path rename readiness

Required evidence:
- all public import paths are inventoried
- downstream repo references and protocol tests are counted
- shim/alias policy is defined if imports change
- repo-local examples and docs are updated consistently

Minimum proof:
- code search / grep inventory of imports
- at least one import smoke test from downstream or fixture-backed integration code
- explicit decision on whether old import paths remain supported temporarily

### 4. CLI-binary rename readiness

Required evidence:
- one canonical binary target is chosen
- automation, docs, scripts, and examples using the old binary are inventoried
- `--help`, `--json`, and at least one representative command continue to work
- alias behavior is explicit if the old binary remains temporarily

Minimum proof:
- binary/help check
- one JSON-mode command check
- one representative workflow command check
- docs/install section updated or a deliberate deferral recorded

## Family-wide non-goals

This matrix does not authorize:
- literal family repo renames now
- broad import rewrites now
- umbrella CLI work
- MCP-first integration
- runtime unification
- monolith moves
- package churn done only for cosmetic alignment

## Suggested use in loop 7

Repo-local audits should cite this matrix and then publish repo-specific tables using the same fields:
- current canonical
- post-rename target
- acceptable legacy alias
- hard blocker

That keeps the family on one naming contract while each repo proves readiness honestly and independently.

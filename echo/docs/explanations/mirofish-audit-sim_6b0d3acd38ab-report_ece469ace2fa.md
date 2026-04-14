# MiroFish simulation/report audit: `sim_6b0d3acd38ab` / `report_ece469ace2fa`

> Diátaxis: explanation
> Date: 2026-03-16
> Scope: end-to-end audit of the simulation preparation flow, runtime behavior, report generation, language drift, and Codex CLI fit for this workload.

## TL;DR

The graph/workbench direction is solid, but the current Codex CLI-backed runtime/report path is not reliable enough for serious multi-agent simulation yet.

**Bottom line:** this is a strong graph-first prototype, but not yet a trustworthy end-to-end simulation/reporting system.

## Quick scorecard

- **Graph extraction / ontology / entity modeling:** good
- **Workbench / task orchestration concept:** good
- **Preparation pipeline correctness:** mixed
- **Simulation runtime quality:** weak
- **Report generation reliability:** weak
- **Codex CLI as backend for OASIS + report interviews:** weak

## 1) What actually happened

### A. Graph layer: decent

The graph for this run was coherent:

- **28 nodes**
- **10 edges**
- entity types included:
  - `FamilyCaregiver`
  - `CareSeekingFamily`
  - `HomeHealthAide`
  - `ChildcareProvider`
  - `StateLegislator`
  - `IndustryAssociation`
  - `AdvocacyGroup`
  - `Organization`
  - `FederalAgency`

#### Assessment

This is the strongest part of the system right now.

#### Limitation

It is still sparse:

- 28 nodes / 10 edges is enough to be useful
- but not enough to support especially rich emergent social dynamics by itself

So the current graph is:

- good for structured foresight
- not yet rich enough for high-confidence simulation claims

### B. Preparation pipeline: it completed, but not cleanly

There were **two different prepare tasks** for the same simulation:

- `c37299e4-bdbf-4986-b177-60351845d7f0`
- `decc4c81-976f-4fb4-9fee-48acdcbbe228`

Both ended `completed`.

#### Why that is a problem

The system allowed concurrent preparation for the same simulation ID.

That means artifacts for a single run could be:

- regenerated
- overwritten
- partially out of sync
- mutated while the simulation is already starting

That is a correctness bug, not just a performance issue.

#### Root cause

There is no per-simulation lock in:

- `backend/app/tools/prepare_simulation.py`

It checks whether the simulation is already prepared, but it does not prevent:

- prepare while preparing
- prepare while running
- duplicate background tasks for the same simulation

### C. Simulation runtime: completed, but weak quality

The run did finish:

- `runner_status: completed`
- `current_round: 168 / 168`
- `completed_at: 2026-03-16T17:06:27`

So technically it was:

- not stuck
- not crashed
- completed

#### But meaningful activity was extremely low

From the action logs:

- **Twitter meaningful actions:** 22
- **Reddit meaningful actions:** 14
- across **168 rounds**

And the meaningful actions were only:

- `CREATE_POST`

There was no meaningful volume of:

- replies/comments
- likes
- reposts
- follows
- debate chains

#### DB evidence

The simulation DBs were dominated by low-value events:

- `twitter_simulation.db`
  - `refresh`: 954
  - `sign_up`: 28
  - `interview`: 17
  - `create_post`: 11
- `reddit_simulation.db`
  - `refresh`: 291
  - `sign_up`: 10
  - `create_post`: 7

#### What this means

The simulation mostly did:

- sign-up
- refresh
- almost no social dynamics

So even though it ran 168 rounds, it did not produce much emergent behavior.

This is a major issue.

### D. Cross-platform population inconsistency

The live DB user counts were:

- `twitter_simulation.db` → **28 users**
- `reddit_simulation.db` → **10 users**

That means the two platforms were not actually running with the same prepared population.

#### Why this is serious

The run is internally inconsistent:

- Twitter had one agent population
- Reddit had a smaller one

That makes cross-platform conclusions shaky.

#### Likely cause

This strongly matches the earlier prep-race issue:

- one prep task completed
- another kept writing/re-preparing
- the simulation launched against unstable artifacts

## 2) Telemetry / state tracking problems

### A. `state.json` is stale / wrong

Even after success/completion, `backend/uploads/simulations/sim_6b0d3acd38ab/state.json` still showed old state such as:

- old `LLM_API_KEY is not configured`
- `twitter_status: not_started`
- `reddit_status: not_started`

Even though the run had already completed.

### B. `run_state.json` is also partly wrong

Examples included:

- `simulated_hours: 0`
- `rounds_count: 0`
- stale `updated_at`
- recent actions frozen early

### C. Action logger total rounds bug

In:

- `backend/scripts/action_logger.py`

simulation start logging sets:

- `total_rounds = total_simulation_hours * 2`

So with 168 hours it reported **336 rounds**, which is wrong for this config.

Actual config was:

- `minutes_per_round: 60`
- so it should be **168 rounds**

#### Assessment

Telemetry is currently not a reliable source of truth.

## 3) Why the simulation quality was poor

This is probably the biggest architectural finding.

### The CLI bridge is not feature-complete for OASIS

In:

- `backend/app/utils/oasis_llm.py`

runtime logs repeatedly showed:

- `CLIModel ignores tool schemas; tool calling is not supported in OASIS CLI mode`

#### Why this matters

OASIS/CAMEL expects richer model behavior around tool schemas and structured interaction.

But the CLI bridge currently just wraps Codex into a plain-text completion shim.

So the runtime is effectively:

- pretending to be OpenAI-compatible
- while dropping tool-calling semantics

#### Likely outcome

That is likely why the run showed:

- almost no real interaction behavior
- mostly refresh/no-op behavior
- very shallow action diversity

#### Strong conclusion

**Codex CLI via the current shim is not a good fit for OASIS runtime behavior.**

It can run, but it does not run well enough.

## 4) Report generation audit

### A. The report failed

Report ID:

- `report_ece469ace2fa`

Current state:

- `meta.json` → `status: failed`
- `progress.json` → failed
- no `section_04.md`
- no assembled full report markdown

Failure:

- `Codex CLI timed out after 180s`

Task:

- `e92dfc59-c13b-4ca3-8787-f245d99e473b`
- `status: failed`

So the report shown in the UI is partial, not final.

### B. What did complete

These files were generated:

- `section_01.md`
- `section_02.md`
- `section_03.md`

Then generation failed on:

- section 4

#### Timing

The report took roughly 30+ minutes before failing, which is too slow for this workflow.

### C. Why the report turned Chinese

This is clear from the code and artifacts.

#### Root cause 1: no explicit English target is enforced

In:

- `backend/app/services/report_agent.py`

there is language-consistency logic that says if the requirement/source are Chinese, the report should be in Chinese.

But it does not symmetrically enforce the opposite case:

- if requirement/source are English, force the report to stay in English

So the language policy is asymmetrical.

#### Root cause 2: the model drifted into Chinese during generation

This happened visibly in the report logs.

Section 1 started with English tool queries, but later section tool calls shifted into Chinese, including Chinese `insight_forge` and `report_context` prompts.

Once the model started operating in Chinese, later sections reinforced that choice.

#### Root cause 3: parts of the toolchain are Chinese-biased

In:

- `backend/app/services/kuzu_tools.py`

there is Chinese-specific post-processing such as:

- Chinese sentence splitting
- Chinese punctuation `。`
- Chinese marker cleanup

So the retrieval/interview summarization layer is not language-neutral.

#### Why the quotes got translated

The prompt explicitly says quoted tool content should be translated into the report language.

So once the report language drifted to Chinese, the system intentionally translated English evidence into Chinese.

That is why a Chinese report appeared even though the scenario itself was English.

### D. Report quality: readable, but overstates the simulation

The partial report is not nonsense. Sections 1–2 are reasonably readable.

But there are serious limitations.

#### Good

- coherent structure
- decent narrative flow
- some honest caveats
- Section 3 explicitly admits when interviews timed out and evidence is thin

#### Bad

It is built on a very narrow evidence base:

- sparse graph
- very few actual simulation actions
- repeated reliance on the same small set of facts
- repeated use of interview outputs rather than emergent timeline data

#### Big conceptual issue

Because the simulation itself produced very little real behavior, the report is not really reporting on rich emergent social dynamics.

It is closer to:

- graph facts
- agent profiles
- interview outputs
- extrapolated narrative synthesis

That is not the same thing as a strong multi-agent forecast.

## 5) Interview system issues

### A. Report interviews timed out

In Section 3:

- `Agent Interview` returned `0 interviewed / 28`
- timeout waiting for command response after **180s**

So report generation lost one of its core evidence channels mid-run.

### B. Post-run interview path hit OS arg length failure

Later there was also:

- `OSError: [Errno 7] Argument list too long: 'codex'`

This comes from:

- `backend/app/utils/llm_client.py`

because it calls:

- `subprocess.run(["codex", "exec", "--skip-git-repo-check", prompt], ... )`

That means the entire prompt is passed as a command-line argument.

When interview prompts become large, Linux rejects it.

#### This is a direct bug

Fix:

- pass prompt via stdin
- or a temp file
- not argv

## 6) Recurring patterns that should be addressed

### Pattern 1: mutable artifacts / race conditions

The same simulation ID can be:

- re-prepared twice
- run while artifacts are still changing
- reported on while state is stale

#### Fix

- add per-simulation lock
- disallow prepare when status is `PREPARING` or `RUNNING`
- make run snapshots immutable:
  - freeze `reddit_profiles.json`
  - freeze `twitter_profiles.csv`
  - freeze `simulation_config.json`
  - copy them into a run-specific folder before launching

### Pattern 2: state truth is fragmented

There are multiple semi-truths:

- task files
- `state.json`
- `run_state.json`
- logs
- report progress

They drift.

#### Fix

- choose one source of truth for runtime state
- derive frontend progress from that
- always clear old `error` fields on rerun
- write status transitions atomically

### Pattern 3: Codex CLI timeouts everywhere

There were 180s timeouts in:

- persona generation
- report generation
- interviews

#### Fix

- shorter prompts
- shorter personas
- fewer live interviews
- lower batch sizes
- cache persona outputs
- avoid using CLI for heavy report sections

### Pattern 4: real-entity safety friction

Named real actors caused issues, including:

- `Trump administration`
- `New York City`
- earlier also `AARP` and `Federal government`

These are exactly the entities most likely to trigger:

- refusals
- fictionalization
- de-impersonation language

#### Fix

For real governments, public institutions, and national organizations:

- stop asking for a high-fidelity social media persona
- use a safer institutional stance template instead
- for example: mission, incentives, tone, likely policy posture, risk tolerance
- not “reconstruct their voice”

### Pattern 5: OASIS runtime depends on features the CLI shim does not support

This is the deepest recurring problem.

#### Fix options

1. **Best fix:** use a real API model for runtime/report
2. **If subscription-only:** stop using the current OASIS tool-calling runtime and replace it with a simpler simulation architecture

## 7) Is using the subscription right for this?

### Honest answer

**As currently architected: no, not for the whole pipeline.**

#### Codex CLI subscription is okay for:

- translation
- code refactors
- ontology extraction
- graph/entity prep
- maybe short persona generation

#### It is not a good fit here for:

- long-running multi-agent OASIS runtime
- batch interviews
- tool-rich report generation
- huge prompt payloads

#### Why

The system is paying the price of:

- subprocess startup
- CLI latency
- no true tool-calling compatibility
- OS argument-size limits
- weak throughput under batch workloads

And the artifacts make this clear:

- the simulation ran but produced poor dynamics
- the report took ~30 minutes and failed
- interviews timed out
- post-run interviews hit argv overflow

#### Verdict

If Codex CLI remains the only backend, the architecture will keep fighting the tool.

## 8) What to do instead

### Best path: hybrid architecture

Keep Codex CLI for:

- development
- translation
- graph/ontology extraction
- possibly persona drafting

Use an API model for:

- OASIS runtime
- report generation
- interview / synthesis steps

That is the cleanest, most pragmatic split.

### If the project must stay subscription-only

Then the current OASIS approach should not stay as-is.

Instead, redesign toward a lighter panel-simulation workflow:

- generate structured personas once
- run batched future rounds with summary prompts
- produce:
  - likely reactions
  - coalition shifts
  - pressure points
  - timeline deltas

But do not keep a tool-calling social simulation with live interviews on top of a CLI shim.

That would fit CLI much better.

## 9) What to fix first

### P0 — must fix

1. **Per-simulation locking**
   - prevent duplicate prepare/report tasks for the same simulation
2. **Immutable run snapshots**
   - no artifact mutation after launch
3. **State cleanup**
   - remove stale `LLM_API_KEY` error
   - unify runtime status
4. **Explicit target language**
   - derive `report_language = en`
   - enforce it in prompts and validation
   - detect CJK drift before finalizing sections
5. **Fix Codex argv bug**
   - use stdin or tempfile, not argv
6. **Stop pretending CLI fully supports tool-calling runtime**
   - either replace that path or clearly disable unsupported behavior

### P1 — high ROI

7. **Shorter personas**
8. **Template-based personas for real institutions**
9. **Cache personas**
10. **Reduce live report interviews**
11. **Use logs/actions instead of costly live interviews where possible**
12. **Lower round counts for CLI runs**

### P2 — quality upgrades

13. **Improve graph density**
14. **Improve edge extraction**
15. **Make UI show partial/failed report honestly**
16. **Fix action telemetry** (`total_rounds`, simulated hours, etc.)

## 10) What to do with this current run/report

### Simulation run

Treat it as:

- debugging evidence
- not production analysis

### Current report

Treat it as:

- partial draft
- failed
- not final

#### Can it be scrubbed back to English?

Yes, but that splits into two tasks.

##### A. Cosmetic scrub

Sections 1–3 can be translated back to English.

That is easy.

##### B. Real fix

That does not solve:

- missing section 4
- report failure state
- sparse evidence
- weak simulation dynamics

So translation alone is not enough.

#### Preferred approach

- mark this report as partial/failed
- keep it as a debugging artifact
- regenerate only after language enforcement, timeout reduction, interview fixes, and runtime/backend decisions

## 11) Final judgment

### What is strong

- graph extraction
- workbench/session/task direction
- modular backend cleanup

### What is weak

- runtime simulation fidelity
- task locking/state correctness
- report robustness
- subscription-backed runtime throughput

### Overall call

This is worth continuing, but not on the assumption that the current Codex-CLI-backed OASIS/report stack is almost there.

What is real and worth building on:

- the graph
- the structured workbench
- the simulation prep ideas
- the report UX concept

What needs a decisive change:

- backend choice for runtime/report
- language control
- task locking
- evidence grounding

## Recommended next actions

1. Add a duplicate-prepare/report lock.
2. Fix stale state and telemetry truth.
3. Fix Codex CLI prompt transport (`stdin`/tempfile instead of argv).
4. Enforce explicit report language.
5. Decide whether runtime/report stay on CLI or move to an API-backed path.
6. Rerun only after the race-condition and state bugs are fixed.

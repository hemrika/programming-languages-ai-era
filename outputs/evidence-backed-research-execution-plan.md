## Version

v0.5 (2026-05-02) — current. Prior versions (v0.1 5-dimension, v0.2 6-dimension, v0.3 7-dimension, v0.4 10-dimension with native/ecosystem split + dependency-risk) are visible in git history.

## v0.4 → v0.5 changelog

v0.5 adds an eleventh dimension — `reachability_to_top_tier` (5%) — scoring forward-trajectory plausibility: how reachable is 5.0 on each below-5 cell within a 3–5-year horizon. The new dimension is funded by reducing `strategic_viability` from 10% to 5%, since SV had implicitly absorbed some forward-trajectory signal that the new axis captures explicitly.

- New: `reachability_to_top_tier` (5%) — anchored on gap_size + in_motion_signals + steward_investment + structural_vs_ecosystem + compounding_pressure
- `strategic_viability` 10% → 5%

The ranking compresses at the top under v0.5: TypeScript and Go tie at 4.01 (TypeScript catches Go via Reach=4.0); .NET sits at 3.99 with the cohort's strongest forward bet (EDR=4.5, Reach=4.5 — both highest). Per-language gap analysis lives in `outputs/reachability-analysis.md`.

## v0.3 → v0.4 changelog

v0.3 conflated language-native AI capability with ecosystem-package AI capability and applied inclusion rules asymmetrically (Pydantic credited to Python's structured-output score; Newtonsoft.Json was omitted from .NET's). v0.4 split the two AI-era dimensions into native + ecosystem halves and introduced an ecosystem-dependency-risk axis:

- `ai_systems_interoperability` (15%) → `ai_systems_native` (7.5%) + `ai_systems_ecosystem` (7.5%)
- `structured_output_maturity` (10%) → `structured_output_native` (5%) + `structured_output_ecosystem` (5%)
- New: `ecosystem_dependency_risk` (5%) — funded by reducing `runtime_ecosystem` from 15% to 10%

Combined AI-systems weight (15%) and combined structured-output weight (10%) were unchanged from v0.3. Every claim about a specific library carries a `backer:` field. The native/ecosystem split is documented in `framework/dimensions.md`.

# Evidence-Backed Research Execution Plan

## Objective

Move the project from a framework scaffold to a defensible, evidence-backed assessment of programming languages in the AI era.

The goal is not to produce opinions about languages. The goal is to produce traceable conclusions where every evaluation can be inspected through this chain:

```text
Insight → Evaluation → Claim → Source
```

## Operating principles

1. No score without justification.
2. No major claim without a source.
3. No conclusion without counterclaims.
4. Counterclaims are linked to the positive claim they qualify, via a `counters:` field on the counterclaim.
5. Separate facts, interpretations, predictions, and speculation.
6. Prefer primary sources, specifications, official docs, empirical studies, and reproducible data.
7. Keep claims atomic.
8. Keep evaluations structured.
9. Treat every score as provisional until reviewed.
10. **Greenfield framing is a constraint, not a flavor.** Installed base, code volume, and incumbent gravity are not credited as advantages. The question being answered is: starting a new AI-era project today, what would you choose?

## Research workflow

```text
Source discovery
  → Source triage
  → Atomic claim extraction
  → Claim normalization (with counters: links)
  → Language evaluation updates
  → Cross-language comparison
  → Insight synthesis
  → Review and challenge
  → Final output
```

## Phase 1 — Baseline inventory

### Goal

Establish the initial research universe.

### Scope

Cohort languages (10):

- python
- typescript
- dotnet (C#)
- java
- kotlin
- rust
- go
- swift
- elixir
- cpp

The cohort was reduced from 13 to 10 by dropping Mojo and Zig (pre-1.0), Julia (narrowly numerical), and Haskell (a verification reference rather than a default). The remaining 10 cover the languages a greenfield team is actually deciding between.

Evaluation dimensions (10) and current weights:

| Dimension | Weight |
|---|---:|
| Human cognition (HC) | 15% |
| Machine cognition (MC) | 15% |
| AI-agent operability (AO) | 20% |
| Runtime and ecosystem (RE) | 10% |
| Strategic viability (SV) | 10% |
| AI-systems native (AIN) | 7.5% |
| AI-systems ecosystem (AIE) | 7.5% |
| Structured-output native (SON) | 5% |
| Structured-output ecosystem (SOE) | 5% |
| Ecosystem dependency risk (EDR) | 5% |

Greenfield framing is an explicit constraint: forward-looking properties (governance, future fit, AI-training representation, ecosystem velocity, ecosystem viability for new projects) are credited; legacy installed base is not.

Scores use the 9-level half-point rubric (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0); see `framework/scoring-rubric.md`.

### Tasks

- Confirm the 10-language cohort.
- Confirm the 7 evaluation dimensions.
- Confirm scoring weights.
- Identify missing criteria.
- Mark all existing scores as draft.

### Deliverables

- Updated `framework/evaluation-framework.md`
- Updated `framework/dimensions.md`
- Updated `framework/scoring-rubric.md`
- One baseline comparison table

### Exit criteria

- Every cohort language has an evaluation YAML file with all 7 dimensions scored.
- Every draft score has a confidence value and a justification.
- Half-point scores are used only where they record genuine differentiation.

## Phase 2 — Source acquisition

### Goal

Collect credible sources for each language and criterion.

### Source types

| Source type | Preferred use |
|---|---|
| Official documentation | Language semantics, tooling, governance |
| Specifications | Syntax, type system, runtime semantics |
| Compiler/tool docs | Diagnostics, static analysis, build/test workflows |
| Package ecosystem reports | Adoption, ecosystem maturity |
| Developer surveys | Adoption and talent signals |
| Academic papers | Verification, type systems, static analysis, safety |
| Security reports | Memory safety, vulnerability classes |
| Benchmark suites | Performance and tooling behavior |
| Case studies | Operational adoption and migration evidence |

### Tasks

- Capture sources in **per-language source registries**: `sources/<language>-sources.yaml` (one file per cohort language).
- Group sources by language and criterion.
- Label source reliability.
- Capture publication date or version date.
- Identify stale or deprecated sources.

### Deliverables

- One `sources/<language>-sources.yaml` per cohort language (10 files).
- Per-language verification status field at the top of each `claims/<language>.yaml`.

### Exit criteria

Each cohort language has at least:

- 2 primary sources
- 2 ecosystem/adoption sources
- 1 tooling source
- 1 counterevidence source or limitation source

## Phase 3 — Atomic claim extraction

### Goal

Convert source material into reusable evidence units.

### Claim format

Each claim must contain:

```yaml
- id: rust-001
  claim: Rust's ownership and borrowing model catches many memory-management errors at compile time.
  dimension: machine_cognition
  criterion: security_posture
  evidence_type: language_specification
  confidence: high
  polarity: positive
  source: rust-src-001
  notes: Applies to safe Rust; unsafe Rust requires separate treatment.
```

Counterclaims link to the positive claim they qualify via the `counters:` field:

```yaml
- id: rust-011
  claim: The unsafe keyword opts out of selected compiler-enforced safety checks for low-level operations.
  dimension: machine_cognition
  criterion: security_posture
  evidence_type: language_specification
  confidence: high
  polarity: negative
  source: rust-src-011
  counters: [rust-001, rust-002]
  notes: Unsafe Rust narrows the structural memory-safety guarantee to the safe subset.
```

The validator checks that every `counters:` entry references an existing claim id within the same file.

### Claim rules

- One claim = one idea.
- Claims must be falsifiable or challengeable.
- Claims must not combine evidence and conclusion.
- Claims must identify scope limitations.
- Negative or limiting claims should link to the positive claims they qualify via `counters:`.

### Tasks

- Extract 20-30 claims per cohort language (current corpus: ~241 atomic claims across the 10 languages).
- Add claims to `claims/<language>.yaml`.
- Normalize criterion names to match `framework/dimensions.md`.
- Assign confidence and polarity.
- Add `counters:` links from negative/limiting claims to the positive claims they qualify.

### Deliverables

- Updated claim YAML files
- Counters graph: every positive high-confidence claim should have at least one counter where one exists in evidence.

### Exit criteria

- Every draft score has at least 2 supporting claims.
- Every high-confidence positive claim has at least one counterclaim where the evidence supports one.
- Every low score has at least one supporting negative claim.

## Phase 4 — Evaluation update

### Goal

Turn claims into scored evaluations.

### Evaluation rules

Each language × dimension score must include:

- `score`: 1.0–5.0 in 0.5-point increments per the 9-level rubric in `framework/scoring-rubric.md`
- `confidence`: low / medium / high
- `justification`: prose
- `supporting_claims`: list of claim ids in the same dimension

The 9-level rubric:

| Score | Meaning |
|---:|---|
| 1.0 | Structurally weak, not greenfield-defensible |
| 1.5 | Weak with one mitigating factor |
| 2.0 | Usable but with significant friction |
| 2.5 | Usable; mitigations partly close known gaps |
| 3.0 | Adequate |
| 3.5 | Adequate-plus; one strong forward signal |
| 4.0 | Strong |
| 4.5 | Strong; multiple forward signals reinforce |
| 5.0 | Excellent / strategically advantaged |

Half-point scores are used to record genuine differentiation between languages where an integer would force false equality.

### Tasks

- Update `evaluations/<language>.yaml`.
- Add claim references to each score.
- Recalculate weighted scores via `scripts/score_summary.py`.
- Run `scripts/validate_evaluations.py`.
- Review score drift against the original hypothesis.

### Deliverables

- Updated evaluation YAML files
- Weighted score summary (`scripts/score_summary.py`)
- Confidence heatmap (`outputs/confidence-heatmap.md`, generated by `scripts/confidence_heatmap.py`)
- Open-question list

### Exit criteria

- `python scripts/validate_evaluations.py` passes.
- `python scripts/score_summary.py` produces the expected ranking.
- Every evaluation has traceable claim support.

## Phase 5 — Cross-language comparison

### Goal

Identify patterns that are not visible from single-language evaluations.

### Current artifacts

The original 8-track plan was consolidated into 4 comparison files plus 4 insight files. The mapping is documented in `comparisons/overview.md` ("Track coverage" section).

Comparison files (`comparisons/`):

1. `overview.md` — full matrix, headline findings, track coverage map.
2. `lens-analysis.md` — verification, agentic, safety, abstraction lenses across the cohort.
3. `dynamic-vs-static.md` — gradual-typing bridge between dynamic and static cohorts.
4. `agent-friendly-languages.md` — operability deep dive.

Insight files (`insights/`):

1. `agentic-feedback-loops.md`
2. `ai-favors-verifiability.md`
3. `safety-pressure.md`
4. `incumbent-risk.md` — formerly "legacy-gravity"; renamed in 2ff2ade to reflect greenfield framing.

### Tasks

- Update the four comparison files when scores or ranking shift.
- Compare scores and evidence strength.
- Separate technical merit from ecosystem gravity.
- Identify where AI changes the historical trade-offs.

### Exit criteria

- At least 5 cross-language patterns are documented across `comparisons/`.
- Each pattern cites supporting evaluations and claims.
- Each major pattern includes at least one plausible counterinterpretation.

## Phase 6 — Insight synthesis

### Goal

Convert repeated patterns into higher-order conclusions.

### Insight files

The 4 insight files in `insights/`:

1. `agentic-feedback-loops.md` — operability tracks toolchain unification and LSP exposure, not type-system depth.
2. `ai-favors-verifiability.md` — AI raises the price of cheap compile-time falsification.
3. `safety-pressure.md` — memory safety has crossed from technical preference to regulatory selection criterion.
4. `incumbent-risk.md` — under greenfield + AI-era pressure, incumbent gravity is not protective.

### Insight types

| Type | Description |
|---|---|
| Thesis | Strong claim supported by multiple evaluations |
| Pattern | Repeated observation across languages |
| Prediction | Future-facing conclusion with uncertainty |
| Risk | Failure mode or blind spot |
| Open question | Unresolved issue requiring more research |

### Tasks

- Update `insights/*.md`.
- Link each insight to evaluations and claims.
- Identify confidence level.
- Record counterclaims.
- Separate present-state findings from future predictions.

### v0.3 review note

Under v0.3 framing, **every insight should be re-checked when ranking changes.** The most recent reshuffle (Python +1 over Go on structured-output) required updating `agentic-feedback-loops.md` because the prior narrative emphasized Go's tooling lead as the agent-friendly default. The other three insights held structurally and were marked "Verified under v0.3."

### Exit criteria

- Every insight has traceability.
- Every prediction has explicit uncertainty.
- Every major thesis has counterclaims.
- After every ranking change, each insight is re-checked and either updated or marked "Verified under v0.3" at the bottom.

## Phase 7 — Review and challenge

### Goal

Reduce bias, unsupported reasoning, and premature conclusions.

### Review checklist (v0.3)

- Are sources current enough?
- Are official claims overtrusted?
- Are ecosystem claims separated from language-design claims?
- Are AI-era assumptions explicit?
- Are dynamic-language advantages fairly represented?
- **Are legacy advantages improperly credited?** (inverted from prior "Are legacy-language advantages fairly represented?" to reflect the greenfield-framing constraint)
- Are safety claims scoped correctly?
- Are scores comparable across languages?

The formal v0.3 walk of this checklist lives in `outputs/v0.3-review-pass.md`.

### Tasks

- Walk the checklist against current scores.
- Stress-test top-ranked languages.
- Add counterclaims where positive claims lack qualification.
- Lower confidence where evidence is weak.
- Mark unresolved claims clearly.

### Exit criteria

- No final conclusion depends only on speculative reasoning.
- No language is evaluated only by strengths or only by weaknesses.
- Every major conclusion has passed one explicit challenge pass.

## Phase 8 — Final outputs

### Goal

Produce usable outputs from the research base.

### Current outputs

- `outputs/report.md` — full evidence-backed report.
- `outputs/report-story.md` — story-driven sibling of the report (Stories That Explain + Man In A Hole).
- `outputs/deck-outline.md` — slide outline for presentation.
- `outputs/programming-languages-ai-era.pptx` — generated deck (re-upload pending FUSE issue).
- `outputs/evidence-backed-research-execution-plan.md` — this document.
- `outputs/confidence-heatmap.md` — language × dimension confidence grid (new in v0.3).
- `outputs/v0.3-review-pass.md` — formal Phase 7 review against current scores (new in v0.3).

### v0.3 backlog (deferred deliverables)

- Executive summary — short-form derivative of `report.md`.
- Decision memo — opinionated recommendation by domain.
- Research backlog — open-question and counterclaim-gap list.

These are not currently real deliverables; they are listed here as v0.3 backlog so future passes can either produce them or formally drop them.

### Tasks

- Keep `outputs/report.md` and `outputs/deck-outline.md` synchronized when scores shift.
- Re-upload `programming-languages-ai-era.pptx` when FUSE workspace permits.
- Generate `confidence-heatmap.md` from current evaluations after every score change.
- Run a fresh v0.3 review pass after major ranking changes.

### Exit criteria

- Every report claim links back to an insight, evaluation, claim, or source.
- Limitations are explicit.
- Scores and confidence levels are visible.

## Cadence

Research now runs in **dimension-wide passes** rather than per-language batches. The 10-language cohort is small enough, and the dimension count high enough, that scoring one dimension across all 10 languages in a single pass produces more comparable results than going language-by-language. (The prior per-language order list was retired with the move to v0.3.)

A typical pass:

1. Read or refresh sources for the dimension being scored.
2. Update or add claims in `claims/<lang>.yaml` for each cohort language.
3. Update the dimension's cell in each `evaluations/<lang>.yaml`.
4. Run `validate_evaluations.py` and `score_summary.py`.
5. Update `comparisons/overview.md` matrix.
6. Re-check insight files; update or mark "Verified under v0.3."
7. Refresh `report.md`, `deck-outline.md`, `confidence-heatmap.md`.

## GitHub workflow

### Branches

Use short-lived branches:

```text
research/<lang>-sources
research/<lang>-claims
research/<dimension>-pass
comparison/<topic>
insight/<topic>
```

### Pull requests

Use pull requests for reviewable changes:

- source additions
- claim additions (including counters: links)
- score changes
- comparison updates
- insight promotion or re-check

### Labels

```text
evaluation
language
source
claim
counterclaim
comparison
insight
needs-evidence
review
v0.3
final
```

## Definition of done

A language evaluation is done when:

- evaluation YAML exists with all 7 dimensions scored
- at least 20 atomic claims exist
- every dimension has at least 2 supporting claims
- every high-confidence positive claim has a `counters:` link from a counterclaim where one exists in evidence
- the per-language source registry `sources/<lang>-sources.yaml` is populated
- `validate_evaluations.py` passes for that language
- comparison notes reference at least one of the language's claims

A project conclusion is done when:

- it is stated as an insight
- supporting evaluations are listed
- supporting claims are listed
- sources are traceable
- counterclaims are listed (and reach the positive claim via `counters:`)
- confidence is assigned
- limitations are explicit

## Immediate next actions

1. **Re-upload `outputs/programming-languages-ai-era.pptx`** once the FUSE-mount issue is resolved (the deck currently lags the v0.3 outline).
2. **Refresh `outputs/deck-outline.md`** to reflect the 7-dimension framework, current 10-language ranking, the Python/Go swap as a story beat, and the structured-output dimension as a load-bearing concept.
3. **Generate `outputs/confidence-heatmap.md`** via `scripts/confidence_heatmap.py` and commit both.
4. **Walk the Phase 7 review checklist** (greenfield-inverted) and capture results in `outputs/v0.3-review-pass.md`. Any score adjustments surfaced are documented but not made in the same commit.
5. **Re-pass the four insight files** for the Python/Go swap and 7-dimension framework; update `agentic-feedback-loops.md` substantively, mark the others "Verified under v0.3" if they hold structurally.
6. **Add a "Track coverage" section** to `comparisons/overview.md` mapping the original 8 plan tracks to current artifacts.

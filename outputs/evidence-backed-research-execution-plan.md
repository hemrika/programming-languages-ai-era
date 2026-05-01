## Version

v0.3 (2026-04-30) — current. Prior versions (v0.1 5-dimension, v0.2 6-dimension) are visible in git history.

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

Evaluation dimensions (7) and current weights:

| Dimension | Weight |
|---|---:|
| Human cognition (HC) | 15% |
| Machine cognition (MC) | 15% |
| AI-agent operability (AO) | 20% |
| Runtime and ecosystem (RE) | 15% |
| Strategic viability (SV) | 10% |
| AI-systems interoperability (AI-sys) | 15% |
| Structured-output maturity (StructOut) | 10% |

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

Under v0.3 framing, **every insight should be re-checked when ranking changes.** The most rece
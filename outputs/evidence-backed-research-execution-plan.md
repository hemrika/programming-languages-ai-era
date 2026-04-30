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
4. Separate facts, interpretations, predictions, and speculation.
5. Prefer primary sources, specifications, official docs, empirical studies, and reproducible data.
6. Keep claims atomic.
7. Keep evaluations structured.
8. Treat every score as provisional until reviewed.

## Research workflow

```text
Source discovery
  → Source triage
  → Atomic claim extraction
  → Claim normalization
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

Initial languages:

- Rust
- Python
- TypeScript
- Go
- Java
- C#
- C++
- Kotlin
- Swift
- Haskell
- OCaml
- Zig
- SQL

Initial dimensions:

- Human cognition
- Machine cognition
- AI-agent operability
- Runtime and ecosystem
- Strategic viability

### Tasks

- Confirm the language list.
- Confirm the evaluation dimensions.
- Confirm scoring weights.
- Identify missing criteria.
- Mark all existing scores as draft.
- Create one tracking issue per language.

### Deliverables

- Updated `framework/evaluation-framework.md`
- Updated `framework/scoring-rubric.md`
- One issue per language
- One baseline comparison table

### Exit criteria

- Every target language has a profile file.
- Every target language has an evaluation YAML file.
- Every draft score has a confidence value and justification.

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
| Academic papers | verification, type systems, static analysis, safety |
| Security reports | memory safety, vulnerability classes |
| Benchmark suites | performance and tooling behavior |
| Case studies | operational adoption and migration evidence |

### Tasks

- Create source records in `sources/source-notes.md` or `sources/sources.bib`.
- Group sources by language and criterion.
- Label source reliability.
- Capture publication date or version date.
- Identify stale or deprecated sources.

### Deliverables

- Updated `sources/reading-list.md`
- Updated `sources/source-notes.md`
- Updated `sources/sources.bib`

### Exit criteria

Each priority language has at least:

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
id: rust-001
claim: Rust's ownership and borrowing model catches many memory-management errors at compile time.
language: Rust
criterion: security_posture
source: source-id
source_type: official_documentation
evidence_type: structural
confidence: high
polarity: positive
status: draft
notes: Applies to safe Rust; unsafe Rust requires separate treatment.
```

### Claim rules

- One claim = one idea.
- Claims must be falsifiable or challengeable.
- Claims must not combine evidence and conclusion.
- Claims must identify scope limitations.
- Claims should include counterclaims when available.

### Tasks

- Extract 10–20 claims per priority language.
- Add claims to `claims/<language>.yaml`.
- Normalize criterion names.
- Assign confidence and polarity.
- Identify unsupported assumptions.

### Deliverables

- Updated claim YAML files
- Claim inventory by criterion
- List of unsupported assumptions

### Exit criteria

- Every draft score has at least 2 supporting claims.
- Every high score has at least 1 counterclaim or limitation.
- Every low score has at least 1 supporting negative claim.

## Phase 4 — Evaluation update

### Goal

Turn claims into scored evaluations.

### Evaluation rules

Each language × dimension score must include:

- score: 1–5
- confidence: low / medium / high
- justification
- supporting claims
- counterclaims
- unresolved questions

### Tasks

- Update `evaluations/*.yaml`.
- Add claim references to each score.
- Recalculate weighted scores.
- Run validation.
- Review score drift against the original hypothesis.

### Deliverables

- Updated evaluation YAML files
- Weighted score summary
- Confidence heatmap
- Open-question list

### Exit criteria

- `python scripts/validate_evaluations.py` passes.
- Every evaluation has traceable claim support.
- Scores are marked `reviewed` only after counterclaims are considered.

## Phase 5 — Cross-language comparison

### Goal

Identify patterns that are not visible from single-language evaluations.

### Comparison tracks

1. Dynamic vs static languages
2. Systems languages
3. Enterprise languages
4. Web/application languages
5. AI/data ecosystem languages
6. Agent-friendly languages
7. Verification-friendly languages
8. Legacy-gravity languages

### Tasks

- Update `comparisons/*.md`.
- Compare scores and evidence strength.
- Separate technical merit from ecosystem gravity.
- Identify where AI changes the historical trade-offs.

### Deliverables

- Updated comparison notes
- Ranked language clusters
- Trade-off matrix
- Counter-thesis list

### Exit criteria

- At least 5 cross-language patterns are documented.
- Each pattern cites supporting evaluations and claims.
- Each pattern includes at least one plausible counterinterpretation.

## Phase 6 — Insight synthesis

### Goal

Convert repeated patterns into higher-order conclusions.

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

### Deliverables

- Updated insight notes
- Executive thesis list
- Open question list

### Exit criteria

- Every insight has traceability.
- Every prediction has explicit uncertainty.
- Every major thesis has counterclaims.

## Phase 7 — Review and challenge

### Goal

Reduce bias, unsupported reasoning, and premature conclusions.

### Review checklist

- Are sources current enough?
- Are official claims overtrusted?
- Are ecosystem claims separated from language-design claims?
- Are AI-era assumptions explicit?
- Are dynamic-language advantages fairly represented?
- Are legacy-language advantages fairly represented?
- Are safety claims scoped correctly?
- Are scores comparable across languages?

### Tasks

- Create review issues for major conclusions.
- Stress-test top-ranked languages.
- Add counterclaims.
- Lower confidence where evidence is weak.
- Mark unresolved claims clearly.

### Deliverables

- Review issues
- Revised scores
- Counterclaim inventory
- Confidence adjustments

### Exit criteria

- No final conclusion depends only on speculative reasoning.
- No language is evaluated only by strengths or only by weaknesses.
- Every major conclusion has passed one explicit challenge pass.

## Phase 8 — Final outputs

### Goal

Produce usable outputs from the research base.

### Output formats

- Full report
- Executive summary
- Slide deck outline
- Language ranking table
- Decision memo
- Research backlog

### Tasks

- Update `outputs/report.md`.
- Update `outputs/deck-outline.md`.
- Produce ranked summaries by dimension.
- Produce a final limitations section.

### Deliverables

- Evidence-backed report
- Presentation outline
- Final comparison matrix
- Research backlog

### Exit criteria

- Every report claim links back to an insight, evaluation, claim, or source.
- Limitations are explicit.
- Scores and confidence levels are visible.

## Cadence

Use research batches.

### Batch size

One batch should cover either:

- one language across all dimensions, or
- one criterion across all priority languages.

### Recommended order

1. Rust
2. TypeScript
3. Python
4. Go
5. Java
6. C#
7. C++
8. Kotlin
9. Swift
10. Haskell / OCaml / Zig / SQL

## GitHub workflow

### Branches

Use short-lived branches:

```text
research/rust-sources
research/typescript-claims
research/python-evaluation
comparison/static-vs-dynamic
insight/ai-favors-verifiability
```

### Issues

Use issues for units of work:

- `Evaluate: Rust`
- `Capture sources: Rust compiler diagnostics`
- `Extract claims: TypeScript static analysis`
- `Compare: Go vs Rust agentic repair loops`
- `Challenge thesis: AI favors strongly typed languages`

### Pull requests

Use pull requests for reviewable changes:

- source additions
- claim additions
- score changes
- comparison updates
- insight promotion

### Labels

```text
evaluation
language
source
claim
comparison
insight
counterclaim
needs-evidence
review
final
```

## Definition of done

A language evaluation is done when:

- profile exists
- evaluation YAML exists
- at least 10 atomic claims exist
- every dimension has supporting claims
- every high-confidence score has source support
- counterclaims are recorded
- validation passes
- comparison notes are updated

A project conclusion is done when:

- it is stated as an insight
- supporting evaluations are listed
- supporting claims are listed
- sources are traceable
- counterclaims are listed
- confidence is assigned
- limitations are explicit

## Immediate next actions

1. Create GitHub issues for Rust, TypeScript, Python, and Go evidence passes.
2. Add source IDs and source schema.
3. Upgrade claim schema to include source references.
4. Add claim references to evaluation YAML.
5. Run the first evidence pass on Rust.

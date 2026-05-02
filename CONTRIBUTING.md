# Contributing

This document describes how to add evidence, propose corrections, and propose framework changes to the v0.6 schema-locked draft. The repository owner reviews every change against the validator and the framework's stated philosophy.

## Repository invariants

- **Every score traces to a claim.** No score moves without an upstream `claims/<lang>.yaml` change.
- **Every claim cites a primary source.** `source:` is mandatory; the source must resolve in `sources/<lang>-sources.yaml`.
- **Counterclaims are first-class.** A positive claim that materially carries a score should have at least one same-dimension counterclaim linking back via `counters:`.
- **The validator is the contract.** `python scripts/validate_evaluations.py` must pass on every push and PR. CI also re-runs `score_summary.py` and re-renders the confidence heatmap to detect drift.

## Adding a claim

1. Open `claims/<language>.yaml`.
2. Append a claim with a fresh sequential id (`<lang>-NNN`).
3. Required fields: `id`, `claim`, `dimension`, `criterion`, `evidence_type`, `confidence` (low/medium/high), `polarity` (positive/negative), `source`, `notes`.
4. Required when the claim names a specific third-party library (Pydantic, Tokio, LangChain, etc.) and is positive: `backer` (one of `language_stewards`, `commercial_first_party`, `commercial_third_party`, `community_multi_maintainer`, `community_single_maintainer`, `research`).
5. If the claim is positive and load-bearing for a score >= 4.0, also file a same-dimension counterclaim with `counters: [<positive-id>]`. The validator warns when this is missing.
6. Cite the source in `sources/<lang>-sources.yaml`. New sources need: `id`, `title`, `url`, `publication_date`, `reliability` (high/medium/low), and a one-line description of what the source establishes.

Example:

```yaml
- id: typescript-099
  claim: "Foo.js v3.0 ships first-party Anthropic and OpenAI adapters."
  dimension: ai_systems_ecosystem
  backer: commercial_first_party
  criterion: agent_framework_support
  evidence_type: official_tooling_documentation
  confidence: high
  polarity: positive
  source: typescript-src-099
  notes: The Foo.js 3.0 release notes describe first-party adapter support shipped from a vendor-stewarded npm org.
  counters: [typescript-100]
```

## Adding a counterclaim

1. Same file, same flow.
2. `polarity: negative`.
3. `counters: [<id of positive claim it opposes>]`.
4. The counterclaim is a separate piece of evidence — it must cite its own primary source. Do not author counterclaims that simply restate "the positive claim might be wrong" without independent evidence.

## Proposing a score correction

1. Open an issue with the proposed new score, the evaluation cell (e.g. `python.runtime_ecosystem`), and the new evidence.
2. Minimum bar: at least two pieces of evidence — one supporting the move and one counterclaim acknowledging the strongest opposing argument. A correction without a counterclaim suggests the move is under-anchored.
3. The repository owner files a PR that updates `evaluations/<lang>.yaml`, adds the upstream claim(s) in `claims/<lang>.yaml`, adds the source(s) in `sources/<lang>-sources.yaml`, and re-runs the validator.
4. If the move shifts the headline ranking, the change description must call that out explicitly.

## Proposing a dimension change

Dimension changes are SemVer-significant.

1. **Additive change** (new dimension, new sub-criterion, new lens): v1.x bump. File an RFC-style proposal in `proposals/<descriptive-name>.md` first. The proposal must specify: the dimension definition, the proposed weight, where the weight is taken from, the rubric anchors at 1/3/5, and a worked example for at least three cohort languages.
2. **Breaking change** (removing or merging dimensions, changing the score scale, redefining cohort membership): v2.x bump. Same RFC process, plus an explicit migration note for every claim and evaluation file affected.
3. The proposal is reviewed against the framework's stated philosophy in `framework/decisions.md`. A change that contradicts a documented decision must include a counter-rationale and a proposed update to the decision log.

## SemVer policy

- **v0.x:** Pre-1.0. Schema may shift; framework version is stamped on every evaluation file.
- **v0.6:** First locked draft. Schema changes require a SemVer bump.
- **v1.0:** Calibrated, externally reviewed, schema stable, predictions live.
- **v1.x:** Backward-compatible additions only — new dimensions, new anchors, new sources, new claims, score corrections that don't change the rubric.
- **v2.x:** Breaking changes — dimension removals, scale changes, cohort changes.

## Reviewer expectations

A PR is merge-ready when:

- `python scripts/validate_evaluations.py` exits clean.
- `python scripts/score_summary.py` reflects any rank-changing edits.
- `python scripts/confidence_heatmap.py` is re-run if confidence values changed; the regenerated `outputs/confidence-heatmap.md` is committed.
- New claims have sources; new positive library-naming claims have backers; new counterclaims link via `counters:`.
- The PR description names the cells touched and the rank change (if any).

## What this repository is not

- Not a popularity contest. Don't open PRs that read "X is better than Y, please bump X."
- Not a vendor channel. Backer transparency is the response to vendor framing.
- Not a maintenance-estate calculator. The framing is greenfield; PRs that re-introduce installed-base credit are out of scope.

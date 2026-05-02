# Road to v1.0

The framework is at v0.5: an 11-dimension, 10-language, single-rater draft anchored in ~390 atomic claims and 173 counter-links. v1.0 is not about adding more — it is about earning the version number through stability, calibration, and external testing.

## Five-phase plan

### Phase 1 — Schema lock (v0.6)

The schema stops being a moving target. The validator newly enforces: `framework_version` stamp at the top of every evaluation file (must equal the current framework version); mandatory `source:` on every claim; `backer:` required on positive claims that name a specific library (heuristic — see `scripts/validate_evaluations.py`); and a warning when an evaluation cell scores 4.0 or higher without at least one counterclaim on the same dimension linking back to a supporting claim. CI runs the validator, the score summary, and the confidence-heatmap regenerator on every push and pull request, and fails if the heatmap drifts from the YAML it summarizes.

v0.6 is the boundary between "draft" and "we know what the framework is." Anything below v0.6 was schema-fluid; from v0.6 on, every additive change is SemVer-disciplined and every breaking change is a v2.x conversation.

### Phase 2 — Multi-rater calibration (v0.7)

Recruit two to three additional raters whose language preferences span the cohort (one TS/Python-leaning, one Rust/Go-leaning, one JVM/.NET-leaning is the working target). Each rater independently scores the full 110-cell matrix using the v0.6 rubric without seeing the existing scores. Disagreement is measured cell-by-cell; aggregate inter-rater reliability is reported via Krippendorff's alpha (or an analogue suitable for ordinal half-point data).

For every cell where the spread exceeds 0.5, the raters meet, walk the supporting claims and counterclaims, and either converge or document the disagreement as a known-fragile cell. The README Status updates from "single-rater draft" to "three-rater calibrated," and `outputs/calibration.md` records the per-cell rater table, the alpha, and the unresolved cells.

### Phase 3 — Sensitivity analysis (v0.8)

Each dimension weight is perturbed at ±2.5% and ±5% (with the remaining weights rescaled proportionally), and the headline ranking is recomputed. Per-language rank stability is recorded: how often each language holds its rank, and at what perturbation a rank flips with a neighbor. The output, `outputs/sensitivity-analysis.md`, separates findings into "robust" (rank holds under all reasonable perturbations) and "fragile" (flips under small perturbations), and reports a per-language stability band.

The point is not to declare the ranking objective — it is to make explicit which conclusions survive reasonable disagreement on weights and which do not. Going forward, a fragile finding is reported as fragile, not as a fact.

### Phase 4 — External challenge round (v0.9)

The framework, the scoring rubric, and the per-language evaluations are sent to roughly five external reviewers spanning the cohort's language preferences. Each is asked to surface their strongest objection — to the framing, to a dimension, to a specific score, or to a specific claim. Every objection is logged in `outputs/external-review.md` with the reviewer, the objection, the response, and the resulting framework or score change (or a documented decision not to change).

External review is what catches domain-specific blind spots that single-rater work and even multi-rater calibration cannot: a senior Swift engineer notices what the cohort raters have systematically under-weighted; a Rust-async maintainer corrects an AIE claim; a JVM-platform architect challenges the Reach scoring on Project Panama.

### Phase 5 — Empirical commitments and governance (v1.0)

Five to ten falsifiable predictions are extracted from the framework, each with a measurable check and a date stamp. They are recorded in `outputs/predictions.md` together with the v1.1 review checkpoint protocol — a v1.1 release will grade each prediction and adjust the framework where reality has diverged from it. `CONTRIBUTING.md` documents the claim-addition, score-correction, and dimension-proposal workflows, including the SemVer policy (v1.x is backward-compatible; v2.x can break the schema). The README Status moves from "draft" to "v1.0."

v1.0 is the moment the framework starts paying its empirical debts: from this point on, the predictions are scored, not merely asserted.

## Polish work (parallel to phases)

- Stories That Explain pass on `outputs/report.md`
- Properly designed PPTX (currently outline only)
- `framework/glossary.md` — defining the framework's terms of art in one place
- `framework/decisions.md` — decision log capturing the why behind each major framework choice
- `research/` disposition: re-score on v0.5 schema or formally retire as out-of-cohort reference

## What v1.0 explicitly is NOT

- Not "complete coverage." The cohort is bounded by design — Mojo, Zig, Julia, and Haskell remain out of cohort.
- Not "objectively correct." Subjectivity is acknowledged, not eliminated; calibration and sensitivity analysis bound it, they do not erase it.
- Not "the final word." v1.0 starts the empirical-validation clock; v1.1 grades the predictions and updates the framework against reality.
- Not driven by adding more. Adding a 12th dimension before locking what we have is anti-v1.0.

## Effort estimate

| Phase | Wall-clock | Driver |
|---|---|---|
| Phase 1 — Schema lock | 1–2 days | sandbox-executable |
| Phase 2 — Multi-rater calibration | 4–8 weeks | rater availability |
| Phase 3 — Sensitivity analysis | 1–2 days | sandbox-executable |
| Phase 4 — External challenge round | 4–6 weeks | reviewer turnaround |
| Phase 5 — Predictions + governance | 1 week | sandbox-executable |
| Polish | 1–2 weeks | sandbox-executable |

If Phases 2 and 4 run concurrently rather than serially, realistic v1.0 ship date is 3–4 months.

## Sandbox-executable vs user-action-required

- **Sandbox-executable:** Phase 1, Phase 3, Phase 5, and all polish work. These can be done from this side without external participants.
- **User-action-required:** Phase 2 (multi-rater calibration) and Phase 4 (external challenge round). Both depend on recruiting and coordinating external participants and must be initiated by the repository owner.

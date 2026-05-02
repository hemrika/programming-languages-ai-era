# Decisions Log

The major framework choices and the rationale behind each. Each entry: the date the decision was made, what was decided, what alternative was considered, what would falsify the choice. Decisions are versioned with the framework; superseded decisions are kept and annotated rather than deleted.

## D1 — Split AI-systems into native + ecosystem (v0.4, 2026-04-30)

**Decision.** The single `ai_systems_interoperability` dimension (15%) was replaced by `ai_systems_native` (7.5%) and `ai_systems_ecosystem` (7.5%).

**Rationale.** The pre-split scoring conflated language-native capability with ecosystem-package capability and applied inclusion rules asymmetrically. Pydantic had been credited to Python's structured-output score while Newtonsoft.Json had been omitted from .NET's. The split makes the rule symmetric: Microsoft-shipped AI Foundry counts native for .NET; community-maintained Anthropic.SDK counts ecosystem for .NET. Same rule, both sides of the line.

**Alternative considered.** Keep one dimension and document the asymmetry. Rejected because asymmetry under one number invites cherry-picking; two numbers force the rater to commit explicitly.

**Falsification.** If raters routinely struggle to assign a library to native vs ecosystem (the line is unclear in practice), or if the two numbers move together so reliably that the split adds no information, revisit and merge.

## D2 — Add ecosystem-dependency-risk (v0.4, 2026-04-30)

**Decision.** A new EDR dimension (5%, pulled from RE) scores backer-mix and load-bearing-dependency resilience. Higher score = lower risk = better. Introduced the `backer:` field on claims.

**Rationale.** A 5.0 backed by Microsoft is not the same as a 5.0 backed by three OSS volunteers. The pre-EDR rubric had no place to record that distinction; the score looked identical, the risk was different. EDR makes that risk a first-class number.

**Alternative considered.** Bake dependency-risk into the SV dimension. Rejected because SV is forward-looking governance/viability of the language itself; EDR is present-state resilience of the library stack. Different time horizon, different unit of analysis.

**Falsification.** If EDR scores are systematically uncorrelated with actual dependency-failure events over a 3-year empirical window (a v1.x prediction), or if raters cannot consistently assign backer types, revisit.

## D3 — Add reachability-to-top-tier (v0.5, 2026-05-02)

**Decision.** A new Reach dimension (5%, pulled from SV) scores forward-trajectory plausibility — how plausibly each below-5 cell in a language's row can move to 5.0 within a 3-5 year horizon.

**Rationale.** v0.4 captured present-state capability (AIN/AIE/SON/SOE) and present-state dependency risk (EDR) but did not separate forward-trajectory plausibility from current strategic viability. Two languages with identical SV scores can have very different odds of closing their gaps depending on steward investment, in-motion proposals, and the structural-vs-ecosystem nature of each gap. Reach scores that explicitly.

**Alternative considered.** Leave forward trajectory implicit in SV's `future fit` and `ecosystem velocity` criteria. Rejected because SV had become a multi-purpose container; forward trajectory deserved its own commitment.

**Falsification.** If 3-year retrospective shows that high-Reach languages did not actually close their gaps faster than low-Reach languages, the dimension is providing no signal.

## D4 — Drop Mojo, Zig, Julia, Haskell from cohort (v0.5, 2026-05-02)

**Decision.** The validated cohort is the 10 realistic greenfield-decision languages. Mojo, Zig, Julia, and Haskell remain in `research/` as v0.1-schema reference material.

**Rationale.** Mojo's status was preview; Zig was pre-1.0; Julia is dominantly scientific computing rather than greenfield AI-app development; Haskell's distance from the realistic decision set was too great to score it usefully against AO/AIE/SOE. Including them with low scores generated noise without signal.

**Alternative considered.** Keep all 14 with explicit "experimental" annotations. Rejected because the scoring rubric was anchored to realistic-greenfield comparisons; pasting research-grade languages into that frame produced misleading numbers.

**Falsification.** If one of the dropped languages reaches credible greenfield AI-era adoption (e.g., Mojo reaches stable 1.0 with material agent-framework support), it returns to cohort and gets scored on the v0.6 rubric.

## D5 — Move from integer 1-5 to half-point scoring (v0.5, 2026-05-02)

**Decision.** Scores in `{1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0}`, validated by the script.

**Rationale.** Integer-only scoring forced raters into either under-stating or over-stating in cases where the evidence was clearly between two anchors. Half-points absorb those judgment calls without expanding the rubric to a 1-10 scale (which would invite false precision).

**Alternative considered.** 1-10 scale. Rejected because 10 anchors are harder to define rigorously and harder to defend in calibration.

**Falsification.** If multi-rater calibration in v0.7 shows that raters routinely split between adjacent half-points the same way they used to split between integers, the half-points are noise and we revert.

## D6 — Greenfield framing rather than installed-base credit (v0.1)

**Decision.** Languages are evaluated for the greenfield decision. Installed base, existing code, and incumbent gravity are not scored as advantages.

**Rationale.** Installed-base credit is a maintenance-estate question, not an AI-era language-choice question. A 100-million-line legacy codebase is a constraint on the team holding it; it is not evidence that a new project should adopt the same language. The two questions ("what should we adopt for new work?" vs "what should we keep maintaining?") deserve separate frames.

**Alternative considered.** Weight installed base as a 5-10% dimension. Rejected because that re-merges the two frames and turns the framework into a measure of what already exists rather than a forward-looking decision aid.

**Falsification.** If greenfield-only scoring produces rankings that are consistently rejected by practitioners who report that installed-base gravity is decisive even for new work in their domain, document the constraint and consider a maintenance-estate companion variant.

## D7 — Specific weight allocations (v0.5, 2026-05-02)

**Decision.** AO at 20% (highest single weight), HC + MC at 15% each, RE at 10%, SV / SON / SOE / EDR / Reach at 5% each, AIN + AIE at 7.5% each.

**Rationale.** AO is the dimension that most directly drives the agent-feedback-loop value the framework is trying to surface; it earns the heaviest weight. HC and MC are the irreducible cognition halves (human and machine readers of the code). The 7.5% for AIN/AIE preserves the v0.3 combined 15% for AI-systems while honoring the native/ecosystem split. The 5% dimensions are present-state risk and forward trajectory — important enough to score, not load-bearing enough to dominate.

**Alternative considered.** Equal weights across all 11 dimensions. Rejected because equal weights are a defensible default only when there's no theory of which dimensions matter most; the framework has a theory (AO is the agent-loop driver) and weights it.

**Falsification.** Sensitivity analysis (`outputs/sensitivity-analysis.md`) shows what perturbations break the headline ranking. If multi-rater calibration in v0.7 produces large per-rater weight disagreement, the weights themselves go up for review in v0.8 sensitivity work.

## D8 — Schema lock at v0.6 (2026-05-02)

**Decision.** v0.6 stamps `framework_version: v0.6` on every evaluation file, makes `source` mandatory on every claim, requires `backer` on positive claims that name a specific library, and warns when a cell at score >= 4.0 has no same-dimension counterclaim coverage. Further additive changes follow SemVer; breaking changes go to v2.x.

**Rationale.** Anything below v0.6 was schema-fluid; the framework was still discovering what it was. v0.6 freezes the contract so multi-rater calibration, sensitivity analysis, external review, and predictions can run against a stable target. CI enforces the contract.

**Alternative considered.** Continue iterating on the schema until v1.0. Rejected because calibration (Phase 2) requires a stable schema to score against; raters cannot calibrate against a moving target.

**Falsification.** If multi-rater calibration in v0.7 surfaces a structural schema gap that demands a breaking change, the schema becomes v2.x rather than another v0.x patch — which is what the SemVer policy is for.

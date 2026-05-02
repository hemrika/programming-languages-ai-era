# Glossary

Terms of art used in this framework, defined in one place. Where a term has a specific technical meaning here that differs from its colloquial usage, the framework definition takes precedence.

## Framing

**Greenfield framing.** Languages are evaluated for the choice "starting a new AI-era project today, what would you choose?" — not for the volume of existing code or installed base. Maintenance-estate teams should re-weight.

**Native vs ecosystem.** A capability is *native* when it is shipped by the language stewards or a first-party commercial owner (Microsoft for .NET; Apple for Swift; the Go team; the Rust Foundation; OpenJDK/Oracle for Java; the PSF for Python; JetBrains for Kotlin; Dashbit/Plataformatec for Elixir; ISO and major-vendor compilers for C++). It is *ecosystem* when it is shipped by anyone else, including third-party commercial vendors (Anthropic, OpenAI), well-resourced communities (Pydantic, LangChain), and individual maintainers.

**Cohort.** The 10 languages scored against the v0.6 framework: C++, .NET (C#), Elixir, Go, Java, Kotlin, Python, Rust, Swift, TypeScript. Mojo, Zig, Julia, and Haskell are out of cohort and held in `research/` as reference material.

**Lens.** A cross-cutting read across the dimensions. The framework documents four lenses: verification advantage, agentic operability, safety pressure, abstraction compression. Lenses do not contribute to the weighted score; they organize narrative.

## Evidence model

**Claim.** An atomic statement about a language, with a primary-source citation. Lives in `claims/<lang>.yaml`. Has an `id`, `dimension`, `criterion`, `evidence_type`, `confidence`, `polarity`, `source`, and optional `backer`, `counters`, `notes`.

**Counterclaim.** A claim of opposite polarity that links back to a specific positive claim via `counters: [<id>]`. The counter is an independent piece of evidence, not a restatement.

**Supporting claim.** A claim referenced from an evaluation cell's `supporting_claims:` list. The claim's `dimension` must equal the evaluation cell's dimension.

**Source.** A primary-source citation in `sources/<lang>-sources.yaml` with `id`, `title`, `url`, `publication_date`, `reliability`, and a description.

**Evaluation.** A scored cell in `evaluations/<lang>.yaml` for one (language, dimension) pair, with `score`, `confidence`, `justification`, and `supporting_claims`.

**Polarity.** Positive (claim supports a higher score) or negative (claim drags the score down). Counterclaims are negative claims linked to a positive.

**Confidence.** The rater's certainty in a score: `high` means well-anchored and unlikely to move on review; `medium` means could move 0.5; `low` means another rater could reasonably challenge it.

**Backer.** Who underwrites a load-bearing dependency. One of `language_stewards`, `commercial_first_party`, `commercial_third_party`, `community_multi_maintainer`, `community_single_maintainer`, `research`. Required on positive claims that name specific third-party libraries.

## Dimensions

Eleven weighted dimensions; see `framework/dimensions.md` for full criteria and `framework/scoring-rubric.md` for anchors.

**Human cognition (HC, 15%).** Readability, refactor safety, mental-model size, idiom convergence — how well humans hold the language in their head.

**Machine cognition (MC, 15%).** Static analyzability, type-system strength, what a tool or model can prove without running the program.

**AI-agent operability (AO, 20%).** How well agents can drive build/test/refactor loops: editor-server quality, test-feedback latency, error-message machine-readability, structured tool integration.

**Runtime / ecosystem (RE, 10%).** Library maturity, package management, runtime characteristics for new projects.

**Strategic viability (SV, 5%).** Governance quality, future fit, AI-training-corpus density.

**AI-systems native (AIN, 7.5%).** What the language and stewards ship for LLM/agent integration directly. Anthropic-from-language-stewards counts here.

**AI-systems ecosystem (AIE, 7.5%).** What the third-party ecosystem provides (Anthropic SDK, LangChain, vector-store clients, etc.).

**Structured-output native (SON, 5%).** Language and standard-library support for emitting/validating structured shapes (JSON Schema generation, type-safe parse, refinement types).

**Structured-output ecosystem (SOE, 5%).** Library support: Pydantic, Zod, Serde, schemars, Jackson, etc.

**Ecosystem dependency risk (EDR, 5%).** Backer-mix and resilience of load-bearing dependencies. Higher = lower risk = more diverse, better-resourced backers behind the libraries the language relies on.

**Reachability to top tier (Reach, 5%).** Forward-trajectory plausibility: can the below-5 cells in this language's row plausibly reach 5.0 in a 3-5 year horizon? Higher = more reachable.

## Process

**Cell.** One (language × dimension) score in the matrix. The matrix is 10 × 11 = 110 cells.

**Half-point scoring.** Scores in `{1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0}`. Introduced in v0.5.

**Schema lock.** v0.6: the schema is now stable; further additions follow SemVer.

**Calibration.** Multi-rater scoring of the full matrix; planned for v0.7. Disagreements >0.5 are walked back to the supporting claims.

**Sensitivity analysis.** Weight-perturbation analysis: which conclusions survive a +-2.5% to +-5% shift on each dimension's weight? See `outputs/sensitivity-analysis.md`.

**Robust finding.** A ranking that holds across all reasonable weight perturbations.

**Fragile finding.** A ranking that flips with at least one neighbor under some perturbation.

**Prediction.** A falsifiable, date-stamped commitment derived from the framework. See `outputs/predictions.md`.

**Validator.** `scripts/validate_evaluations.py`. Checks dimensional completeness, score validity, claim resolution, source citations, backer fields where required, framework-version stamp, and warns on counter-link coverage gaps.

**Status.** The README's one-line description of where the framework stands: from "draft" through "v0.6 schema-locked draft" through "three-rater calibrated" to "v1.0."

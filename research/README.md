# Research material — out of cohort

The Haskell, Julia, Mojo, and Zig profiles in this folder are research notes, not part of the validated 10-language cohort. They were dropped from the cohort during the v0.3 cut and retained here as reference material.

These files use the v0.1 evaluation schema (5 dimensions, integer 1–5 scores). They are not refreshed for v0.5 (11 dimensions, half-point scoring, native/ecosystem split, dependency-risk, reachability) and are not comparable with the cohort matrix in `comparisons/overview.md`.

`scripts/validate_evaluations.py` and `scripts/score_summary.py` only scan `claims/`, `evaluations/`, and `sources/` at the top level — files under `research/` are out of scope by location, not by allowlist filtering.

## Why these languages were dropped from the cohort

- **Haskell** — verification reference rather than a default greenfield choice; small ecosystem; not where AI-era greenfield decisions actually land.
- **Julia** — narrowly numerical; outside the realistic AI-application greenfield decision set.
- **Mojo** — pre-1.0 at the time of the v0.3 cut; trajectory unproven.
- **Zig** — pre-1.0 at the time of the v0.3 cut; ecosystem nascent.

Treat the per-language files here as historical context only. Anything that scores or compares against the cohort lives outside this folder.

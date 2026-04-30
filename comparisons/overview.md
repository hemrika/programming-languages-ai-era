# Comparison Overview

## Method

All scores reflect framework v0.1, draft evaluations as of 2026-04-30. Weighted score uses framework weights: Human cognition 20%, Machine cognition 25%, AI-agent operability 25%, Runtime/ecosystem 20%, Strategic viability 10%. Scores are 1-5 per the rubric in `framework/scoring-rubric.md`. Justifications draw on the per-language claims under `claims/` and the cross-cutting lens reading in `lens-analysis.md`.

These are draft scores intended to be falsifiable by the underlying claims, not final verdicts. They will move as evidence is added or revised.

## Full matrix (14 languages)

| Language    | HC | MC | AO | RE | SV | Weighted |
|---          |---:|---:|---:|---:|---:|---:|
| TypeScript  | 4  | 4  | 5  | 4  | 5  | 4.35 |
| Go          | 5  | 4  | 5  | 4  | 4  | 4.45 |
| Rust        | 3  | 5  | 4  | 4  | 5  | 4.20 |
| Kotlin      | 4  | 4  | 4  | 4  | 4  | 4.00 |
| .NET (C#)   | 4  | 4  | 4  | 4  | 4  | 4.00 |
| Python      | 4  | 3  | 4  | 5  | 5  | 4.05 |
| Swift       | 4  | 4  | 3  | 4  | 3  | 3.65 |
| Java        | 3  | 4  | 3  | 5  | 4  | 3.75 |
| Elixir      | 4  | 3  | 3  | 4  | 3  | 3.40 |
| Haskell     | 3  | 5  | 2  | 3  | 3  | 3.25 |
| Zig         | 4  | 4  | 3  | 3  | 3  | 3.40 |
| C++         | 2  | 3  | 2  | 5  | 4  | 3.05 |
| Julia       | 3  | 3  | 2  | 3  | 3  | 2.75 |
| Mojo        | 3  | 3  | 2  | 2  | 3  | 2.55 |

HC = Human cognition, MC = Machine cognition, AO = AI-agent operability, RE = Runtime and ecosystem, SV = Strategic viability.

## Reading the matrix

Three clusters emerge.

**Top tier (>= 4.0 weighted).** Go, TypeScript, Rust, Python, Kotlin, .NET. These are the languages whose structural properties, ecosystems, and operability characteristics combine to produce the strongest AI-era profiles. Each wins for different reasons - Go and TypeScript on agent operability, Rust on verification and safety, Python on ecosystem dominance, Kotlin and .NET on balanced strength.

**Middle tier (3.0-3.99 weighted).** Java, Swift, Elixir, Haskell, Zig, C++. These have either a structural strength offset by an operability or ecosystem weakness (Haskell, Zig, Elixir) or a high-gravity legacy position offset by an AI-era liability (Java, C++, Swift on cross-platform).

**Lower tier (< 3.0 weighted).** Julia, Mojo. Both have narrow domain strength but unproven or constrained generality. Mojo in particular reflects a forward bet on AI-native compilation that has not yet produced the ecosystem to support it.

## Headline findings

1. **No language sweeps.** The highest weighted score (Go, 4.45) reflects breadth, not domination. Every top-tier language has at least one structural weakness - Rust's learning curve, Python's verification gap, TypeScript's runtime semantics, Go's deliberate abstraction limits.

2. **AI-agent operability is the most discriminating dimension.** It separates Go and TypeScript from Haskell and C++ even when the underlying language quality is comparable on other axes. Operability captures fast feedback, deterministic tooling, clear diagnostics, and shallow project structure - properties that compound for agents.

3. **Strategic viability and runtime/ecosystem are correlated but not identical.** Python has maximum ecosystem strength and remains strategically viable despite verification weakness. C++ has equivalent ecosystem strength but a strategic-viability discount from the safety pressure documented in `lens-analysis.md`.

4. **Verification leaders do not automatically lead overall.** Haskell scores 5 on machine cognition but 2 on AI-agent operability. The framework's weighting reflects a position that verification *and* operability must both be present for AI-era advantage.

5. **The dynamic-static gap is narrowing where gradual typing exists.** TypeScript, Python (typed), and Elixir (typespecs/Gradient) demonstrate that dynamic-origin languages can recover much of the static advantage if their ecosystems commit to type discipline. See `dynamic-vs-static.md`.

## How to use this document

This overview is intentionally compressed. For the reasoning behind any cell:

- Per-language detail: `claims/<language>.yaml` and (where present) `evaluations/<language>.md`.
- Dimension definitions and weights: `framework/evaluation-framework.md` and `framework/dimensions.md`.
- Cross-cutting reads: `lens-analysis.md` (five lenses) and `agent-friendly-languages.md` (operability deep dive).
- Dynamic vs static comparison: `dynamic-vs-static.md`.

## Limitations

- v0.1 scores are author-judgment grounded in claims, not the result of a calibrated multi-rater process.
- Several languages (Mojo, Zig, Julia) are evolving rapidly; scores reflect a 2026-04-30 snapshot.
- The framework weights themselves are a working assumption. A reasonable reader could weight runtime/ecosystem higher (favoring Python, Java, C++) or AI-agent operability higher (favoring Go, TypeScript). The matrix is robust to small weight perturbations but not to large ones.

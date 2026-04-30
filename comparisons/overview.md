# Comparison Overview

## Method

All scores reflect framework v0.1, draft evaluations as of 2026-04-30 under the **greenfield framing** documented in `framework/evaluation-framework.md`. Installed base, existing code volume, and incumbent gravity are not scored as advantages; languages are credited for forward-looking properties (governance, future fit, AI-training representation, ecosystem velocity, library maturity for new projects). Weighted score uses framework weights: Human cognition 20%, Machine cognition 25%, AI-agent operability 25%, Runtime/ecosystem 20%, Strategic viability 10%. Scores are 1-5 per the rubric in `framework/scoring-rubric.md`. Justifications draw on the per-language claims under `claims/` and the cross-cutting lens reading in `lens-analysis.md`.

These are draft scores intended to be falsifiable by the underlying claims, not final verdicts. They will move as evidence is added or revised.

## Full matrix (14 languages)

| Language    | HC | MC | AO | RE | SV | Weighted |
|---          |---:|---:|---:|---:|---:|---:|
| Go          | 5  | 4  | 5  | 4  | 4  | 4.45 |
| TypeScript  | 4  | 4  | 5  | 4  | 4  | 4.25 |
| Rust        | 3  | 5  | 4  | 4  | 5  | 4.15 |
| Kotlin      | 4  | 4  | 4  | 4  | 4  | 4.00 |
| .NET (C#)   | 4  | 4  | 4  | 4  | 4  | 4.00 |
| Python      | 4  | 3  | 4  | 5  | 4  | 3.95 |
| Swift       | 4  | 4  | 3  | 4  | 3  | 3.65 |
| Java        | 3  | 4  | 3  | 4  | 3  | 3.45 |
| Zig         | 4  | 4  | 3  | 3  | 3  | 3.45 |
| Elixir      | 4  | 3  | 3  | 4  | 3  | 3.40 |
| Haskell     | 3  | 5  | 2  | 3  | 3  | 3.25 |
| Julia       | 3  | 3  | 2  | 3  | 3  | 2.75 |
| Mojo        | 3  | 3  | 2  | 2  | 4  | 2.65 |
| C++         | 2  | 3  | 2  | 3  | 2  | 2.45 |

HC = Human cognition, MC = Machine cognition, AO = AI-agent operability, RE = Runtime and ecosystem, SV = Strategic viability.

## Reading the matrix

Three clusters emerge under greenfield framing.

**Top tier (>= 4.0 weighted).** Go, TypeScript, Rust, Kotlin, .NET. These are the languages whose structural properties, ecosystems, and operability characteristics combine to produce the strongest forward-looking AI-era profiles. Each wins for different reasons - Go and TypeScript on agent operability, Rust on verification and safety, Kotlin and .NET on balanced strength. Python sits just below this line at 3.95, dropping from the top tier as installed-base credit is removed.

**Middle tier (3.0-3.99 weighted).** Python, Swift, Java, Zig, Elixir, Haskell. Each has either a structural strength offset by an operability or ecosystem weakness (Haskell, Zig, Elixir) or carried a legacy premium that no longer applies (Java, Python on strategic viability). Modern-typed languages with no installed-base story (Zig) sit alongside modernized incumbents whose forward-looking case is narrower than their historic position suggested (Java).

**Lower tier (< 3.0 weighted).** Julia, Mojo, C++. C++ drops sharply under greenfield framing: the runtime/ecosystem and strategic-viability scores both lose their installed-base premium, leaving the documented memory-safety pressure (Microsoft, Chromium, Android, NSA, ONCD) as the dominant signal. Mojo rises slightly because AI-native design is exactly the forward bet the framework now credits, though ecosystem narrowness keeps the overall score low. Julia's narrow numerical-computing focus remains the binding constraint.

## Headline findings

1. **Greenfield framing reshuffles the bottom of the matrix more than the top.** The top three (Go, TypeScript, Rust) hold their positions because their cases were already forward-looking. C++ drops 0.6 points and falls to the bottom of the matrix. Java drops 0.3 points. Python drops out of the top tier. Mojo rises slightly.

2. **No language sweeps.** The highest weighted score (Go, 4.45) reflects breadth, not domination. Every top-tier language has at least one structural weakness - Rust's learning curve, TypeScript's runtime semantics, Go's deliberate abstraction limits.

3. **AI-agent operability is the most discriminating dimension.** It separates Go and TypeScript from Haskell and C++ even when the underlying language quality is comparable on other axes. Operability captures fast feedback, deterministic tooling, clear diagnostics, and shallow project structure - properties that compound for agents.

4. **Strategic viability and runtime/ecosystem are correlated but no longer dominated by incumbency.** Under greenfield framing, both dimensions credit forward-looking signals (ecosystem velocity, AI-training-corpus density, governance, future fit) rather than installed code volume. Python keeps a strong runtime/ecosystem score because ML-domain library velocity is forward-relevant; C++ does not because its remaining forward signal on this axis is dominated by safety pressure.

5. **Verification leaders do not automatically lead overall.** Haskell scores 5 on machine cognition but 2 on AI-agent operability. The framework's weighting reflects a position that verification *and* operability must both be present for AI-era advantage.

6. **The dynamic-static gap is narrowing where gradual typing exists.** TypeScript, Python (typed), and Elixir (typespecs/Gradient) demonstrate that dynamic-origin languages can recover much of the static advantage if their ecosystems commit to type discipline. See `dynamic-vs-static.md`.

## How to use this document

This overview is intentionally compressed. For the reasoning behind any cell:

- Per-language detail: `claims/<language>.yaml` and `evaluations/<language>.yaml`.
- Dimension definitions and weights: `framework/evaluation-framework.md` and `framework/dimensions.md`.
- Cross-cutting reads: `lens-analysis.md` (four lenses) and `agent-friendly-languages.md` (operability deep dive).
- Dynamic vs static comparison: `dynamic-vs-static.md`.

## Limitations

- v0.1 scores are author-judgment grounded in claims, not the result of a calibrated multi-rater process.
- Several languages (Mojo, Zig, Julia) are evolving rapidly; scores reflect a 2026-04-30 snapshot.
- The framework weights themselves are a working assumption. A reasonable reader could weight runtime/ecosystem higher (favoring Python) or AI-agent operability higher (favoring Go, TypeScript). The matrix is robust to small weight perturbations but not to large ones.
- Greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question, and the matrix above will under-credit Java, Python, and C++ for that purpose.

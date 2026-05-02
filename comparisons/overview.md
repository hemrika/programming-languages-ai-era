# Comparison Overview

## Method

All scores reflect framework v0.4, draft evaluations as of 2026-05-02 under the **greenfield framing** documented in `framework/evaluation-framework.md`. Installed base, existing code volume, and incumbent gravity are not scored as advantages; languages are credited for forward-looking properties (governance, future fit, AI-training representation, ecosystem velocity, library maturity for new projects). The framework distinguishes **ecosystem viability** (forward production-readiness today: deployment, observability, integration with non-language systems) from **ecosystem velocity** (the forward rate of language and library improvement). Both are forward-looking and both are credited; legacy installed-base scope is not.

The framework scores **ten** weighted dimensions: Human cognition (15%), Machine cognition (15%), AI-agent operability (20%), Runtime/ecosystem (10%), Strategic viability (10%), AI-systems native (7.5%), AI-systems ecosystem (7.5%), Structured-output native (5%), Structured-output ecosystem (5%), and **Ecosystem dependency risk (5%)** — the backer-mix and resilience of load-bearing dependencies (higher = lower risk = better). The AI-systems and structured-output dimensions are each split into native (what the language steward ships first-party) and ecosystem (third-party, community, commercial-third-party libraries) halves so a 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers; the dependency-risk axis records the difference.

The cohort is 10 languages (cpp, dotnet, elixir, go, java, kotlin, python, rust, swift, typescript). Mojo, Zig, Julia, and Haskell are out of cohort.

## Track coverage

The execution plan (`outputs/evidence-backed-research-execution-plan.md`) lists eight comparison tracks. The framework consolidates them across the four comparison files and four insight files actually maintained, since several tracks share evidence. The mapping below makes the plan-to-artifact relationship explicit:

| Plan track | Current artifact |
|---|---|
| Dynamic vs static | `comparisons/dynamic-vs-static.md` |
| Systems languages | `comparisons/lens-analysis.md` (verification + safety lenses) |
| Enterprise languages | `comparisons/lens-analysis.md` (cross-cutting), `insights/incumbent-risk.md` |
| Web/application languages | `comparisons/lens-analysis.md` (agentic + abstraction lenses) |
| AI/data ecosystem languages | `comparisons/overview.md` (AI-systems and structured-output dimensions), `insights/ai-favors-verifiability.md` |
| Agent-friendly languages | `comparisons/agent-friendly-languages.md`, `insights/agentic-feedback-loops.md` |
| Verification-friendly languages | `comparisons/lens-analysis.md` (verification lens), `insights/ai-favors-verifiability.md` |
| Legacy-gravity → Incumbent-risk | `insights/incumbent-risk.md` |

Standalone documents not in the original track list:

- `comparisons/overview.md` — the ten-dimension matrix and weighted ranking that anchors the rest.
- `insights/safety-pressure.md` — the institutional/regulatory selection-pressure thesis derived from the safety lens.

## Full matrix (10 languages, 10 dimensions)

| Language    | HC  | MC  | AO  | RE  | SV  | AIN | AIE | SON | SOE | EDR | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---:|
| Go          | 5   | 4   | 5   | 4   | 4   | 2.0 | 3.5 | 3.0 | 3.0 | 3.5 | 4.04 |
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 3.0 | 4.01 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4.0 | 3.5 | 4.0 | 3.5 | 4.5 | 3.96 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3.0 | 3.0 | 3.5 | 3.0 | 4.0 | 3.85 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 1.5 | 3.5 | 2.0 | 4.0 | 3.5 | 3.75 |
| Python      | 4   | 3   | 4   | 5   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 2.5 | 3.74 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 4.0 | 2.0 | 3.5 | 2.0 | 3.5 | 3.40 |
| Java        | 3   | 4   | 3   | 4.5 | 3   | 2.0 | 4.0 | 3.0 | 3.5 | 4.0 | 3.38 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 3.0 | 2.0 | 1.5 | 2.5 | 3.0 | 3.13 |
| C++         | 2   | 3   | 2   | 4   | 2   | 2.5 | 3.0 | 1.0 | 2.0 | 3.0 | 2.46 |

HC = Human cognition (15%), MC = Machine cognition (15%), AO = AI-agent operability (20%), RE = Runtime/ecosystem (10%), SV = Strategic viability (10%), AIN = AI-systems native (7.5%), AIE = AI-systems ecosystem (7.5%), SON = Structured-output native (5%), SOE = Structured-output ecosystem (5%), EDR = Ecosystem dependency risk (5%). Weighted is the dimension-weighted sum.

## Reading the matrix

Three clusters emerge.

**Top tier (≥3.85 weighted).** Go, TypeScript, .NET, Kotlin. The ranking compresses sharply at the top: Go 4.04, TypeScript 4.01, .NET 3.96, Kotlin 3.85. **Go ranks #1** — its operability and human-cognition leads carry through both halves of the AI-systems split, and its EDR profile (commercial-first-party SDKs from Anthropic and OpenAI; Google-stewarded language) is moderate but stable. **TypeScript** is a near-tie with Go: AIE=5.0 and SOE=5.0 are best-in-class but the AIN=1.5 / SON=2.5 native scores cap the lift. **.NET** ranks third on Microsoft's first-party AI surface (Semantic Kernel, Microsoft.Extensions.AI, ONNX Runtime .NET) and an EDR of 4.5 — the highest in the cohort — anchored by Microsoft commercial-vendor backing.

**Middle tier (3.40–3.85 weighted).** Rust, Python, Swift. **Python ranks #6 at 3.74** — its AI-systems profile is bimodal (AIN=1.5 because PSF ships no AI packages; AIE=5.0, best in cohort) and the EDR=2.5 profile (Pydantic community-multi-maintainer, Instructor single-maintainer, Outlines small-commercial) holds the weighted total below Go and TypeScript despite tier-leading ecosystem halves. **Rust** anchors on MC=5 / SV=5 with SOE=4.0 via Serde + schemars; EDR=3.5 reflects Rust Foundation backing offset by Serde's bus-factor concentration. **Swift's** AIN=4.0 reflects Apple's first-party AI surface (Core ML, MLX, Foundation Models).

**Lower tier (<3.40 weighted).** Java, Elixir, C++. Java's 3.38 reflects strong ecosystem (AIE=4.0, EDR=4.0) offset by a weak AIN=2.0. Elixir's 3.13 keeps the BEAM-driven RE=4.5 but Elixir's set-theoretic typing being still in research keeps SON=1.5 anchored. C++ at 2.46 is the only language under 3.0.

## Headline findings

1. **Go takes the top slot.** Go's HC=5 / AO=5 lead carries at full weight (35% combined) while TypeScript's AIE=5 / SOE=5 ecosystem strength is offset by AIN=1.5 / SON=2.5 on the native halves. The 0.03-point gap between Go (4.04) and TypeScript (4.01) reads as a near-tie at the top, not a clear winner.

2. **Python's structural exposure is visible in the matrix.** Python's AI-systems profile is bimodal — AIE=5.0 and SOE=5.0 are tier-leading on the ecosystem halves, while AIN=1.5 (PSF ships no AI packages), SON=2.5 (PEP 484 hints are advisory at runtime), and EDR=2.5 (Pydantic community-multi-maintainer, Instructor single-maintainer, Outlines small-commercial) hold the weighted total at 3.74, ranking #6.

3. **The dependency-risk axis rewards Microsoft, JetBrains, and OpenJDK stewardship.** EDR=4.5 (.NET), 4.0 (Java), 4.0 (Kotlin) anchor the middle of the table. Languages with single-maintainer load-bearing dependencies (Python's Instructor, TypeScript's Zod, C++'s llama.cpp + nlohmann/json) score lower — Python 2.5, TypeScript 3.0, C++ 3.0. The dependency-risk axis is the one most likely to move next: if Pydantic adds maintainers or if Anthropic ships a first-party Outlines-equivalent, Python's EDR moves up.

4. **AI-agent operability is the most discriminating axis.** Operability separates Go and TypeScript (AO=5) from C++ (AO=2) more sharply than any other dimension. With AO at 20% weight, this axis alone contributes ±0.6 points to the ranking — larger than any AI-era dimension's individual contribution.

5. **Apple's first-party Swift AI surface is correctly credited on the native half.** Swift's AIN=4.0 reflects Core ML + MLX + Foundation Models as language-steward-shipped, while AIE=2.0 reflects the thin cross-platform ecosystem. Apple's AI-platform investment is durable but Apple-platform-bound.

6. **Verification advantage does not automatically translate to overall ranking.** Rust (MC=5, SV=5) leads on machine cognition and strategic viability but trails the top tier (3.75) because its agent-framework and structured-output ecosystem layers are younger than Python or TypeScript and its AIN=1.5 reflects the absence of a first-party Rust AI runtime. The framework's weighting reflects that verification, operability, AI-systems integration, dependency resilience, and structured-output maturity must all be present for top-tier AI-era position.

## How to use this document

For the reasoning behind any cell:

- Per-language detail: `claims/<language>.yaml` and `evaluations/<language>.yaml`.
- Dimension definitions and weights: `framework/evaluation-framework.md` and `framework/dimensions.md`.
- Cross-cutting reads: `lens-analysis.md` (four lenses) and `agent-friendly-languages.md` (operability deep dive).
- Dynamic vs static comparison: `dynamic-vs-static.md`.

## Limitations

- Scores are author-judgment grounded in claims, not a calibrated multi-rater process.
- Weights are working assumptions. A reasonable reader could reweight runtime/ecosystem higher (favoring Python and the JVM languages), AI-agent operability higher (favoring Go and TypeScript), or dependency-risk higher (favoring .NET and Java). The matrix is robust to small weight perturbations but not to large ones.
- Greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question.
- The native/ecosystem split is sensitive to how "language steward" is defined. The framework draws the line at the entity that ships the canonical language toolchain (Microsoft for .NET; Apple for Swift; JetBrains for Kotlin; Dashbit/Plataformatec for Elixir; PSF for Python; Go team for Go; Rust Foundation for Rust; OpenJDK/Oracle for Java; ISO and major-vendor compilers for C++). Edge cases (CUDA as the language-of-the-stack for accelerators; Dashbit's relationship to Elixir governance) are documented in `framework/dimensions.md`.
- The AI-systems and structured-output ecosystems are evolving rapidly. Expect EDR scores to move first as commercial vendors ship first-party SDKs that displace single-maintainer projects.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
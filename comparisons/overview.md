# Comparison Overview

## Method

All scores reflect framework v0.5, draft evaluations as of 2026-05-02 under the **greenfield framing** documented in `framework/evaluation-framework.md`. Installed base, existing code volume, and incumbent gravity are not scored as advantages; languages are credited for forward-looking properties (governance, future fit, AI-training representation, ecosystem velocity, library maturity for new projects). The framework distinguishes **ecosystem viability** (forward production-readiness today: deployment, observability, integration with non-language systems) from **ecosystem velocity** (the forward rate of language and library improvement). Both are forward-looking and both are credited; legacy installed-base scope is not.

The framework scores **eleven** weighted dimensions: Human cognition (15%), Machine cognition (15%), AI-agent operability (20%), Runtime/ecosystem (10%), Strategic viability (5%), AI-systems native (7.5%), AI-systems ecosystem (7.5%), Structured-output native (5%), Structured-output ecosystem (5%), Ecosystem dependency risk (5%) — the backer-mix and resilience of load-bearing dependencies (higher = lower risk = better) — and **Reachability to top tier (5%)** — forward-trajectory plausibility, how reachable is 5.0 on each below-5 cell within a 3–5-year horizon. The AI-systems and structured-output dimensions are each split into native (what the language steward ships first-party) and ecosystem (third-party, community, commercial-third-party libraries) halves so a 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers; the dependency-risk axis records the present-state difference, and the reachability axis records the forward-trajectory difference.

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

- `comparisons/overview.md` — the eleven-dimension matrix and weighted ranking that anchors the rest.
- `insights/safety-pressure.md` — the institutional/regulatory selection-pressure thesis derived from the safety lens.

## Full matrix (10 languages, 11 dimensions)

| Language    | HC  | MC  | AO  | RE  | SV  | AIN | AIE | SON | SOE | EDR | RCH | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---:|
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 3.0 | 4.0 | 4.01 |
| Go          | 5   | 4   | 5   | 4   | 4   | 2.0 | 3.5 | 3.0 | 3.0 | 3.5 | 3.5 | 4.01 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4.0 | 3.5 | 4.0 | 3.5 | 4.5 | 4.5 | 3.99 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3.0 | 3.0 | 3.5 | 3.0 | 4.0 | 4.0 | 3.85 |
| Python      | 4   | 3   | 4   | 5   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 2.5 | 3.5 | 3.71 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 1.5 | 3.5 | 2.0 | 4.0 | 3.5 | 3.5 | 3.67 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 4.0 | 2.0 | 3.5 | 2.0 | 3.5 | 3.0 | 3.40 |
| Java        | 3   | 4   | 3   | 4.5 | 3   | 2.0 | 4.0 | 3.0 | 3.5 | 4.0 | 3.5 | 3.40 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 3.0 | 2.0 | 1.5 | 2.5 | 3.0 | 2.5 | 3.10 |
| C++         | 2   | 3   | 2   | 4   | 2   | 2.5 | 3.0 | 1.0 | 2.0 | 3.0 | 2.0 | 2.46 |

HC = Human cognition (15%), MC = Machine cognition (15%), AO = AI-agent operability (20%), RE = Runtime/ecosystem (10%), SV = Strategic viability (5%), AIN = AI-systems native (7.5%), AIE = AI-systems ecosystem (7.5%), SON = Structured-output native (5%), SOE = Structured-output ecosystem (5%), EDR = Ecosystem dependency risk (5%), RCH = Reachability to top tier (5%). Weighted is the dimension-weighted sum.

## Reading the matrix

Three clusters emerge.

**Top tier (≥3.85 weighted).** TypeScript, Go, .NET, Kotlin. The ranking compresses sharply at the top: TypeScript 4.01, Go 4.01, .NET 3.99, Kotlin 3.85. **TypeScript and Go tie at the top** — TypeScript's AIE=5.0 / SOE=5.0 ecosystem strength matched by Reach=4.0 (Microsoft stewardship plus commercial-vendor velocity) lifts it level with Go's HC=5 / AO=5 lead. **.NET** ranks third — Microsoft's first-party AI surface (Semantic Kernel, Microsoft.Extensions.AI, ONNX Runtime .NET) and EDR=4.5 (highest in the cohort) are now joined by Reach=4.5 (also highest), making .NET's forward bet the strongest in the cohort even as its present-state weighted total trails the leaders.

**Middle tier (3.40–3.85 weighted).** Python, Rust, Swift, Java. **Python at 3.71** — AI-systems profile remains bimodal (AIN=1.5 because PSF ships no AI packages; AIE=5.0 best in cohort) and EDR=2.5 holds the weighted total below the leaders despite tier-leading ecosystem halves; Reach=3.5 reflects sustained typing-PEP cadence offset by structural AIN absence. **Rust at 3.67** anchors on MC=5 / SV=5 with SOE=4.0 via Serde + schemars; Reach=3.5 reflects verification ceiling already at top while AIN closing path is steward-absent. **Swift's** AIN=4.0 reflects Apple's first-party AI surface, but Reach=3.0 records the Apple-locked trajectory.

**Lower tier (<3.40 weighted).** Elixir, C++. Elixir at 3.10 keeps the BEAM-driven RE=4.5 but Reach=2.5 records the wide gap-size and slow-velocity outlook. C++ at 2.46 is the only language under 3.0; Reach=2.0 compounds the present-state gap with low closing-path plausibility.

## Headline findings

1. **TypeScript and Go tie at the top.** Go's HC=5 / AO=5 lead carries at full weight, but TypeScript's AIE=5 / SOE=5 ecosystem strength combined with Reach=4.0 (Microsoft stewardship + commercial-vendor velocity) lifts it level. Both score 4.01 — a true tie at the top, not a near-tie.

2. **Python's structural exposure is visible in the matrix.** Python's AI-systems profile is bimodal — AIE=5.0 and SOE=5.0 are tier-leading on the ecosystem halves, while AIN=1.5 (PSF ships no AI packages), SON=2.5 (PEP 484 hints are advisory at runtime), and EDR=2.5 hold the weighted total at 3.71, ranking #5.

3. **The dependency-risk axis rewards Microsoft, JetBrains, and OpenJDK stewardship.** EDR=4.5 (.NET), 4.0 (Java), 4.0 (Kotlin) anchor the middle of the table. Languages with single-maintainer load-bearing dependencies (Python's Instructor, TypeScript's Zod, C++'s llama.cpp + nlohmann/json) score lower — Python 2.5, TypeScript 3.0, C++ 3.0. The dependency-risk axis is the one most likely to move next: if Pydantic adds maintainers or if Anthropic ships a first-party Outlines-equivalent, Python's EDR moves up.

4. **Reachability narrows the spread at the top.** Reach=4.5 (.NET), 4.0 (TypeScript, Kotlin) lift the trajectory bet for vendor-stewarded languages; Reach=2.0–2.5 (C++, Elixir) compound their current-state gaps with low closing-path plausibility. The dimension separates "where each language is now" from "where each language is plausibly going" — and shows that .NET, despite trailing TypeScript and Go on present-state weighted total, has the strongest forward trajectory of the cohort.

5. **AI-agent operability is the most discriminating axis.** Operability separates Go and TypeScript (AO=5) from C++ (AO=2) more sharply than any other dimension. With AO at 20% weight, this axis alone contributes ±0.6 points to the ranking — larger than any AI-era dimension's individual contribution.

6. **Apple's first-party Swift AI surface is correctly credited on the native half.** Swift's AIN=4.0 reflects Core ML + MLX + Foundation Models as language-steward-shipped, while AIE=2.0 reflects the thin cross-platform ecosystem and Reach=3.0 records the Apple-locked trajectory.

7. **Verification advantage does not automatically translate to overall ranking.** Rust (MC=5, SV=5) leads on machine cognition and strategic viability but trails the top tier (3.67) because its agent-framework and structured-output ecosystem layers are younger than Python or TypeScript and its AIN=1.5 reflects the absence of a first-party Rust AI runtime. Reach=3.5 records the tradeoff: verification ceiling at top, AIN structurally absent.

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

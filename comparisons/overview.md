# Comparison Overview

## Method

All scores reflect framework v0.3, draft evaluations as of 2026-05-01 under the **greenfield framing** documented in `framework/evaluation-framework.md`. Installed base, existing code volume, and incumbent gravity are not scored as advantages; languages are credited for forward-looking properties (governance, future fit, AI-training representation, ecosystem velocity, library maturity for new projects). The framework distinguishes **ecosystem viability** (forward production-readiness today: deployment, observability, integration with non-language systems such as databases, OS, hardware, accelerators) from **ecosystem velocity** (the forward rate of language and library improvement). Both are forward-looking and both are credited; legacy installed-base scope is not.

The framework now scores seven weighted dimensions: Human cognition (15%), Machine cognition (15%), AI-agent operability (20%), Runtime/ecosystem (15%), Strategic viability (10%), AI-systems interoperability (15%), and **Structured-output maturity (10%)** — added in v0.3 to capture how mature the language's ecosystem is for the type/data layer that sits between LLM output and program logic: schema-validated JSON parsing, LLM tool-call argument typing, constrained generation support, type-safe structured outputs from LLM SDKs, and JSON Schema generation from native types. Five percentage points were pulled from each of Machine cognition and AI-systems interoperability — both conceptually adjacent to the new dimension. Scores are 1.0–5.0 in 0.5-point increments per the rubric in `framework/scoring-rubric.md`. Justifications draw on the per-language claims under `claims/` and the cross-cutting lens reading in `lens-analysis.md`.

These are draft scores intended to be falsifiable by the underlying claims, not final verdicts.

The cohort is 10 languages (cpp, dotnet, elixir, go, java, kotlin, python, rust, swift, typescript). Mojo, Zig, Julia, and Haskell were dropped: Mojo and Zig pre-1.0, Julia narrowly numerical, Haskell a verification reference rather than a default. The remaining 10 cover the languages a greenfield team is actually deciding between.

## Full matrix (10 languages, 7 dimensions)

| Language    | HC  | MC  | AO  | RE  | SV  | AI  | SO  | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---: |---:|
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 4.5 | 5.0 | 4.38 |
| Python      | 4   | 3   | 4   | 5   | 4   | 5   | 5.0 | 4.25 |
| Go          | 5   | 4   | 5   | 4   | 4   | 3.5 | 3.0 | 4.17 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4   | 4.0 | 4.00 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 3   | 3.5 | 3.90 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3   | 3.5 | 3.88 |
| Java        | 3   | 4   | 3   | 4.5 | 3   | 3.5 | 3.5 | 3.50 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 2.5 | 2.5 | 3.25 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 2   | 2.5 | 3.25 |
| C++         | 2   | 3   | 2   | 4   | 2   | 3   | 2.0 | 2.60 |

HC = Human cognition (15%), MC = Machine cognition (15%), AO = AI-agent operability (20%), RE = Runtime and ecosystem (15%), SV = Strategic viability (10%), AI = AI-systems interoperability (15%), SO = Structured-output maturity (10%). Weighted sum the seven columns at their dimension weights.

## Reading the matrix

Three clusters emerge.

**Top tier (>= 4.0 weighted).** TypeScript, Python, Go, .NET. The 7th dimension lifts Python past Go: Python's Pydantic-backed structured-output stack and TypeScript's Zod-driven equivalent both score 5.0 on the new axis, reshuffling the order at the top. TypeScript retains the lead. Go's structured-output ecosystem is solid but lacks an LLM-specific Pydantic/Zod equivalent and fragments across validator libraries.

**Middle tier (3.0-3.99 weighted).** Rust, Kotlin, Java, Elixir, Swift. Rust's Serde + schemars + Rust-enum sum-type modeling lift it on the new axis (SO=3.5) and keep it above Kotlin by 0.02. Java holds steady at 3.50 with Records + Jackson + LangChain4j. Elixir and Swift now tie at 3.25 — Swift's Apple-platform structured-output thinness and Elixir's community-maintained instructor_ex pull both down by similar amounts.

**Lower tier (< 3.0 weighted).** C++ alone. The production-grade compiler ecosystem and accelerator-host advantages remain credited, but the absence of a Pydantic-equivalent schema layer and the lack of standard reflection (P2996 still in progress) push the structured-output score to 2.0; documented memory-safety pressure continues to dominate strategic viability.

## Headline findings

1. **Structured-output maturity reshuffles the top tier.** Adding a 7th dimension that scores how mature a language's schema-validation, LLM tool-call typing, constrained-generation, and JSON-Schema-from-types stack is moves Python past Go. Pydantic + Instructor + Outlines for Python and Zod + Vercel AI SDK + zod-to-json-schema for TypeScript define the tier-leading 5.0 anchor. Go's encoding/json + struct-tags is type-safe but the validation ecosystem is fragmented and the LLM-specific ergonomics layer is thinner.

2. **Half-point scores still reveal genuine differentiation.** Kotlin (MC=4.5), Java (RE=4.5), and Elixir (RE=4.5) retain their integer-4-line moves. The new axis adds further half-step differentiation: Rust (SO=3.5), Kotlin (SO=3.5), Java (SO=3.5), Elixir (SO=2.5), Swift (SO=2.5).

3. **AI-agent operability is still the most discriminating dimension among the operability/safety axes.** Operability separates Go and TypeScript from C++ even when underlying language quality is comparable on other dimensions. Operability tracks toolchain unification and LSP-exposed semantic models, not type-system depth.

4. **Strategic viability and runtime/ecosystem remain forward-looking under greenfield framing.** Python keeps a strong runtime/ecosystem score because ML-domain library velocity is forward-relevant; C++ keeps a strong runtime/ecosystem score because its production toolchain and hardware integration are forward-relevant; both lose strategic-viability credit that previously came from installed base.

5. **Verification advantage does not automatically translate to overall ranking.** Rust (MC=5) leads on machine cognition but trails the top tier because its agent-framework and structured-output layers are younger than Python or TypeScript. The framework's weighting reflects that verification, operability, AI-systems integration, and structured-output maturity must all be present for top-tier AI-era position.

6. **The dynamic-static gap is narrowing where gradual typing and runtime validation co-exist.** TypeScript and Python both reach SO=5.0 because Zod and Pydantic combine schema-as-code with type inference (TypeScript) or runtime validation (Python). The boundary between LLM output and program logic is now defended at runtime even where the host type system is dynamic.

## How to use this document

For the reasoning behind any cell:

- Per-language detail: `claims/<language>.yaml` and `evaluations/<language>.yaml`.
- Dimension definitions and weights: `framework/evaluation-framework.md` and `framework/dimensions.md`.
- Cross-cutting reads: `lens-analysis.md` (four lenses) and `agent-friendly-languages.md` (operability deep dive).
- Dynamic vs static comparison: `dynamic-vs-static.md`.

## Limitations

- v0.3 scores are author-judgment grounded in claims, not a calibrated multi-rater process.
- Weights are working assumptions. A reasonable reader could reweight runtime/ecosystem higher (favoring Python and the JVM languages) or AI-agent operability higher (favoring Go and TypeScript). The matrix is robust to small weight perturbations but not to large ones.
- Greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question, and the matrix above will under-credit Java, Python, and C++ for that purpose.
- The AI-systems interoperability and Structured-output maturity dimensions are recent additions; the underlying ecosystems are evolving rapidly. Expect scores on both axes to shift as MCP adoption broadens, additional first-party SDKs land, and constrained-generation tooling matures.

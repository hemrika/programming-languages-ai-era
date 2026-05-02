# Programming Languages in the AI Era

*A greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development.* **Framework v0.4** (2026-05-02).

## TL;DR

Across 10 languages scored on **ten** weighted dimensions and read through four cross-cutting lenses, the top tier is **Go (4.04)**, **TypeScript (4.01)**, **.NET / C# (3.96)**, **Kotlin (3.85)**. **Rust (3.75)** and **Python (3.74)** sit just below in a near-tie. Swift, Java, Elixir, and C++ trail in the lower tier.

**Go ranks #1** because its operability and human-cognition advantages carry at full weight while its commercial-first-party SDK ecosystem (Anthropic Go SDK, OpenAI Go SDK) and Google language stewardship anchor the dependency-risk profile. **Python ranks #6 at 3.74**: its AI-systems profile is bimodal — AIE=5.0 (best in cohort) on the ecosystem half against AIN=1.5 on the native half because PSF ships no AI packages — and the EDR=2.5 score reflects Pydantic community-multi-maintainer, Instructor single-maintainer, and Outlines small-commercial backing. **.NET ranks third** because Microsoft's first-party Semantic Kernel + Microsoft.Extensions.AI + ONNX Runtime .NET stack delivers AIN=4.0 and EDR=4.5 (highest in cohort) reflects Microsoft-vendor anchoring.

The full matrix sits in `comparisons/overview.md` and is reproduced in *The Matrix* below. Recommendations by domain follow in *Recommendations by Use Case*.

## Framing

This report evaluates languages from a **greenfield** position: a new AI-era project starting today, not a maintenance estate. Installed base, code volume, and incumbent gravity are not credited. The framework instead credits forward-looking properties: governance quality, future fit, AI-training representation, ecosystem velocity, and ecosystem viability.

Each language is scored 1.0–5.0 in 0.5-point increments on **ten** dimensions:

- **Human cognition (15%)** — can humans understand and govern the code?
- **Machine cognition (15%)** — can compilers, analyzers, and AI systems reason about it?
- **AI-agent operability (20%)** — can agents safely modify and verify it?
- **Runtime and ecosystem (10%)** — can it run production systems?
- **Strategic viability (10%)** — will it remain relevant?
- **AI-systems native (7.5%)** — what the language steward ships first-party for AI: Microsoft Semantic Kernel for .NET, Apple Core ML / MLX for Swift, JetBrains kotlinx-serialization for Kotlin, Dashbit's Bumblebee/Nx for Elixir.
- **AI-systems ecosystem (7.5%)** — third-party / community / commercial-third-party libraries: Anthropic SDKs, OpenAI SDKs, LangChain ports, MCP SDKs published outside the steward, vector-store clients.
- **Structured-output native (5%)** — schema-validated parsing, types-to-schema generation, exhaustiveness in steward-shipped facilities: System.Text.Json + JsonSchemaExporter, Codable, encoding/json, kotlinx-serialization.
- **Structured-output ecosystem (5%)** — Pydantic, Zod, Serde, Jackson, Newtonsoft.Json, Hibernate Validator, Ecto, Instructor, Outlines, Vercel AI SDK structured outputs.
- **Ecosystem dependency risk (5%)** — the backer-mix and resilience of load-bearing dependencies. **Higher = lower risk = better.**

Four cross-cutting lenses read across the dimensions:

1. **Verification advantage** — what the compiler can falsify before code runs.
2. **Agentic development advantage** — fast feedback, deterministic tooling, clear diagnostics.
3. **Safety pressure** — alignment with regulatory and platform-vendor selection criteria.
4. **Abstraction compression** — how much behaviour is expressed per line, with what cost in implicit context.

What this report does credit: forward governance, future fit under AI-era pressure, training-corpus representation, library availability for new projects, ecosystem viability, AI-systems integration depth (split into native and ecosystem), structured-output maturity (split into native and ecosystem), and the resilience of load-bearing dependencies. What it does not credit: legacy installed base, the volume of code already written, or the inertia of any incumbent.

## The Matrix

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

Three clusters emerge. **Top tier (>=3.85).** Go, TypeScript, .NET, Kotlin. **Middle tier (3.40–3.84).** Rust, Python, Swift. **Lower tier (<3.40).** Java, Elixir, C++. The script `scripts/score_summary.py` regenerates this table from the per-language evaluations.

## Five Findings

### 1. Go takes the top slot.

Go's HC=5 / AO=5 lead carries at full weight (35% combined) while TypeScript's AIE=5 / SOE=5 ecosystem strength is offset on the native halves by AIN=1.5 / SON=2.5. The 0.03-point gap between Go (4.04) and TypeScript (4.01) reads as a near-tie at the top, not a clear winner. Go sits 0.30 above Python (3.74).

### 2. Python's structural exposure is visible in the matrix.

Python's AI-systems profile is bimodal — strong on the ecosystem half, weak on the native half — which holds the weighted total below Go and TypeScript. Python earns AIE=5.0 [python-021, python-022, python-023, python-024, python-025] and SOE=5.0 [python-026, python-027, python-028, python-029] — tier-leading on the ecosystem halves. AIN=1.5 (PSF ships no AI packages [python-036]), SON=2.5 (PEP 484 hints are advisory at runtime [python-030]), and EDR=2.5 (Pydantic community-multi-maintainer [python-031], Instructor single-maintainer [python-032], Outlines small-commercial [python-033]) hold the weighted total at 3.74, ranking #6.

### 3. The dependency-risk axis rewards Microsoft, JetBrains, and OpenJDK stewardship.

EDR=4.5 (.NET) [dotnet-029, dotnet-030, dotnet-031, dotnet-032, dotnet-033], EDR=4.0 (Java) [java-029, java-030, java-031, java-032, java-033], EDR=4.0 (Kotlin) [kotlin-030, kotlin-031, kotlin-032, kotlin-033, kotlin-034] anchor the middle of the table. Microsoft funds the .NET runtime and the in-box AI surface as a single commercial-vendor strategy. OpenJDK's multi-vendor stewardship (Oracle, IBM, Red Hat) anchors the JVM. JetBrains stewardship anchors Kotlin at both the language and serialization layers. Languages with single-maintainer load-bearing dependencies (Python's Instructor [python-032], TypeScript's Zod [typescript-029], C++'s llama.cpp [cpp-027] + nlohmann/json [cpp-028]) score lower — Python 2.5, TypeScript 3.0, C++ 3.0. The dependency-risk axis is the one most likely to move next: if Pydantic adds maintainers or Anthropic ships a first-party Outlines-equivalent, Python's EDR moves up.

### 4. AI-agent operability is the most discriminating dimension.

Operability separates Go and TypeScript (AO=5) [go-003, go-015, typescript-006, typescript-007] from C++ (AO=2) [cpp-012, cpp-015] more sharply than any other dimension. With AO at 20% weight, this axis alone contributes ±0.6 points to the ranking — larger than any AI-era dimension's individual contribution. The pattern tracks toolchain unification and LSP-exposed semantic models, not type-system depth. Go has a single canonical command [go-003], single canonical formatter [go-002], and gopls as the official LSP server [go-015]. TypeScript reaches the same surface from a dynamic substrate via strict-mode [typescript-004], discriminated unions [typescript-002], and the language service Microsoft itself originated [typescript-006, typescript-007].

### 5. Apple's first-party Swift AI surface is correctly credited on the native half.

Swift's AIN=4.0 reflects Core ML + MLX + Foundation Models as language-steward-shipped [swift-019, swift-023], while AIE=2.0 reflects the thin cross-platform ecosystem [swift-020, swift-021, swift-022]. Apple's AI-platform investment is durable but Apple-platform-bound; Linux/server-side Swift AI dependencies remain community-multi-maintainer.

## Per-Language Verdicts

### Go — 4.04 — *Default for backend services where deliberate minimalism is acceptable; top of the table.*

Strongest forward case: a uniquely low-friction agent profile built from a single canonical command covering the full development loop [go-003], gofmt as a single canonical formatter [go-002], and gopls as the official LSP server [go-015]. AI-systems integration: Anthropic Go SDK [go-020], OpenAI Go SDK [go-021], official MCP Go SDK [go-022], production Kafka and Postgres clients [go-023]. Structured-output: encoding/json + struct tags [go-025] is steward-shipped, openai-go schema generation [go-026], invopop/jsonschema for native types-to-JSON-Schema [go-028]. EDR=3.5 reflects Google language stewardship plus commercial-first-party SDKs from Anthropic and OpenAI; the validation library landscape is fragmented and LangChainGo is community-only [go-033]. **Load-bearing risk:** the deliberate type-system minimalism — no sum types, late generics, no exhaustive enums [go-017] — and the agent-framework ecosystem lag [go-024] remain real.

### TypeScript — 4.01 — *Default for application work in the JavaScript-shaped world; near-tie with Go.*

Strongest forward case: an optional static type layer over JavaScript [typescript-001] with discriminated unions for exhaustive narrowing [typescript-002] and a strict-mode bundle [typescript-004], all served through a Microsoft-maintained Language Service [typescript-006] over the Language Server Protocol Microsoft originated [typescript-007]. AI-systems ecosystem is tier-leading at AIE=5.0: Anthropic SDK [typescript-019], OpenAI SDK [typescript-020], LangChain.js [typescript-021], official MCP TypeScript SDK [typescript-022], TypeScript LlamaIndex [typescript-023]. Structured-output ecosystem also tier-leading at SOE=5.0: Zod [typescript-024], Zod-typed tool calls [typescript-025], Vercel AI SDK [typescript-026], zod-to-json-schema [typescript-027]. **Load-bearing risk:** no language-steward-shipped AI surface (AIN=1.5) [typescript-034], type system is intentionally not sound [typescript-005, typescript-017], EDR=3.0 reflects Zod's single-maintainer concentration [typescript-029] offset by Microsoft language-layer backing [typescript-031].

### .NET (C#) — 3.96 — *Ranks third on the strength of the Microsoft-first-party AI surface and the dependency-risk anchor.*

Strongest forward case: nullable reference types with static null-state flow analysis [dotnet-003], pattern-matching family across switch expressions [dotnet-004], Roslyn as a public compiler-platform API exposing the live SemanticModel [dotnet-006, dotnet-014]. **AIN=4.0 anchors the climb:** Microsoft Semantic Kernel [dotnet-020], MCP C# SDK with Microsoft co-maintenance [dotnet-021], ONNX Runtime .NET [dotnet-022], OpenAI .NET via Microsoft [dotnet-023]. Structured-output native is tier-leading at SON=4.0: System.Text.Json + source generation [dotnet-024], JsonSchemaExporter [dotnet-027], Semantic Kernel function calling [dotnet-025]. **EDR=4.5 is the highest in the cohort** [dotnet-029, dotnet-030, dotnet-031, dotnet-032, dotnet-033] — nearly the entire load-bearing AI/SO surface is Microsoft-first-party. **Load-bearing risk:** nullable reference types are opt-in [dotnet-012], MSBuild surface [dotnet-011], smaller AIE than Python or TypeScript [dotnet-019].

### Kotlin — 3.85 — *Default for JVM application work; ranks fourth on EDR credit.*

Strongest forward case: nullable types as a type-system distinction [kotlin-001], sealed hierarchies with exhaustive `when` [kotlin-002, kotlin-003] (MC=4.5), coroutines for structured concurrency [kotlin-006], Kotlin Multiplatform stable across JVM/Android/iOS/JS/Native [kotlin-015]. AIN=3.0 reflects JetBrains-shipped MCP Kotlin SDK [kotlin-021] and Kotlin Multiplatform [kotlin-023]. SON=3.5 with kotlinx-serialization (JetBrains-stewarded) [kotlin-025] and sealed classes + exhaustive when [kotlin-026]. **EDR=4.0** [kotlin-030, kotlin-031, kotlin-032, kotlin-033, kotlin-034] — JetBrains commercial-vendor backing at the language layer plus JVM-interop access to LangChain4j and OpenJDK. **Load-bearing risk:** governance dependence on JetBrains [kotlin-009], thin Kotlin-native AI tooling [kotlin-024], Kotlin-only structured-output ecosystem trails Java's [kotlin-029].

### Rust — 3.75 — *Default for systems, infrastructure, and security-sensitive work.*

Strongest forward case: ownership-checked memory rules without garbage collection [rust-001, rust-002, rust-003], exhaustive `match` over enums [rust-006, rust-007], external regulatory alignment via NSA recommendations and Android telemetry [rust-015, rust-016, rust-017]. AIE=3.5: official MCP Rust SDK [rust-027], async-openai [rust-028], HuggingFace candle [rust-029], production Postgres/Kafka [rust-031]. SON=2.0 reflects no first-party Rust schema-validation library; SOE=4.0 with Serde [rust-032] + schemars [rust-033] + Rust-enum tagged unions [rust-035]. **EDR=3.5** [rust-037, rust-038, rust-039, rust-040, rust-041] balances the Rust Foundation's multi-vendor backing against Serde and schemars community-multi-maintainer profiles. **Load-bearing risk:** AIN=1.5 (no first-party Rust AI runtime [rust-042]), agent-framework ecosystem younger than Python or TypeScript [rust-030].

### Python — 3.74 — *Ranks #6 on a bimodal AI-systems profile: tier-leading ecosystem, weak native, dependency-risk-exposed.*

Strongest forward case: top GitHub language by activity [python-012], sustained typing PEP cadence [python-016], pyright/Pylance + bundled typeshed stubs [python-018], uv as a Rust-based fast package manager [python-011]. AIE=5.0 (best in cohort) with Anthropic SDK [python-021], OpenAI SDK [python-022], LangChain Python [python-023], MCP Python SDK [python-024], universal vector-store coverage [python-025]. SOE=5.0 with Pydantic [python-026], OpenAI Pydantic response_format [python-027], Instructor [python-028], Outlines [python-029]. **AIN=1.5** because PSF ships no AI-specific package [python-036]. **SON=2.5** because PEP 484 hints are advisory at runtime [python-030]. **EDR=2.5** [python-031, python-032, python-033, python-034, python-035] — Pydantic community-multi-maintainer, Instructor single-maintainer (Jason Liu), Outlines small-commercial. The native + ecosystem split records the structural exposure that ecosystem-only credit would obscure.

### Swift — 3.40 — *Default for Apple-platform application work; native-AI credit reflects Apple's first-party stack.*

Strongest forward case: optionals as a type-system distinction [swift-001], memory-safety rules with conflicting-access detection [swift-004], language-level async/await and actors [swift-003], an open Swift Evolution process [swift-006]. **AIN=4.0** for Apple's first-party ML stack via Core ML / Create ML [swift-019] and MLX [swift-023]. SON=3.5 with Codable [swift-024] and enum + exhaustive switch [swift-025]. **Load-bearing risk:** AIE=2.0 (no first-party Anthropic or OpenAI Swift SDKs [swift-021], cross-platform agent-framework support essentially absent [swift-022]). EDR=3.5 strong on Apple-platform AI; weaker on cross-platform Swift surface [swift-031, swift-032].

### Java — 3.38 — *Forward case is narrower than its historic position suggested.*

Strongest forward case: virtual threads as a JVM-level concurrency primitive [java-006], structured concurrency in JEP 453 [java-015], records and sealed classes for closed-hierarchy pattern matching [java-002, java-003, java-004]. AIE=4.0 with Anthropic Java SDK [java-019], LangChain4j [java-020], official MCP Java SDK [java-021], Apache Kafka client [java-022], ONNX Runtime Java [java-023]. SOE=3.5 with Jackson + Bean Validation [java-024], LangChain4j AI Services [java-025]. **EDR=4.0** [java-029, java-030, java-031, java-032, java-033] — OpenJDK multi-vendor stewardship, Hibernate Validator (Red Hat), Anthropic first-party Java SDK. **Load-bearing risk:** AIN=2.0 (OpenJDK ships no AI module first-party [java-034]), pre-records boilerplate [java-013], preview-feature delays [java-016].

### Elixir — 3.13 — *Default for fault-tolerant distributed systems and real-time AI-augmented UIs.*

Strongest forward case: BEAM process and concurrency model [elixir-001, elixir-004], OTP supervision trees [elixir-002], Phoenix LiveView [elixir-009, elixir-014]. AIN=3.0 with Bumblebee on Nx (Dashbit-stewarded) [elixir-019, elixir-020] and Phoenix.PubSub for BEAM-native streaming [elixir-021]. SOE=2.5 with Ecto changesets [elixir-024] + instructor_ex [elixir-025]. **Load-bearing risk:** dynamically typed [elixir-005] with set-theoretic types still in research [elixir-016, elixir-027]; LLM-provider SDKs mostly community-maintained [elixir-022]; agent-framework ecosystem small [elixir-023]; SON=1.5 reflects no native compile-time contract safety; EDR=3.0 mixes Dashbit anchoring with single-maintainer instructor_ex [elixir-030].

### C++ — 2.46 — *Default only for accelerator host code where the safety penalty is knowingly accepted.*

Strongest forward case: ISO standardization with three-yearly revisions [cpp-001], C++20 modules and ranges [cpp-002], the dominant accelerator and inference toolchains — llama.cpp implemented in C++ [cpp-017], ONNX Runtime C++ API [cpp-018], CUDA/ROCm/HIP/SYCL/oneAPI all primarily targeting C++ [cpp-013, cpp-019], librdkafka for streaming [cpp-021], and llama.cpp's native GBNF JSON-schema-constrained decoding [cpp-024]. **Load-bearing risk:** memory-safety pressure [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008]; AIN=2.5 with no ISO-shipped AI facilities [cpp-032]; SON=1.0 (no native reflection, no in-box validation [cpp-026]); EDR=3.0 mixes commercial-first-party CUDA/ONNX backing with single-maintainer concentration on llama.cpp and nlohmann/json [cpp-027, cpp-028].

## Recommendations by Use Case

| Domain | Primary | Alternatives | Trade-off |
|---|---|---|---|
| Greenfield application work | TypeScript or Go | Kotlin, .NET (C#) | Operability and AI-systems ecosystem breadth (TS) versus operability and language-steward AI dependency-risk anchor (Go). |
| Systems / infrastructure / security-sensitive | Rust | Go | Verification and safety [rust-001, rust-015], accepting compile-time and learning-curve cost [rust-020, rust-025]. |
| Data / AI/ML / scripting / AI-systems integration | Python | TypeScript (for data products) | Most complete AI-systems ecosystem [python-021..025] over verification gap and dependency-risk profile [python-030, python-032]. Treat type discipline as day-one investment. |
| AI-application work where vendor-anchored dependencies matter | .NET | Java | Microsoft-first-party Semantic Kernel + Microsoft.Extensions.AI + ONNX Runtime .NET [dotnet-020, dotnet-022, dotnet-026] for EDR=4.5 anchoring. |
| Fault-tolerant distributed systems | Elixir | Go, Rust | BEAM runtime properties [elixir-001, elixir-002] over verification ceiling [elixir-005, elixir-016]. |
| AI-native compute kernels | Rust | C++ (only where unavoidable) | Rust's accelerator/ML ecosystem [rust-022, rust-029] over C++ memory-safety exposure [cpp-004, cpp-006]. |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] | Native platform integration [swift-003, swift-014, swift-019], accepting cross-platform AI integration thinness [swift-021]. |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) | Toolchain access [cpp-013, cpp-019], explicitly accepting safety penalty [cpp-004, cpp-006]. |
| JVM application work needing AI integration | Java | Kotlin | LangChain4j [java-020] and Anthropic Java SDK [java-019] for direct JVM use; Kotlin for null-safety and abstraction. |

## Limitations

The framework weights (HC 15%, MC 15%, AO 20%, RE 10%, SV 10%, AIN 7.5%, AIE 7.5%, SON 5%, SOE 5%, EDR 5%) are working assumptions. A reasonable reader could weight runtime/ecosystem higher (favouring Python and the JVM languages), AI-agent operability higher (favouring Go and TypeScript), or dependency-risk higher (favouring .NET and Java). The matrix is robust to small weight perturbations but not to large ones.

The snapshot date is **2026-05-02**. The AI-systems and structured-output ecosystems and the dependency-risk profile are the most volatile axes: MCP adoption is broadening, first-party SDKs are landing, structured-output libraries are converging on Pydantic/Zod-shaped patterns, and commercial vendors are increasingly publishing first-party SDKs that displace single-maintainer projects. Expect EDR scores to move first.

The greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question, and this matrix will under-credit Java, Python, and C++ for that purpose.

The native/ecosystem split is sensitive to how "language steward" is defined. The framework draws the line at the entity that ships the canonical language toolchain. Edge cases (CUDA as the language-of-the-stack for accelerators; Dashbit's relationship to Elixir governance) are documented in `framework/dimensions.md`.

Finally, the scores are single-rater author judgments grounded in atomic claims with primary-source citations, not the average of an independent expert panel. Each cell traces through Insight → Evaluation → Claim → Source.

## Reading and Reproducibility

The corpus is structured for traceability:

- **Framework** — `framework/dimensions.md` (criteria), `framework/evaluation-framework.md` (weights and lenses), `framework/scoring-rubric.md` (1.0–5.0 rubric in 0.5-point increments).
- **Claims** — `claims/<language>.yaml`, ~340 atomic claims across 10 languages, each with a primary-source citation, explicit polarity, and (since v0.4) `backer:` tag.
- **Sources** — `sources/<language>-sources.yaml`, ~280 source entries with publication metadata.
- **Evaluations** — `evaluations/<language>.yaml`, per-language ten-dimension scores with `supporting_claims:` traceability into the claim corpus.
- **Comparisons** — `comparisons/overview.md`, `comparisons/lens-analysis.md`, `comparisons/agent-friendly-languages.md`, `comparisons/dynamic-vs-static.md`.
- **Insights** — `insights/agentic-feedback-loops.md`, `insights/ai-favors-verifiability.md`, `insights/safety-pressure.md`, `insights/incumbent-risk.md`.

The matrix is reproducible via `scripts/score_summary.py`, which reads `evaluations/*.yaml` and emits the table in `comparisons/overview.md`. The full methodology is documented in `outputs/evidence-backed-research-execution-plan.md`.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
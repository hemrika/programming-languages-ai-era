# Programming Languages in the AI Era

*A greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development.* **Framework v0.5** (2026-05-02).

## TL;DR

Across 10 languages scored on **eleven** weighted dimensions and read through four cross-cutting lenses, the top tier is **TypeScript (4.01)**, **Go (4.01)**, **.NET / C# (3.99)**, **Kotlin (3.85)**. **Python and Rust tie at 3.71** in the middle tier. **Java (3.50)** holds solo #7. Swift sits at 3.40, with Elixir and C++ in the lower tier.

**TypeScript and Go tie at the top** — TypeScript's AIE=5 / SOE=5 ecosystem strength combined with Reach=4.0 (Microsoft stewardship + commercial-vendor velocity) lifts it level with Go's HC=5 / AO=5 lead. **Python ranks #5 at 3.71**: its AI-systems profile is bimodal — AIE=5.0 (best in cohort) on the ecosystem half against AIN=1.5 on the native half because PSF ships no AI packages — and the EDR=2.5 score reflects Pydantic community-multi-maintainer, Instructor single-maintainer, and Outlines small-commercial backing. **.NET ranks third at 3.99** because Microsoft's first-party Semantic Kernel + Microsoft.Extensions.AI + ONNX Runtime .NET stack delivers AIN=4.0; EDR=4.5 (highest in cohort) and Reach=4.5 (also highest) make .NET's forward bet the strongest in the cohort even as its present-state weighted total trails the leaders.

The full matrix sits in `comparisons/overview.md` and is reproduced in *The Matrix* below. Recommendations by domain follow in *Recommendations by Use Case*.

## Framing

This report evaluates languages from a **greenfield** position: a new AI-era project starting today, not a maintenance estate. Installed base, code volume, and incumbent gravity are not credited. The framework instead credits forward-looking properties: governance quality, future fit, AI-training representation, ecosystem velocity, and ecosystem viability.

Each language is scored 1.0–5.0 in 0.5-point increments on **eleven** dimensions:

- **Human cognition (15%)** — can humans understand and govern the code?
- **Machine cognition (15%)** — can compilers, analyzers, and AI systems reason about it?
- **AI-agent operability (20%)** — can agents safely modify and verify it?
- **Runtime and ecosystem (10%)** — can it run production systems?
- **Strategic viability (5%)** — will it remain relevant?
- **AI-systems native (7.5%)** — what the language steward ships first-party for AI: Microsoft Semantic Kernel for .NET, Apple Core ML / MLX for Swift, JetBrains kotlinx-serialization for Kotlin, Dashbit's Bumblebee/Nx for Elixir.
- **AI-systems ecosystem (7.5%)** — third-party / community / commercial-third-party libraries: Anthropic SDKs, OpenAI SDKs, LangChain ports, MCP SDKs published outside the steward, vector-store clients.
- **Structured-output native (5%)** — schema-validated parsing, types-to-schema generation, exhaustiveness in steward-shipped facilities: System.Text.Json + JsonSchemaExporter, Codable, encoding/json, kotlinx-serialization.
- **Structured-output ecosystem (5%)** — Pydantic, Zod, Serde, Jackson, Newtonsoft.Json, Hibernate Validator, Ecto, Instructor, Outlines, Vercel AI SDK structured outputs.
- **Ecosystem dependency risk (5%)** — the backer-mix and resilience of load-bearing dependencies. **Higher = lower risk = better.**
- **Reachability to top tier (5%)** — forward-trajectory plausibility, how reachable is 5.0 on each below-5 cell within a 3–5-year horizon. **Higher = more reachable.**

Four cross-cutting lenses read across the dimensions:

1. **Verification advantage** — what the compiler can falsify before code runs.
2. **Agentic development advantage** — fast feedback, deterministic tooling, clear diagnostics.
3. **Safety pressure** — alignment with regulatory and platform-vendor selection criteria.
4. **Abstraction compression** — how much behaviour is expressed per line, with what cost in implicit context.

What this report does credit: forward governance, future fit under AI-era pressure, training-corpus representation, library availability for new projects, ecosystem viability, AI-systems integration depth (split into native and ecosystem), structured-output maturity (split into native and ecosystem), and the resilience of load-bearing dependencies. What it does not credit: legacy installed base, the volume of code already written, or the inertia of any incumbent.

## The Matrix

| Language    | HC  | MC  | AO  | RE  | SV  | AIN | AIE | SON | SOE | EDR | RCH | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---:|
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 3.0 | 4.0 | 4.01 |
| Go          | 5   | 4   | 5   | 4   | 4   | 2.0 | 3.5 | 3.0 | 3.0 | 3.5 | 3.5 | 4.01 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4.0 | 3.5 | 4.0 | 3.5 | 4.5 | 4.5 | 3.99 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3.0 | 3.0 | 3.5 | 3.0 | 4.0 | 4.0 | 3.85 |
| Python      | 4   | 3   | 4   | 5   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 2.5 | 3.5 | 3.71 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 1.5 | 4.0 | 2.0 | 4.0 | 3.5 | 3.5 | 3.71 |
| Java        | 3   | 4   | 3.5 | 4.5 | 3   | 2.0 | 4.0 | 3.0 | 3.5 | 4.0 | 3.5 | 3.50 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 4.0 | 2.0 | 3.5 | 2.0 | 3.5 | 3.0 | 3.40 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 3.0 | 2.0 | 1.5 | 2.5 | 3.0 | 2.5 | 3.10 |
| C++         | 2   | 3   | 2   | 4   | 2   | 2.5 | 3.0 | 1.0 | 2.0 | 3.0 | 2.0 | 2.46 |

Three clusters emerge. **Top tier (>=3.85).** TypeScript, Go, .NET, Kotlin. **Middle tier (3.40–3.84).** Python and Rust tied at 3.71, Java 3.50, Swift 3.40. **Lower tier (<3.40).** Elixir, C++. The script `scripts/score_summary.py` regenerates this table from the per-language evaluations.

## Six Findings

### 1. TypeScript and Go tie at the top.

Both score 4.01. Go's HC=5 / AO=5 lead carries at full weight (35% combined). TypeScript's AIE=5 / SOE=5 ecosystem strength combined with Reach=4.0 (Microsoft stewardship + commercial-vendor velocity from Vercel and others) lifts it level despite AIN=1.5 / SON=2.5 on the native halves. TypeScript and Go sit 0.30 above Python (3.71).

### 2. Python's structural exposure is visible in the matrix.

Python's AI-systems profile is bimodal — strong on the ecosystem half, weak on the native half — which holds the weighted total below TypeScript and Go. Python earns AIE=5.0 [python-021, python-022, python-023, python-024, python-025] and SOE=5.0 [python-026, python-027, python-028, python-029] — tier-leading on the ecosystem halves. AIN=1.5 (PSF ships no AI packages [python-036]), SON=2.5 (PEP 484 hints are advisory at runtime [python-030]), and EDR=2.5 (Pydantic community-multi-maintainer [python-031], Instructor single-maintainer [python-032], Outlines small-commercial [python-033]) hold the weighted total at 3.71, ranking #5. Reach=3.5 [python-037, python-038, python-039, python-040, python-041] reflects sustained typing-PEP cadence offset by structural AIN absence.

### 3. The dependency-risk axis rewards Microsoft, JetBrains, and OpenJDK stewardship.

EDR=4.5 (.NET) [dotnet-029, dotnet-030, dotnet-031, dotnet-032, dotnet-033], EDR=4.0 (Java) [java-029, java-030, java-031, java-032, java-033], EDR=4.0 (Kotlin) [kotlin-030, kotlin-031, kotlin-032, kotlin-033, kotlin-034] anchor the middle of the table. Microsoft funds the .NET runtime and the in-box AI surface as a single commercial-vendor strategy. OpenJDK's multi-vendor stewardship (Oracle, IBM, Red Hat) anchors the JVM. JetBrains stewardship anchors Kotlin at both the language and serialization layers. Languages with single-maintainer load-bearing dependencies (Python's Instructor [python-032], TypeScript's Zod [typescript-029], C++'s llama.cpp [cpp-027] + nlohmann/json [cpp-028]) score lower — Python 2.5, TypeScript 3.0, C++ 3.0.

### 4. Reachability separates the trajectory bets.

Reach=4.5 (.NET) [dotnet-034, dotnet-035, dotnet-036, dotnet-037, dotnet-038], Reach=4.0 (TypeScript [typescript-035, typescript-036, typescript-037, typescript-038, typescript-039], Kotlin [kotlin-035, kotlin-036, kotlin-037, kotlin-038, kotlin-039]) lift the trajectory bet for vendor-stewarded languages. Reach=2.0–2.5 (C++ [cpp-033, cpp-034, cpp-035, cpp-036, cpp-037], Elixir [elixir-034, elixir-035, elixir-036, elixir-037, elixir-038]) compound their current-state gaps with low closing-path plausibility. The dimension separates "where each language is now" from "where each language is plausibly going" — and shows that .NET, despite trailing the leaders on present-state weighted total, has the strongest forward bet of the cohort.

### 5. AI-agent operability is the most discriminating dimension.

Operability separates Go and TypeScript (AO=5) [go-003, go-015, typescript-006, typescript-007] from C++ (AO=2) [cpp-012, cpp-015] more sharply than any other dimension. With AO at 20% weight, this axis alone contributes ±0.6 points to the ranking — larger than any AI-era dimension's individual contribution. The pattern tracks toolchain unification and LSP-exposed semantic models, not type-system depth. Go has a single canonical command [go-003], single canonical formatter [go-002], and gopls as the official LSP server [go-015]. TypeScript reaches the same surface from a dynamic substrate via strict-mode [typescript-004], discriminated unions [typescript-002], and the language service Microsoft itself originated [typescript-006, typescript-007].

### 6. Apple's first-party Swift AI surface is correctly credited on the native half.

Swift's AIN=4.0 reflects Core ML + MLX + Foundation Models as language-steward-shipped [swift-019, swift-023], while AIE=2.0 reflects the thin cross-platform ecosystem [swift-020, swift-021, swift-022]. Apple's AI-platform investment is durable but Apple-platform-bound; Linux/server-side Swift AI dependencies remain community-multi-maintainer. Reach=3.0 [swift-034, swift-035, swift-036, swift-037, swift-038] records the Apple-locked trajectory.

## Per-Language Verdicts

### TypeScript — 4.01 — *Default for application work in the JavaScript-shaped world; tied at the top.*

Strongest forward case: an optional static type layer over JavaScript [typescript-001] with discriminated unions for exhaustive narrowing [typescript-002] and a strict-mode bundle [typescript-004], all served through a Microsoft-maintained Language Service [typescript-006] over the Language Server Protocol Microsoft originated [typescript-007]. AI-systems ecosystem is tier-leading at AIE=5.0: Anthropic SDK [typescript-019], OpenAI SDK [typescript-020], LangChain.js [typescript-021], official MCP TypeScript SDK [typescript-022], TypeScript LlamaIndex [typescript-023]. Structured-output ecosystem also tier-leading at SOE=5.0: Zod [typescript-024], Zod-typed tool calls [typescript-025], Vercel AI SDK [typescript-026], zod-to-json-schema [typescript-027]. **Reach=4.0** [typescript-035, typescript-036, typescript-037, typescript-038, typescript-039] — Microsoft stewardship anchors trajectory; commercial-vendor velocity (Vercel) closes ecosystem-half gaps. **Load-bearing risk:** no language-steward-shipped AI surface (AIN=1.5) [typescript-034], type system is intentionally not sound [typescript-005, typescript-017], EDR=3.0 reflects Zod's single-maintainer concentration [typescript-029] offset by Microsoft language-layer backing [typescript-031].

### Go — 4.01 — *Default for backend services where deliberate minimalism is acceptable; tied at the top.*

Strongest forward case: a uniquely low-friction agent profile built from a single canonical command covering the full development loop [go-003], gofmt as a single canonical formatter [go-002], and gopls as the official LSP server [go-015]. AI-systems integration: Anthropic Go SDK [go-020], OpenAI Go SDK [go-021], official MCP Go SDK [go-022], production Kafka and Postgres clients [go-023]. Structured-output: encoding/json + struct tags [go-025] is steward-shipped, openai-go schema generation [go-026], invopop/jsonschema for native types-to-JSON-Schema [go-028]. EDR=3.5 reflects Google language stewardship plus commercial-first-party SDKs from Anthropic and OpenAI; the validation library landscape is fragmented and LangChainGo is community-only [go-033]. **Reach=3.5** [go-036, go-037, go-038, go-039, go-040] — type-system minimalism is structural and won't move; AIE closing path is in motion via commercial vendors. **Load-bearing risk:** the deliberate type-system minimalism — no sum types, late generics, no exhaustive enums [go-017] — and the agent-framework ecosystem lag [go-024] remain real.

### .NET (C#) — 3.99 — *Ranks third on the strength of the Microsoft-first-party AI surface, dependency-risk, and reachability anchors.*

Strongest forward case: nullable reference types with static null-state flow analysis [dotnet-003], pattern-matching family across switch expressions [dotnet-004], Roslyn as a public compiler-platform API exposing the live SemanticModel [dotnet-006, dotnet-014]. **AIN=4.0 anchors the climb:** Microsoft Semantic Kernel [dotnet-020], MCP C# SDK with Microsoft co-maintenance [dotnet-021], ONNX Runtime .NET [dotnet-022], OpenAI .NET via Microsoft [dotnet-023]. Structured-output native is tier-leading at SON=4.0: System.Text.Json + source generation [dotnet-024], JsonSchemaExporter [dotnet-027], Semantic Kernel function calling [dotnet-025]. **EDR=4.5 is the highest in the cohort** [dotnet-029, dotnet-030, dotnet-031, dotnet-032, dotnet-033] — nearly the entire load-bearing AI/SO surface is Microsoft-first-party. **Reach=4.5 is also the highest in the cohort** [dotnet-034, dotnet-035, dotnet-036, dotnet-037, dotnet-038] — Microsoft is investing across nearly every below-5 cell, with annual major release cadence supporting forward-trajectory bets. **Load-bearing risk:** nullable reference types are opt-in [dotnet-012], MSBuild surface [dotnet-011], smaller AIE than Python or TypeScript [dotnet-019].

### Kotlin — 3.85 — *Default for JVM application work; ranks fourth on EDR and Reach credit.*

Strongest forward case: nullable types as a type-system distinction [kotlin-001], sealed hierarchies with exhaustive `when` [kotlin-002, kotlin-003] (MC=4.5), coroutines for structured concurrency [kotlin-006], Kotlin Multiplatform stable across JVM/Android/iOS/JS/Native [kotlin-015]. AIN=3.0 reflects JetBrains-shipped MCP Kotlin SDK [kotlin-021] and Kotlin Multiplatform [kotlin-023]. SON=3.5 with kotlinx-serialization (JetBrains-stewarded) [kotlin-025] and sealed classes + exhaustive when [kotlin-026]. **EDR=4.0** [kotlin-030, kotlin-031, kotlin-032, kotlin-033, kotlin-034] — JetBrains commercial-vendor backing at the language layer plus JVM-interop access to LangChain4j and OpenJDK. **Reach=4.0** [kotlin-035, kotlin-036, kotlin-037, kotlin-038, kotlin-039] — JetBrains stewardship plus stable Kotlin Multiplatform; remaining gaps concentrate in ecosystem halves. **Load-bearing risk:** governance dependence on JetBrains [kotlin-009], thin Kotlin-native AI tooling [kotlin-024], Kotlin-only structured-output ecosystem trails Java's [kotlin-029].

### Python — 3.71 — *Ranks #5 on a bimodal AI-systems profile: tier-leading ecosystem, weak native, dependency-risk-exposed.*

Strongest forward case: top GitHub language by activity [python-012], sustained typing PEP cadence [python-016], pyright/Pylance + bundled typeshed stubs [python-018], uv as a Rust-based fast package manager [python-011]. AIE=5.0 (best in cohort) with Anthropic SDK [python-021], OpenAI SDK [python-022], LangChain Python [python-023], MCP Python SDK [python-024], universal vector-store coverage [python-025]. SOE=5.0 with Pydantic [python-026], OpenAI Pydantic response_format [python-027], Instructor [python-028], Outlines [python-029]. **AIN=1.5** because PSF ships no AI-specific package [python-036]. **SON=2.5** because PEP 484 hints are advisory at runtime [python-030]. **EDR=2.5** [python-031, python-032, python-033, python-034, python-035] — Pydantic community-multi-maintainer, Instructor single-maintainer (Jason Liu), Outlines small-commercial. **Reach=3.5** [python-037, python-038, python-039, python-040, python-041] — typing-PEP cadence and Astral velocity offset by structural AIN absence at the steward.

### Rust — 3.71 — *Default for systems, infrastructure, and security-sensitive work; tied with Python at #5/6.*

Strongest forward case: ownership-checked memory rules without garbage collection [rust-001, rust-002, rust-003], exhaustive `match` over enums [rust-006, rust-007], external regulatory alignment via NSA recommendations and Android telemetry [rust-015, rust-016, rust-017]. AIE=4.0: production Postgres clients sqlx and tokio-postgres plus Kafka via rdkafka [rust-031], HuggingFace's candle inference runtime [rust-029], async-openai as the de-facto OpenAI client [rust-028], official MCP Rust SDK [rust-027], and the maturing Rig / swiftide / langchain-rust agent-framework cohort [rust-030]. SON=2.0 reflects no first-party Rust schema-validation library; SOE=4.0 with Serde [rust-032] + schemars [rust-033] + Rust-enum tagged unions [rust-035]. **EDR=3.5** [rust-037, rust-038, rust-039, rust-040, rust-041] balances the Rust Foundation's multi-vendor backing against Serde and schemars community-multi-maintainer profiles. **Reach=3.5** [rust-043, rust-044, rust-045, rust-046, rust-047] — verification ceiling already at top; AIN closing path is steward-absent. **Load-bearing risk:** AIN=1.5 (no first-party Rust AI runtime [rust-042]); agent-framework breadth still trails Python and TypeScript even after the recent maturation [rust-030].

### Swift — 3.40 — *Default for Apple-platform application work; native-AI credit reflects Apple's first-party stack.*

Strongest forward case: optionals as a type-system distinction [swift-001], memory-safety rules with conflicting-access detection [swift-004], language-level async/await and actors [swift-003], an open Swift Evolution process [swift-006]. **AIN=4.0** for Apple's first-party ML stack via Core ML / Create ML [swift-019] and MLX [swift-023]. SON=3.5 with Codable [swift-024] and enum + exhaustive switch [swift-025]. **Reach=3.0** [swift-034, swift-035, swift-036, swift-037, swift-038] — Apple-locked trajectory caps cross-platform reachability. **Load-bearing risk:** AIE=2.0 (no first-party Anthropic or OpenAI Swift SDKs [swift-021], cross-platform agent-framework support essentially absent [swift-022]). EDR=3.5 strong on Apple-platform AI; weaker on cross-platform Swift surface [swift-031, swift-032].

### Java — 3.50 — *Solo #7; AO lift on Eclipse JDT.LS maturity and AI-training-corpus density.*

Strongest forward case: virtual threads as a JVM-level concurrency primitive [java-006], structured concurrency in JEP 453 [java-015], records and sealed classes for closed-hierarchy pattern matching [java-002, java-003, java-004]. AO=3.5 reflects Eclipse JDT Language Server maturity [java-014] and Java's AI-training-corpus density [java-011] arguing past the 3.0 anchor; build-tool fragmentation between Maven and Gradle and heavier project structure remain real friction. AIE=4.0 with Anthropic Java SDK [java-019], LangChain4j [java-020], official MCP Java SDK [java-021], Apache Kafka client [java-022], ONNX Runtime Java [java-023]. SOE=3.5 with Jackson + Bean Validation [java-024], LangChain4j AI Services [java-025]. **EDR=4.0** [java-029, java-030, java-031, java-032, java-033] — OpenJDK multi-vendor stewardship, Hibernate Validator (Red Hat), Anthropic first-party Java SDK. **Reach=3.5** [java-035, java-036, java-037, java-038, java-039] — sustained JEP cadence offset by AIN steward-absence and preview-cycle delays. **Load-bearing risk:** AIN=2.0 (OpenJDK ships no AI module first-party [java-034]), pre-records boilerplate [java-013], preview-feature delays [java-016].

### Elixir — 3.10 — *Default for fault-tolerant distributed systems and real-time AI-augmented UIs.*

Strongest forward case: BEAM process and concurrency model [elixir-001, elixir-004], OTP supervision trees [elixir-002], Phoenix LiveView [elixir-009, elixir-014]. AIN=3.0 with Bumblebee on Nx (Dashbit-stewarded) [elixir-019, elixir-020] and Phoenix.PubSub for BEAM-native streaming [elixir-021]. SOE=2.5 with Ecto changesets [elixir-024] + instructor_ex [elixir-025]. **Reach=2.5** [elixir-034, elixir-035, elixir-036, elixir-037, elixir-038] — set-theoretic types in research, small ecosystem footprint, wide gap-size. **Load-bearing risk:** dynamically typed [elixir-005] with set-theoretic types still in research [elixir-016, elixir-027]; LLM-provider SDKs mostly community-maintained [elixir-022]; agent-framework ecosystem small [elixir-023]; SON=1.5 reflects no native compile-time contract safety; EDR=3.0 mixes Dashbit anchoring with single-maintainer instructor_ex [elixir-030].

### C++ — 2.46 — *Default only for accelerator host code where the safety penalty is knowingly accepted.*

Strongest forward case: ISO standardization with three-yearly revisions [cpp-001], C++20 modules and ranges [cpp-002], the dominant accelerator and inference toolchains — llama.cpp implemented in C++ [cpp-017], ONNX Runtime C++ API [cpp-018], CUDA/ROCm/HIP/SYCL/oneAPI all primarily targeting C++ [cpp-013, cpp-019], librdkafka for streaming [cpp-021], and llama.cpp's native GBNF JSON-schema-constrained decoding [cpp-024]. **Reach=2.0 is the lowest in the cohort** [cpp-033, cpp-034, cpp-035, cpp-036, cpp-037] — memory-safety pressure compounds against C++; most below-5 cells are structural to the language design and will not close inside the planning horizon. **Load-bearing risk:** memory-safety pressure [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008]; AIN=2.5 with no ISO-shipped AI facilities [cpp-032]; SON=1.0 (no native reflection, no in-box validation [cpp-026]); EDR=3.0 mixes commercial-first-party CUDA/ONNX backing with single-maintainer concentration on llama.cpp and nlohmann/json [cpp-027, cpp-028].

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

The framework weights (HC 15%, MC 15%, AO 20%, RE 10%, SV 5%, AIN 7.5%, AIE 7.5%, SON 5%, SOE 5%, EDR 5%, Reach 5%) are working assumptions. A reasonable reader could weight runtime/ecosystem higher (favouring Python and the JVM languages), AI-agent operability higher (favouring Go and TypeScript), dependency-risk higher (favouring .NET and Java), or reachability higher (favouring .NET and the vendor-stewarded languages). The matrix is robust to small weight perturbations but not to large ones.

The snapshot date is **2026-05-02**. The AI-systems and structured-output ecosystems and the dependency-risk profile are the most volatile axes: MCP adoption is broadening, first-party SDKs are landing, structured-output libraries are converging on Pydantic/Zod-shaped patterns, and commercial vendors are increasingly publishing first-party SDKs that displace single-maintainer projects. Expect EDR scores to move first.

The greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question, and this matrix will under-credit Java, Python, and C++ for that purpose.

The native/ecosystem split is sensitive to how "language steward" is defined. The framework draws the line at the entity that ships the canonical language toolchain. Edge cases (CUDA as the language-of-the-stack for accelerators; Dashbit's relationship to Elixir governance) are documented in `framework/dimensions.md`.

Finally, the scores are single-rater author judgments grounded in atomic claims with primary-source citations, not the average of an independent expert panel. Each cell traces through Insight → Evaluation → Claim → Source.

## Reading and Reproducibility

The corpus is structured for traceability:

- **Framework** — `framework/dimensions.md` (criteria), `framework/evaluation-framework.md` (weights and lenses), `framework/scoring-rubric.md` (1.0–5.0 rubric in 0.5-point increments).
- **Claims** — `claims/<language>.yaml`, ~390 atomic claims across 10 languages, each with a primary-source citation, explicit polarity, and (since v0.4) `backer:` tag.
- **Sources** — `sources/<language>-sources.yaml`, ~280 source entries with publication metadata.
- **Evaluations** — `evaluations/<language>.yaml`, per-language eleven-dimension scores with `supporting_claims:` traceability into the claim corpus.
- **Comparisons** —
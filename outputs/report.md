# Programming Languages in the AI Era

*A greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development.*

## TL;DR

Across 10 languages, scored on six weighted dimensions and read through four cross-cutting lenses, **TypeScript (4.30)**, **Go (4.25)**, **Python (4.15)** and **.NET / C# (4.00)** form the top tier for greenfield AI-era projects. **Rust (3.95)** and **Kotlin (3.90)** sit just below, separated only by their AI-systems integration depth. Java, Swift, and Elixir occupy a middle tier where each has a real structural strength offset by a load-bearing AI-integration or operability gap. C++ trails at the bottom for memory-safety pressure that has crossed from technical preference into regulatory selection criterion.

The headline is that the framework's 6th dimension — **AI-systems interoperability** — reshuffles the top. Python returns to the top tier on the strength of the dominant LLM SDK and agent-framework story; TypeScript takes the lead by combining strong agent operability with first-party MCP and LangChain.js coverage. Go remains close behind on operability breadth despite a thinner agent-framework ecosystem. Every top-tier language carries a documented weakness: Rust's young agent-framework ecosystem, TypeScript's unsound runtime semantics, Kotlin's single-vendor governance exposure, Go's deliberate abstraction limits, .NET's MSBuild ceremony.

The full matrix sits in `comparisons/overview.md` and is reproduced in *The Matrix* below. Recommendations by domain follow in *Recommendations by Use Case*.

## Framing

This report evaluates languages from a **greenfield** position: a new AI-era project starting today, not a maintenance estate. Installed base, code volume, and incumbent gravity are not credited. The framework instead credits forward-looking properties: governance quality, future fit, AI-training representation, ecosystem velocity, and ecosystem viability (the production-readiness a new project inherits today — compiler toolchains, ABI, deployment, observability, accelerator integration). The framework specification lives in `framework/evaluation-framework.md`.

Each language is scored 1.0–5.0 in 0.5-point increments on six dimensions:

- **Human cognition (15%)** — can humans understand and govern the code?
- **Machine cognition (20%)** — can compilers, analyzers, and AI systems reason about it?
- **AI-agent operability (20%)** — can agents safely modify and verify it?
- **Runtime and ecosystem (15%)** — can it run production systems?
- **Strategic viability (10%)** — will it remain relevant?
- **AI-systems interoperability (20%)** — does it plug into the data layer, LLM providers, agent frameworks, MCP, inference runtimes, streaming, and observability that an AI-era system depends on?

Four cross-cutting lenses read across the dimensions:

1. **Verification advantage** — what the compiler can falsify before code runs.
2. **Agentic development advantage** — fast feedback, deterministic tooling, clear diagnostics.
3. **Safety pressure** — alignment with regulatory and platform-vendor selection criteria.
4. **Abstraction compression** — how much behaviour is expressed per line, with what cost in implicit context.

What this report does credit: forward governance, future fit under AI-era pressure, training-corpus representation, library availability for new projects, ecosystem viability as a property a greenfield project can lean on today, and AI-systems integration depth. What it does not credit: legacy installed base, the volume of code already written, or the inertia of any incumbent.

## The Matrix

| Language    | HC  | MC  | AO  | RE  | SV  | AI  | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---:|
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 4.5 | 4.30 |
| Go          | 5   | 4   | 5   | 4   | 4   | 3.5 | 4.25 |
| Python      | 4   | 3   | 4   | 5   | 4   | 5   | 4.15 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4   | 4.00 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 3   | 3.95 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3   | 3.90 |
| Java        | 3   | 4   | 3   | 4.5 | 3   | 3.5 | 3.53 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 2   | 3.30 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 2.5 | 3.28 |
| C++         | 2   | 3   | 2   | 4   | 2   | 3   | 2.70 |

HC = Human cognition (15%), MC = Machine cognition (20%), AO = AI-agent operability (20%), RE = Runtime/ecosystem (15%), SV = Strategic viability (10%), AI = AI-systems interoperability (20%).

Three clusters emerge. **Top tier (≥4.0).** TypeScript, Go, Python, .NET. **Middle tier (3.0–3.99).** Rust, Kotlin, Java, Swift, Elixir. **Lower tier (<3.0).** C++. The script `scripts/score_summary.py` regenerates this table from the per-language evaluations.

## Five Findings

### 1. AI-systems interoperability reshuffles the top.

Adding a 6th dimension that scores how cleanly a language plugs into the data layer, LLM providers (Anthropic, OpenAI), agent frameworks (LangChain, Semantic Kernel, LlamaIndex), protocols (MCP, function-calling), inference runtimes (ONNX, llama.cpp, candle), streaming, and observability changes the ranking. Python returns to top tier (AI=5) on the strength of its first-party Anthropic [python-021], OpenAI [python-022], LangChain [python-023], and MCP [python-024] coverage plus universal vector-store clients [python-025]. TypeScript takes the lead with AI=4.5 on parallel Anthropic [typescript-019] and OpenAI [typescript-020] SDKs, LangChain.js [typescript-021], the official MCP TypeScript SDK [typescript-022], and a TypeScript LlamaIndex distribution [typescript-023]. .NET earns AI=4 with Anthropic [dotnet-019] and OpenAI [dotnet-023] SDKs, Microsoft Semantic Kernel [dotnet-020], the official MCP C# SDK [dotnet-021], and ONNX Runtime .NET [dotnet-022]. Go (AI=3.5) [go-020, go-021, go-022, go-023, go-024] and Java (AI=3.5) [java-019, java-020, java-021, java-022, java-023] follow with strong infrastructure-side integration but thinner agent-framework depth. C++ (AI=3) is the host for llama.cpp [cpp-017], ONNX Runtime [cpp-018], and CUDA/ROCm/SYCL [cpp-019] but has no first-party LLM SDK or agent-framework story [cpp-020].

### 2. AI-agent operability is the most discriminating dimension among the structural axes.

Operability separates the matrix more sharply than any other axis. Go and TypeScript score 5 on AI-agent operability while C++ scores 2 — and the gap holds even where the underlying language quality is comparable on other dimensions. The pattern is that operability tracks **toolchain unification and LSP-exposed semantic models**, not type-system depth. Go has a single canonical command covering build, test, format, vet, dependency management and documentation [go-003], a single canonical formatter [go-002], minimum-version-selection dependency resolution [go-004], and gopls as the official LSP server [go-015]. TypeScript reaches the same surface from a dynamic substrate: an opt-in strict-mode bundle [typescript-004], discriminated unions for exhaustive narrowing [typescript-002], a Microsoft-maintained language service [typescript-006] and the Language Server Protocol Microsoft itself originated [typescript-007]. .NET ships Roslyn as a public compiler-platform API [dotnet-006, dotnet-014] and a unified `dotnet` CLI [dotnet-010]. C++ has cppreference [cpp-012] but no canonical build system and uneven C++20 module adoption [cpp-015].

### 3. AI raises the value of cheap verification.

Agents write more code than humans can read; the bottleneck shifts from generation to validation. Languages whose compilers can falsify a candidate change without execution gain proportional value. The strongest verification structures cluster in four languages — Rust's ownership-checked memory rules [rust-001, rust-002, rust-003] with exhaustive `match` [rust-006], Kotlin's nullable-type distinction [kotlin-001] and exhaustive `when` over sealed hierarchies [kotlin-002, kotlin-003] (now MC=4.5 with v0.2 half-point rescoring), .NET's nullable-reference-type flow analysis [dotnet-003] and pattern-matching family [dotnet-004], Swift's optionals [swift-001] and memory-safety access rules [swift-004]. A second pattern is **verification velocity**: TypeScript's `satisfies` operator [typescript-016], Python's sustained typing-PEP cadence [python-016] and PEP 695 generics [python-004], Elixir's set-theoretic type research [elixir-007]. The trajectory is toward verification, not away from it.

### 4. Safety pressure has crossed from technical preference to regulatory criterion.

Four independent institutional vantage points have aligned on memory safety as a structural language property they actively select for: Microsoft Security Response Center reports approximately 70% of CVEs Microsoft assigns are memory-safety issues [cpp-004]; the Chromium project independently reports approximately 70% of high-severity bugs are memory-safety bugs [cpp-005]; the U.S. National Security Agency's *Software Memory Safety* sheet recommends shifting from memory-unsafe languages and explicitly names C and C++ [cpp-006]; the Office of the National Cyber Director's 2024 *Back to the Building Blocks* report repeats the recommendation [cpp-007]. Google's Android telemetry shows memory-safety vulnerabilities declining as new native code shifted toward memory-safe languages including Rust [cpp-008, rust-016, rust-017]. Languages with structural memory safety (Rust [rust-001], JVM-verified Kotlin [kotlin-001], Swift [swift-004], BEAM-isolated Elixir [elixir-002, elixir-004], CLI-typed .NET [dotnet-002, dotnet-003]) align with this pressure; C++ alone is in the "exposed" tier in `comparisons/lens-analysis.md`. Python's exposure differs in kind — runtime-error rather than memory-unsafety [python-002, python-019] — and is not a regulatory focus.

### 5. Half-point scoring exposes genuine differentiation that integer-only rounding hides.

Three rescoring moves under v0.2 land where the supporting claims justify a step beyond "strong" without reaching "excellent": Kotlin machine_cognition 4 → 4.5 [kotlin-001, kotlin-002, kotlin-003], Java runtime_ecosystem 4 → 4.5 [java-006, java-009, java-010, java-015], Elixir runtime_ecosystem 4 → 4.5 [elixir-001, elixir-002, elixir-003, elixir-009]. AI-systems interoperability records additional half-step differentiation: TypeScript 4.5, Go 3.5, Java 3.5, Elixir 2.5. The integer-only matrix forced false equality between Kotlin and the integer-4 cluster on machine cognition and between Java and Elixir and the integer-4 cluster on runtime/ecosystem; the half-point pass fixes those without inflating the rubric.

## Per-Language Verdicts

### TypeScript — 4.30 — *Default for application work in the JavaScript-shaped world.*

Strongest forward case: an optional static type layer over JavaScript [typescript-001] with discriminated unions for exhaustive narrowing [typescript-002] and a strict-mode bundle [typescript-004], all served through a Microsoft-maintained Language Service [typescript-006] over the Language Server Protocol Microsoft originated [typescript-007]. AI-systems integration is the broadest in the cohort: Anthropic SDK [typescript-019], OpenAI SDK [typescript-020], LangChain.js [typescript-021], official MCP TypeScript SDK [typescript-022], and TypeScript LlamaIndex [typescript-023]. **Load-bearing risk:** the type system is intentionally not sound — `any` opts a value out of checking [typescript-005], assertions and function-bivariance produce holes [typescript-017], and types are erased at compile time with no runtime representation [typescript-018]. Strict-mode discipline is what makes TypeScript an AI-era asset rather than a liability.

### Go — 4.25 — *Default for backend services where deliberate minimalism is acceptable.*

Strongest forward case: a uniquely low-friction agent profile built from a single canonical command covering the full development loop [go-003], gofmt as a single canonical formatter [go-002], and gopls as the official LSP server [go-015]. AI-systems integration: Anthropic Go SDK [go-020], OpenAI Go SDK [go-021], official MCP Go SDK [go-022], production Kafka and Postgres clients [go-023]. **Load-bearing risk:** the deliberate type-system minimalism — no sum types, late generics, no exhaustive enums [go-017] — is real; the agent-framework ecosystem (LangChainGo) lags Python and TypeScript [go-024]. Go wins on operability breadth, not on agent-framework depth.

### Python — 4.15 — *Default for data, AI/ML, and AI systems integration; second-best for general application work.*

Strongest forward case: top GitHub language by activity [python-012], sustained typing PEP cadence [python-016] with PEP 484 hints [python-003] and PEP 695 generics [python-004], pyright/Pylance and bundled typeshed stubs [python-018], uv as a Rust-based fast package manager [python-011], and the most complete AI-systems integration story in the cohort: Anthropic Python SDK [python-021], OpenAI Python SDK [python-022], canonical LangChain Python implementation [python-023], official MCP Python SDK [python-024], universal vector-store coverage [python-025]. **Load-bearing risk:** type hints are not enforced at runtime [python-002], the dynamic runtime surfaces type errors only at execution time [python-015], and stub coverage fragments across the dependency graph [python-020]. Typed Python in CI from day one is the only sustainable AI-era posture.

### .NET (C#) — 4.00 — *Default for Microsoft-shop application and service work, broadly capable beyond.*

Strongest forward case: nullable reference types with static null-state flow analysis [dotnet-003], pattern-matching family across switch expressions [dotnet-004], Roslyn as a public compiler-platform API exposing the live SemanticModel to analyzers, code fixes, and source generators [dotnet-006, dotnet-014], and a Microsoft-backed AI stack (Anthropic .NET SDK [dotnet-019], Semantic Kernel [dotnet-020], MCP C# SDK [dotnet-021], ONNX Runtime .NET [dotnet-022], OpenAI .NET [dotnet-023]). **Load-bearing risk:** nullable reference types are opt-in and configured per project [dotnet-012]; MSBuild remains a configuration-language attack surface [dotnet-011]; ECMA-334/335 standardization in practice tracks Microsoft's reference implementation [dotnet-018].

### Rust — 3.95 — *Default for systems, infrastructure, and security-sensitive work.*

Strongest forward case: ownership-checked memory rules without garbage collection [rust-001, rust-002, rust-003], exhaustive `match` over enums [rust-006, rust-007], external regulatory alignment via NSA recommendations and Android telemetry [rust-015, rust-016, rust-017], and a credible AI-systems story (official MCP Rust SDK [rust-027], async-openai [rust-028], HuggingFace candle [rust-029], production Postgres/Kafka [rust-031]). **Load-bearing risk:** the ownership model carries a real learning curve [rust-020], compile times remain a friction point on large workspaces [rust-025], the async ecosystem splits across runtimes [rust-026], and the agent-framework ecosystem (Rig, swiftide, langchain-rust) is younger than Python or TypeScript [rust-030].

### Kotlin — 3.90 — *Default for JVM application work and increasingly for cross-platform.*

Strongest forward case: nullable types as a type-system distinction [kotlin-001], sealed hierarchies with exhaustive `when` [kotlin-002, kotlin-003] (now MC=4.5 in v0.2), coroutines for structured concurrency [kotlin-006], Kotlin Multiplatform stable across JVM/Android/iOS/JS/Native [kotlin-015], and an official MCP Kotlin SDK [kotlin-021] with full Java-interop access to the JVM AI stack [kotlin-022, kotlin-023]. **Load-bearing risk:** governance dependence on JetBrains [kotlin-009], strategic positioning tied to Google's continued Android prioritization [kotlin-020], null safety bypassable through Java-interop platform types [kotlin-017], and a thin Kotlin-native AI tooling ecosystem [kotlin-024].

### Java — 3.53 — *Forward case is narrower than its historic position suggested but stronger than v0.1 indicated.*

Strongest forward case: virtual threads as a JVM-level concurrency primitive [java-006], structured concurrency in JEP 453 [java-015], records and sealed classes for closed-hierarchy pattern matching [java-002, java-003, java-004], and a credible JVM AI stack: Anthropic Java SDK [java-019], LangChain4j [java-020], official MCP Java SDK [java-021], canonical Kafka client [java-022], ONNX Runtime Java [java-023]. The runtime/ecosystem rescore to 4.5 reflects the JVM's uniquely production-grade depth. **Load-bearing risk:** the build-tool ecosystem is split between Maven and Gradle [java-011], pre-records boilerplate is recognized verbosity [java-013], preview features stabilize across multiple releases delaying LTS availability [java-016].

### Swift — 3.30 — *Default for Apple-platform application work.*

Strongest forward case: optionals as a type-system distinction [swift-001], memory-safety rules with conflicting-access detection [swift-004], language-level async/await and actors [swift-003], an open Swift Evolution process [swift-006], and Apple's first-party ML stack via Core ML [swift-019] and MLX [swift-023]. **Load-bearing risk:** Apple's primary positioning around its own platforms creates platform-aligned governance [swift-011, swift-016], server-side Swift on Linux lags Apple-platform feature availability [swift-018, swift-020], no first-party Anthropic or OpenAI Swift SDKs [swift-021], and cross-platform agent-framework support is essentially absent [swift-022].

### Elixir — 3.28 — *Default for fault-tolerant distributed systems and real-time AI-augmented UIs.*

Strongest forward case: BEAM process and concurrency model [elixir-001, elixir-004], OTP supervision trees as structured fault-tolerance [elixir-002], Phoenix LiveView as a credible substrate for server-driven real-time interfaces [elixir-009, elixir-014] (RE rescored to 4.5 in v0.2), Bumblebee on Nx for native inference [elixir-019, elixir-020], and BEAM-native streaming via Phoenix.PubSub and GenStage [elixir-021]. **Load-bearing risk:** Elixir is dynamically typed [elixir-005] with set-theoretic types still in research [elixir-016]; LiveView's server-driven rendering ties front-end lifecycle to a stateful socket [elixir-017]; LLM-provider SDKs are mostly community-maintained [elixir-022]; the agent-framework ecosystem is small [elixir-023].

### C++ — 2.70 — *Default only for accelerator host code where the safety penalty is knowingly accepted.*

Strongest forward case: ISO standardization with three-yearly revisions [cpp-001], C++20 modules and ranges [cpp-002], and the dominant accelerator and inference toolchains — llama.cpp implemented in C++ [cpp-017], ONNX Runtime C++ API [cpp-018], CUDA/ROCm/HIP/SYCL/oneAPI all primarily targeting C++ [cpp-013, cpp-019], and librdkafka for streaming [cpp-021]. **Load-bearing risk:** memory-safety pressure (MSRC, Chromium, NSA, ONCD, Android) [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008] and undefined-behaviour exposure [cpp-011]; first-party LLM SDKs and agent frameworks are essentially absent in C++ [cpp-020]. Strategic viability scores 2 for memory-safety reasons.

## Recommendations by Use Case

| Domain | Primary | Alternatives | Trade-off |
|---|---|---|---|
| Greenfield application work | TypeScript | Kotlin, .NET (C#) | Operability and AI-systems integration breadth, accepting unsoundness in TypeScript [typescript-005, typescript-017]. |
| Systems / infrastructure / security-sensitive | Rust | Go | Verification and safety [rust-001, rust-015], accepting compile-time and learning-curve cost [rust-020, rust-025]. |
| Data / AI/ML / scripting / AI-systems integration | Python | TypeScript (for data products) | Most complete AI-systems story [python-021, python-022, python-023, python-024, python-025] over verification gap [python-002, python-019]. Treat type discipline as day-one investment. |
| Fault-tolerant distributed systems | Elixir | Go, Rust | BEAM runtime properties [elixir-001, elixir-002] over verification ceiling [elixir-005, elixir-016]. |
| AI-native compute kernels | Rust | C++ (only where unavoidable) | Rust's accelerator/ML ecosystem (wgpu, candle, burn) [rust-022, rust-029] over C++ memory-safety exposure [cpp-004, cpp-006]. |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] | Native platform integration [swift-003, swift-014, swift-019], accepting Apple-aligned governance [swift-011] and cross-platform AI integration thinness [swift-021]. |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) | Toolchain access [cpp-013, cpp-019], explicitly accepting safety penalty [cpp-004, cpp-006]. |
| JVM application work needing AI integration | Java | Kotlin | LangChain4j [java-020] and Anthropic Java SDK [java-019] for direct JVM use; Kotlin for null-safety and abstraction. |

For **greenfield application work** TypeScript wins on the broadest joint operability-and-AI-integration profile; Kotlin and .NET are credible where the JVM or .NET runtimes are already operationally preferred. For **systems and infrastructure**, Rust pays operability cost for verification and safety gains. For **data, ML, and AI-systems integration**, Python's ecosystem is the deepest and the AI-systems integration story is unmatched. For **fault-tolerant distributed systems**, Elixir's BEAM properties are not matched by other languages. For **AI-native compute kernels**, Rust's accelerator stack is the lower-risk alternative to C++. For **Apple-platform application work**, Swift is the native default.

## Limitations

The framework weights (HC 15%, MC 20%, AO 20%, RE 15%, SV 10%, AI 20%) are working assumptions. A reasonable reader could weight runtime/ecosystem higher (favouring Python and the JVM languages) or AI-agent operability higher (favouring Go and TypeScript). The matrix is robust to small weight perturbations but not to large ones.

The snapshot date is **2026-04-30**. The new AI-systems interoperability dimension is the most volatile: MCP adoption is broadening, first-party SDKs are landing, and agent-framework ecosystems in Rust, Kotlin, Java, and Elixir are evolving rapidly. Expect AI-axis scores to shift within twelve months.

The greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question, and this matrix will under-credit Java, Python, and C++ for that purpose.

Finally, the scores are single-rater author judgments grounded in atomic claims with primary-source citations, not the average of an independent expert panel. Each cell traces through Insight → Evaluation → Claim → Source.

## Reading and Reproducibility

The corpus is structured for traceability:

- **Framework** — `framework/dimensions.md` (criteria), `framework/evaluation-framework.md` (weights and lenses), `framework/scoring-rubric.md` (1.0–5.0 rubric in 0.5-point increments).
- **Claims** — `claims/<language>.yaml`, 241 atomic claims across 10 languages, each with a primary-source citation and explicit polarity.
- **Sources** — `sources/<language>-sources.yaml`, 186 source entries with publication metadata.
- **Evaluations** — `evaluations/<language>.yaml`, per-language six-dimension scores with `supporting_claims:` traceability into the claim corpus.
- **Comparisons** — `comparisons/overview.md`, `comparisons/lens-analysis.md`, `comparisons/agent-friendly-languages.md`, `comparisons/dynamic-vs-static.md`.
- **Insights** — `insights/agentic-feedback-loops.md`, `insights/ai-favors-verifiability.md`, `insights/safety-pressure.md`, `insights/incumbent-risk.md`.

The matrix is reproducible via `scripts/score_summary.py`, which reads `evaluations/*.yaml` and emits the table in `comparisons/overview.md`. The full methodology is documented in `outputs/evidence-backed-research-execution-plan.md`.

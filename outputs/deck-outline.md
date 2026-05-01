# Programming Languages in the AI Era — Deck Outline

*Source: outputs/report.md. Anchored in 241 atomic claims across 10 languages.*

## Slide 1 — Title

Programming Languages in the AI Era — a greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development. Framework v0.2, snapshot 2026-04-30. Author: Rutger Hemrika.

## Slide 2 — The question

If you were starting a new project today, which language would you pick — and how would you defend that choice when AI agents are doing more of the writing? Installed base and incumbent gravity stop being load-bearing once a team commits to a greenfield codebase. The question this deck answers: which languages are forward-fit for AI-era development, on the evidence available now, with every claim traceable to a primary source.

## Slide 3 — Framing

Greenfield framing: no credit for legacy installed base, code volume, or incumbent gravity. Six weighted dimensions — Human cognition (15%), Machine cognition (20%), AI-agent operability (20%), Runtime/ecosystem (15%), Strategic viability (10%), AI-systems interoperability (20%). Half-point scores 1.0–5.0 in 0.5 increments. Four cross-cutting lenses: verification, agentic operability, safety pressure, abstraction compression. Forward properties credited: governance, future fit, AI-training representation, ecosystem velocity, ecosystem viability, and AI-systems integration depth. Legacy code volume is not.

## Slide 4 — The matrix

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

AI = AI-systems interoperability (20%), the v0.2 sixth dimension capturing LLM-provider SDKs, agent frameworks, MCP, inference runtimes, and streaming/observability integration. Three tiers: top (>=4.0) TypeScript, Go, Python, .NET. Middle (3.0-3.99) Rust, Kotlin, Java, Swift, Elixir. Lower (<3.0) C++. The lead reflects joint operability + AI-systems integration breadth.

## Slide 5 — Finding 1: AI-agent operability is most discriminating

Among the structural axes, operability separates the matrix more sharply than any other. Go and TypeScript score 5; C++ scores 2. The pattern tracks **toolchain unification and LSP-exposed semantic models**, not type-system depth. Go ships a single canonical command for build/test/format/vet/deps/docs [go-003], a canonical formatter [go-002], MVS dependency resolution [go-004], and gopls as official LSP [go-015]. TypeScript reaches the same surface from a dynamic substrate via strict-mode [typescript-004], discriminated unions [typescript-002], and the language service Microsoft itself originated [typescript-006, typescript-007]. .NET ships Roslyn as a public compiler-platform API [dotnet-006, dotnet-014]. C++ lacks a single canonical build surface [cpp-015].

## Slide 6 — Finding 2: AI raises the value of cheap verification

Agents write more code than humans can read; the bottleneck shifts from generation to validation. Languages whose compilers can falsify a candidate change without execution gain proportional value. Strongest verification clusters: Rust ownership rules [rust-001, rust-002, rust-003] with exhaustive `match` [rust-006]; Kotlin nullables and sealed `when` [kotlin-001, kotlin-002, kotlin-003]; .NET nullable-reference-type flow analysis [dotnet-003, dotnet-004]; Swift optionals and access rules [swift-001, swift-004]. Verification velocity is also visible: TypeScript `satisfies` [typescript-016], Python typing-PEP cadence [python-016, python-004], Elixir set-theoretic types [elixir-007].

## Slide 7 — Finding 3: Safety pressure has crossed into regulatory territory

Four independent institutions now treat memory safety as a structural language property they actively select for. Microsoft Security Response Center: ~70% of Microsoft-assigned CVEs are memory-safety issues [cpp-004]. Chromium: ~70% of high-severity bugs are memory-safety bugs [cpp-005]. NSA *Software Memory Safety* names C and C++ [cpp-006]. ONCD's 2024 *Back to the Building Blocks* repeats the recommendation [cpp-007]. Android telemetry shows memory-safety vulnerabilities declining as new native code shifted to memory-safe languages including Rust [cpp-008, rust-016, rust-017]. Memory-safe languages (Rust [rust-001], Kotlin/JVM [kotlin-001], Swift [swift-004], Elixir/BEAM [elixir-002, elixir-004], .NET [dotnet-002, dotnet-003]) align with the pressure; C++ is alone in the exposed tier.

## Slide 8 — Finding 4: Incumbent gravity does not insulate

Greenfield framing is the lever that exposes this. C++ retains forward credit for accelerator host code [cpp-013] and ISO standardization [cpp-001] but loses 0.4 points because safety pressure dominates strategic viability. Java retains forward credit for virtual threads [java-006], structured concurrency JEP 453 [java-015], and Maven Central [java-010] — but the legacy adoption premium is gone, and Kotlin's null-safety [kotlin-001] and sealed types [kotlin-002] now sit inside Java's own ecosystem. Python keeps RE=5 because ML-domain library velocity is forward-relevant [python-012] and typing PEP cadence is a verification-velocity signal [python-016, python-018] — but unenforced hints [python-002] and fragmented stub coverage [python-020] keep the verification weakness load-bearing. None of these languages collapses; their forward case becomes domain-specific rather than default.

## Slide 9 — Finding 5: Gradual typing has narrowed the dynamic-vs-static gap

The original binary is becoming a spectrum. TypeScript's static layer over JavaScript [typescript-001] with discriminated unions [typescript-002] and structural typing [typescript-003] reaches an AI-era profile competitive with mature static languages — score 4.30, ahead of Kotlin and .NET. Python typing has advanced through PEPs 484, 526, 544, 612, 646, 692, 695 [python-016], with PEP 695 generic syntax [python-004] and pyright/Pylance-bundled stubs [python-018] giving agents enough signal to operate in well-typed Python. Elixir is researching set-theoretic types [elixir-007, elixir-013] and supports Dialyzer success-typing [elixir-006]. Per-class means under v0.2: static-mature 3.82, dynamic+gradual 3.91 — the dynamic-plus-gradual class actually edges ahead because the dominant LLM SDKs and agent frameworks ship Python and TypeScript first. The predictive feature is gradual typing, not original origin.

## Slide 10 — Top-tier verdicts

- **TypeScript (4.30)** — default for application work in the JavaScript-shaped world. Strict-mode discipline [typescript-004] plus AI-systems breadth: LangChain.js [typescript-021], official MCP TS SDK [typescript-022], Anthropic and OpenAI SDKs [typescript-019, typescript-020]. Risk: type system is intentionally not sound [typescript-005, typescript-017].
- **Go (4.25)** — default for backend services where deliberate minimalism is acceptable. Wins on operability breadth [go-003, go-015]; AI-systems coverage at 3.5 with Anthropic [go-020], OpenAI [go-021], MCP [go-022] SDKs but thinner agent-framework depth [go-024]. Risk: type-system minimalism is real [go-017, go-018].
- **Python (4.15)** — default for data, AI/ML, and AI-systems integration. AI-systems score 5 with Anthropic [python-021], OpenAI [python-022], LangChain [python-023], MCP [python-024], universal vector stores [python-025]. Risk: type hints not enforced at runtime [python-002].
- **.NET / C# (4.00)** — default for Microsoft-shop application and service work. Roslyn as public compiler-platform API [dotnet-006, dotnet-014]; AI-systems via Semantic Kernel [dotnet-020], MCP C# SDK [dotnet-021], ONNX Runtime .NET [dotnet-022]. Risk: NRT is opt-in [dotnet-012], MSBuild ceremony [dotnet-011].

## Slide 11 — Other notable verdicts

- **Rust (3.95)** — default for systems, infrastructure, security-sensitive work. Ownership rules [rust-001] plus regulatory alignment [rust-015, rust-016]; AI-systems at 3 (MCP Rust SDK [rust-027], async-openai [rust-028], candle [rust-029]) trailing Python and TypeScript on agent-framework depth [rust-030].
- **Kotlin (3.90)** — default for JVM application work and increasingly cross-platform [kotlin-015]; v0.2 lifts MC to 4.5 on null-safety + sealed types + when exhaustiveness [kotlin-001, kotlin-002, kotlin-003]; AI-systems at 3 via JVM interop and the official MCP Kotlin SDK [kotlin-021]. Risk: JetBrains governance dependence [kotlin-009].
- **Elixir (3.28)** — default for fault-tolerant distributed systems. BEAM concurrency and OTP supervision [elixir-001, elixir-002]; Phoenix LiveView [elixir-009] for real-time AI-augmented UIs; runtime/ecosystem rescored to 4.5 in v0.2.
- **C++ (2.70)** — default only for accelerator host code where the safety penalty is knowingly accepted [cpp-013, cpp-019]. ISO standardization [cpp-001] and modules/ranges [cpp-002] retained; AI-systems credit 3 via llama.cpp [cpp-017], ONNX C++ [cpp-018], CUDA/ROCm/SYCL host [cpp-019]. The dominant signal pushing new projects away is safety pressure [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008].

## Slide 12 — Recommendations by domain

| Domain | Primary | Alternatives |
|---|---|---|
| Greenfield application work | TypeScript | Kotlin, .NET (C#) |
| Systems / infrastructure / security-sensitive | Rust | Go |
| Data / AI/ML / AI-systems integration | Python (typed, day-one) | TypeScript for data products |
| Fault-tolerant distributed systems | Elixir | Go, Rust |
| AI-native compute kernels | Rust | C++ only where unavoidable |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) |
| JVM application work needing AI integration | Java (LangChain4j, Anthropic Java SDK) | Kotlin |

No single language is a default for everything. AI-era language choice becomes more domain-sensitive, not less. Most organizations will run two or three of these in parallel; the polyglot interaction surface is part of the work.

## Slide 13 — Limitations and closing

**Limitations.** Framework weights are working assumptions, not a calibrated multi-rater output; small weight perturbations are absorbed, large ones are not. Snapshot date 2026-04-30 — Elixir's set-theoretic types [elixir-007] could move that language's verification score before its next major release; Python's typing PEP cadence [python-016] continues to land each release. Greenfield framing is a deliberate choice; maintenance-estate teams should re-weight. Single-rater judgment grounded in 241 atomic claims with primary-source citations — every cell traces through Insight → Evaluation → Claim → Source and is intended to be falsifiable.

**Closing thesis.** AI raises the price of cheap verification, ergonomic agentic operability, and structural safety. The languages that pay all three taxes win the next decade — none of them by default.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# Programming Languages in the AI Era — Deck Outline

*Source: outputs/report.md. Anchored in 255 atomic claims across 14 languages.*

## Slide 1 — Title

Programming Languages in the AI Era — a greenfield evaluation of 14 languages against the demands of AI-assisted and AI-agentic software development. Framework v0.1, snapshot 2026-04-30. Author: Rutger Hemrika.

## Slide 2 — The question

If you were starting a new project today, which language would you pick — and how would you defend that choice when AI agents are doing more of the writing? Installed base and incumbent gravity stop being load-bearing once a team commits to a greenfield codebase. The question this deck answers: which languages are forward-fit for AI-era development, on the evidence available now, with every claim traceable to a primary source.

## Slide 3 — Framing

Greenfield framing: no credit for legacy installed base, code volume, or incumbent gravity. Five weighted dimensions — Human cognition (20%), Machine cognition (25%), AI-agent operability (25%), Runtime/ecosystem (20%), Strategic viability (10%). Four cross-cutting lenses: verification, agentic operability, safety pressure, abstraction compression. Forward properties credited: governance, future fit, AI-training representation, ecosystem velocity, ecosystem viability. Legacy code volume is not.

## Slide 4 — The matrix

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
| C++         | 2  | 3  | 2  | 4  | 2  | 2.65 |

Three tiers: top (>=4.0) Go, TypeScript, Rust, Kotlin, .NET. Middle (3.0-3.99) Python, Swift, Java, Zig, Elixir, Haskell. Lower (<3.0) Julia, Mojo, C++. The lead reflects breadth, not domination.

## Slide 5 — Finding 1: AI-agent operability is most discriminating

Operability separates the matrix more sharply than any other axis. Go and TypeScript score 5; Haskell and C++ score 2. The pattern tracks **toolchain unification and LSP-exposed semantic models**, not type-system depth. Go ships a single canonical command for build/test/format/vet/deps/docs [go-003], a canonical formatter [go-002], MVS dependency resolution [go-004], and gopls as official LSP [go-015]. TypeScript reaches the same surface from a dynamic substrate via strict-mode [typescript-004], discriminated unions [typescript-002], and the language service Microsoft itself originated [typescript-006, typescript-007]. .NET ships Roslyn as a public compiler-platform API [dotnet-006, dotnet-014]. Haskell and C++ lack a single canonical build surface [haskell-006, haskell-007, cpp-015].

## Slide 6 — Finding 2: AI raises the value of cheap verification

Agents write more code than humans can read; the bottleneck shifts from generation to validation. Languages whose compilers can falsify a candidate change without execution gain proportional value. Strongest verification clusters: Rust ownership rules [rust-001, rust-002, rust-003] with exhaustive `match` [rust-006]; Haskell Hindley-Milner [haskell-002] with Liquid Haskell refinements [haskell-005]; Kotlin nullables and sealed `when` [kotlin-001, kotlin-002, kotlin-003]; .NET nullable-reference-type flow analysis [dotnet-003, dotnet-004]; Swift optionals and access rules [swift-001, swift-004]. Verification velocity is also visible: TypeScript `satisfies` [typescript-016], Python typing-PEP cadence [python-016, python-004], Elixir set-theoretic types [elixir-007], Mojo compile-time parameters [mojo-004, mojo-005].

## Slide 7 — Finding 3: Safety pressure has crossed into regulatory territory

Four independent institutions now treat memory safety as a structural language property they actively select for. Microsoft Security Response Center: ~70% of Microsoft-assigned CVEs are memory-safety issues [cpp-004]. Chromium: ~70% of high-severity bugs are memory-safety bugs [cpp-005]. NSA *Software Memory Safety* names C and C++ [cpp-006]. ONCD's 2024 *Back to the Building Blocks* repeats the recommendation [cpp-007]. Android telemetry shows memory-safety vulnerabilities declining as new native code shifted to memory-safe languages including Rust [cpp-008, rust-016, rust-017]. Memory-safe languages (Rust [rust-001], Kotlin/JVM [kotlin-001], Swift [swift-004], Elixir/BEAM [elixir-002, elixir-004], .NET [dotnet-002, dotnet-003]) align with the pressure; C++ is alone in the exposed tier.

## Slide 8 — Finding 4: Incumbent gravity does not insulate

Greenfield framing is the lever that exposes this. C++ retains forward credit for accelerator host code [cpp-013] and ISO standardization [cpp-001] but loses 0.4 points because safety pressure dominates strategic viability. Java retains forward credit for virtual threads [java-006], structured concurrency JEP 453 [java-015], and Maven Central [java-010] — but the legacy adoption premium is gone, and Kotlin's null-safety [kotlin-001] and sealed types [kotlin-002] now sit inside Java's own ecosystem. Python keeps RE=5 because ML-domain library velocity is forward-relevant [python-012] and typing PEP cadence is a verification-velocity signal [python-016, python-018] — but unenforced hints [python-002] and fragmented stub coverage [python-020] keep the verification weakness load-bearing. None of these languages collapses; their forward case becomes domain-specific rather than default.

## Slide 9 — Finding 5: Gradual typing has narrowed the dynamic-vs-static gap

The original binary is becoming a spectrum. TypeScript's static layer over JavaScript [typescript-001] with discriminated unions [typescript-002] and structural typing [typescript-003] reaches an AI-era profile competitive with mature static languages — score 4.25, ahead of Kotlin and .NET. Python typing has advanced through PEPs 484, 526, 544, 612, 646, 692, 695 [python-016], with PEP 695 generic syntax [python-004] and pyright/Pylance-bundled stubs [python-018] giving agents enough signal to operate in well-typed Python. Elixir is researching set-theoretic types [elixir-007, elixir-013] and supports Dialyzer success-typing [elixir-006]. Per-class means: static-mature 3.88, dynamic+gradual 3.87 — effectively tied at the top. The predictive feature is gradual typing, not original origin.

## Slide 10 — Top-tier verdicts

- **Go (4.45)** — default for backend services where deliberate minimalism is acceptable. Wins on operability breadth [go-003, go-015]. Risk: type-system minimalism is real [go-017, go-018].
- **TypeScript (4.25)** — default for application work in the JavaScript-shaped world. Strict-mode discipline [typescript-004] is the asset. Risk: type system is intentionally not sound [typescript-005, typescript-017].
- **Rust (4.15)** — default for systems, infrastructure, security-sensitive work. Ownership rules [rust-001] plus regulatory alignment [rust-015, rust-016]. Risk: learning curve and compile times [rust-020, rust-025].
- **Kotlin (4.00)** — default for JVM application work and increasingly cross-platform [kotlin-015]. Risk: JetBrains governance dependence [kotlin-009].
- **.NET / C# (4.00)** — default for Microsoft-shop application and service work. Roslyn as public compiler-platform API [dotnet-006, dotnet-014]. Risk: NRT is opt-in [dotnet-012], MSBuild ceremony [dotnet-011].

## Slide 11 — Other notable verdicts

- **Python (3.95)** — default for data, AI/ML, and scripting; second-best for general application work. ML ecosystem velocity [python-012] plus typing trajectory [python-016, python-018] vs unenforced hints and runtime-only type errors [python-002, python-015, python-020]. Typed Python in CI is the only sustainable production posture.
- **Mojo (2.65)** — a forward bet on AI-native compute kernels. MLIR-based compilation targeting heterogeneous hardware [mojo-002, mojo-013] and compile-time parameters with ownership conventions [mojo-004, mojo-005]. Risk: single-vendor governance under Modular [mojo-008], pre-1.0 status [mojo-010], small training-corpus footprint [mojo-012].
- **C++ (2.65)** — default only for accelerator host code where the safety penalty is knowingly accepted [cpp-013]. ISO standardization [cpp-001] and modules/ranges [cpp-002] retained. The dominant signal pushing new projects away is safety pressure [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008].

## Slide 12 — Recommendations by domain

| Domain | Primary | Alternatives |
|---|---|---|
| Greenfield application work | TypeScript | Kotlin, .NET (C#) |
| Systems / infrastructure / security-sensitive | Rust | Zig, Go |
| Data / AI/ML / scripting | Python (typed, day-one) | TypeScript for data products, Julia for numerics |
| Fault-tolerant distributed systems | Elixir | Go, Rust |
| AI-native compute kernels | Mojo (forward bet), Rust | C++ only where unavoidable |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) |

No single language is a default for everything. AI-era language choice becomes more domain-sensitive, not less. Most organizations will run two or three of these in parallel; the polyglot interaction surface is part of the work.

## Slide 13 — Limitations and closing

**Limitations.** Framework weights are working assumptions, not a calibrated multi-rater output; small weight perturbations are absorbed, large ones are not. Snapshot date 2026-04-30 — Mojo, Zig, Julia, and Elixir's set-theoretic types [mojo-010, zig-006, julia-014, elixir-007] could move scores within twelve months. Greenfield framing is a deliberate choice; maintenance-estate teams should re-weight. Single-rater judgment grounded in 255 atomic claims with primary-source citations — every cell traces through Insight → Evaluation → Claim → Source and is intended to be falsifiable.

**Closing thesis.** AI raises the price of cheap verification, ergonomic agentic operability, and structural safety. The languages that pay all three taxes win the next decade — none of them by default.

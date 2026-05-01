# Programming Languages in the AI Era

*A greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development.*

## TL;DR

Across 10 languages, scored on five weighted dimensions and read through four cross-cutting lenses, **Go (4.45)**, **TypeScript (4.25)**, **Rust (4.15)**, **Kotlin (4.00)** and **.NET / C# (4.00)** form the top tier for greenfield AI-era projects. Python (3.95) sits just below, retained by ML-ecosystem velocity but dropped from the top tier once installed-base credit is removed. Swift, Java and Elixir occupy a middle tier where each has a real structural strength offset by a load-bearing operability or ecosystem weakness. C++ trails at the bottom for memory-safety pressure that has crossed from technical preference into regulatory selection criterion.

The headline is not that Go has "won". The matrix rewards breadth, and Go's lead reflects the joint pressure of AI-agent operability and ecosystem viability rather than dominance on any single axis. Every top-tier language carries a documented weakness: Rust's compile-time and learning-curve cost, TypeScript's unsound runtime semantics, Kotlin's single-vendor governance exposure, Go's deliberate abstraction limits, .NET's MSBuild and analyzer-API ceremony.

The full matrix sits in `comparisons/overview.md` and is reproduced in *The Matrix* below. Recommendations by domain — application work, systems, data/ML, fault-tolerant distributed systems, AI-native kernels, Apple-platform applications — follow in *Recommendations by Use Case*. Read with the limitations and the framework version (v0.1) as part of the reading.

## Framing

This report evaluates languages from a **greenfield** position: a new AI-era project starting today, not a maintenance estate. Installed base, code volume, and incumbent gravity are not credited. The framework instead credits forward-looking properties: governance quality, future fit, AI-training representation, ecosystem velocity, and ecosystem viability (the production-readiness a new project inherits today — compiler toolchains, ABI, deployment, observability, accelerator integration). Both ecosystem viability and ecosystem velocity are forward-looking and both are credited; legacy code volume is not. The framework specification lives in `framework/evaluation-framework.md`.

Each language is scored 1–5 on five dimensions:

- **Human cognition (20%)** — can humans understand and govern the code?
- **Machine cognition (25%)** — can compilers, analyzers, and AI systems reason about it?
- **AI-agent operability (25%)** — can agents safely modify and verify it?
- **Runtime and ecosystem (20%)** — can it run production systems?
- **Strategic viability (10%)** — will it remain relevant?

Four cross-cutting lenses read across the dimensions:

1. **Verification advantage** — what the compiler can falsify before code runs.
2. **Agentic development advantage** — fast feedback, deterministic tooling, clear diagnostics.
3. **Safety pressure** — alignment with regulatory and platform-vendor selection criteria.
4. **Abstraction compression** — how much behaviour is expressed per line, with what cost in implicit context.

What this report **does** credit: forward governance, future fit under AI-era pressure, training-corpus representation, library availability for new projects, and ecosystem viability as a property a greenfield project can lean on today. What it **does not** credit: legacy installed base, the volume of code already written, or the inertia of any incumbent. Teams whose primary task is *maintaining* a Java, C++, or Python estate should re-weight; the framework here addresses a different question.

## The Matrix

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
| Elixir      | 4  | 3  | 3  | 4  | 3  | 3.40 |
| C++         | 2  | 3  | 2  | 4  | 2  | 2.65 |

HC = Human cognition, MC = Machine cognition, AO = AI-agent operability, RE = Runtime/ecosystem, SV = Strategic viability.

Three clusters emerge. **Top tier (≥4.0).** Go, TypeScript, Rust, Kotlin, .NET — the languages whose structural properties, ecosystems, and operability characteristics combine to produce the strongest joint AI-era profiles. Each wins for different reasons: Go and TypeScript on agent operability, Rust on verification and safety, Kotlin and .NET on balanced strength. **Middle tier (3.0–3.99).** Python, Swift, Java, Elixir — each has either a structural strength offset by a real operability or ecosystem cost (Elixir) or carried legacy premium that no longer applies (Java, Python on strategic viability). **Lower tier (<3.0).** C++ — exposed by safety pressure that the framework reads as a strategic-viability criterion. The script `scripts/score_summary.py` regenerates this table from the per-language evaluations.

## Five Findings

### 1. AI-agent operability is the most discriminating dimension.

Operability separates the matrix more sharply than any other axis. Go and TypeScript score 5 on AI-agent operability while C++ scores 2 — and the gap holds even where the underlying language quality is comparable on other dimensions. The pattern is that operability tracks **toolchain unification and LSP-exposed semantic models**, not type-system depth. Go has a single canonical command covering build, test, format, vet, dependency management and documentation [go-003], a single canonical formatter [go-002], minimum-version-selection dependency resolution [go-004], and gopls as the official LSP server [go-015]. TypeScript reaches the same surface from a dynamic substrate: an opt-in strict-mode bundle [typescript-004], discriminated unions for exhaustive narrowing [typescript-002], a Microsoft-maintained language service [typescript-006] and the Language Server Protocol Microsoft itself originated [typescript-007]. .NET ships Roslyn as a public compiler-platform API [dotnet-006, dotnet-014] and a unified `dotnet` CLI [dotnet-010]. Rust's diagnostics [rust-004] and rust-analyzer [rust-021] sit alongside Cargo's single canonical workflow [rust-008]. C++ has cppreference [cpp-012] but no canonical build system and uneven C++20 module adoption [cpp-015]. The cross-lens reasoning lives in `insights/agentic-feedback-loops.md`.

### 2. AI raises the value of cheap verification.

Agents write more code than humans can read; the bottleneck shifts from generation to validation. Languages whose compilers can falsify a candidate change without execution gain proportional value. The strongest verification structures cluster in four languages — Rust's ownership-checked memory rules [rust-001, rust-002, rust-003] with exhaustive `match` [rust-006], Kotlin's nullable-type distinction [kotlin-001] and exhaustive `when` over sealed hierarchies [kotlin-002, kotlin-003], .NET's nullable-reference-type flow analysis [dotnet-003] and pattern-matching family [dotnet-004], Swift's optionals [swift-001] and memory-safety access rules [swift-004]. A second pattern is **verification velocity**: TypeScript's `satisfies` operator [typescript-016], Python's sustained typing-PEP cadence [python-016] and PEP 695 generics [python-004], Elixir's set-theoretic type research [elixir-007]. The trajectory is toward verification, not away from it. The reasoning lives in `insights/ai-favors-verifiability.md`. Verification leadership does not automatically translate to overall ranking — Rust scores 5 on machine cognition but 4 on operability — but the direction of travel is unambiguous.

### 3. Safety pressure has crossed from technical preference to regulatory criterion.

Four independent institutional vantage points have aligned on memory safety as a structural language property they actively select for: Microsoft Security Response Center reports approximately 70% of CVEs Microsoft assigns are memory-safety issues [cpp-004]; the Chromium project independently reports approximately 70% of high-severity bugs are memory-safety bugs [cpp-005]; the U.S. National Security Agency's *Software Memory Safety* sheet recommends shifting from memory-unsafe languages and explicitly names C and C++ [cpp-006]; the Office of the National Cyber Director's 2024 *Back to the Building Blocks* report repeats the recommendation [cpp-007]. Google's Android telemetry shows memory-safety vulnerabilities declining as new native code shifted toward memory-safe languages including Rust [cpp-008, rust-016, rust-017]. Languages with structural memory safety (Rust [rust-001], JVM-verified Kotlin [kotlin-001], Swift [swift-004], BEAM-isolated Elixir [elixir-002, elixir-004], CLI-typed .NET [dotnet-002, dotnet-003]) align with this pressure; C++ is alone in the "exposed" tier in `comparisons/lens-analysis.md`. C++ counter-claims [cpp-014, cpp-015] note accelerator-dialect divergence and uneven module adoption but do not unwind the regulatory direction. Python's exposure differs in kind — runtime-error rather than memory-unsafety [python-002, python-019] — and is not a regulatory focus. The full reading lives in `insights/safety-pressure.md`.

### 4. Incumbent gravity does not insulate against forward AI-era pressure.

The framework's greenfield framing is the lever that exposes this. C++ retains forward production credit for accelerator host code [cpp-013] and ISO standardization [cpp-001], but loses 0.4 points relative to legacy framings because the safety pressure documented in finding 3 dominates strategic viability. Java retains forward credit for virtual threads [java-006], structured concurrency JEP 453 [java-015], the JVM's portable bytecode and verifier [java-009], and Maven Central as forward ecosystem viability [java-010] — but the legacy adoption premium is gone, and verification competition from Kotlin's null-safety [kotlin-001] and sealed types [kotlin-002] now sits inside Java's own ecosystem. Python keeps runtime/ecosystem at 5 because ML-domain library velocity is forward-relevant [python-012, python-013] and the typing PEP cadence [python-016] and pyright/Pylance with bundled stubs [python-018] are real verification-velocity signals — but PEP 484 hints not being runtime-enforced [python-002] and stub coverage fragmenting across the dependency graph [python-020] keep the verification weakness load-bearing. None of these languages collapses; their forward case becomes domain-specific rather than default. The full reading lives in `insights/incumbent-risk.md`.

### 5. Gradual typing has narrowed the dynamic-versus-static gap where it has been adopted.

The original dynamic-versus-static binary is becoming a spectrum. TypeScript's static layer over JavaScript [typescript-001] with discriminated unions [typescript-002] and structural typing [typescript-003] reaches an AI-era profile competitive with mature static languages — score 4.25, ahead of Kotlin and .NET. Python's typing system has advanced through PEPs 484, 526, 544, 612, 646, 692, 695 [python-016], with PEP 695 generic syntax [python-004] and pyright/Pylance bundled stubs [python-018] giving agents enough signal to operate in well-typed Python codebases. Elixir is researching a set-theoretic type system [elixir-007, elixir-013] and already supports Dialyzer's success-typing analysis [elixir-006]. The gap that remains is the bridge between languages that have invested in static structure and languages that have not: plain JavaScript continues to lose ground to TypeScript. The headline is that *gradual typing* — not the original static or dynamic origin — is the most predictive feature. The full reading lives in `comparisons/dynamic-vs-static.md`.

## Per-Language Verdicts

### Go — 4.45 — *Default for backend services where deliberate minimalism is acceptable.*

Strongest forward case: a uniquely low-friction agent profile built from a single canonical command covering the full development loop [go-003], gofmt as a single canonical formatter [go-002], and gopls as the official LSP server [go-015]. Goroutines and channels [go-005] plus high developer-survey satisfaction [go-013] reinforce the position. **Load-bearing risk:** the deliberate type-system minimalism — no sum types, late generics, no exhaustive enums [go-017] — is real, and `if err != nil` boilerplate increases code volume on every call site [go-018]. Go wins on operability breadth, not on verification ceiling.

### TypeScript — 4.25 — *Default for application work in the JavaScript-shaped world.*

Strongest forward case: an optional static type layer over JavaScript [typescript-001] with discriminated unions for exhaustive narrowing [typescript-002] and a strict-mode bundle [typescript-004], all served through a Microsoft-maintained Language Service [typescript-006] over the Language Server Protocol Microsoft originated [typescript-007]. **Load-bearing risk:** the type system is intentionally not sound — `any` opts a value out of checking [typescript-005], assertions and function-bivariance produce holes [typescript-017], and types are erased at compile time with no runtime representation [typescript-018]. Strict-mode discipline is what makes TypeScript an AI-era asset rather than a liability.

### Rust — 4.15 — *Default for systems, infrastructure, and security-sensitive work.*

Strongest forward case: ownership-checked memory rules without garbage collection [rust-001, rust-002, rust-003], exhaustive `match` over enums [rust-006, rust-007], and external regulatory alignment via NSA recommendations and Android telemetry [rust-015, rust-016, rust-017]. Cargo [rust-008], rust-analyzer [rust-021], Tokio [rust-023], and the emerging accelerator/ML ecosystem (wgpu, candle, burn) [rust-022] reinforce the position. **Load-bearing risk:** the ownership model carries a real learning curve [rust-020], compile times remain a friction point on large workspaces [rust-025], and the async ecosystem splits across runtimes [rust-026]. Rust pays operability cost for verification and safety gains.

### Kotlin — 4.00 — *Default for JVM application work and increasingly for cross-platform.*

Strongest forward case: nullable types as a type-system distinction [kotlin-001], sealed hierarchies with exhaustive `when` [kotlin-002, kotlin-003], coroutines for structured concurrency [kotlin-006], and Kotlin Multiplatform now stable across JVM/Android/iOS/JS/Native [kotlin-015]. **Load-bearing risk:** governance dependence on a single primary vendor (JetBrains) [kotlin-009] and strategic positioning tied to Google's continued Android prioritization [kotlin-020]; null safety is bypassable through Java-interop platform types [kotlin-017].

### .NET (C#) — 4.00 — *Default for Microsoft-shop application and service work, broadly capable beyond.*

Strongest forward case: nullable reference types with static null-state flow analysis [dotnet-003], pattern-matching family across switch expressions [dotnet-004], and Roslyn as a public compiler-platform API exposing the live SemanticModel to analyzers, code fixes, and source generators [dotnet-006, dotnet-014]. **Load-bearing risk:** nullable reference types are opt-in and configured per project [dotnet-012]; MSBuild remains a configuration-language attack surface [dotnet-011]; ECMA-334/335 standardization in practice tracks Microsoft's reference implementation [dotnet-018].

### Python — 3.95 — *Default for data, AI/ML, and scripting; second-best for general application work.*

Strongest forward case: top GitHub language by activity [python-012] and a sustained typing PEP cadence [python-016] with PEP 484 hints [python-003] and PEP 695 generics [python-004], served by pyright/Pylance and bundled typeshed stubs [python-018], with uv as a Rust-based fast package manager [python-011]. **Load-bearing risk:** type hints are not enforced at runtime [python-002], the dynamic runtime surfaces type errors only at execution time [python-015], and stub coverage fragments across the dependency graph [python-020]. Typed Python in CI from day one is the only sustainable AI-era posture.

### Swift — 3.65 — *Default for Apple-platform application work.*

Strongest forward case: optionals as a type-system distinction [swift-001], memory-safety rules with conflicting-access detection [swift-004], language-level async/await and actors [swift-003], and an open Swift Evolution process [swift-006]. **Load-bearing risk:** Apple's primary positioning around its own platforms creates platform-aligned governance [swift-011, swift-016], and server-side Swift on Linux lags Apple-platform feature availability [swift-018].

### Java — 3.45 — *Forward case is narrower than its historic position suggested.*

Strongest forward case: virtual threads as a JVM-level concurrency primitive [java-006], structured concurrency in JEP 453 [java-015], records and sealed classes for closed-hierarchy pattern matching [java-002, java-003, java-004]. **Load-bearing risk:** the build-tool ecosystem is split between Maven and Gradle [java-011], pre-records boilerplate is recognized verbosity [java-013], and preview features stabilize across multiple releases delaying LTS availability [java-016]. JVM-native modern languages (Kotlin) sit inside Java's ecosystem with stronger structural typing.

### Elixir — 3.40 — *Default for fault-tolerant distributed systems and real-time AI-augmented UIs.*

Strongest forward case: BEAM process and concurrency model [elixir-001, elixir-004], OTP supervision trees as structured fault-tolerance [elixir-002], and Phoenix LiveView as a credible substrate for server-driven real-time interfaces [elixir-009, elixir-014]. **Load-bearing risk:** Elixir is dynamically typed [elixir-005] with set-theoretic types still in research/early adoption [elixir-016]; LiveView's server-driven rendering ties front-end lifecycle to a stateful socket [elixir-017].

### C++ — 2.65 — *Default only for accelerator host code where the safety penalty is knowingly accepted.*

Strongest forward case: ISO standardization with three-yearly revisions [cpp-001], C++20 modules and ranges [cpp-002], and the dominant accelerator toolchains (CUDA, ROCm/HIP, SYCL, oneAPI) all primarily targeting C++ as their host language [cpp-013]. **Load-bearing risk:** memory-safety pressure (MSRC, Chromium, NSA, ONCD, Android) [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008] and undefined-behaviour exposure [cpp-011]. Strategic viability scores 2 for memory-safety reasons.

## Recommendations by Use Case

| Domain | Primary | Alternatives | Trade-off |
|---|---|---|---|
| Greenfield application work | TypeScript | Kotlin, .NET (C#) | Operability and ecosystem breadth, accepting unsoundness in TypeScript [typescript-005, typescript-017]. |
| Systems / infrastructure / security-sensitive | Rust | Go | Verification and safety [rust-001, rust-015], accepting compile-time and learning-curve cost [rust-020, rust-025]. |
| Data / AI/ML / scripting | Python | TypeScript (for data products) | ML ecosystem velocity [python-012] over verification gap [python-002, python-019]. Treat type discipline as day-one investment. |
| Fault-tolerant distributed systems | Elixir | Go, Rust | BEAM runtime properties [elixir-001, elixir-002] over verification ceiling [elixir-005, elixir-016]. |
| AI-native compute kernels | Rust | C++ (only where unavoidable) | Rust's accelerator/ML ecosystem (wgpu, candle, burn) [rust-022] over C++ memory-safety exposure [cpp-004, cpp-006]. |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] | Native platform integration [swift-003, swift-014], accepting Apple-aligned governance [swift-011]. |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) | Toolchain access [cpp-013], explicitly accepting safety penalty [cpp-004, cpp-006]. |

For **greenfield application work** (web, mobile, internal tools), TypeScript is the primary recommendation because its joint operability-and-verification profile is the broadest in the matrix; Kotlin and .NET are credible alternatives where the JVM or .NET runtimes are already operationally preferred. For **systems and infrastructure**, Rust pays operability cost for verification and safety gains that align with the regulatory direction in finding 3; Go is the alternative where deliberate minimalism is desired over verification ceiling. For **data and ML**, Python's ecosystem velocity remains forward-relevant despite the verification gap, but typed Python in CI from project start is the only sustainable posture. For **fault-tolerant distributed systems**, Elixir's BEAM properties are not matched by other languages, and the verification gap is acceptable given OTP's runtime guarantees. For **AI-native compute kernels**, Rust's accelerator ecosystem (wgpu, candle, burn) is the lower-risk alternative to C++; C++ remains the default only when accelerator host code forces it. For **Apple-platform application work**, Swift is the native default; Kotlin Multiplatform is the cross-platform alternative now stable across iOS targets [kotlin-015]. The portfolio note in `comparisons/lens-analysis.md` is concrete: no single language is a default for everything, and AI-era language choice becomes more domain-sensitive, not less.

## Limitations

The framework weights (HC 20%, MC 25%, AO 25%, RE 20%, SV 10%) are working assumptions, not the output of a calibrated multi-rater process. A reasonable reader could weight runtime/ecosystem higher (favouring Python and the JVM languages) or AI-agent operability higher (favouring Go and TypeScript). The matrix is robust to small weight perturbations but not to large ones; the report should be read as the output of *a* defensible weighting, not *the* weighting.

The snapshot date is **2026-04-30**. Several languages are evolving rapidly and the scores are time-bound: Elixir's set-theoretic type system [elixir-007, elixir-013] could move that language's verification score before its next major release; Python's typing PEP cadence [python-016] continues to land each release.

The greenfield framing is itself a deliberate choice. Teams whose primary task is *maintaining* large incumbent estates should re-weight: legacy gravity reappears as an advantage in that question, and this matrix will under-credit Java, Python and C++ for that purpose. The report does not address bilingual-team or polyglot-portfolio questions in depth beyond the recommendations table; in practice, most engineering organizations operate two or three of these languages simultaneously, and the cross-language interaction surface is not part of the scoring.

Finally, the scores are single-rater author judgments grounded in atomic claims with primary-source citations, not the average of an independent expert panel. Each cell traces through Insight → Evaluation → Claim → Source, and is intended to be falsifiable by the underlying evidence — but a reader who disagrees with a specific score should follow the trail to the claim and the source rather than treating the cell as authoritative.

## Reading and Reproducibility

The corpus is structured for traceability. Every cell in the matrix decomposes into:

- **Framework** — `framework/dimensions.md` (criteria), `framework/evaluation-framework.md` (weights and lenses), `framework/scoring-rubric.md` (1–5 rubric).
- **Claims** — `claims/<language>.yaml`, 191 atomic claims across 10 languages, each with a primary-source citation and explicit polarity.
- **Sources** — `sources/<language>-sources.yaml`, 136 source entries with publication metadata.
- **Evaluations** — `evaluations/<language>.yaml`, per-language dimension scores with `supporting_claims:` traceability into the claim corpus.
- **Comparisons** — `comparisons/overview.md` (matrix and headline findings), `comparisons/lens-analysis.md` (the four lenses), `comparisons/agent-friendly-languages.md` (operability deep dive), `comparisons/dynamic-vs-static.md`.
- **Insights** — `insights/agentic-feedback-loops.md`, `insights/ai-favors-verifiability.md`, `insights/safety-pressure.md`, `insights/incumbent-risk.md`.

The matrix is reproducible via `scripts/score_summary.py`, which reads `evaluations/*.yaml` and emits the table in `comparisons/overview.md`. Validation of every claim citation in this report is reproducible via the script in the execution plan; every cited claim ID resolves to a row in the corresponding `claims/<lang>.yaml` file. The full methodology is documented in `outputs/evidence-backed-research-execution-plan.md`.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
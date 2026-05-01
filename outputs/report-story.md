# Programming Languages in the AI Era

*Why is the AI-era language ranking led by the language with the simplest types?*

## TL;DR

For thirty years, language choice was decided by gravity. **That stopped working in 2024.** The Known world: pick the language with the largest installed base, the deepest library catalog, the most developers on the market. Java for enterprise, C++ for systems, Python for data, JavaScript for the web. Predictable, safe, defensible. Boring on purpose.

Then a single number changed the conversation. Microsoft and the Chromium project both reported, separately, that approximately 70% of the security vulnerabilities they triage are memory-safety bugs — buffer overflows, use-after-frees, the same family of mistakes for thirty years. Within four years, the U.S. National Security Agency and the White House Office of the National Cyber Director had named C and C++ in writing as memory-unsafe and called for adoption of memory-safe languages for new projects. Memory safety crossed from a developer preference to a regulatory selection criterion.

AI agents arrived in the same window. They started writing code at production scale, and "fast feedback for an agent" became a real number on a budget. The Unknown world rewards different properties: how cheaply a language can be verified, how cleanly its semantic model exposes itself to an LSP, how aligned the language is with the new safety guidance.

But this isn't a simple morality play. The greenfield bet isn't *verification* defeating *operability* — it's *both at once, in tension*. Rust tops verification and lands third on weighted total. Go tops operability and tops the matrix overall, despite ranking last in the cohort on type-system expressiveness. The pattern repeats: languages that win one axis and lose its opposite settle in the middle. The top of the matrix is where both rents get paid.

**What this is about, for you:** if you're starting a new project today and AI agents will write a substantial fraction of the code, which language gives your team cheap verification, fast feedback, and forward position — without paying rent for legacy you don't have? Ten languages, ranked. Every assertion traceable to a primary source.

## Framing

Picking a language used to mean choosing a tribe. The tribe came with a hiring market, a conference circuit, a corporate sponsor, a stack of O'Reilly books. The choice was social as much as technical, and the social half hardened into gravity: the more code already written in a language, the more written in it next quarter. A rational equilibrium for thirty years. No longer the equilibrium that matters for a project not yet written.

This report evaluates each language from a deliberately greenfield position. Installed base, code volume, incumbent inertia — none of it earns credit. That choice is load-bearing. A team maintaining a million lines of Java has a different question to answer; this report is not for them. This is for the team starting today, with AI agents in the loop, asking which language gives them the best forward posture for the next three years.

The framework had to make five decisions. Can humans understand and govern the code (**Human cognition**, 20%)? Can compilers, analyzers, and AI systems reason about it (**Machine cognition**, 25%)? Can agents safely modify and verify it (**AI-agent operability**, 25%)? Can the runtime carry production traffic (**Runtime and ecosystem**, 20%)? Will the language still be the right choice in three years (**Strategic viability**, 10%)? Operability and machine cognition together carry half the weight — a bet that the AI-era discriminator is the feedback loop, not the syntax.

Four lenses cut across the dimensions: **verification advantage** (what the compiler falsifies before code runs), **agentic development advantage** (fast feedback, deterministic tooling, clear diagnostics), **safety pressure** (alignment with regulatory and platform-vendor selection criteria), **abstraction compression** (behaviour per line, with what implicit context cost).

What the framework credits: governance quality, future fit, training-corpus representation, library availability, and ecosystem viability. What it does not credit: legacy installed base, lines of code already written, incumbent inertia. The framework lives in `framework/evaluation-framework.md`.

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

Read the table from the top and the surprise is immediate: the leader has the simplest type system in the cohort. That isn't a glitch in the weighting. It is the central finding compressed into one row.

**Top tier — both rents paid.** Go, TypeScript, Rust, Kotlin, .NET clear 4.0 by combining a credible operability story with structural strength on the verification or safety side. Go and TypeScript win on operability. Rust wins on verification and safety. Kotlin and .NET pay both rents at "good enough" — and in a framework that punishes any zero, "good enough on every axis" beats "perfect on one and weak on another."

**Middle tier — strength offset by structural cost.** Python, Swift, Java, Elixir. Each carries a real asset (ML library velocity, Apple-platform integration, modern JVM concurrency, BEAM properties) and a cost the framework refuses to discount (type erasure, lagging Linux posture, build-tool fragmentation, dynamic typing).

**Lower tier — under named pressure.** C++ alone, exposed by regulatory pressure read as strategic-viability. Lower-tier doesn't mean wrong-tier; the bet is conditional and the conditions are nameable.

## Five Findings

### 1. AI-agent operability is the dimension that does the most separating.

The Known story about agents: they need smart compilers. The Unknown story, visible in this matrix: they need *unified toolchains*. Go and TypeScript score 5 on AI-agent operability. C++ scores 2. The gap holds even where underlying language quality on other dimensions is comparable. Operability tracks **toolchain unification and LSP-exposed semantic models**, not type-system depth.

Go has a single canonical command covering build, test, format, vet, dependency management, and documentation [go-003], a single canonical formatter [go-002], minimum-version-selection dependency resolution [go-004], and gopls as the official LSP server [go-015]. TypeScript reaches the same surface from a dynamic substrate: opt-in strict mode [typescript-004], discriminated unions [typescript-002], a Microsoft-maintained language service [typescript-006], and the Language Server Protocol Microsoft originated [typescript-007]. .NET ships Roslyn [dotnet-006, dotnet-014] and a unified `dotnet` CLI [dotnet-010]. Rust's diagnostics [rust-004] and rust-analyzer [rust-021] sit alongside Cargo's canonical workflow [rust-008].

C++ has cppreference [cpp-012] but no canonical build system and uneven C++20 module adoption [cpp-015].

### 2. AI raises the value of cheap verification.

When a human writes the code, the bottleneck is generation. When an agent writes the code, the bottleneck is validation — agents produce more candidate diffs than any human can read. A compiler that can falsify a candidate without execution is worth more in the Unknown than it ever was in the Known.

The strongest verification structures cluster in four languages: Rust's ownership-checked memory rules [rust-001, rust-002, rust-003] with exhaustive `match` [rust-006]; Kotlin's nullable-type distinction [kotlin-001] and exhaustive `when` over sealed hierarchies [kotlin-002, kotlin-003]; .NET's nullable-reference-type flow analysis [dotnet-003] and pattern-matching family [dotnet-004]; Swift's optionals [swift-001] and conflicting-access detection [swift-004].

A second pattern is **verification velocity** — the rate at which a language is closing its verification gap. TypeScript's `satisfies` operator [typescript-016], Python's typing-PEP cadence [python-016] with PEP 695 generics [python-004], Elixir's set-theoretic type research [elixir-007]. The cohort trajectory is toward verification, not away from it. Verification leadership doesn't translate automatically — Rust scores 5 on machine cognition but 4 on operability — but the direction is unambiguous. Reading: `insights/ai-favors-verifiability.md`.

### 3. Safety pressure crossed from preference to criterion.

For a long time, "memory safety" was a religious argument. Then it became a number, and the number was the same number from two independent vantage points. The Microsoft Security Response Center reports approximately 70% of CVEs Microsoft assigns are memory-safety issues [cpp-004]. The Chromium project, independently, reports approximately 70% of high-severity bugs are memory-safety bugs [cpp-005]. Two organizations triaging different code, on different release cadences, reaching the same fraction.

That number moved policy. The U.S. National Security Agency's *Software Memory Safety* sheet recommends shifting away from memory-unsafe languages and explicitly names C and C++ [cpp-006]. The White House Office of the National Cyber Director's 2024 *Back to the Building Blocks* report repeats the recommendation [cpp-007]. Google's Android telemetry shows memory-safety vulnerabilities declining as new native code shifted toward memory-safe languages including Rust [cpp-008, rust-016, rust-017].

Languages with structural memory safety align: Rust [rust-001], JVM-verified Kotlin [kotlin-001], Swift [swift-004], BEAM-isolated Elixir [elixir-002, elixir-004], CLI-typed .NET [dotnet-002, dotnet-003]. C++ stands alone in the "exposed" tier. Counter-claims about accelerator-dialect divergence [cpp-014, cpp-015] don't unwind the regulatory direction. Python's exposure differs in kind — runtime-error, not memory-unsafety [python-002] — and is not a regulatory focus. Reading: `insights/safety-pressure.md`.

### 4. Incumbent gravity does not insulate against forward AI-era pressure.

The greenfield framing is the lever that exposes this. Incumbency alone no longer pays the rent. C++ keeps forward credit for accelerator host code [cpp-013] and ISO standardization [cpp-001], but loses points relative to legacy framings because safety pressure dominates strategic viability.

Java retains forward credit for virtual threads [java-006], structured concurrency in JEP 453 [java-015], and Maven Central [java-010]. But the legacy adoption premium is gone, and verification competition from Kotlin's null-safety [kotlin-001] and sealed types [kotlin-002] now sits inside Java's own ecosystem. Python keeps runtime/ecosystem at 5 because ML library velocity is forward-relevant [python-012, python-013] and the typing PEP cadence [python-016] with pyright/Pylance [python-018] are real verification-velocity signals — but PEP 484 hints not being runtime-enforced [python-002] keeps the verification weakness load-bearing. None of the three collapses; their forward case becomes domain-specific. Reading is in `insights/incumbent-risk.md`.

### 5. Gradual typing has narrowed the dynamic-versus-static gap where adopted.

The original binary — dynamic versus static — was always too coarse, and AI-era pressure has retired it. TypeScript's static layer over JavaScript [typescript-001], with discriminated unions [typescript-002] and structural typing [typescript-003], reaches a profile competitive with mature static languages. It scores 4.25 — ahead of Kotlin and .NET, both 4.00.

Python's typing has advanced through PEPs 484, 526, 544, 612, 646, 692, 695 [python-016], with PEP 695 generics [python-004] and pyright/Pylance [python-018] giving agents enough signal in well-typed codebases. Elixir is researching set-theoretic types [elixir-007, elixir-013] and supports Dialyzer success-typing [elixir-006]. The gap remaining is between languages investing in static structure and those that haven't; plain JavaScript continues to lose ground to TypeScript. Headline: *gradual typing* — not static or dynamic origin — is the most predictive feature. Reading: `comparisons/dynamic-vs-static.md`.

## Per-Language Verdicts

### Go — 4.45 — *Default for backend services where deliberate minimalism is acceptable.*

**The rise.** Go enters the AI era with a uniquely low-friction agent profile: a single canonical command for the full development loop [go-003], gofmt as the canonical formatter [go-002], gopls as the official LSP server [go-015], goroutines and channels as a runtime concurrency primitive [go-005]. Operability isn't a feature; it's the worldview.

**The fall.** That same minimalism is a ceiling. No sum types, generics arrived late, no exhaustive enums [go-017]. The `if err != nil` pattern adds boilerplate at every call site [go-018]. Go cannot falsify what its type system cannot express.

**The climb.** Go lands first not by winning verification but by winning the rest. For greenfield backend services — networked infrastructure, agents reading and editing code at scale, teams who prefer explicit dullness to implicit cleverness — Go's joint operability profile beats every other language in the cohort.

### TypeScript — 4.25 — *Default for application work in the JavaScript-shaped world.*

**The rise.** TypeScript layers an optional static type system over JavaScript [typescript-001], with discriminated unions for exhaustive narrowing [typescript-002] and a strict-mode bundle escalating to near-static discipline [typescript-004]. The Microsoft-maintained Language Service [typescript-006] talks to editors over the Language Server Protocol Microsoft originated [typescript-007].

**The fall.** The type system is intentionally not sound. `any` opts a value out of checking [typescript-005]; assertions and function-bivariance produce holes [typescript-017]; types are erased at compile time with no runtime representation [typescript-018]. Strict-mode discipline is what makes TypeScript an asset rather than a liability.

**The climb.** Right answer when the project lives in the JavaScript ecosystem and the team commits to strict mode from day one. Lands at 4.25 — verification-velocity carries it past static-typed peers.

### Rust — 4.15 — *Default for systems, infrastructure, and security-sensitive work.*

**The rise.** Ownership-checked memory rules without garbage collection [rust-001, rust-002, rust-003], exhaustive `match` over enums [rust-006, rust-007], and regulatory alignment via NSA and Android telemetry [rust-015, rust-016, rust-017]. Cargo unifies the workflow [rust-008], rust-analyzer is a high-quality LSP [rust-021], and an accelerator/ML ecosystem is emerging in wgpu, candle, burn [rust-022].

**The fall.** The ownership model carries a learning curve [rust-020]. Compile times remain a friction point on large workspaces [rust-025]. The async ecosystem splits across runtimes [rust-026].

**The climb.** Right answer when the project is systems-shaped and the cost of a memory-safety incident exceeds the learning-curve cost — infrastructure, security tooling, kernels, anything regulators watch.

### Kotlin — 4.00 — *Default for JVM application work and increasingly for cross-platform.*

**The rise.** Nullable types as a first-class distinction [kotlin-001], sealed hierarchies with exhaustive `when` [kotlin-002, kotlin-003], coroutines for structured concurrency [kotlin-006], and Multiplatform now stable across JVM, Android, iOS, JS, Native [kotlin-015].

**The fall.** Governance leans on a single primary vendor (JetBrains) [kotlin-009], strategic positioning is tied to Google's continued Android prioritization [kotlin-020], and null safety is bypassable through Java-interop platform types [kotlin-017].

**The climb.** Right answer when the project lives on the JVM, the team is already there, or cross-platform mobile is on the roadmap. Top-tier; both rents paid at "good enough."

### .NET (C#) — 4.00 — *Default for Microsoft-shop application and service work.*

**The rise.** Nullable reference types with static null-state flow analysis [dotnet-003], a pattern-matching family across switch expressions [dotnet-004], and Roslyn as a public compiler-platform API exposing the live SemanticModel to analyzers and source generators [dotnet-006, dotnet-014]. A unified `dotnet` CLI [dotnet-010].

**The fall.** Nullable reference types are opt-in and configured per project [dotnet-012]. MSBuild remains a configuration-language attack surface [dotnet-011]. ECMA-334/335 standardization in practice tracks Microsoft's reference implementation [dotnet-018] — formal openness, practical single-vendor.

**The climb.** Right answer for Microsoft-shop application and service work, credible well beyond. Co-leads the second top-tier band with Kotlin.

### Python — 3.95 — *Default for data, AI/ML, and scripting; second-best for general application work.*

**The rise.** Top GitHub language by activity [python-012], sustained typing PEP cadence [python-016] including PEP 484 hints [python-003] and PEP 695 generics [python-004], pyright/Pylance with typeshed stubs [python-018], uv as a fast package manager [python-011], unmatched ML-library gravity [python-013].

**The fall.** Type hints are not enforced at runtime [python-002]. The dynamic runtime surfaces type errors only at execution time [python-015]. Stub coverage fragments across the dependency graph [python-020].

**The climb.** Right answer for data, ML, and scripting — ecosystem gravity alone justifies it. For general application work, second-best behind TypeScript. Typed Python in CI from day one is the only sustainable AI-era posture.

### Swift — 3.65 — *Default for Apple-platform application work.*

**The rise.** Optionals as a type-system distinction [swift-001], memory-safety rules with conflicting-access detection [swift-004], language-level async/await and actors [swift-003], an open Swift Evolution process [swift-006].

**The fall.** Apple's positioning creates platform-aligned governance [swift-011, swift-016]. Server-side Swift on Linux lags Apple-platform feature availability [swift-018]. The language is excellent; its non-Apple posture is not.

**The climb.** Right answer for Apple-platform work, full stop. Outside that domain, Kotlin Multiplatform and TypeScript are stronger forward bets.

### Java — 3.45 — *Forward case is narrower than its historic position suggested.*

**The rise.** Virtual threads as a JVM-level concurrency primitive [java-006], structured concurrency in JEP 453 [java-015], records and sealed classes for closed-hierarchy pattern matching [java-002, java-003, java-004]. Modern Java is substantively better than the Java most teams remember.

**The fall.** The build-tool ecosystem splits between Maven and Gradle [java-011]. Pre-records boilerplate is recognized verbosity [java-013]. Preview features stabilize across multiple releases [java-016]. Kotlin sits inside Java's own ecosystem with stronger structural typing.

**The climb.** Right answer when the project is JVM-shaped and the team's hiring market is narrower than Kotlin's. Middle-tier — competent everywhere, dominant nowhere greenfield teams operate.

### Elixir — 3.40 — *Default for fault-tolerant distributed systems and real-time AI-augmented UIs.*

**The rise.** The BEAM process and concurrency model [elixir-001, elixir-004], OTP supervision trees as structured fault tolerance [elixir-002], Phoenix LiveView as a substrate for server-driven real-time interfaces [elixir-009, elixir-014]. Runtime properties not matched in the cohort.

**The fall.** Elixir is dynamically typed [elixir-005] with set-theoretic types still in research [elixir-016]. LiveView's server-driven rendering ties front-end lifecycle to a stateful socket [elixir-017].

**The climb.** Right answer when fault tolerance and soft-real-time interactivity are the defining properties. The verification gap is acceptable when OTP's runtime guarantees do the work the type system would have.

### C++ — 2.65 — *Default only for accelerator host code where the safety penalty is knowingly accepted.*

**The rise.** ISO standardization with three-yearly revisions [cpp-001], C++20 modules and ranges [cpp-002], and dominant accelerator toolchains — CUDA, ROCm/HIP, SYCL, oneAPI — all primarily targeting C++ [cpp-013].

**The fall.** Memory-safety pressure from MSRC, Chromium, NSA, ONCD, and Android telemetry [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008]. Undefined-behaviour exposure [cpp-011]. No canonical build system and uneven module adoption [cpp-015]. Strategic viability scores 2 for memory-safety reasons.

**The climb.** Right answer only when accelerator host code forces it. For everything else, the regulatory direction makes a different language the lower-risk bet.

## Recommendations by Use Case

The question is not "which language is best" but "which language is right for this project." Name the situation, the answer, and the trade-off you are accepting.

| Domain | Primary | Alternatives | The trade-off you are accepting |
|---|---|---|---|
| Greenfield application work | TypeScript | Kotlin, .NET (C#) | Operability and ecosystem breadth, in exchange for unsoundness [typescript-005, typescript-017] |
| Systems / infrastructure / security-sensitive | Rust | Go | Verification and safety [rust-001, rust-015], in exchange for compile-time and learning-curve cost [rust-020, rust-025] |
| Data / AI/ML / scripting | Python | TypeScript (data products) | ML ecosystem velocity [python-012] over verification gap [python-002] — typed-from-day-one is the price |
| Fault-tolerant distributed systems | Elixir | Go, Rust | BEAM runtime properties [elixir-001, elixir-002] over verification ceiling [elixir-005] |
| AI-native compute kernels | Rust | C++ (only where unavoidable) | Rust accelerator/ML ecosystem (wgpu, candle, burn) [rust-022] over C++ memory-safety exposure [cpp-004] |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] | Native platform integration [swift-003] in exchange for Apple-aligned governance [swift-011] |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) | Toolchain access [cpp-013], with memory-safety penalty knowingly accepted [cpp-006] |

For **greenfield application work** — web, mobile, internal tools — TypeScript wins on the broadest joint operability-and-verification profile; Kotlin and .NET are credible where the JVM or .NET runtime is operationally preferred. For **systems or infrastructure**, Rust pays operability cost for verification and safety gains aligned with the regulatory direction; Go is the alternative when deliberate minimalism is preferred over verification ceiling. For **data or ML**, Python's ecosystem velocity is forward-relevant — typed-from-day-one is non-negotiable. For **fault-tolerant distributed systems**, Elixir's BEAM properties aren't matched in this cohort. For **AI-native compute kernels**, Rust's accelerator/ML stack is the forward path; C++ only when accelerator host code forces it. For **Apple platforms**, Swift is the native default; Kotlin Multiplatform is the cross-platform alternative.

No single language is a default for everything. AI-era language choice is becoming more domain-sensitive, not less.

## Limitations

What this report can't tell you. The framework weights (HC 20%, MC 25%, AO 25%, RE 20%, SV 10%) are working assumptions, not the output of a calibrated multi-rater process. A reader could weight runtime/ecosystem higher (favouring Python and the JVM languages) or AI-agent operability higher (favouring Go and TypeScript). The matrix is robust to small weight perturbations, not to large ones. Read it as the output of *a* defensible weighting, not *the* weighting.

Snapshot date is **2026-04-30**. Elixir's set-theoretic type work [elixir-007, elixir-013] could move that language's verification score before its next major release. Python's typing PEP cadence [python-016] continues to land each release, and TypeScript's type-system additions ship on the same cadence as the JavaScript surface they layer over.

The greenfield framing is itself a deliberate choice. A team maintaining a million-line incumbent estate has a different question; legacy gravity reappears as an advantage there, and this matrix under-credits Java, Python, and C++ for that purpose. Bilingual-team and polyglot-portfolio questions are out of scope.

Scores are single-rater author judgments grounded in atomic claims with primary-source citations, not the average of an expert panel. Each cell traces Insight to Evaluation to Claim to Source. A reader who disagrees should follow the trail to the source, not treat the cell as authoritative.

## Reading and Reproducibility

The corpus is structured for traceability. **Framework** in `framework/` (criteria, weights, lenses, rubric); **Claims** in `claims/<language>.yaml` (191 atomic claims, each with a primary-source citation); **Sources** in `sources/<language>-sources.yaml` (136 entries); **Evaluations** in `evaluations/<language>.yaml`; **Comparisons** and **Insights** in their named directories. The matrix is reproducible via `scripts/score_summary.py`. Methodology: `outputs/evidence-backed-research-execution-plan.md`.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
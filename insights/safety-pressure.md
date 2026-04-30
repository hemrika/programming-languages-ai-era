# Safety Pressure

## Thesis

Memory safety has crossed from technical preference to regulatory and platform-owner selection criterion. As AI raises the volume of generated code, the cost of a memory-safety defect compounds, and four independent forces - government guidance, platform vendors, browser projects, and OS owners - have aligned on memory safety as a structural language property they actively select for. Languages with structural memory safety align with this pressure; languages without it face cumulative regulatory and ecosystem headwinds. This is falsifiable: if memory safety remained a technical preference rather than an institutional selection criterion, the cited guidance and telemetry would not all converge on the same recommendation against the same set of languages.

## Evidence

Four institutional pillars mark the crossing. Microsoft's Security Response Center reports that approximately 70 percent of the CVEs Microsoft assigns are memory-safety issues, across products written largely in C and C++ [cpp-004]. The Chromium project independently reports approximately 70 percent of high-severity security bugs are memory-safety bugs [cpp-005]. The U.S. National Security Agency's *Software Memory Safety* Cybersecurity Information Sheet recommends shifting from memory-unsafe languages and explicitly names C and C++ [cpp-006]. The U.S. Office of the National Cyber Director's 2024 *Back to the Building Blocks* report repeats the recommendation [cpp-007]. Google's Android security data shows memory-safety vulnerabilities declined as new native code shifted toward memory-safe languages including Rust [cpp-008, rust-016], with zero memory-safety vulnerabilities discovered in Android Rust code at the time of the Android 13 report [rust-017]. Four sources, four independent vantage points - regulator, platform owner, browser project, OS owner - converging on the same selection criterion.

Languages with structural memory safety align with this pressure. Rust's ownership system manages memory through compiler-checked rules without garbage collection or manual free [rust-001], with single-owner semantics [rust-002] and lifetime-checked references [rust-003]; the unsafe boundary is explicitly scoped [rust-011, rust-012] but does not undo the structural alignment. Kotlin runs on the JVM with its mandatory verifier [java-009], adding null-safety as a type-system guarantee [kotlin-001]. Swift specifies memory-safety rules including detection of conflicting access [swift-004]. Elixir's BEAM gives process isolation and explicit failure semantics [elixir-002, elixir-004]. Haskell's purity and type system give a strong default safety posture [haskell-001]. .NET runs on the CLI with Common Type System metadata [dotnet-002] and adds nullable reference types [dotnet-003]. The lens analysis in `comparisons/lens-analysis.md` puts Rust, Haskell, Kotlin, .NET, and Swift at the top of the safety-pressure tier and C++ alone at "exposed."

C++'s counter-claims [cpp-014, cpp-015, cpp-016] track that accelerator C++ dialects diverge from ISO C++, modules adoption is uneven, and the Core Guidelines are advisory and configuration-dependent. None of these undoes regulatory exposure: the NSA, ONCD, MSRC, Chromium, and Android signals are all about memory safety as a language property, not about whether a project follows the Core Guidelines. The forward production credit C++ retains for accelerator host code [cpp-013] coexists with the safety penalty rather than offsetting it.

Python's exposure differs in kind. The dynamically typed runtime [python-001, python-015] surfaces type errors only at execution time, and PEP 484 hints are not runtime-enforced [python-002, python-019]. This is runtime-error exposure, not memory-unsafety exposure - regulators have not focused on Python the way they have on C and C++ - but for AI-generated systems running at scale it is real.

## Counter-positions

The strongest counter is that type safety alone does not address all production-relevant safety risks. Supply-chain attacks, prompt injection, and model-output safety are AI-era concerns that memory-safe languages do not directly mitigate. A team building greenfield AI infrastructure faces these threats orthogonally to language choice. The counter is correct as a scope point but does not unwind the thesis: the four pillars cited above explicitly target memory safety, and the regulatory direction has continued to reinforce that focus rather than dilute it. Memory safety is one selection criterion among several; the point is that this criterion has crossed an institutional threshold the others have not.

## Implications

For greenfield AI-era language choice, memory safety is no longer optional in regulated domains. Greenfield C++ adoption faces compounding headwinds, particularly in defense, finance, and platform contexts where the cited guidance applies directly. Rust is structurally favored for systems work where C or C++ would historically have been the default. Per the matrix in `comparisons/overview.md`, C++ scores 2 on strategic viability and weighted 2.65 - same tier as Mojo but for memory-safety reasons rather than ecosystem-stage reasons. The portfolio note in `comparisons/lens-analysis.md` is explicit: greenfield C++ is a default only where accelerator host code is unavoidable, with the safety penalty knowingly accepted.

## Reading

- `comparisons/lens-analysis.md` - the safety pressure lens
- `comparisons/overview.md` - C++'s greenfield score and reasoning
- `claims/cpp.yaml`, `claims/rust.yaml` - regulatory and platform-owner sources

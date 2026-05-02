# Cross-Cutting Lens Analysis

The framework defines four cross-cutting lenses (`framework/evaluation-framework.md`). This document evaluates each language against each lens and reads across them to identify the strongest cross-lens profiles.

## 1. Verification advantage

Languages whose structure makes program properties machine-checkable.

| Tier | Languages |
|---|---|
| Strong | Rust |
| Moderate | Kotlin, TypeScript, .NET, Swift, Java, Go |
| Weak | Python, Elixir, C++ |

Pure verification ranking is led by Rust. Its mature ecosystem and operability give it the strategically dominant verification position; ownership and borrow-checking provide compile-time memory-safety guarantees that no other language in the cohort matches.

## 2. Agentic development advantage

Languages where AI agents can write, modify, test, and verify code with low friction.

| Tier | Languages |
|---|---|
| Strong | TypeScript, Go |
| Moderate | Python, Rust, .NET, Kotlin |
| Constrained | Java, Swift, Elixir |
| Difficult | C++ |

See `agent-friendly-languages.md` for the per-language reasoning.

## 3. Safety pressure

Where AI-generated change carries unusually high blast radius, languages that prevent or contain those errors are favored.

| Tier | Languages |
|---|---|
| Strong | Rust, Kotlin, .NET, Swift |
| Moderate | TypeScript, Go, Java, Elixir |
| Weak | Python |
| Exposed | C++ |

Safety pressure is increasingly policy-aware, not merely technical. The White House ONCD report (2024), Microsoft Security Response Center analyses (2019), Android security publications (2022), and Chromium memory-safety reports collectively mark memory safety as a structural property regulators and platform owners now actively select for. C++ is the most exposed mainstream language under this lens; Python's exposure is different in kind (runtime errors rather than memory unsafety) but real for production AI-generated systems.

## 4. Abstraction compression

Languages that allow expressing more behavior in fewer lines without compromising clarity.

| Tier | Languages |
|---|---|
| Strong | Kotlin, Elixir, TypeScript |
| Moderate | Rust, Swift, .NET, Python |
| Weak | Go, Java, C++ |

Compression is double-edged. Go's intentional weakness on this lens is part of its agent-friendliness story - there is less hidden behavior an agent must reconstruct from context. Kotlin's strength contributes to readability and abstraction quality but raises the implicit-context surface an AI agent must reconstruct.

## Reading across the lenses

The framework reads across four lenses (verification, agentic, safety, abstraction). The AI-era dimensions — AI-systems native, AI-systems ecosystem, structured-output native, structured-output ecosystem, and ecosystem dependency risk (added across v0.2, v0.3, and v0.4) — interact with all four lenses but do not warrant a fifth lens of their own; they function as cross-cutting *capability* axes (what the language plugs into for data, LLMs, agent frameworks, MCP, inference, streaming, observability; how mature the type/data layer between LLM output and program logic is; how durable the load-bearing dependencies are) rather than structural properties of the language itself. Read the AI-era dimensions as the axes that decide ranking *given* the four-lens profile.

No single language wins all four lenses. The strongest cross-lens profiles in this set:

- **Rust.** Strong on verification and safety; moderate on agentic and abstraction. Greenfield momentum in systems and infrastructure is the forward-looking signal. The Rust ML/accelerator ecosystem (wgpu, candle, burn) and Tokio's production-grade async runtime extend this position into AI-systems work.
- **TypeScript.** Strong on agentic; moderate on verification, safety, and abstraction. Modern typed-language credit comes from the gradual-typing layer, not the underlying JavaScript runtime. The `satisfies` operator and incremental Language Service semantic model reinforce the AI-tooling integration story.
- **Kotlin.** Strong on safety and abstraction; moderate on verification and agentic. JVM interop is incidental - the greenfield case rests on null-safety, sealed types, coroutines, and Flow, with Kotlin Multiplatform now stable across JVM/Android/iOS/JS/Native targets as a forward cross-platform bet.
- **Go.** Strong on agentic; moderate on safety; deliberately weak on abstraction. Convention-driven tooling (gofmt, gopls, the integrated go command) produces a uniquely low-friction agent profile for new services.

The strongest greenfield positions (verification + agentic + safety) cluster around Rust, TypeScript, and Kotlin.

## Where the lenses disagree

Two cases where the lenses pull in different directions are worth flagging:

- **Python.** Maximum ecosystem (forward-relevant in ML/data); weak verification; weak safety. The framework's central question for Python is whether AI-era pressure on verification erodes its position faster than the gradual-typing PEP cadence (PEP 484, 526, 544, 612, 646, 692, 695) and the typed-stub ecosystem (typeshed, pyright) rebuild it. The annual PEP 602 release cadence is a forward velocity signal in the same direction.
- **Rust.** Maximum verification and safety; only moderate agentic. Strong static structure pays operability cost in compile times and learning curve, but the verification and safety lenses align with regulatory direction in a way no other cohort language matches.

## A note on C++ under recalibrated greenfield framing

C++ presents the cleanest case for separating two distinct forward-looking properties from legacy gravity. The recalibrated runtime/ecosystem score (4) credits production-grade compiler toolchains (Clang, GCC, MSVC), ABI stability, OS and hardware integration, and the fact that the dominant accelerator stacks (CUDA, ROCm/HIP, SYCL, oneAPI) all primarily target C++ as their host language. These are forward ecosystem-viability properties a greenfield C++ project would inherit today - distinct from any legacy-installed-base credit. The strategic-viability score (2) reflects the safety pressure (NSA, ONCD, MSRC, Chromium, Android) that is the dominant active forward signal pushing new projects away. The two scores together produce a 2.70 weighted total under v0.2 - alone at the bottom of the matrix, exposed on safety while retaining production-toolchain credit. The new AI-systems interoperability dimension scores C++ at 3 (inference-runtime credit for llama.cpp, ONNX C++, CUDA/ROCm host) but the agent-framework absence prevents the score from rising above the integer-3 line.

## Implications for portfolio thinking

For a team selecting languages across a portfolio of AI-era greenfield projects, this lens analysis suggests:

- **Default for greenfield application work.** TypeScript or Kotlin - strong on agentic and abstraction with reasonable safety.
- **Default for systems, infrastructure, security-sensitive.** Rust - pays the operability cost for verification and safety gains, with a credible accelerator/ML path emerging.
- **Default for data, AI/ML, scripting.** Python - accepting the verification gap but leveraging ecosystem velocity in ML and the steady typing-PEP cadence.
- **Default for fault-tolerant distributed systems.** Elixir - operability cost accepted for runtime properties no other language matches; LiveView is a credible substrate for real-time AI-augmented UIs.
- **Default for accelerator host code where C++ is unavoidable.** C++ - explicitly accepting the safety penalty in exchange for the production toolchain and accelerator ecosystem.

No language is a default for *everything*. The framework's central output is that AI-era language choice becomes more domain-sensitive, not less.

## Corpus note

The claim corpus underlying this analysis has been expanded along five forward-driven axes that reflect the greenfield framing:

1. **AI-tooling integration.** Language servers, semantic-model APIs, and analyzer/code-fix infrastructures usable by editors and agents (TypeScript Language Service, Roslyn, JDT.LS, Kotlin LSP, pyright/Pylance + typeshed, rust-analyzer, gopls, sourcekit-lsp).
2. **Hardware-aware design.** Accelerator targeting and heterogeneous compilation (Rust wgpu/candle/burn, C++ CUDA/ROCm/SYCL/oneAPI).
3. **Concurrency model fit.** Language-level concurrency primitives suited to AI-era workloads (Java structured concurrency JEP 453, Go goroutines+channels, Phoenix LiveView/PubSub, Swift distributed actors, Kotlin Flow, Rust Tokio).
4. **Verification velocity.** The rate of formal-methods or static-analysis improvement (Python typing PEPs, TypeScript `satisfies`, Elixir set-theoretic types research).
5. **Ecosystem velocity.** Forward language-and-library evolution cadence (Java JEP cadence, Rust RFC + Project Goals, Python annual cadence per PEP 602, Kotlin Multiplatform momentum, .NET annual major releases, Elixir release cadence).

The AI-systems and structured-output dimensions are split into native (language-steward-shipped) and ecosystem (third-party / commercial) halves, and a separate dimension — `ecosystem_dependency_risk` — scores the backer-mix of load-bearing dependencies. The split is structural rather than cosmetic: a language's AI-era position is decomposed along (a) what the language steward ships (Microsoft Semantic Kernel for .NET, Apple Core ML / MLX for Swift, JetBrains kotlinx-serialization for Kotlin, Dashbit's Bumblebee/Nx for Elixir, encoding/json for Go, Codable for Swift) versus (b) what the surrounding ecosystem provides (Pydantic, Zod, Serde, Anthropic SDKs, OpenAI SDKs, LangChain ports, vector-store clients) and (c) how robust the backers of those ecosystem dependencies are. The `reachability_to_top_tier` dimension overlays a forward-trajectory plausibility score on each language's below-5 cells. None of these warrants a fifth lens — they remain capability axes inside the four-lens reading. Every claim that names a specific library carries a `backer:` field, and the weighting separates what the steward owns from what the community provides.

Per-claim detail lives in `claims/<language>.yaml`; per-source documentation lives in `sources/<language>-sources.yaml`.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
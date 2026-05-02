# Evaluation Framework

**Version: v0.4** (2026-05-02). v0.3 (2026-04-30) added structured-output maturity as a 7th dimension. v0.4 splits the two AI-era dimensions into native + ecosystem halves and introduces an ecosystem-dependency-risk dimension; total dimension count rises from 7 to 10.

## Objective

Evaluate programming languages for the AI era: a period where software is increasingly written, modified, reviewed, tested, and maintained by humans working with AI systems and autonomous agents.

## Framing

This research evaluates languages from a **greenfield** perspective. Installed base, existing code, and incumbent gravity are not scored as advantages. The question is: starting a new AI-era project today, what would you choose, and why? Languages are credited for forward-looking properties (governance quality, future fit, AI-training representation, ecosystem velocity) and not for owning a large amount of legacy code.

## Primary question

Which programming languages become more valuable when AI systems participate deeply in software development?

## Evaluation dimensions

| Dimension | Weight |
|---|---:|
| Human cognition (HC) | 15% |
| Machine cognition (MC) | 15% |
| AI-agent operability (AO) | 20% |
| Runtime and ecosystem (RE) | 10% |
| Strategic viability (SV) | 10% |
| AI-systems native (AIN) | 7.5% |
| AI-systems ecosystem (AIE) | 7.5% |
| Structured-output native (SON) | 5% |
| Structured-output ecosystem (SOE) | 5% |
| Ecosystem dependency risk (EDR) | 5% |

Combined AI-systems weight (15%) and combined structured-output weight (10%) are unchanged from v0.3. The new EDR dimension is funded by reducing Runtime and ecosystem from 15% to 10% — RE previously absorbed some ecosystem-resilience signal implicitly, and EDR now scores it explicitly.

## v0.4 changelog

**Why the split.** v0.3 conflated language-native capability with ecosystem-package capability and applied inclusion rules asymmetrically (Pydantic credited to Python's structured-output score, Newtonsoft.Json omitted from .NET's). It also did not capture dependency-risk: a 5.0 backed by Microsoft scored identical to a 5.0 backed by three OSS volunteers.

**What v0.4 changes.**

- `ai_systems_interoperability` (15%) is split into `ai_systems_native` (7.5%) and `ai_systems_ecosystem` (7.5%).
- `structured_output_maturity` (10%) is split into `structured_output_native` (5%) and `structured_output_ecosystem` (5%).
- A new `ecosystem_dependency_risk` (5%) dimension scores the backer-mix and resilience of load-bearing dependencies. Higher score = lower risk = better.
- The 5% for EDR is pulled from RE (15% → 10%).

**Native vs ecosystem rule.** Native = stewarded by the language team or first-party shipped (Microsoft for .NET; Apple for Swift; JetBrains for Kotlin; Dashbit/Plataformatec for Elixir; PSF for Python; Go team for Go; Rust Foundation for Rust; OpenJDK/Oracle for Java; ISO/major-vendor compilers for C++). Ecosystem = everything else, including Anthropic and OpenAI SDKs, LangChain/LangChain.js/LangChain4j, Pydantic, Zod, Vercel AI SDK, Serde, Jackson, Newtonsoft.Json, llama.cpp, nlohmann/json. Full rule and per-library calls are in `framework/dimensions.md`.

## Cross-cutting lenses

1. Verification advantage
2. Agentic development advantage
3. Safety pressure
4. Abstraction compression

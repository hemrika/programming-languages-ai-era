# Programming Languages in the AI Era — Deck Outline

*Source: outputs/report.md. Anchored in ~340 atomic claims across 10 languages. Framework v0.4.*

## Slide 1 — Title

Programming Languages in the AI Era — a greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development. Framework v0.4, snapshot 2026-05-02. Author: Rutger Hemrika.

## Slide 2 — The question

If you were starting a new project today, which language would you pick — and how would you defend that choice when AI agents are doing more of the writing? Installed base and incumbent gravity stop being load-bearing once a team commits to a greenfield codebase. The question this deck answers: which languages are forward-fit for AI-era development, on the evidence available now, with every claim traceable to a primary source.

## Slide 3 — Framing

Greenfield framing: no credit for legacy installed base, code volume, or incumbent gravity. **Ten** weighted dimensions — Human cognition (15%), Machine cognition (15%), AI-agent operability (20%), Runtime/ecosystem (10%), Strategic viability (10%), AI-systems native (7.5%), AI-systems ecosystem (7.5%), Structured-output native (5%), Structured-output ecosystem (5%), Ecosystem dependency risk (5%). Half-point scores 1.0–5.0. Four cross-cutting lenses: verification, agentic operability, safety pressure, abstraction compression. Forward properties credited; legacy code volume is not.

## Slide 4 — The matrix

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

AIN/AIE = AI-systems native (7.5%) and ecosystem (7.5%). SON/SOE = Structured-output native (5%) and ecosystem (5%). EDR = Ecosystem dependency risk (5%) — higher = lower risk. Three tiers: top (≥3.85) Go, TypeScript, .NET, Kotlin. Middle (3.40–3.84) Rust, Python, Swift. Lower (<3.40) Java, Elixir, C++.

## Slide 5 — Finding 1: Go takes the top slot

Go (4.04) leads the matrix on a HC=5 / AO=5 profile that carries at full weight (35% combined). TypeScript (4.01) sits 0.03 below in a near-tie: AIE=5.0 and SOE=5.0 are best-in-class on the ecosystem halves but AIN=1.5 / SON=2.5 cap the lift. Go ranks 0.30 above Python (3.74) on the strength of operability and human cognition combined with a stable EDR=3.5 anchored by Google language stewardship and commercial-first-party Anthropic and OpenAI Go SDKs.

## Slide 6 — Finding 2: Python's structural exposure

Python (3.74, #6) carries a bimodal AI-systems profile — strong ecosystem, weak native, dependency-risk-exposed. AIE=5.0 [python-021..025] and SOE=5.0 [python-026..029] are tier-leading on the ecosystem halves. AIN=1.5 (PSF ships no AI packages [python-036]), SON=2.5 (PEP 484 hints advisory at runtime [python-030]), and EDR=2.5 (Pydantic community-multi-maintainer [python-031], Instructor single-maintainer [python-032], Outlines small-commercial [python-033]) hold the weighted total below Go and TypeScript despite the tier-leading ecosystem halves.

## Slide 7 — Finding 3: Dependency-risk rewards Microsoft, JetBrains, OpenJDK stewardship

EDR=4.5 (.NET), 4.0 (Java), 4.0 (Kotlin) anchor the middle of the table. Microsoft funds the .NET runtime and the in-box AI surface as a single commercial-vendor strategy [dotnet-020, dotnet-022, dotnet-029]. OpenJDK's multi-vendor stewardship anchors the JVM [java-033]. JetBrains stewardship anchors Kotlin at language and serialization layers [kotlin-030]. Languages with single-maintainer load-bearing dependencies score lower — Python 2.5 [python-031, python-032], TypeScript 3.0 [typescript-029], C++ 3.0 [cpp-027, cpp-028]. The dependency-risk axis is the one most likely to move next.

## Slide 8 — Finding 4: AI-agent operability is the most discriminating dimension

Operability separates Go and TypeScript (AO=5) from C++ (AO=2). With AO at 20% weight, this axis alone contributes ±0.6 points to the ranking — larger than any AI-era dimension's individual contribution. The pattern tracks toolchain unification and LSP-exposed semantic models [go-003, go-015, typescript-006, typescript-007, dotnet-006, dotnet-014], not type-system depth.

## Slide 9 — Finding 5: Safety pressure and verification advantage hold

Memory-safety pressure has crossed from technical preference into regulatory criterion. Microsoft Security Response Center: ~70% of CVEs are memory-safety [cpp-004]. Chromium: ~70% of high-severity bugs [cpp-005]. NSA Software Memory Safety names C and C++ [cpp-006]. ONCD's Back to the Building Blocks repeats the recommendation [cpp-007]. Memory-safe languages (Rust [rust-001], Kotlin/JVM [kotlin-001], Swift [swift-004], Elixir/BEAM [elixir-002, elixir-004], .NET [dotnet-002, dotnet-003]) align with the pressure; C++ is alone in the exposed tier. AI raises the value of cheap verification — agents write more code than humans can read — and the structured-output-native dimension extends the verification surface to schema-validated boundaries between LLM output and program logic.

## Slide 10 — Top-tier verdicts

- **Go (4.04)** — default for backend services where deliberate minimalism is acceptable. Operability breadth [go-003, go-015]; AI-systems coverage with Anthropic [go-020], OpenAI [go-021], MCP [go-022] SDKs at AIE=3.5; SON=3.0 via encoding/json + struct tags. EDR=3.5 from Google language stewardship and commercial-first-party SDKs.
- **TypeScript (4.01)** — default for application work in the JavaScript-shaped world. Strict-mode discipline [typescript-004] plus AI-systems breadth: LangChain.js [typescript-021], official MCP TS SDK [typescript-022], Anthropic and OpenAI SDKs [typescript-019, typescript-020], Zod-led structured-output ergonomics [typescript-026, typescript-027]. AIE=5.0 and SOE=5.0 (best in cohort). EDR=3.0 — Zod single-maintainer concentration offset by Microsoft language stewardship.
- **.NET / C# (3.96)** — default for Microsoft-shop application and service work. Roslyn as public compiler-platform API [dotnet-006, dotnet-014]; AIN=4.0 with Semantic Kernel [dotnet-020], MCP C# SDK [dotnet-021], ONNX Runtime .NET [dotnet-022]; SON=4.0 via System.Text.Json + JsonSchemaExporter. **EDR=4.5 — highest in the cohort.**
- **Kotlin (3.85)** — default for JVM application work and increasingly cross-platform [kotlin-015]; MC=4.5 on null-safety + sealed types + when exhaustiveness [kotlin-001, kotlin-002, kotlin-003]; AIN=3.0 via JetBrains-shipped MCP Kotlin SDK [kotlin-021]. SON=3.5 via kotlinx-serialization (JetBrains). EDR=4.0 with JetBrains commercial-vendor anchoring.

## Slide 11 — Other notable verdicts

- **Rust (3.75)** — default for systems, infrastructure, security-sensitive work. Ownership rules [rust-001] plus regulatory alignment [rust-015, rust-016]; AIE=3.5 (MCP Rust SDK [rust-027], async-openai [rust-028], candle [rust-029]) trailing Python and TypeScript on agent-framework depth [rust-030]. SOE=4.0 via Serde + schemars. EDR=3.5 — Rust Foundation multi-vendor backing offset by Serde bus-factor.
- **Python (3.74)** — ranks #6. AIE=5.0 with Anthropic [python-021], OpenAI [python-022], LangChain [python-023], MCP [python-024], universal vector stores [python-025]; SOE=5.0 with Pydantic [python-026], Instructor [python-028], Outlines [python-029]. AIN=1.5 (PSF ships no AI packages [python-036]). EDR=2.5 — single-maintainer Instructor [python-032], small-commercial Outlines [python-033].
- **Swift (3.40)** — Apple-platform default. AIN=4.0 (Core ML, MLX, Foundation Models) [swift-019, swift-023]; AIE=2.0 (no first-party Anthropic/OpenAI Swift SDK [swift-021]). SON=3.5 via Codable. The native/ecosystem split credits Apple's first-party stack on the native half while recording the thin cross-platform ecosystem on the ecosystem half.
- **Java (3.38)** — virtual threads [java-006], structured concurrency JEP 453 [java-015], AIE=4.0 with LangChain4j [java-020] and Anthropic Java SDK [java-019]. EDR=4.0 with OpenJDK multi-vendor stewardship.
- **Elixir (3.13)** — BEAM concurrency and OTP supervision [elixir-001, elixir-002]; Phoenix LiveView [elixir-009]. AIN=3.0 via Bumblebee/Nx (Dashbit-stewarded) [elixir-019, elixir-020]. SOE=2.5 via Ecto + instructor_ex.
- **C++ (2.46)** — default only for accelerator host code. AIN=2.5 via CUDA/ROCm/SYCL [cpp-019]; AIE=3.0 via llama.cpp [cpp-017], ONNX C++ [cpp-018]. SON=1.0; safety pressure dominates [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008].

## Slide 12 — Recommendations by domain

| Domain | Primary | Alternatives |
|---|---|---|
| Greenfield application work | TypeScript or Go | Kotlin, .NET (C#) |
| AI-application work where vendor-anchored deps matter | .NET (Semantic Kernel) | Java |
| AI-application work where ecosystem breadth matters | TypeScript or Python | .NET |
| Backend services | Go | Rust, .NET |
| Systems / infrastructure / security-sensitive | Rust | Go |
| Data / AI/ML / AI-systems integration | Python (typed, day-one) | TypeScript |
| Fault-tolerant distributed systems | Elixir | Go, Rust |
| AI-native compute kernels | Rust | C++ only where unavoidable |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) |
| JVM application work needing AI integration | Java (LangChain4j, Anthropic Java SDK) | Kotlin |

No single language is a default for everything. AI-era language choice becomes more domain-sensitive, not less. Most organizations will run two or three of these in parallel; the polyglot interaction surface is part of the work.

## Slide 13 — Limitations and closing

**Limitations.** Framework weights are working assumptions. Snapshot date 2026-05-02 — EDR is the most volatile axis (commercial vendors increasingly ship first-party SDKs that displace single-maintainer projects). Greenfield framing is a deliberate choice; maintenance-estate teams should re-weight. Single-rater judgment grounded in primary-source citations.

**Closing thesis.** AI raises the price of cheap verification, ergonomic agentic operability, structural safety, structured-output ergonomics, and resilient dependency anchoring. The languages that pay all five taxes win the next decade — and the framework shows that the leaders on the resilient-dependency axis (Go, .NET, Kotlin, Java) overlap only partly with the leaders on the ecosystem-ergonomics axis (TypeScript, Python, .NET). The greenfield default is no longer a single language; it is a portfolio.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
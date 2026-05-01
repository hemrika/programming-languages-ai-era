# Programming Languages in the AI Era — Deck Outline

*Source: outputs/report.md. Anchored in 290+ atomic claims across 10 languages. Framework v0.3.*

## Slide 1 — Title

Programming Languages in the AI Era — a greenfield evaluation of 10 languages against the demands of AI-assisted and AI-agentic software development. Framework v0.3, snapshot 2026-04-30. Author: Rutger Hemrika.

## Slide 2 — The question

If you were starting a new project today, which language would you pick — and how would you defend that choice when AI agents are doing more of the writing? Installed base and incumbent gravity stop being load-bearing once a team commits to a greenfield codebase. The question this deck answers: which languages are forward-fit for AI-era development, on the evidence available now, with every claim traceable to a primary source.

## Slide 3 — Framing

Greenfield framing: no credit for legacy installed base, code volume, or incumbent gravity. Seven weighted dimensions — Human cognition (15%), Machine cognition (15%), AI-agent operability (20%), Runtime/ecosystem (15%), Strategic viability (10%), AI-systems interoperability (15%), Structured-output maturity (10%). Half-point scores 1.0–5.0 in 0.5 increments. Four cross-cutting lenses: verification, agentic operability, safety pressure, abstraction compression. Forward properties credited: governance, future fit, AI-training representation, ecosystem velocity, ecosystem viability, AI-systems integration depth, and the type/data layer between LLM output and program logic. Legacy code volume is not.

## Slide 4 — The matrix

| Language    | HC  | MC  | AO  | RE  | SV  | AI  | SO  | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---: |---:|
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 4.5 | 5.0 | 4.38 |
| Python      | 4   | 3   | 4   | 5   | 4   | 5.0 | 5.0 | 4.25 |
| Go          | 5   | 4   | 5   | 4.5 | 4   | 3.5 | 3.0 | 4.17 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4.0 | 4.0 | 4.00 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 3.0 | 3.5 | 3.90 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3.0 | 3.5 | 3.88 |
| Java        | 3   | 4   | 3   | 4.5 | 3   | 3.5 | 3.5 | 3.50 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 2.5 | 2.5 | 3.25 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 2.0 | 2.5 | 3.25 |
| C++         | 2   | 3   | 2   | 4   | 2   | 3.0 | 2.0 | 2.60 |

AI = AI-systems interoperability (15%). SO = Structured-output maturity (10%) — the v0.3 seventh dimension covering schema-validated parsing, LLM tool-call typing, constrained generation, and structured-output libraries. Three tiers: top (≥4.0) TypeScript, Python, Go, .NET. Middle (3.0–3.99) Rust, Kotlin, Java, Elixir, Swift. Lower (<3.0) C++. The lead reflects joint operability + AI-systems integration breadth + structured-output ergonomics.

## Slide 5 — The Python/Go swap (v0.3 narrative beat)

Under v0.3, Python (4.25) overtakes Go (4.17) by 0.08 points. Mechanically, the lift comes from the new structured-output dimension: Python scores SO=5.0 (Pydantic + Instructor + native OpenAI Pydantic response_format), while Go scores SO=3.0 (encoding/json + struct tags is type-safe, but the validation ecosystem is fragmented and the LLM-specific structured-output ergonomics layer is thinner). At a 10% weight, the 2-point gap on SO contributes +0.20 to Python's weighted total. Python also leads on AI-systems interop (5.0 vs Go's 3.5) which adds another +0.225 at 15% weight. Go's structural toolchain story has not changed — Go's operability lead remains real — but the dimensions that matter for AI-application work have shifted toward Python and TypeScript.

## Slide 6 — Finding 1: AI-agent operability is most discriminating

Among the structural axes, operability separates the matrix more sharply than any other. Go and TypeScript score 5; C++ scores 2. The pattern tracks **toolchain unification and LSP-exposed semantic models**, not type-system depth. Go ships a single canonical command for build/test/format/vet/deps/docs [go-003], a canonical formatter [go-002], MVS dependency resolution [go-004], and gopls as official LSP [go-015]. TypeScript reaches the same surface from a dynamic substrate via strict-mode [typescript-004], discriminated unions [typescript-002], and the language service Microsoft itself originated [typescript-006, typescript-007]. .NET ships Roslyn as a public compiler-platform API [dotnet-006, dotnet-014]. C++ lacks a single canonical build surface [cpp-015].

## Slide 7 — Finding 2: AI raises the value of cheap verification

Agents write more code than humans can read; the bottleneck shifts from generation to validation. Languages whose compilers can falsify a candidate change without execution gain proportional value. Strongest verification clusters: Rust ownership rules [rust-001, rust-002, rust-003] with exhaustive `match` [rust-006]; Kotlin nullables and sealed `when` [kotlin-001, kotlin-002, kotlin-003]; .NET nullable-reference-type flow analysis [dotnet-003, dotnet-004]; Swift optionals and access rules [swift-001, swift-004]. Verification velocity is also visible: TypeScript `satisfies` [typescript-016], Python typing-PEP cadence [python-016, python-004], Elixir set-theoretic types [elixir-007]. The structured-output dimension introduces a third verification axis — schema-validated boundaries between LLM output and program logic — where Python (Pydantic) and TypeScript (Zod) lead.

## Slide 8 — Finding 3: Safety pressure has crossed into regulatory territory

Four independent institutions now treat memory safety as a structural language property they actively select for. Microsoft Security Response Center: ~70% of Microsoft-assigned CVEs are memory-safety issues [cpp-004]. Chromium: ~70% of high-severity bugs are memory-safety bugs [cpp-005]. NSA *Software Memory Safety* names C and C++ [cpp-006]. ONCD's 2024 *Back to the Building Blocks* repeats the recommendation [cpp-007]. Android telemetry shows memory-safety vulnerabilities declining as new native code shifted to memory-safe languages including Rust [cpp-008, rust-016, rust-017]. Memory-safe languages (Rust [rust-001], Kotlin/JVM [kotlin-001], Swift [swift-004], Elixir/BEAM [elixir-002, elixir-004], .NET [dotnet-002, dotnet-003]) align with the pressure; C++ is alone in the exposed tier.

## Slide 9 — Finding 4: Incumbent gravity does not insulate

Greenfield framing is the lever that exposes this. C++ retains forward credit for accelerator host code [cpp-013] and ISO standardization [cpp-001] but loses ground because safety pressure dominates strategic viability. Java retains forward credit for virtual threads [java-006], structured concurrency JEP 453 [java-015], and Maven Central [java-010] — but the legacy adoption premium is gone, and Kotlin's null-safety [kotlin-001] and sealed types [kotlin-002] now sit inside Java's own ecosystem. Python keeps RE=5 because ML-domain library velocity is forward-relevant [python-012] and typing PEP cadence is a verification-velocity signal [python-016, python-018] — and the v0.3 structured-output dimension lifts Python from boundary to top-tier for AI-application work specifically.

## Slide 10 — Finding 5: Structured-output maturity is the new AI-app dimension

The AI-application boundary — the type/data layer between LLM output and program logic — is itself a verification surface, and it is dominated by Python (Pydantic, Instructor, Outlines) and TypeScript (Zod, ArkType, Vercel AI SDK). Both score SO=5.0. .NET reaches 4.0 with System.Text.Json + Semantic Kernel function calling. Rust and Kotlin score 3.5 (Serde+schemars; kotlinx-serialization). Go scores 3.0; Swift and Elixir 2.5; C++ 2.0. Why this matters: every LLM-driven application validates structured outputs at the boundary on every call, and the language ecosystem's investment in this layer is now load-bearing for AI-application velocity.

## Slide 11 — Top-tier verdicts

- **TypeScript (4.38)** — default for application work in the JavaScript-shaped world. Strict-mode discipline [typescript-004] plus AI-systems breadth: LangChain.js [typescript-021], official MCP TS SDK [typescript-022], Anthropic and OpenAI SDKs [typescript-019, typescript-020], Zod-led structured-output ergonomics [typescript-026, typescript-027]. Cleanest cross-dimension winner.
- **Python (4.25)** — default for data, AI/ML, and AI-application work. AI-systems score 5 with Anthropic [python-021], OpenAI [python-022], LangChain [python-023], MCP [python-024], universal vector stores [python-025]; structured-output 5 with Pydantic [python-026], Instructor [python-027], Outlines [python-028], OpenAI native Pydantic [python-029]. Risk: type hints not enforced at runtime [python-002].
- **Go (4.25)** — default for backend services where deliberate minimalism is acceptable. Wins on operability breadth [go-003, go-015]; AI-systems coverage at 3.5 with Anthropic [go-020], OpenAI [go-021], MCP [go-022] SDKs but thinner agent-framework depth [go-024]. Structured-output trails at 3.0. Risk: type-system minimalism is real [go-017, go-018].
- **.NET / C# (4.00)** — default for Microsoft-shop application and service work. Roslyn as public compiler-platform API [dotnet-006, dotnet-014]; AI-systems via Semantic Kernel [dotnet-020], MCP C# SDK [dotnet-021], ONNX Runtime .NET [dotnet-022]; structured-output via System.Text.Json + records.

## Slide 12 — Other notable verdicts

- **Rust (3.90)** — default for systems, infrastructure, security-sensitive work. Ownership rules [rust-001] plus regulatory alignment [rust-015, rust-016]; AI-systems at 3 (MCP Rust SDK [rust-027], async-openai [rust-028], candle [rust-029]) trailing Python and TypeScript on agent-framework depth [rust-030]. Structured-output at 3.5 via Serde + schemars.
- **Kotlin (3.88)** — default for JVM application work and increasingly cross-platform [kotlin-015]; v0.2 lifts MC to 4.5 on null-safety + sealed types + when exhaustiveness [kotlin-001, kotlin-002, kotlin-003]; AI-systems at 3 via JVM interop and the official MCP Kotlin SDK [kotlin-021]. Structured-output at 3.5 via kotlinx-serialization. Risk: JetBrains governance dependence [kotlin-009].
- **Elixir (3.25)** — default for fault-tolerant distributed systems. BEAM concurrency and OTP supervision [elixir-001, elixir-002]; Phoenix LiveView [elixir-009] for real-time AI-augmented UIs; runtime/ecosystem rescored to 4.5 in v0.2. Structured-output at 2.5 via Ecto + instructor_ex.
- **C++ (2.60)** — default only for accelerator host code where the safety penalty is knowingly accepted [cpp-013, cpp-019]. ISO standardization [cpp-001] and modules/ranges [cpp-002] retained; AI-systems credit 3 via llama.cpp [cpp-017], ONNX C++ [cpp-018], CUDA/ROCm/SYCL host [cpp-019]. Structured-output at 2.0. The dominant signal pushing new projects away is safety pressure [cpp-004, cpp-005, cpp-006, cpp-007, cpp-008].

## Slide 13 — Recommendations by domain

| Domain | Primary | Alternatives |
|---|---|---|
| Greenfield application work | TypeScript | Kotlin, .NET (C#) |
| AI-application work (LLM-calling, agent frameworks) | TypeScript or Python | .NET (Semantic Kernel) |
| Backend services | Go | Rust, .NET |
| Systems / infrastructure / security-sensitive | Rust | Go |
| Data / AI/ML / AI-systems integration | Python (typed, day-one) | TypeScript for data products |
| Fault-tolerant distributed systems | Elixir | Go, Rust |
| AI-native compute kernels | Rust | C++ only where unavoidable |
| Apple-platform application work | Swift | Kotlin Multiplatform [kotlin-015] |
| Accelerator host code where C++ is forced | C++ | Rust (where accelerator support exists) |
| JVM application work needing AI integration | Java (LangChain4j, Anthropic Java SDK) | Kotlin |

No single language is a default for everything. AI-era language choice becomes more domain-sensitive, not less. Most organizations will run two or three of these in parallel; the polyglot interaction surface
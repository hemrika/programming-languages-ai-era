# Programming Languages in the AI Era: A Greenfield Reset

*Why incumbent gravity stops being the right answer once AI is doing more of the writing — and what to use instead.*

By Rutger Hemrika · 2026-05-02

## The question senior engineering leaders have to defend

If you were starting a new project today, which language would you pick — and how would you defend that choice when AI agents are doing more of the writing?

Most teams reach for the language they already run in production. I think that gets the question wrong. Rank ten languages on eleven weighted dimensions under a deliberate greenfield framing — no installed-base credit, no incumbent gravity — and the result that surprises senior readers is this: TypeScript and Go tie at the top at 4.01, the joint cohort ceiling on weighted total, but the cohort's strongest forward bet is .NET, sitting 0.02 behind at 3.99 today and carrying the cohort's highest dependency-risk resilience score (4.5, no other language reaches it) plus the cohort's highest reachability score (4.5, also alone). Almost no one is positioning it that way. I am, and the rest of this piece is the case I would make to a CTO who pushes back.

## Why a greenfield reset

Greenfield framing is a deliberate constraint, not naivety. Installed-base reasoning answers a different question — how to maintain what already exists — and rewards a different set of properties: legacy gravity, training-data familiarity, the cost of porting. Senior leaders who let those properties drive new-project decisions end up extending an estate they would not start today.

Greenfield framing brackets the maintenance question and asks the strategic one: starting a new AI-era project today, which forward-looking properties do you want underneath the AI agents that will write more of the code than your humans do? The dimensions that matter are governance quality, future fit, AI-training-corpus representation, ecosystem velocity, and the resilience of load-bearing dependencies. The dimensions that do not are the volume of code already written and the inertia of the incumbent.

Critics will read this and say I am ignoring legacy reality. I am not — I am bracketing it. Maintenance estates need different math, and I say so explicitly: teams whose primary task is *maintaining* large incumbent estates should re-weight, and legacy gravity reappears as an advantage in that question. This is not that question.

If installed base alone were sufficient to carry forward strategic viability, removing legacy credit would not have moved any incumbent's score. It moved several.

## The eleven dimensions

I score ten languages — C++, .NET, Elixir, Go, Java, Kotlin, Python, Rust, Swift, TypeScript — on eleven weighted dimensions, each on a 1.0–5.0 scale in 0.5 increments. The dimensions group cleanly:

- **Cognition.** Human Cognition (15%) — readability and governance — and Machine Cognition (15%) — how cleanly compilers, analyzers, and AI systems can reason about the code.
- **Agentic.** AI-Agent Operability (20%) — how cleanly an AI coding agent can navigate, edit, test, and verify the code. The single largest-weighted dimension.
- **Runtime.** Runtime and Ecosystem (10%) and Strategic Viability (5%). Can it run production systems, and will it remain relevant.
- **AI-systems.** AI-Systems Native (7.5%) — what the language steward ships first-party — and AI-Systems Ecosystem (7.5%) — what third parties ship.
- **Structured-output.** Structured-Output Native (5%) and Structured-Output Ecosystem (5%). Schema-validated parsing and types-to-schema generation, again split into steward and ecosystem halves.
- **Risk.** Ecosystem Dependency Risk (5%) — the resilience of load-bearing libraries' maintainership, where higher means lower risk — and Reachability to Top Tier (5%) — the forward-trajectory plausibility of closing each below-5 cell within a 3–5-year horizon.

The native/ecosystem split is the methodological choice that does the most work. A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three open-source volunteers. The dependency-risk axis records the present-state difference; the reachability axis records the forward-trajectory difference.

## The matrix and the ranking

| Language    | HC  | MC  | AO  | RE  | SV  | AIN | AIE | SON | SOE | EDR | RCH | Weighted |
|---          |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---: |---:|
| TypeScript  | 4   | 4   | 5   | 4   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 3.0 | 4.0 | 4.01 |
| Go          | 5   | 4   | 5   | 4   | 4   | 2.0 | 3.5 | 3.0 | 3.0 | 3.5 | 3.5 | 4.01 |
| .NET (C#)   | 4   | 4   | 4   | 4   | 4   | 4.0 | 3.5 | 4.0 | 3.5 | 4.5 | 4.5 | 3.99 |
| Kotlin      | 4   | 4.5 | 4   | 4   | 4   | 3.0 | 3.0 | 3.5 | 3.0 | 4.0 | 4.0 | 3.85 |
| Python      | 4   | 3   | 4   | 5   | 4   | 1.5 | 5.0 | 2.5 | 5.0 | 2.5 | 3.5 | 3.71 |
| Rust        | 3   | 5   | 4   | 4   | 5   | 1.5 | 4.0 | 2.0 | 4.0 | 3.5 | 3.5 | 3.71 |
| Java        | 3   | 4   | 3.5 | 4.5 | 3   | 2.0 | 4.0 | 3.0 | 3.5 | 4.0 | 3.5 | 3.50 |
| Swift       | 4   | 4   | 3   | 4   | 3   | 4.0 | 2.0 | 4.0 | 2.0 | 3.5 | 3.0 | 3.42 |
| Elixir      | 4   | 3   | 3   | 4.5 | 3   | 3.0 | 2.0 | 1.5 | 2.5 | 3.0 | 2.5 | 3.10 |
| C++         | 2   | 3   | 2   | 4   | 2   | 2.5 | 3.0 | 1.0 | 2.0 | 3.0 | 2.0 | 2.46 |

Three things to read at the strategic level. The top is dense — TypeScript and Go tied at the cohort ceiling of 4.01, .NET 0.02 behind at 3.99, Kotlin 0.16 behind at 3.85, four languages packed inside a 0.16 band. The middle is stratified — Python and Rust tied at 3.71 (0.30 behind the leaders, fifth-and-sixth in the cohort), Java alone at 3.50, Swift alone at 3.42, each separated from its neighbours by 0.08–0.21. The bottom is alone — Elixir at 3.10 and C++ at 2.46, the only two languages under 3.42 and the only two under 3.10 respectively, with a 0.64-point gap between them that no other neighbour pair in the matrix matches. The compression at the top is the more interesting strategic fact: the leader is a three-way bet, not a winner.

## Three findings that matter at the strategic level

### Finding A — The top is a three-way bet, not a single winner

Go, TypeScript, and .NET sit within 0.02 of each other on weighted total — three languages inside a 0.02 band, with the next-closest neighbour (Kotlin at 3.85) sitting 0.14 further down. They are not the same bet, and treating them as interchangeable is the most expensive mistake in the cohort.

Go is the bet on backend services. Its strongest single score is on Human Cognition — how easy code is for a human to read and govern at scale — where it earns HC=5, alone at the cohort ceiling, with six other languages tied a step down at 4 from a deliberately small surface area. It also reaches the cohort ceiling on AI-Agent Operability — how cleanly an AI coding agent can navigate, edit, test, and verify the code — at AO=5, on the strength of `go build`, `go test`, `go vet`, and `go mod` as a single canonical command surface, gofmt as the single canonical formatter, and gopls as the official Language Server Protocol implementation. AO=5 is shared only with TypeScript; no other language reaches the AI-agent-operability ceiling. The agent loop closes faster on Go than on any other language in the cohort. Most of the Cloud Native Computing Foundation's load-bearing infrastructure — etcd, containerd, Helm, Prometheus, Kubernetes itself — is written in Go. If the next five years are about backend systems written and modified by agents at scale, Go is the platform bet that pays.

TypeScript is the bet on AI-application work. It hits the cohort ceiling on AI-Systems Ecosystem — what third parties ship for AI integration — at AIE=5.0, shared only with Python; no other language reaches it, and the next-highest is Java and Rust tied at 4.0. The libraries underneath are Anthropic's official TypeScript SDK, the OpenAI Node SDK, LangChain.js, the official MCP TypeScript SDK with Anthropic co-stewardship, and a TypeScript LlamaIndex distribution. It also ties Python at the cohort ceiling on Structured-Output Ecosystem — what third parties ship for parsing LLM output — at SOE=5.0; the next-highest is Rust at 4.0. The libraries underneath are Zod as the de facto schema-validation standard, the Vercel AI SDK with `generateObject` and `streamObject`, and `zod-to-json-schema` feeding tool-call definitions. TypeScript and Python are the only two languages in the cohort that hit the ceiling on both ecosystem halves; no other language reaches either ceiling. If the next five years are dominated by AI-augmented application surfaces — chat interfaces, agent orchestration, structured-output pipelines — TypeScript is the platform bet that pays.

.NET is the bet on forward trajectory. It hits the cohort ceiling on AI-Systems Native — what the language steward ships first-party — at AIN=4.0, on the strength of Microsoft Semantic Kernel, Microsoft.Extensions.AI (which landed in the .NET 9 distribution), ONNX Runtime .NET, and the MCP C# SDK with Microsoft co-maintenance alongside Anthropic. AIN=4.0 is shared only with Swift; no other language reaches it, and the next-highest is Kotlin and Elixir at 3.0. It also takes the cohort's highest score on Ecosystem Dependency Risk at EDR=4.5, alone at the ceiling; the next-highest is Java and Kotlin tied at 4.0. Nearly the entire load-bearing AI surface — runtime, language, AI primitives, structured-output surface, MCP — is Microsoft-first-party. It also takes the cohort's highest score on Reachability to Top Tier at Reach=4.5, also alone at the ceiling; the next-highest is TypeScript and Kotlin tied at 4.0. Microsoft is investing across every below-5 cell with annual major release cadence. .NET is the only language in the cohort that takes both crowns — EDR ceiling and Reach ceiling — and no other language carries either. If the next five years rewards stewardship concentration and vendor-anchored supply chains, .NET is the platform bet that pays.

The CTO framing is direct: if you bet wrong on which workload dominates, you bet wrong on the language. The reasonable response is not to pick one and pretend the others do not exist. It is to know which workload your platform actually carries, and to choose accordingly.

This finding is wrong if a fourth workload class — accelerator-bound or fault-tolerant — turns out to dominate. In that case Rust or Elixir reorders the question. The matrix exposes the bet; it does not pretend to remove it.

### Finding B — Dependency risk is real and almost no one is pricing it

Pydantic has more power over Python's AI position than Microsoft has over .NET's. That is not a metaphor. It is a structural fact, and most teams are not pricing it.

Python's Structured-Output Ecosystem score is 5.0 — the cohort ceiling, tied with TypeScript and unmatched by any other language. The score rests on Pydantic, Instructor, and Outlines. Pydantic is maintained by a small group of active contributors — none employed full-time on the project, none backed by a commercial vendor; the Rust core (`pydantic-core` via PyO3) is itself a multi-language supply-chain artifact resting on the same small group. Instructor is single-maintainer (Jason Liu). Outlines is small-commercial. The composite Ecosystem Dependency Risk score for Python is 2.5 — alone at the cohort floor on EDR. No other language sits below 3.0; the next-lowest are TypeScript, Elixir, and C++ tied at 3.0.

The contrast with .NET is the point. .NET's Structured-Output Native is 4.0 (cohort ceiling, tied only with Swift) from System.Text.Json with source generators and JsonSchemaExporter — all Microsoft-stewarded. .NET's AI-Systems Native is 4.0 (also cohort ceiling, tied only with Swift) from Semantic Kernel, Microsoft.Extensions.AI, and ONNX Runtime .NET — all Microsoft-stewarded. EDR=4.5, alone at the cohort ceiling. If a single Pydantic maintainer steps away tomorrow, Python's AI-application story has a problem. If a single Microsoft engineer steps away tomorrow, .NET's AI-application story does not.

The same lens applies further down the matrix. TypeScript's EDR=3.0 sits in the lower third of the cohort (only Python's 2.5 is lower) and is held back by Zod's single-maintainer concentration — Colin McDonnell carries the load, and Microsoft's stewardship of TypeScript does not extend to Zod. C++'s EDR=3.0 — tied with TypeScript and Elixir at the second-lowest tier — mixes commercial-first-party CUDA and ONNX Runtime backing with single-maintainer concentration on llama.cpp (Georgi Gerganov) and nlohmann/json (Niels Lohmann). Single-maintainer load-bearing libraries sit one bus-factor event from being a strategic problem.

Senior teams already think this way about cloud-vendor concentration — multi-region, multi-account, exit-cost analysis. The same lens applies to library stewardship, and almost no team applies it. The strongest objection is "but our team can fork it." That objection is where most architecture decision records stop, and it is wrong by the time the fork has to absorb a CVE response, an upstream API drift, and a frontier-model SDK change in the same week.

This finding is wrong if community-multi-maintainer turns out to be more resilient than single-vendor stewardship under stress. The empirical case for that is thin. If Pydantic gains three additional active maintainers by 2027-05-02, Python's EDR moves up and the thesis tightens around the libraries that did not.

### Finding C — Reachability separates "where it is" from "where it's going"

A current-state ranking is a snapshot. The Reachability dimension scores forward-trajectory plausibility — how reachable is 5.0 on each below-5 cell within a 3–5-year horizon. For 5-year platform bets, reachability matters more than this-year ranking.

.NET ranks #3 today on weighted total but alone at #1 on Reach at 4.5 — the cohort ceiling, with no other language reaching it. Microsoft is investing across nearly every below-5 cell in the .NET row, with annual major release cadence supporting the trajectory. The forward bet is the strongest in the cohort even though the present-state weighted total trails the leaders by only 0.02.

C++ ranks #10 today on weighted total and alone at #10 on Reach at 2.0 — the lowest forward-trajectory score I assign to any language, with the next-lowest (Elixir at 2.5) sitting half a point above. Memory-safety pressure compounds against C++ from four institutions converging on the same conclusion. The U.S. National Security Agency's *Software Memory Safety* Cybersecurity Information Sheet recommends shifting from memory-unsafe languages and explicitly names C and C++. The U.S. Office of the National Cyber Director's *Back to the Building Blocks* report repeats the recommendation at the executive-branch policy level. Microsoft's Security Response Center reports that approximately 70% of Microsoft-assigned CVEs are memory-safety issues. The Chromium project independently reports approximately 70% of high-severity security bugs are memory-safety bugs — different codebase, different team, same number. Android telemetry shows memory-safety vulnerabilities decline as new native code shifts to memory-safe languages. Most of C++'s below-5 cells are structural to language design and will not close inside the planning horizon.

The other end of the matrix shows the same logic. TypeScript and Kotlin both score Reach=4.0 — tied for second-highest behind .NET, vendor-stewarded, with closing paths visible. Elixir scores Reach=2.5 — set-theoretic types remain in research, the ecosystem footprint is small, the gap-size is wide; only C++ sits lower. Reachability is the dimension that punishes hand-waving forward-trajectory claims and rewards specificity.

This finding is wrong if a non-vendor-stewarded language ships a structural step-change — a Python type system that becomes runtime-enforced, a Rust first-party AI runtime — that the Reach scoring did not anticipate. The probability is non-zero. I commit a number anyway, because a forward-trajectory claim that refuses to commit is not a claim.

## Three predictions I am willing to be graded on in 12 months

I am writing eight falsifiable predictions, each date-stamped, each with a measurable check, each tied to a framework score. Three carry the most signal for senior readers:

1. **Pydantic gains at least three active maintainers by 2027-05-02 — or Python's EDR drops toward 2.0 in the next major framework revision.** The check is GitHub maintainer-activity stats for `pydantic/pydantic`: six-month merged-PR count by maintainer.

2. **Microsoft ships a first-party Anthropic SDK for .NET by 2027-11-02, lifting .NET's AIN by at least 0.5.** The check is a repository under `microsoft/` or `Anthropic/` with a .NET S
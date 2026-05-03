# Programming Languages in the AI Era: A Greenfield Reset

*Why incumbent gravity stops being the right answer once AI is doing more of the writing — and what to use instead.*

By Rutger Hemrika · 2026-05-02

## The question senior engineering leaders have to defend

If you were starting a new project today, which language would you pick — and how would you defend that choice when AI agents are doing more of the writing?

Most teams reach for the language they already run in production. The framework I built to interrogate that instinct says they are getting the question wrong. Rank ten languages on eleven weighted dimensions under a deliberate greenfield framing — no installed-base credit, no incumbent gravity — and the result that surprises senior readers is this: TypeScript and Go tie at the top at 4.01, the joint cohort ceiling on weighted total, but the cohort's strongest forward bet is .NET, sitting 0.02 behind at 3.99 today and carrying the cohort's highest dependency-risk score (4.5, no other language reaches it) plus the cohort's highest reachability score (4.5, also alone). Almost no one is positioning it that way.

The rest of this piece is the framework you can use to make and defend that bet.

## Why a greenfield reset

Greenfield framing is a deliberate constraint, not naivety. Installed-base reasoning answers a different question — how to maintain what already exists — and rewards a different set of properties: legacy gravity, training-data familiarity, the cost of porting. Senior leaders who let those properties drive new-project decisions end up extending an estate they would not start today.

Greenfield framing brackets the maintenance question and asks the strategic one: starting a new AI-era project today, which forward-looking properties do you want underneath the AI agents that will write more of the code than your humans do? The dimensions that matter are governance quality, future fit, AI-training-corpus representation, ecosystem velocity, and the resilience of load-bearing dependencies. The dimensions that do not are the volume of code already written and the inertia of the incumbent.

Critics will read this and say I am ignoring legacy reality. I am not — I am bracketing it. Maintenance estates need different math, and the framework explicitly says so: teams whose primary task is *maintaining* large incumbent estates should re-weight, and legacy gravity reappears as an advantage in that question. This is not that question.

If installed base alone were sufficient to carry forward strategic viability, removing legacy credit from the framework would not have moved any incumbent's score. It moved several.

## The eleven dimensions

The framework scores ten languages — C++, .NET, Elixir, Go, Java, Kotlin, Python, Rust, Swift, TypeScript — on eleven weighted dimensions, each on a 1.0–5.0 scale in 0.5 increments. The dimensions group cleanly:

- **Cognition.** Human cognition (15%) and machine cognition (15%). Can humans understand and govern the code, and can compilers, analyzers, and AI systems reason about it.
- **Agentic.** AI-agent operability (20%). Can agents safely modify and verify it. The single largest-weighted dimension in the framework.
- **Runtime.** Runtime and ecosystem (10%) and strategic viability (5%). Can it run production systems, and will it remain relevant.
- **AI-systems.** AI-systems native (7.5%) and AI-systems ecosystem (7.5%). What the language steward ships first-party for AI, separated from what third parties ship.
- **Structured-output.** Structured-output native (5%) and structured-output ecosystem (5%). Schema-validated parsing and types-to-schema generation, again split into steward and ecosystem halves.
- **Risk.** Ecosystem dependency risk (5%) and reachability to top tier (5%). The backer-mix and resilience of load-bearing dependencies, and the forward-trajectory plausibility of closing each below-5 cell within a 3–5-year horizon.

The native/ecosystem split is the methodological choice that does the most work. A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers. The dependency-risk axis records the present-state difference; the reachability axis records the forward-trajectory difference. The repository at `github.com/hemrika/programming-languages-ai-era` ships the full rubric, the per-cell rationale, and the source claims.

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

Go, TypeScript, and .NET sit within 0.02 of each other on weighted total — three languages inside a 0.02 band, with the next-closest neighbour (Kotlin at 3.85) sitting 0.14 further down. They are not the same bet.

Go is the bet on backend services. HC=5 — Go is the only language in the cohort to reach the human-cognition ceiling, with a deliberately small surface area; six other languages cluster a step down at 4. AO=5 from a single canonical command, gofmt as the single canonical formatter, and gopls as the official Language Server Protocol implementation. AO=5 is shared only with TypeScript; no other language in the cohort reaches the AI-agent-operability ceiling. The agent loop closes faster on Go than on any other language in the cohort. If the next five years are about backend systems written and modified by agents at scale, Go is the platform bet that pays.

TypeScript is the bet on AI-application work. AIE=5.0 — TypeScript hits the cohort ceiling on AI-systems ecosystem, shared only with Python; no other language reaches it, and the next-highest is Java and Rust tied at 4.0. The libraries underneath are Anthropic's official SDK, OpenAI's official SDK, LangChain.js, the official MCP TypeScript SDK, and LlamaIndex. SOE=5.0 ties Python at the structured-output-ecosystem ceiling, again the only two languages to reach it; the next-highest is Rust at 4.0. The libraries underneath are Zod, Vercel AI SDK structured outputs, and zod-to-json-schema. TypeScript and Python are the only two languages in the cohort that hit the ceiling on both ecosystem halves; no other language reaches the ceiling on either. If the next five years are dominated by AI-augmented application surfaces — chat interfaces, agent orchestration, structured-output pipelines — TypeScript is the platform bet that pays.

.NET is the bet on forward trajectory. AIN=4.0 from Microsoft Semantic Kernel, Microsoft.Extensions.AI, ONNX Runtime .NET, and the MCP C# SDK with Microsoft co-maintenance. AIN=4.0 is the cohort ceiling, shared only with Swift; no other language reaches it, and the next-highest is Kotlin and Elixir at 3.0. EDR=4.5 is alone at the cohort ceiling on dependency risk — no other language reaches 4.5, and the next-highest is Java and Kotlin tied at 4.0. Nearly the entire load-bearing AI surface is Microsoft-first-party. Reach=4.5 is also alone at the cohort ceiling on reachability — no other language reaches 4.5, and the next-highest is TypeScript and Kotlin tied at 4.0. Microsoft is investing across every below-5 cell with annual major release cadence. .NET is the only language in the cohort that takes both crowns — EDR ceiling and Reach ceiling — and no other language carries either. If the next five years rewards stewardship concentration and vendor-anchored supply chains, .NET is the platform bet that pays.

The CTO framing is direct: if you bet wrong on which workload dominates, you bet wrong on the language. The reasonable response is not to pick one and pretend the others do not exist. It is to know which workload your platform actually carries, and to choose accordingly.

This finding is wrong if a fourth workload class — accelerator-bound or fault-tolerant — turns out to dominate. In that case Rust or Elixir reorders the question. The matrix exposes the bet; it does not pretend to remove it.

### Finding B — Dependency risk is real and almost no one is pricing it

Pydantic has more power over Python's AI position than Microsoft has over .NET's. That is not a metaphor. It is a structural fact the matrix makes visible.

Python's structured-output-ecosystem score is 5.0 — the cohort ceiling, tied with TypeScript and unmatched by any other language. The score rests on Pydantic, Instructor, and Outlines. Pydantic carries community-multi-maintainer governance — better than single-maintainer, worse than commercial-vendor-backed. Instructor is single-maintainer (Jason Liu). Outlines is small-commercial. The composite ecosystem-dependency-risk score for Python is 2.5 — alone at the cohort floor on EDR. No other language sits below 3.0; the next-lowest are TypeScript, Elixir, and C++ tied at 3.0.

The contrast with .NET is the point. .NET's structured-output-native is 4.0 (cohort ceiling, tied only with Swift) from System.Text.Json with source generators and JsonSchemaExporter — all Microsoft-stewarded. .NET's AI-systems-native is 4.0 (also cohort ceiling, tied only with Swift) from Semantic Kernel, Microsoft.Extensions.AI, and ONNX Runtime .NET — all Microsoft-stewarded. EDR=4.5, alone at the cohort ceiling. If a single Pydantic maintainer steps away tomorrow, Python's AI-application story has a problem. If a single Microsoft engineer steps away tomorrow, .NET's AI-application story does not.

The same lens applies further down the matrix. TypeScript's EDR=3.0 sits in the lower third of the cohort (only Python's 2.5 is lower) and is held back by Zod's single-maintainer concentration. C++'s EDR=3.0 — tied with TypeScript and Elixir at the second-lowest tier — mixes commercial-first-party CUDA and ONNX backing with single-maintainer concentration on llama.cpp and nlohmann/json. Single-maintainer load-bearing libraries sit one bus-factor event from being a strategic problem.

Senior teams already think this way about cloud-vendor concentration — multi-region, multi-account, exit-cost analysis. The same lens applies to library stewardship, and almost no team applies it. The framework forces the question onto the page.

This finding is wrong if community-multi-maintainer turns out to be more resilient than single-vendor stewardship under stress. The empirical case for that is thin. If Pydantic gains three additional active maintainers by 2027-05-02, Python's EDR moves up and the thesis tightens around the libraries that did not.

### Finding C — Reachability separates "where it is" from "where it's going"

A current-state ranking is a snapshot. The reachability dimension scores forward-trajectory plausibility — how reachable is 5.0 on each below-5 cell within a 3–5-year horizon. For 5-year platform bets, reachability matters more than this-year ranking.

.NET ranks #3 today on weighted total but alone at #1 on Reach at 4.5 — the cohort ceiling, with no other language reaching it. Microsoft is investing across nearly every below-5 cell in the .NET row, with annual major release cadence supporting the trajectory. The forward bet is the strongest in the cohort even though the present-state weighted total trails the leaders by only 0.02.

C++ ranks #10 today on weighted total and alone at #10 on Reach at 2.0 — the lowest forward-trajectory score the framework assigns to any language, with the next-lowest (Elixir at 2.5) sitting half a point above. Memory-safety pressure compounds — the NSA's *Software Memory Safety* recommendation, the ONCD's *Back to the Building Blocks* report, MSRC reporting roughly 70% of CVEs are memory-safety issues, Chromium reporting the same 70% figure for high-severity bugs, Android telemetry showing memory-safety vulnerabilities decline as new native code shifts toward memory-safe languages. Most of C++'s below-5 cells are structural to the language design and will not close inside the planning horizon.

The other end of the matrix shows the same logic. TypeScript and Kotlin both score Reach=4.0 — tied for second-highest behind .NET, vendor-stewarded, with closing paths visible. Elixir scores Reach=2.5 — set-theoretic types remain in research, the ecosystem footprint is small, the gap-size is wide; only C++ sits lower. Reachability is the dimension that punishes hand-waving forward-trajectory claims and rewards specificity.

This finding is wrong if a non-vendor-stewarded language ships a structural step-change — a Python type system that becomes runtime-enforced, a Rust first-party AI runtime — that the framework's reachability scoring did not anticipate. The probability is non-zero. The framework commits a number anyway, because a forward-trajectory claim that refuses to commit is not a claim.

## Three predictions I am willing to be graded on in 12 months

The public repository ships eight falsifiable predictions, each date-stamped, each with a measurable check, each tied to a framework score. Three carry the most signal for senior readers:

1. **Pydantic gains at least three active maintainers by 2027-05-02 — or Python's EDR drops toward 2.0 in the next major framework revision.** The check is GitHub maintainer-activity stats for `pydantic/pydantic`: six-month merged-PR-count by maintainer.

2. **Microsoft ships a first-party Anthropic SDK for .NET by 2027-11-02, lifting .NET's AIN by at least 0.5.** The check is a GitHub repository under `microsoft/` or `Anthropic/` with .NET SDK label and Microsoft engineering attribution.

3. **C++ greenfield share in security-sensitive domains continues to decline year-over-year through 2027-05-02.** The check is the named industry surveys — CNCF, JetBrains, RedMonk, GitHub Octoverse — restricted to greenfield-project signal where the survey breaks it out.

The grading happens in public. The v1.1 review checkpoint is **2027-05-02**, with each prediction marked resolved (yes / no / partial). If a prediction lands counter to the fram
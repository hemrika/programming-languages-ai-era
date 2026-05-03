# Don't Pick a Language for Where It Is. Pick It for Where It's Going.

*The Reachability dimension separates current-state ranking from forward-trajectory plausibility. For a 5-year platform bet, trajectory matters more than this-year score.*

By Rutger Hemrika · 2026-05-02

## Two CTOs read the same matrix

Two CTOs read the same matrix and reach different conclusions. The one who only reads the present-state ranking picks differently from the one who reads Reach.

The matrix puts TypeScript and Go tied at the top at 4.01 — the joint cohort ceiling on weighted total — with .NET behind at 3.99, only 0.02 off the lead. The CTO reading the weighted total alone picks TypeScript or Go and treats .NET as a near-miss. The CTO reading Reach picks differently — .NET sits at 4.5 on the trajectory cell, alone at the cohort ceiling on Reach (no other language reaches 4.5), with TypeScript and Kotlin tied for second-highest at 4.0 (half a point behind), and the rest of the cohort at 3.5 or lower. For a five-year platform bet, the trajectory cell is the load-bearing one. The framework records both, separately, and refuses to fold them into one number, because they answer different questions: Reach answers "where is this language going inside the planning horizon," and the weighted total answers "where is it today."

The decision implication is direct. A snapshot is a snapshot. A forward bet needs a forward-trajectory dimension, and the framework's Reachability axis is the form that takes.

## What Reach scores

Reach is a 1.0–5.0 score per language, computed against a five-input rubric. The inputs are explicit and the rubric is on the record.

- **Gap size.** How many cells in the row sit below 5.0, and how big is the aggregate gap. A row with all 4.0s sits closer to top tier than a row with mixed 5.0s and 1.5s.
- **In-motion signals.** Concrete evidence that closing paths are funded and shipping. Microsoft.Extensions.AI release cadence in the .NET row. Project Loom and Project Panama JEP progression in the Java row. Set-theoretic-types research in the Elixir row. Each signal has a named claim ID in the public repo.
- **Steward investment.** What the language steward funds, on what cadence, with what budget. .NET 9 LTS plus annual major releases plus a public roadmap signals Microsoft investment at scale. PSF working-group structure not including AI signals the inverse for Python.
- **Structural versus ecosystem.** Cells that close through language-design changes are slower than cells that close through community or commercial-third-party investment. Rust's compile-time gap is structural to the borrow-check model. TypeScript's soundness gap is a deliberate non-goal. C++'s memory-safety gap is structural to the language. Each is rated for closeability.
- **Compounding pressure.** Whether the closing path is moving with the trend or against it. Memory safety compounds against C++. AI-systems ecosystem investment compounds for TypeScript and Python. Apple-platform lock compounds against Swift cross-platform Reach.

The five inputs combine into a single 1.0–5.0 score per row. The output looks like a number; the rubric underneath is per-cell, with named in-motion signals and named structural blockers in `outputs/reachability-analysis.md`. This is the dimension that punishes hand-waving forward-trajectory claims. "Rust is the future" without a per-cell closing path scores low. "Microsoft ships Microsoft.Extensions.AI on a per-release cadence and the AIN gap is closing 0.5 per major version" scores high.

## The high-Reach cluster

Three languages anchor the high end of the Reach axis: .NET alone at 4.5 (the cohort ceiling, with no other language reaching it), TypeScript and Kotlin tied at 4.0 (the next-highest tier, half a point behind .NET). The next-closest language sits at 3.5. Each is in motion in a different shape.

.NET sits alone at 4.5 — the cohort ceiling on Reach — because Microsoft is investing across nearly every below-5 cell in the .NET row. Microsoft.Extensions.AI ships per-release. Semantic Kernel ships per-release. ONNX Runtime .NET ships per-release. The MCP C# SDK ships with Microsoft co-maintenance. JsonSchemaExporter shipped in the .NET 9 distribution. The C# language design committee is moving on pattern matching, primary constructors, collection expressions, and the discriminated-unions proposal. The aggregate gap-size is small (most cells at 4.0, gap size 1.0 or less per cell), the in-motion signals are all funded by the same steward, and the trajectory is unambiguously up.

TypeScript sits at 4.0 — tied with Kotlin for second-highest on Reach, half a point behind .NET — because Microsoft stewards the language at a predictable cadence (`satisfies`, const type parameters, Language Service refinements per release) and Vercel plus Anthropic plus OpenAI invest in the AI ecosystem at commercial-vendor velocity. The trajectory is up on the language-service axis, capped on soundness — TypeScript's type system is intentionally not sound, and that is a deliberate design choice that will not change in any planned release. AIE=5.0 and SOE=5.0 are already at the cohort ceiling, shared only with Python, so the bet on continued Microsoft + commercial-vendor investment is favorable; AIN=1.5 is the weakest cell — tied at the cohort floor with Python and Rust — and the closing path there is structurally absent.

Kotlin sits at 4.0 — tied with TypeScript for second-highest on Reach — because JetBrains stewards Kotlin as a commercial product with sustained KEEP cadence, Kotlin Multiplatform is stable across iOS/JS/Native targets, and the language-design layer is already at top-tier (MC=4.5, second-highest in the cohort behind Rust's solo MC=5, with sealed types and null safety). The trajectory is up on language-design, mixed on AI / structured-output ecosystems where most JVM AI work uses Java's LangChain4j with Kotlin wrappers rather than Kotlin-first AI tooling.

This is wrong if a steward-shipped step-change closes the gap on a non-clustered language — Apple opening MLX cross-platform, Google sponsoring an AI-Go-SDK initiative, the PSF reversing on first-party AI modules. None of those signals are present in 2026.

## The low-Reach cluster

C++ sits at Reach=2.0 — alone at the cohort floor on Reach, the lowest forward-trajectory score the framework assigns to any language; Elixir's 2.5 is the next-lowest, half a point above — because the safety-pressure axis compounds against the language rather than for it. The NSA, ONCD, MSRC, and Chromium signals are all moving in the direction that lowers C++ Reach, not raises it. Most below-5 cells (HC=2 alone at the cohort floor, AO=2 alone at the cohort floor, SON=1.0 alone at the cohort floor, AIN=2.5) are structural to the language design and will not close inside the planning horizon. P2996 reflection would lift SON if it lands, but SON moving from 1.0 to 3.0 still leaves C++ below the .NET / Swift cohort ceiling at 4.0 and outside top tier on the row total. ISO three-yearly revisions trail vendor-stewarded competitors' cadence.

Elixir sits at Reach=2.5 — second-lowest on Reach, half a point above C++; only these two languages sit below 3.0 on Reach, meaning the framework reads only these two as having gaps it does not expect to close in the 3–5-year horizon — because set-theoretic types are in research (in motion but timeline uncertain), the ecosystem footprint is small relative to AIE / SOE closing paths, and Dashbit's stewardship capacity is meaningfully smaller than Microsoft's or Apple's. Bumblebee and Nx are credible AIN signals but capacity-bounded.

Swift sits at Reach=3.0 — alone at the third-from-bottom tier, half a point below the four-language Go / Rust / Python / Java tier at 3.5 — because Apple invests in Apple-platform AI surface (Core ML, MLX, Foundation Models) but not in cross-platform AI ecosystem development. The trajectory is up on Apple-platform AI, flat on cross-platform AI / structured-output. AIN=4.0 already on Apple platforms — the cohort ceiling, tied with .NET. AIE=2.0 stuck — tied with Elixir at the second-lowest tier, with C++ at 3.0 actually higher — because no one outside Apple is investing in cross-platform Swift AI tooling at meaningful velocity.

This is wrong if a steward-shipped step-change closes the gap on one of these rows. Apple opens MLX cross-platform with first-party Anthropic Swift SDK. The set-theoretic-types Elixir work ships a stable spec inside the planning horizon. A new compiler ships memory-safety-as-default for C++ that gains adoption. The framework's prediction set in the public repo names each of these as a falsifiable form of the Reach call.

## Reading a per-language Reach call

Walk the .NET case in detail to make the rubric concrete. The .NET row has below-5 cells at HC=4 (gap 1.0), MC=4 (gap 1.0), AO=4 (gap 1.0), RE=4 (gap 1.0), SV=4 (gap 1.0), AIN=4.0 (gap 1.0), AIE=3.5 (gap 1.5), SON=4.0 (gap 1.0), SOE=3.5 (gap 1.5).

Aggregate gap-size: 9.5 points across 9 cells, average 1.06 per cell. Concentrated, small. In-motion signals: Microsoft.Extensions.AI, Semantic Kernel, ONNX Runtime .NET, MCP C# SDK, JsonSchemaExporter, the C# language design pipeline. Six named signals, all single-steward, all with public release cadence. Steward investment: annual major release cadence, .NET 9 LTS in production, .NET 10 on roadmap. Structural versus ecosystem: most cells close through Microsoft-stewarded language-version cadence and first-party SDK shipping; the weakest cell (SOE=3.5) is the community-half cell that requires non-Microsoft investment. Compounding pressure: net positive — Microsoft's AI Foundry commitment compounds AIN, AIE, and SON together.

Score: 4.5 — alone at the cohort ceiling on Reach. What would falsify the call: Microsoft missing a major release, Microsoft.Extensions.AI maintenance moving outside Microsoft, the discriminated-unions C# proposal stalling, Microsoft's AI investment shifting away from .NET as a host. None signaled in 2026. The repo's `outputs/reachability-analysis.md` walks the same analysis for every language in the cohort.

## The strategic read

For a 5-year platform bet, Reach matters more than this-year ranking. The two pieces of information answer different questions, and the framework records both rather than blending them.

.NET (#3 on weighted total at 3.99, alone at the cohort ceiling on Reach=4.5) is a different bet than Rust (tied at #5/6 with Python at 3.71, Reach=3.5 in the four-language tier with Go, Java, and Python). Both are credible. Both are forward-looking. The matrix says they are not the same forward bet — Rust's verification-advantage cells already sit at top-tier (MC=5 alone, SV=5 alone), with the AI-systems-native cell structurally absent (AIN=1.5, tied at the cohort floor; Reach contribution: bounded), while .NET's below-5 cells are concentrated, small, and in-motion under one funded steward (Reach contribution: high). The framework makes the difference legible.

The pragmatic recommendation for senior teams running a languag
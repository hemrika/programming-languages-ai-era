# Agent-Friendly Languages

## Working thesis

Agent-friendly languages provide fast feedback, clear diagnostics, deterministic tooling, simple project structures, and strong test workflows. The AI-agent operability dimension explicitly captures these properties. This document expands the operability axis into a per-language ranking and reasoning.

The five operability sub-properties used here:

1. **Fast feedback.** Type-check, compile, and test loops are short enough that an agent can iterate without hitting compute or context budgets.
2. **Deterministic tooling.** Builds, formatters, linters, and package managers behave predictably across machines and CI.
3. **Clear diagnostics.** Errors point at causes, not symptoms. Agents can act on a single message rather than triangulating.
4. **Shallow project structure.** A new agent session can orient with a small number of files and conventional layouts.
5. **Strong test workflows.** Test discovery, execution, and isolation are built in or near-built-in.

## Ranking

### Strong (operability score 5)

- **Go.** Deterministic tooling (`go build`, `go test`, `gofmt`) is a unique combination of speed, predictability, and zero-configuration defaults. Errors are blunt but actionable. Standard library covers most needs without third-party dependency negotiation. Agent failure modes are dominated by genuine logic mistakes, not toolchain friction.
- **TypeScript.** The strongest operability story among dynamic-origin languages: incremental compilation, language-server diagnostics, and a vast tested ecosystem. The cost is configuration variance (tsconfig, bundlers, monorepo tools) that can slow agent orientation in unfamiliar repos. Where conventions are followed (Vite, Next.js, Bun, Deno defaults), the agent experience is excellent.

### Moderate (operability score 4)

- **Python.** Fast feedback and broad ecosystem. Operability is held back by environment fragmentation (pip vs poetry vs uv vs conda), implicit runtime errors that delay failure, and uneven type-stub coverage. Modern toolchains (uv, ruff, pyright) are converging to make this much better; the per-repo variance remains the dominant operability cost.
- **Rust.** Excellent diagnostics (the compiler is famously instructive), strong tooling (`cargo`), good test framework. Held back by compile times and the cognitive cost of borrow-checker errors, which can defeat agents that lack the structural mental model. Score 4 reflects that operability is high *given* the agent has a reasonable Rust prior; the compile-time cost is real for tight iteration loops.
- **.NET (C#).** Mature tooling (`dotnet` CLI), strong language-server, well-defined project structure. Operability cost is solution/project sprawl in older codebases and the historical complexity of MSBuild. Modern .NET (6+) projects are agent-friendly out of the box.
- **Kotlin.** JVM toolchain (Gradle, Maven) is the operability ceiling. Where Gradle is used idiomatically, the experience is good. Where build scripts have accumulated complexity, agents struggle. Language itself is well-suited to agent reasoning.

### Constrained (operability score 3)

- **Java.** Strong language-server tooling, but project layout (multi-module Maven/Gradle) and verbosity slow agent iteration. Test workflows are excellent. The constraint is volume: more code per equivalent task means more context consumed.
- **Swift.** Apple-platform toolchain is closed and slow on iteration. SwiftPM is improving but lags Cargo and npm in convention. Cross-platform Swift is plausible but ecosystem is thin. Agents do well on small Swift projects, less well on Xcode-centric ones.
- **Zig.** Deliberately small surface area, fast compiler, clear errors. Held back by ecosystem thinness and language flux (pre-1.0). The score reflects current state, not the destination. May rise to 4 post-1.0.
- **Elixir.** Phoenix and Mix provide a coherent project shape. Operability is held back by the runtime model (BEAM) requiring agent reasoning patterns that differ from sequential languages, and by the smaller ecosystem of agent-tested patterns.

### Difficult (operability score 2)

- **C++.** The hardest mainstream language for agent operation. Build systems are fragmented (CMake, Bazel, Make, Meson), compile errors from templates are pathological, and the language has too many ways to express the same construct. Agents can succeed in well-disciplined codebases, but the median codebase is operability-hostile.
- **Haskell.** Excellent type errors, but slow feedback (compile times, GHC initialization), high cognitive load, and Cabal/Stack/Nix fragmentation. Agents without a strong Haskell prior produce code that type-checks but is idiomatically wrong. Operability is structurally low even as the language is structurally strong.
- **Mojo.** Early-stage tooling, limited package ecosystem, and a moving language definition. Operability score reflects current state and is expected to rise as the language stabilizes - but the rise is not yet evidenced.
- **Julia.** Excellent for interactive scientific work but operability for autonomous agents is limited by JIT compilation latency, package ecosystem fragility, and a culture of notebook-first development that does not translate to agent workflows.

## Cross-cutting observations

**Operability is partly cultural.** Go and TypeScript benefit not only from language properties but from communities that have converged on conventions. Java and C++ have technically capable tooling that is undermined by per-codebase variance. The lesson: an agent-friendly language without an agent-friendly community is only half the story.

**Compile time is an operability cost, not just a developer-experience one.** Rust and Haskell pay this cost continuously. The cost compounds across agent iterations and is a real reason their operability scores trail their structural quality.

**Fast feedback beats strong structure for agent iteration.** This is the central tension between this lens and the verification lens. Languages that are structurally weaker (Go) but iterate faster outperform structurally stronger languages (Haskell) on operability. The framework treats both as legitimate paths, weighted equally at 25% in the overall score.

**Modern dynamic languages can be agent-friendly.** TypeScript and modern Python (with uv, ruff, pyright) demonstrate that the dynamic-static distinction matters less for operability than tooling investment and convention.

## What this implies for greenfield language choice

If AI-agent operability is the dominant constraint:

- Default to **Go** for backend services where its structural weaknesses (limited abstraction, deliberate type-system minimalism) are acceptable.
- Default to **TypeScript** for application work where its ecosystem fits.
- Choose **Rust** when verification or safety pressure outweighs the operability cost.
- Avoid **C++ greenfield** unless hardware or performance constraints force it; the safety pressure documented in `lens-analysis.md` reinforces this.
- Treat **Mojo, Julia, Zig** as forward bets requiring active risk management until ecosystems mature.

See `lens-analysis.md` for how operability interacts with the other three lenses, and `overview.md` for how it weighs in the overall scoring.

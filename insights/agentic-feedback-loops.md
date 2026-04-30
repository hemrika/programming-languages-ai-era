# Agentic Feedback Loops

## Thesis

AI-agent operability is governed by structural properties of the language and its toolchain - fast feedback, deterministic tooling, a single canonical project workflow, and a semantic model exposed via the Language Server Protocol - more than by the underlying type system's expressive ceiling. Languages whose toolchains expose this stack to agents score 4-5 on AI-agent operability; languages whose toolchains require assembly out of fragmented parts score 2-3, regardless of their verification merits. This is falsifiable: if an expressive type system were the dominant operability driver, Haskell would not sit two tiers below TypeScript on agent operability.

## Evidence

The clearest pattern across the corpus is that operability tracks toolchain unification, not type-system depth. Go has a single canonical command - `go build`, `go test`, `go vet`, `go mod` - covering the full agent loop [go-003], a single canonical formatter [go-002], minimum-version-selection dependency resolution that makes builds reproducible without a lockfile dance [go-004], pkg.go.dev as a versioned documentation index [go-012], and gopls as the official, focused LSP server [go-015]. These properties combine to produce a uniquely low-friction agent profile. TypeScript shows the same pattern from a different starting point: an opt-in strict mode [typescript-004] over a structural type system [typescript-003] with discriminated unions for exhaustive narrowing [typescript-002], a Microsoft-maintained language service [typescript-006], and the Language Server Protocol that Microsoft itself originated alongside the TypeScript tooling [typescript-007]. Both languages score 5 on AI-agent operability.

The same pattern recurs in the middle tier. .NET ships Roslyn as a public compiler-platform API exposing the live SemanticModel to analyzers, code fixes, and source generators [dotnet-006, dotnet-014], with a unified `dotnet` CLI for build/test/run/package [dotnet-010]. Rust ships rust-analyzer as the official LSP server with inlay hints and a deep semantic model [rust-021] and Cargo as the single canonical workflow tool. Kotlin has both the community kotlin-language-server and JetBrains' own LSP implementation exposing the Kotlin semantic model [kotlin-016], with Gradle incremental compilation reducing edit-to-feedback latency [kotlin-011]. Java's Eclipse JDT.LS underlies VS Code Java tooling and other editors [java-014]. Swift's sourcekit-lsp exposes the SourceKit semantic model over LSP for Swift, C, and C++ [swift-014]. Python reaches the same surface through pyright, Pylance, and bundled typeshed stubs that narrow the gap between dynamic library APIs and statically checkable code [python-018]. Mojo's roadmap foregrounds the same direction: compile-time parameters and ownership conventions designed to support static-analysis tooling [mojo-014], offset by its small training-corpus footprint as a new language [mojo-012].

The languages that score 2-3 on operability tell the inverse story. Haskell has HLS as an official LSP server [haskell-014], but a fragmented build-tool surface (Cabal versus Stack) [haskell-006, haskell-007] and a large optional-extensions surface that complicates a single canonical dialect [haskell-004]. C++ has cppreference [cpp-012] but no canonical build system; modules adoption is uneven across compilers and build tools [cpp-015]. Julia historically suffered time-to-first-execution latency from JIT [julia-011], with native code caching [julia-004] only partly closing the gap. Rust's own compile times remain a recognized friction point on large workspaces [rust-025], dragging operability below verification.

## Counter-positions

The strongest counter is that gradual typing closes much of the dynamic-language gap without requiring a fully static type system: TypeScript's structural typing layered over JavaScript [typescript-001], Python's sustained typing-PEP cadence [python-016] and PEP 484 hints [python-003], and Pydantic's runtime validation [python-008] all give agents enough signal to operate effectively. The counter holds for the bridge between dynamic and gradually-typed languages, but does not invalidate the thesis: gradual typing matters because it feeds the same LSP/analyzer pipeline that drives operability in static languages. The point is the toolchain plumbing, not where the types originate.

## Implications

For greenfield AI-era language choice, AI-agent operability deserves to be weighted alongside verification rather than subordinated to it. The matrix in `comparisons/overview.md` reflects this: Go (5) and TypeScript (5) lead AI-agent operability while Haskell (2) and C++ (2) trail despite Haskell's verification ceiling. Default agentic-development picks should privilege languages with unified toolchains and first-class LSP servers; teams that need verification should accept the operability cost knowingly.

## Reading

- `comparisons/agent-friendly-languages.md` - per-language operability deep dive
- `framework/dimensions.md` - AI-agent operability criteria
- `claims/go.yaml`, `claims/typescript.yaml`, `claims/rust.yaml`, `claims/haskell.yaml` - source claims

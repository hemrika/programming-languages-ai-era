# Source Registry Index

The research corpus uses per-language YAML source registries instead of a single reading list. Each file resolves the `<lang>-src-NNN` IDs cited from `claims/<lang>.yaml`.

## Per-language registries

- [C++](cpp-sources.yaml) — 12 entries
- [.NET / C#](dotnet-sources.yaml) — 12 entries
- [Elixir](elixir-sources.yaml) — 12 entries
- [Go](go-sources.yaml) — 12 entries
- [Haskell](haskell-sources.yaml) — 11 entries
- [Java](java-sources.yaml) — 13 entries
- [Julia](julia-sources.yaml) — 11 entries
- [Kotlin](kotlin-sources.yaml) — 14 entries
- [Mojo](mojo-sources.yaml) — 12 entries
- [Python](python-sources.yaml) — 15 entries
- [Rust](rust-sources.yaml) — 18 entries
- [Swift](swift-sources.yaml) — 13 entries
- [TypeScript](typescript-sources.yaml) — 15 entries
- [Zig](zig-sources.yaml) — 11 entries

## Cross-language bibliography

`sources.bib` — BibTeX bibliography with 37 entries used in cross-cutting comparison docs and insights.

## Source types

The registries use these `type:` values:

- `official_documentation` — primary maintainer-published reference material (language reference, runtime docs).
- `official_tooling_documentation` — vendor/maintainer documentation for language toolchains (compilers, build tools, package managers, LSPs).
- `official_reference` — canonical API or library references hosted by the language's primary organization.
- `official_governance_documentation` — language steering, evolution-process, or governance-body publications.
- `government_guidance` — public-sector advisories and recommendations (e.g., NSA Software Memory Safety, ONCD reports).
- `industry_case_study` — production case studies and post-mortems from named organizations (Microsoft Security Response Center, Chromium, Android telemetry).
- `developer_survey` — large-N developer surveys with public methodology (Stack Overflow, JetBrains).
- `language_specification` — formal language specifications (ISO/ECMA standards, language reference grammars).
- `academic_paper` — peer-reviewed research papers cited as primary sources for language-design or verification claims.

## Methodology

Source discovery and triage is documented in `outputs/evidence-backed-research-execution-plan.md`. Every claim in `claims/*.yaml` cites exactly one source; if multiple sources support an assertion, it is split into multiple atomic claims.

## Total

- 255 atomic claims across 14 languages
- 181 source registry entries across 14 files
- 139 counter-claim links resolving Insight → Evaluation → Claim → Source

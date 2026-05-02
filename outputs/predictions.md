# Predictions — Framework v0.6

The framework's value beyond v1.0 depends on whether it predicts. This document lists eight falsifiable predictions, each with a date stamp, a measurable check, and the framework score it commits to. At the v1.1 review checkpoint, each prediction is graded; where reality has diverged from the framework, the framework is updated (not the prediction).

A prediction is meaningful only if there is a state of the world that would falsify it, and a specific date by which the question is settled. "Within a major framework revision" without a date is not a prediction; "by 2027-05-02" is.

## P1 — Pydantic maintainership or Python EDR adjustment

- **Claim:** Either (a) Pydantic gains at least three active maintainers (each merging at least one PR in the prior six months) by **2027-05-02**, or (b) the Python ecosystem-dependency-risk (EDR) score in the next major framework revision trends toward 2.0 from its current 2.5.
- **Framework commitment:** Python EDR = 2.5 today, with the load-bearing Pydantic dependency on a small maintainer group flagged as the largest single risk to Python's structured-output position.
- **Measurable check:** Pull GitHub maintainer-activity stats for `pydantic/pydantic` on 2027-05-02; six-month merged-PR-count by maintainer.
- **Rationale:** Python's SOE = 5.0 rests largely on Pydantic. If maintainership does not broaden, the dependency risk thesis tightens.

## P2 — C++ greenfield share in security-sensitive domains

- **Claim:** C++'s share of new (greenfield, not maintenance) software in defense, finance, and similarly security-sensitive domains continues to decline year-over-year in industry surveys (CNCF, JetBrains, RedMonk, GitHub Octoverse) through **2027-05-02**.
- **Framework commitment:** C++ at rank 10 with weighted 2.46; the case for C++ in greenfield AI-era projects is structurally weak (HC = 2, MC = 3, AIN = 1.5).
- **Measurable check:** Year-over-year language-use trends in the named surveys, restricted to greenfield-project signal where the survey breaks it out (it usually does for "starting a new project").
- **Rationale:** If greenfield C++ share holds steady or rises, the framework's greenfield framing is challenged.

## P3 — TypeScript verification velocity (SON gap)

- **Claim:** TypeScript's structured-output-native (SON) score moves from 2.0 toward 3.0 in the next major framework revision (within 18 months of v1.0), driven by `satisfies`-style verification velocity, the type-test ecosystem, and the resolution of `--erasableSyntaxOnly` ergonomics around schema declaration.
- **Framework commitment:** TS SON = 2.0 today; SOE = 5.0 leans on Zod/Vercel.
- **Measurable check:** A v0.x review of TS SON on 2027-11-02 (18 months after v1.0). Concrete signal: official TC39 progress on type-stripping and `satisfies`-as-verification idioms in the community.
- **Rationale:** TS's tied #1 standing is narrow; SON closing reduces the dependency on the third-party schema ecosystem.

## P4 — Microsoft Anthropic SDK first-party

- **Claim:** An official Microsoft-shipped Anthropic SDK for .NET ships within **18 months of 2026-05-02** (i.e., by 2027-11-02). If it ships, .NET's Anthropic integration moves from `commercial_third_party` to `commercial_first_party` and AIN rises by at least 0.5.
- **Framework commitment:** .NET AIN = 4.0 today; the Anthropic .NET integration is currently community-maintained (.NET Anthropic.SDK community port).
- **Measurable check:** GitHub repo under `microsoft/` or `Anthropic/` with .NET SDK label, MS engineering attribution; first stable release by 2027-11-02.
- **Rationale:** Microsoft has an explicit AI Foundry commitment; an Anthropic SDK is a logical extension. If it does not ship, the .NET AIN ceiling holds.

## P5 — Rust compile-time ergonomics

- **Claim:** Rust's AI-agent operability (AO) lifts from 4.0 to 4.5 in the next major framework revision, driven by parallel-front-end stabilization and `mold`-based linking on by default — both visible in stable rustc by **2027-05-02**.
- **Framework commitment:** Rust AO = 4.0 today; the largest gap to top tier is iteration speed for agent-driven loops.
- **Measurable check:** rustc release notes for parallel front-end status; default linker selection on Linux/macOS; benchmark of cold/incremental rebuild times against the cargo project on a representative AI-era codebase.
- **Rationale:** The Rust AO ceiling depends on the agent loop closing fast enough; the named two changes are the named bottleneck breakers.

## P6 — Java Project Panama and Loom maturation

- **Claim:** Java's machine-cognition (MC) and AI-agent-operability (AO) scores each lift by 0.5 in the next major framework revision after Project Panama vector API stabilization (JEP final) and Project Loom maturation (production virtual-thread defaults), both expected by **2027-05-02**.
- **Framework commitment:** Java MC = 4.0, AO = 3.5 today; the AO ceiling is partly the build/test loop, partly the agent-friendly typed primitives Loom provides.
- **Measurable check:** OpenJDK release notes; presence of vector API as final JEP; virtual-thread defaults in mainstream frameworks (Spring Boot, Quarkus).
- **Rationale:** Java's reachability score depends on these two specifically. If they slip, Reach revises down.

## P7 — Swift cross-platform AI integration ceiling

- **Claim:** Swift's AI-systems-ecosystem (AIE) score does NOT improve materially through **2027-05-02** — AIE stays at or below 2.5 — because Apple-stewardship-driven cross-platform reach (non-Apple agent-framework targets) does not materially expand.
- **Framework commitment:** Swift AIE = 2.5 today; LangChain/LlamaIndex/Semantic Kernel do not ship Swift implementations as of v0.6.
- **Measurable check:** PyPI/npm-equivalent catalog of Swift AI-framework packages on 2027-05-02; presence of a Swift LangChain (or analogue) with non-Apple-platform CI.
- **Rationale:** The framework asserts that steward concentration caps reachability. If Swift AIE jumps to 3.5+, that thesis weakens for Swift specifically.

## P8 — Elixir set-theoretic types

- **Claim:** Elixir's set-theoretic-types proposal reaches a stable spec by **2027-05-02**, OR Elixir's reachability-to-top-tier (Reach) score is revised downward in the next major framework revision.
- **Framework commitment:** Elixir Reach = 2.5 today, in part on the strength of the in-motion set-theoretic types work; if that work stalls, the Reach justification weakens.
- **Measurable check:** elixir-lang.org release notes; presence of stable type-system documentation; community uptake signal in Phoenix and Ecto.
- **Rationale:** A non-shipping forward-trajectory bet is the same as no bet. If Elixir's headline path forward does not deliver, the Reach number must move.

## v1.1 review checkpoint

At **2027-11-02** (18 months after v1.0 ship target of 2026-09-01, allowing a 14-month review window) or earlier if a critical mass of predictions has resolved:

For each prediction:
1. Mark resolved (yes / no / partial) based on the named measurable check.
2. If resolved counter to the framework's commitment, file a v0.x score-correction PR with the new evidence and the proposed score change.
3. If unresolved, extend the date stamp by no more than 12 months and document why.
4. Aggregate the prediction-pass rate as a calibration signal: a v1.0 framework whose predictions land at >= 60% accuracy is doing useful forecasting; below that threshold, the dimension weights and rubric anchors are the first thing to revisit.

The pass rate is itself a finding: frameworks that predict reliably earn the right to opine; frameworks that do not should be re-anchored.

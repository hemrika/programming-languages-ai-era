# Eight Predictions I'm Willing to Have Graded in 12 Months

*If a framework can't be falsified, it isn't useful. Here are the bets I'm placing publicly.*

By Rutger Hemrika · 2026-05-02

## The bet on the record

If my framework is right, these eight things happen by May 2027. If my framework is wrong, they won't, and the matrix needs updating. That is the point of publishing predictions instead of opinions. A prediction has a date stamp, a measurable check, and a state of the world that falsifies it. An opinion has none of those, which is why opinions cost the writer nothing and predictions cost everything.

Eight falsifiable predictions, each tied to a specific framework score, each graded on 2027-05-02 at the v1.1 review checkpoint. The framework version snapshot is v0.6.

## The eight predictions

**P1 — Pydantic maintainership or Python EDR adjustment.** Either Pydantic gains at least three active maintainers (each merging at least one pull request in the prior six months) by 2027-05-02, or Python's Ecosystem Dependency Risk score in the next major framework revision trends toward 2.0 from its current 2.5. Framework commitment: Python EDR=2.5 today (alone at the cohort floor on EDR), with the load-bearing Pydantic dependency on a small maintainer group flagged as the largest single risk to Python's structured-output position. Measurable check: GitHub maintainer-activity stats for `pydantic/pydantic`, six-month merged-PR count by maintainer.

**P2 — C++ greenfield share in security-sensitive domains.** C++'s share of new (greenfield, not maintenance) software in defense, finance, and similarly security-sensitive domains continues to decline year-over-year in industry surveys (CNCF, JetBrains, RedMonk, GitHub Octoverse) through 2027-05-02. Framework commitment: C++ at rank 10 with weighted 2.46 (alone at the cohort floor, the only language under 3.00, with a 0.64-point gap to the next-lowest neighbour); the case for C++ in greenfield AI-era projects is structurally weak (HC=2 alone at the cohort floor, MC=3, AIN=1.5 tied at the cohort floor). Measurable check: year-over-year language-use trends in the named surveys, restricted to greenfield-project signal where the survey breaks it out.

**P3 — TypeScript verification velocity.** TypeScript's Structured-Output Native (SON) score moves from 2.5 toward 3.0 in the next major framework revision, driven by `satisfies`-style verification velocity, the type-test ecosystem, and the resolution of `--erasableSyntaxOnly` ergonomics around schema declaration. Framework commitment: TypeScript SON=2.5 today; SOE=5.0 (alone at the cohort ceiling, tied with Python) leans on Zod and the Vercel AI SDK. Measurable check: a TypeScript SON review on 2027-11-02. Concrete signal: TC39 progress on type-stripping and `satisfies`-as-verification idioms in the community.

**P4 — Microsoft Anthropic SDK first-party.** An official Microsoft-shipped Anthropic SDK for .NET ships within 18 months of 2026-05-02 (i.e., by 2027-11-02). If it ships, .NET's Anthropic integration moves from `commercial_third_party` to `commercial_first_party` and AIN rises by at least 0.5. Framework commitment: .NET AIN=4.0 today (alone at the cohort ceiling, tied only with Swift); the Anthropic .NET integration is currently community-maintained. Measurable check: a repository under `microsoft/` or `Anthropic/` with a .NET SDK label and Microsoft engineering attribution; first stable release by 2027-11-02.

**P5 — Rust compile-time ergonomics.** Rust's AI-Agent Operability lifts from 4.0 to 4.5 in the next major framework revision, driven by parallel-front-end stabilization and `mold`-based linking on by default — both visible in stable rustc by 2027-05-02. Framework commitment: Rust AO=4.0 today; the largest gap to top tier is iteration speed for agent-driven loops. Measurable check: rustc release notes for parallel front-end status, default linker selection on Linux/macOS, benchmark of cold and incremental rebuild times on a representative AI-era codebase.

**P6 — Java Project Panama and Loom maturation.** Java's Machine Cognition and AI-Agent Operability scores each lift by 0.5 in the next major framework revision after Project Panama vector API stabilization (JEP final) and Project Loom maturation (production virtual-thread defaults), both expected by 2027-05-02. Framework commitment: Java MC=4.0, AO=3.5 today; the AO ceiling is partly the build/test loop, partly the agent-friendly typed primitives Loom provides. Measurable check: OpenJDK release notes; vector API as final JEP; virtual-thread defaults in Spring Boot and Quarkus.

**P7 — Swift cross-platform AI integration ceiling.** Swift's AI-Systems Ecosystem score does not improve materially through 2027-05-02 — AIE stays at or below 2.5 — because Apple-stewardship-driven cross-platform reach (non-Apple agent-framework targets) does not materially expand. Framework commitment: Swift AIE=2.0 today (in the bottom tier, tied with Elixir; well below the AIE=5.0 ceiling shared by TypeScript and Python); LangChain, LlamaIndex, and Semantic Kernel do not ship Swift implementations. Measurable check: PyPI / npm-equivalent catalog of Swift AI-framework packages on 2027-05-02; presence of a Swift LangChain (or analogue) with non-Apple-platform CI.

**P8 — Elixir set-theoretic types.** Elixir's set-theoretic-types proposal reaches a stable spec by 2027-05-02, OR Elixir's Reachability score is revised downward in the next major framework revision. Framework commitment: Elixir Reach=2.5 today (in the bottom tier, with only C++ at Reach=2.0 sitting lower), in part on the strength of the in-motion set-theoretic types work; if that work stalls, the Reach justification weakens. Measurable check: elixir-lang.org release notes; presence of stable type-system documentation; community uptake signal in Phoenix and Ecto.

## How they'll be graded

The v1.1 review checkpoint is 2027-05-02. The grading process is public, and the steps are on the record.

For each prediction: mark resolved (yes / no / partial) based on the named measurable check. If resolved counter to my commitment, file a score-correction with the new evidence and the proposed score change. If unresolved, extend the date stamp by no more than 12 months and document why. Aggregate the prediction-pass rate as a calibration signal — a v1.0 framework whose predictions land at 60% or higher accuracy is doing useful forecasting; below that threshold, the dimension weights and rubric anchors are the first thing to revisit.

The pass rate is itself a finding. A framework whose predictions land earns the right to opine. A framework whose predictions miss should be re-anchored. The grading runs in public on the dated milestone.

## What would change my mind

If 4 or more of 8 predictions falsify against my commitment, the framework needs structural revision, not just score adjustments.

That is the line. Below 4 misses, the misses get absorbed as cell-level corrections in the next revision (e.g., Pydantic maintainership broadens, Python EDR moves from 2.5 to 3.0, the matrix updates, the framework continues). At 4 or more misses, the dimension weights and the rubric anchors are the first thing to review, because a calibration miss at that scale signals the framework is measuring the wrong thing or weighting it incorrectly. Specific failure modes I will treat as structural rather than incremental: (a) the safety-pressure thesis weakens — the four institutional pillars walk back the memory-safety guidance; (b) the dependency-risk axis turns out to be uncorrelated with stewardship resilience under stress; (c) the Reachability dimension fails to discriminate forward bets — high-Reach languages do not outperform low-Reach languages on cell-level closing paths inside the planning horizon.

If any of the three structural failure modes lands, the framework gets a v2.0 redesign, with the failure mode documented as the proximate cause. That is the bet I am willing to be on the record for.

## Closing

Eight predictions. One year. Public grading.

Subscribe at `rutgerhemrika.substack.com` for the v1.1 grading post on 2027-05-02. If you want the underlying data, claims, and sources, the framework is open at `github.com/hemrika/programming-languages-ai-era`. The bet is on.

---

*The framework's value beyond v1.0 depends on whether it predicts. The bet is on the record.*
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
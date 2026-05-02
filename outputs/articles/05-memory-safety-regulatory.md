# Memory Safety Crossed Into Regulatory Territory in 2024

*Four independent institutions now treat memory safety as a structural language property they actively select for. Greenfield C++ adoption now carries a knowingly-accepted regulatory risk.*

By Rutger Hemrika · 2026-05-02

## The line that moved

Picking C++ for a new project in 2026 used to be a technical preference. It now carries a regulatory exposure CTOs need to understand.

The shift is not subtle and it is not gradual. Memory safety has crossed from a technical preference debated inside engineering teams to a regulatory and platform-owner selection criterion debated outside them — by the U.S. National Security Agency, the U.S. Office of the National Cyber Director, Microsoft's Security Response Center, the Chromium project, and Google's Android security team. Four independent vantage points, four different institutional incentives, one converging recommendation against the same set of languages. The framework records the convergence as `cpp-006` (NSA), `cpp-007` (ONCD), `cpp-004` (MSRC), `cpp-005` (Chromium), `cpp-008` plus `rust-016` and `rust-017` (Android). The decision implication for senior leaders: greenfield C++ in security-sensitive domains is no longer a default. It is a documented exception with a written risk-acceptance trail.

## The four pillars

Microsoft Security Response Center reports that approximately 70% of the CVEs Microsoft assigns are memory-safety issues, across products written largely in C and C++. The figure has been stable across multiple reporting windows and is the empirical anchor for Microsoft's own internal language-selection guidance. The Chromium project independently reports approximately 70% of high-severity security bugs are memory-safety bugs — a different codebase, a different team, a different reporting methodology, and the same number. Two industrial-scale C++ codebases, two security teams operating independently, two separate reporting pipelines, one converging figure.

The U.S. National Security Agency's *Software Memory Safety* Cybersecurity Information Sheet recommends shifting from memory-unsafe languages and explicitly names C and C++. The U.S. Office of the National Cyber Director's *Back to the Building Blocks* report repeats the recommendation at the executive-branch policy level. Google's Android security data shows memory-safety vulnerabilities decline as new native code shifts toward memory-safe languages, with zero memory-safety vulnerabilities discovered in Android Rust code at the time of the Android 13 report. Four institutions, three different roles (regulator, platform owner, OS owner), one selection criterion.

The structural fact the matrix records is that this convergence is not a 2024 spike that fades. The MSRC figure has held for years; the Chromium figure has held for years; the NSA and ONCD documents are dated 2022 and 2024 respectively and have been reaffirmed in subsequent guidance rather than walked back; the Android telemetry continues to track in the same direction in each annual security report. Four institutions, four different reporting cycles, no walk-back, repeated reaffirmation.

This is wrong if the named guidances are walked back, downgraded, or contradicted by subsequent equivalent-authority documents. The 2024-25 reaffirmation cycle is the opposite of a walk-back. The pattern is intensification, not retreat.

## What aligns with the pressure

Five languages in the cohort align structurally with the institutional pressure, each through a different mechanism.

Rust's ownership system manages memory through compiler-checked rules without garbage collection or manual `free`. Single-owner semantics, lifetime-checked references, and the explicitly-scoped `unsafe` boundary together give Rust the strongest structural alignment in the cohort — and the Android Rust telemetry is the empirical case that the alignment translates into measured outcomes. The framework records Rust at MC=5 and SV=5; the safety-pressure thesis is one reason the strategic-viability cell sits at the top.

Kotlin runs on the JVM with its mandatory bytecode verifier, layered with null-safety as a type-system guarantee. The verifier is not a code-review pattern; it is a runtime invariant the JVM enforces before any class is loaded. .NET runs on the Common Language Infrastructure with metadata-checked types and adds nullable reference types for null-safety. Swift specifies memory-safety rules including detection of conflicting access at compile time. Elixir's BEAM provides process isolation and explicit failure semantics — a different model, same alignment with the safety-pressure axis.

The structural distinction is the point. Each of the five languages aligns through a mechanism the language steward enforces, not through a discipline a team applies. That is what makes the alignment a structural property regulators can select for: the property is invariant across teams that pick the language, and it does not depend on the team's review process. C++ Core Guidelines are advisory and configuration-dependent, which is why the institutional guidance does not credit them as equivalent.

This is wrong if a new language tier emerges that aligns with safety pressure through a different mechanism the framework does not yet score. The probability inside the planning horizon is low — the cohort is stable, and the institutional pressure is reinforcing the existing structural distinctions, not flattening them.

## What's exposed

C++ sits alone in the exposed tier. The framework records C++ at HC=2, MC=3, AO=2, SV=2, weighted total 2.46 — last in the cohort by 0.64 weighted points, the largest gap between consecutive ranks. The safety-pressure axis is one input to the SV=2 score, not the only input, but it is the most cited.

C++'s counter-positions are real and coexist with the safety penalty rather than offsetting it. The accelerator host-language credit (CUDA, ROCm, Vulkan) keeps C++ as the language-of-the-stack for GPU and accelerator runtimes — a forward production credit the framework explicitly records. The C++26 modules work, the WG21 reflection proposal (P2996), and the Core Guidelines are concrete language-improvement signals. None of those undo the institutional convergence cited in the four pillars. Modules adoption is uneven across compilers and build tools. Core Guidelines are advisory. Reflection lifts SON if it lands inside the planning horizon, but SON moving from 1.0 to 3.0 still leaves C++ outside the top tier on the row total.

The framework's lens-analysis treatment puts C++ alone in the "exposed" tier on the safety-pressure axis. That is a structural read, not a stylistic one. Greenfield C++ in security-sensitive domains is now a default only where accelerator host code is unavoidable, with the safety penalty knowingly accepted.

This is wrong if a new compiler ships memory-safety-as-default for C++ and gains adoption — Microsoft's `Safe C++` proposals, Google's `-fbounds-safety`, Apple's similar initiatives are in motion but none have crossed the threshold of "default in production" inside the cohort. If one does, the framework revises the C++ row.

## What changes for CTOs

For CTOs at organizations subject to NSA, CISA, ONCD, or sector-equivalent guidance — defense, financial services, healthcare, federal contractors, platform owners with regulatory surfaces — greenfield C++ now requires explicit risk acceptance with documented rationale. The decision is not blocked. It is logged. The framework's working assumption is that the cost of logging compounds: each successive procurement cycle, each successive certification audit, each successive security review carries the prior risk-acceptance trail with it. Five years out, the cumulative cost of that trail is a strategic line item, not a technical one.

For CTOs outside regulated industries, the calculus is different but not absent. Microsoft, Google, and Apple all use the same telemetry internally that produced the public guidance. Hiring engineers who have been trained on Rust, Kotlin, Swift, or .NET means hiring engineers who have absorbed the safety-pressure framing as a default rather than as a constraint. The talent market reflects the institutional pressure with a delay; the delay is shrinking.

The pragmatic recommendation: greenfield infrastructure that would have defaulted to C++ in 2018 should default to Rust in 2026 unless the project requires accelerator host code, in which case the C++ scope is bounded to the accelerator surface and the rest of the system runs in a memory-safe language. That is the portfolio shape the framework's lens-analysis recommends, and it is the shape that aligns with the institutional convergence rather than fighting it.

This is wrong if a new compiler ships memory-safety-as-default for C++ that gains adoption inside the planning horizon, or if regulatory direction reverses. Neither has been signaled.

## The strategic read

The framing matters. Rust is not structurally favored because regulators love Rust. Rust is structurally favored because the alternative — C and C++ — carries explicit institutional pressure that the alternative cannot offset. The signal is not "pick Rust because the NSA says so." The signal is "C++ is exposed because four institutions converge on it being exposed, and the languages that align structurally with the pressure are the ones that escape the exposure." Different framing, same answer.

The framework's working assumption is that this is the most stable cross-language signal in the cohort. The four pillars do not depend on each other. The four institutions do not coordinate. The convergence is the finding, and the finding has held across reporting cycles. Senior teams that read the matrix and pick C++ for a greenfield system in a regulated industry are betting against the convergence. The framework's version-stamp is v0.6 and the C++ row at 2.46 is the lowest in the cohort by structural design, not by editorial preference.

## What's next in the series

Piece 6 takes the dependency-risk thesis across the cohort — Pydantic, Zod, Instructor, Outlines, llama.cpp, nlohmann/json — and quantifies what single-maintainer load-bearing libraries cost a 5-year platform bet. Piece 7 expands the reachability dimension and walks the per-language gap analysis. The full framework, every per-cell rationale, the source claims, and the v1.1 grading checkpoint live at `github.com/hemrika/programming-languages-ai-era`. Subscribe at `rutgerhemrika.substack.com` for pieces 6–8.

---

*Four institutions converged on memory safety as a structural language property they select for, and the framework records C++ as exposed alone — pick the languages that align with the pressure, or accept the cost of fighting it on the record: `github.com/hemrika/programming-languages-ai-era`.*

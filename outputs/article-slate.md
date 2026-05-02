# Article Slate — Programming Languages in the AI Era

*Thought-leadership series, 8 pieces, anchored on the v0.6 framework. Author: Rutger Hemrika.*

## Locked decisions

- **Audience.** Senior / strategic — CTOs, VP Engineering, senior tech leaders making 5-year platform bets. Not IC-level tooling discussion; not beginner orientation. Reader is making or defending a language choice that will outlive the current quarter.
- **Outlets.** Substack as canonical home — `rutgerhemrika.substack.com` (handle confirmed; not yet set up). Same-day cross-post to LinkedIn long-form. Same-day X thread (6–8 posts). Medium republish 3 days later with canonical link back to Substack. LinkedIn engagement pass on day +5.
- **Cadence.** 8 pieces. Weekly through month 1 (pieces 1–4). Biweekly through months 2–3 (pieces 5–8).
- **Goal.** Personal brand and thought leadership. Sub-goal: make the public framework repository (`github.com/hemrika/programming-languages-ai-era`) the citeable reference for AI-era language evaluation.
- **Voice register.** Confident-but-skeptical. Author writes in first person sparingly but present.

## The 8-piece slate

| # | Title | Thesis | Why senior/strategic | Length | Ship week |
|---:|---|---|---|---:|---:|
| 1 | Programming Languages in the AI Era: A Greenfield Reset | If you remove incumbent gravity, the ranking reshuffles. TypeScript and Go tie at 4.01; .NET sits at 3.99 with the strongest forward trajectory. The framework forces the reader to defend a 5-year platform bet on forward-looking evidence, not installed base. | Anchor piece. Establishes the framework as the citeable reference and previews pieces 2–8. | 2,200 | W1 |
| 2 | Why Native and Ecosystem Are Not the Same 5.0 | A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers. The native/ecosystem split (AIN/AIE, SON/SOE) and EDR axis make supply-chain risk legible at the language level. | Translates supply-chain reasoning senior teams already apply to cloud vendors into the same lens for library stewardship. | 1,500 | W2 |
| 3 | The Pydantic Problem: When One Library Carries a Language | Pydantic, Zod, Instructor, and llama.cpp all sit one bus-factor event from being a strategic problem. EDR=2.5 (Python) versus 4.5 (.NET) makes this visible; senior teams should price it. | Concrete, named-library-level supply-chain analysis. The kind of risk that does not appear on a roadmap until it is already a problem. | 1,800 | W3 |
| 4 | AI-Agent Operability Is the New Developer Velocity | AO at 20% weight is the most discriminating dimension in the matrix. Single-canonical-toolchain languages (Go, TypeScript) pull away from fragmented ones (Java, C++). The strategic signal: agent loops are now the dominant cost center, not human keystrokes. | Reframes "DX" as "operability" — a strategic property, not an IC complaint. | 1,800 | W4 |
| 5 | Reachability: Scoring Where a Language Is Going, Not Just Where It Is | Current-state ranking is a snapshot; the Reach dimension scores forward-trajectory plausibility. .NET ranks #3 today but #1 on Reach. C++ ranks #10 today and #10 on Reach. For 5-year bets, Reach matters more than this-year ranking. | Time-horizon reasoning made explicit. Closes the door on "Rust is the future" hand-waving without specifying the closing path. | 1,800 | W6 |
| 6 | The Memory-Safety Selection Pressure Is Not a Preference Anymore | NSA, ONCD, MSRC ~70%, Chromium ~70%, Android telemetry. Four independent vantage points converge on memory safety as a structural language property regulators select for. Greenfield C++ in security-sensitive domains is now a default only where unavoidable. | Hands the senior reader the regulatory-trajectory argument that defends or unwinds language choices in defense, finance, and platform contexts. | 1,800 | W8 |
| 7 | What I Got Wrong: A Framework Is a Bet, Not an Oracle | Single-rater calibration. Working-assumption weights. Three places I expect the next revision to move scores. Public grading checkpoint at v1.1. | Models the confident-but-skeptical posture explicitly. Builds credibility precisely by surfacing where the framework is most likely to be wrong. | 1,500 | W10 |
| 8 | Three Predictions I'll Be Graded On | The eight falsifiable predictions in the public repo, narrowed to three high-signal ones with public dates. Pydantic maintainership; Microsoft Anthropic .NET SDK; greenfield C++ share in security-sensitive domains. The grading happens in public on 2027-05-02. | Closes the series the way it opens — with a falsifiable bet. The reader leaves knowing the framework's author is willing to be wrong on the record. | 1,400 | W12 |

## Per-piece distribution playbook

For every piece in the slate:

- **Day 0 — Substack.** Canonical publication on `rutgerhemrika.substack.com`. Subscriber-list send. Open graph image is the matrix table or a single annotated chart.
- **Day 0 — LinkedIn long-form.** Same body, LinkedIn-native formatting. Headline tightened for the LinkedIn feed. First comment links to the public repo.
- **Day 0 — X thread.** 6–8 posts. First post is a single load-bearing claim plus a number. Last post links to the Substack canonical. Middle posts surface one named library, one named guidance document, one falsifiable bet. No general "thread on …" framing.
- **Day +3 — Medium republish.** Same body. Canonical link header points back to Substack. Two tags: "AI" and "Software Architecture."
- **Day +5 — LinkedIn engagement pass.** Author replies to every substantive comment within 24 hours. One follow-up post extracted from the comment thread, linking back to the original.

## Voice rules — confident-but-skeptical

The register is "this person knows where the framework breaks." Concretely:

- **Make a clear claim.** "Pydantic has more power over Python's AI position than Microsoft has over .NET's." Not "Pydantic could perhaps be considered influential."
- **Acknowledge counter-cases.** Every section ends with the condition that would invalidate the claim. The reader leaves knowing what would change the author's mind.
- **Cite specific evidence.** Numbers (4.01, 4.5, ~70%), libraries (Pydantic, Zod, Instructor, kotlinx-serialization, Microsoft Semantic Kernel), guidance documents (NSA *Software Memory Safety*, ONCD *Back to the Building Blocks*, MSRC), and named stewards (Microsoft, JetBrains, OpenJDK, Apple, PSF, Dashbit).
- **First person sparingly but present.** "I built this framework because…" appears. Not "A framework was built." Heavy I-narration is avoided.
- **No weasel words.** "Could perhaps suggest" → "shows." "Might be the case" → "is." "Some have argued" → name the source.
- **End sections with falsifiable bets.** "If multi-rater scoring lands cells with >0.5 disagreement, the framework gets revised." The reader can grade the bet later.
- **No version-evolution narration.** Each piece is a snapshot. A single mention of "v0.6" is fine; recurring framework-history is not.

## Audience rules — senior / strategic

- **Lead with decision implication.** First paragraph contains the decision the reader can make from the piece. Methodology comes second.
- **Strategic vocabulary.** Platform bet, trajectory, exposure, stewardship, supply chain, 5-year horizon, compounds, load-bearing.
- **Don't over-explain technical primitives.** Discriminated unions, sum types, source generators, virtual threads — assume the reader has a definition or can ask. Spend the words on what the primitive implies for the platform bet.
- **Translate IC vocabulary up.** "Tooling friction" → "operability." "DX" → "developer velocity." "Ergonomics" → "operability and developer velocity."
- **Bullet points only where prose fails.** The dimensions list, the predictions list, the recommendations-by-domain table. Otherwise prose.

## Working state (as of 2026-05-02)

- **Framework.** v0.6, validator clean. Schema locked. v1.0 ship target 2026-09-01.
- **Anchor piece.** In draft (`outputs/articles/01-greenfield-reset.md`).
- **Pieces 2–8.** Not yet drafted.
- **Substack.** Handle `rutgerhemrika.substack.com` confirmed; publication not yet set up by user. Setup is a prerequisite for piece 1 ship.
- **Public repository.** `https://github.com/hemrika/programming-languages-ai-era`. Citeable from every piece.
- **Predictions grading.** Public v1.1 checkpoint on 2027-05-02. Pieces 7 and 8 trail-end the series into that checkpoint.

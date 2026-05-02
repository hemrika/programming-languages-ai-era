# Evaluation Framework

**Version: v0.5** (2026-05-02). v0.3 (2026-04-30) added structured-output maturity as a 7th dimension. v0.4 split the two AI-era dimensions into native + ecosystem halves and introduced an ecosystem-dependency-risk dimension. v0.5 adds an 11th dimension scoring forward trajectory — `reachability_to_top_tier` — and rebalances 5% from Strategic viability into the new dimension.

## Objective

Evaluate programming languages for the AI era: a period where software is increasingly written, modified, reviewed, tested, and maintained by humans working with AI systems and autonomous agents.

## Framing

This research evaluates languages from a **greenfield** perspective. Installed base, existing code, and incumbent gravity are not scored as advantages. The question is: starting a new AI-era project today, what would you choose, and why? Languages are credited for forward-looking properties (governance quality, future fit, AI-training representation, ecosystem velocity) and not for owning a large amount of legacy code.

## Primary question

Which programming languages become more valuable when AI systems participate deeply in software development?

## Evaluation dimensions

| Dimension | Weight |
|---|---:|
| Human cognition (HC) | 15% |
| Machine cognition (MC) | 15% |
| AI-agent operability (AO) | 20% |
| Runtime and ecosystem (RE) | 10% |
| Strategic viability (SV) | 5% |
| AI-systems native (AIN) | 7.5% |
| AI-systems ecosystem (AIE) | 7.5% |
| Structured-output native (SON) | 5% |
| Structured-output ecosystem (SOE) | 5% |
| Ecosystem dependency risk (EDR) | 5% |
| Reachability to top tier (Reach) | 5% |

Combined AI-systems weight (15%) and combined structured-output weight (10%) are unchanged from v0.4. The new Reach dimension is funded by reducing Strategic viability from 10% to 5% — SV previously absorbed forward-trajectory signal implicitly through its `future fit` and `ecosystem velocity` criteria, and Reach now scores it explicitly.

## v0.5 changelog

**Why a reachability dimension.** v0.4 captured present-state native and ecosystem capability and dependency-risk resilience but did not separate forward-trajectory plausibility from current strategic viability. Two languages with identical SV scores can have very different odds of closing their below-5 gaps within a 3–5-year horizon depending on steward investment, in-motion proposals, and the structural-vs-ecosystem nature of each gap.

**What v0.5 changes.**

- A new `reachability_to_top_tier` (5%) dimension scores how plausibly each below-5 cell in a language's row can move to 5.0 within a 3–5-year horizon. Higher = more reachable.
- The 5% for Reach is pulled from Strategic viability (10% → 5%).
- Total dimension count: 10 → 11.

## v0.4 changelog

**Why the split.** v0.3 conflated language-native capability with ecosystem-package capability and applied inclusion rules asymmetrically (Pydantic credited to Python's structured-output score, Newtonsoft.Json omitted from .NET's). It also did not capture dependency-risk: a 5.0 backed by Microsoft scored identical to a 5.0 backed by three OSS volunteers.

**What v0.4 changes.**

- `ai_systems_interoperability` (15%) is split into `ai_systems_native` (7.5%) and `ai_systems_ecosystem` (7.5%).
- `structured_output_maturity` (10%) is spl
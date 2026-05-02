# Programming Languages in the AI Era

Research repository for evaluating programming languages against the demands of AI-assisted and AI-agentic software development.

**Framework version:** v0.5 (2026-05-02). Snapshot below; see `framework/evaluation-framework.md` for the full version history.

## Core thesis

The AI era will favor languages that are not merely easy to write, but easy to analyze, verify, refactor, test, and operate by both humans and machines — whose load-bearing dependencies are resilient enough to underwrite that promise, and whose forward trajectory plausibly closes the remaining gaps.

## Framing

**Greenfield.** Installed base, existing code volume, and incumbent gravity are not scored as advantages. Languages are credited for forward-looking properties (governance, future fit, AI-training-corpus representation, ecosystem velocity, library maturity for new projects). Maintenance-estate teams should re-weight.

**Native vs ecosystem.** AI-systems and structured-output capability are scored separately for what the language/runtime/stewards ship directly versus what the third-party ecosystem provides. A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers — the dependency-risk dimension records the present-state difference, and the reachability dimension records the forward-trajectory difference.

## Cohort

Ten languages, chosen as the realistic greenfield decision set:

C++, .NET (C#), Elixir, Go, Java, Kotlin, Python, Rust, Swift, TypeScript.

(Mojo, Zig, Julia, and Haskell are out of cohort. Haskell/Julia/Mojo/Zig profile material remains in the repo as research, separate from the validated cohort.)

## Evaluation dimensions

Eleven weighted dimensions on a 1.0–5.0 scale in 0.5-point increments. See `framework/dimensions.md` for criteria and `framework/scoring-rubric.md` for anchors.

| Dimension | Code | Weight |
|---|---|---:|
| Human cognition | HC | 15% |
| Machine cognition | MC | 15% |
| AI-agent operability | AO | 20% |
| Runtime / ecosystem | RE | 10% |
| Strategic viability | SV | 5% |
| AI-systems native | AIN | 7.5% |
| AI-systems ecosystem | AIE | 7.5% |
| Structured-output native | SON | 5% |
| Structured-output ecosystem | SOE | 5% |
| Ecosystem dependency risk (higher = lower risk) | EDR | 5% |
| Reachability to top tier (higher = more reachable) | Reach | 5% |

Four cross-cutting lenses overlay the dimensions: verification, agentic operability, safety pressure, abstraction compression. See `comparisons/lens-analysis.md`.

## Ranking (snapshot)

| Rank | Language | Weighted |
|---:|---|---:|
| 1 | TypeScript | 4.01 |
| 1 | Go | 4.01 |
| 3 | .NET (C#) | 3.99 |
| 4 | Kotlin | 3.85 |
| 5 | Python | 3.71 |
| 5 | Rust | 3.71 |
| 7 | Java | 3.50 |
| 8 | Swift | 3.42 |
| 9 | Elixir | 3.10 |
| 10 | C++ | 2.46 |

TypeScript and Go tie at the top. .NET sits at 3.99 with the cohort's strongest forward bet (EDR=4.5, Reach=4.5 — both highest). Python and Rust tie at 3.71: Python's AI-systems-native gap and high dependency-risk profile hold it down despite tier-leading ecosystem halves; Rust's MC=5 / SV=5 verification ceiling combines with AIE=4.0 (production Postgres/Kafka, candle, async-openai, MCP Rust SDK, the maturing Rig/swiftide/langchain-rust cohort) and SOE=4.0 (Serde + schemars), capped by AIN=1.5. Java holds solo #7 at 3.50, lifted by AO=3.5 on Eclipse JDT.LS maturity and AI-training-corpus density. See `comparisons/overview.md` for the per-cell reasoning.

## Repository structure

| Folder | Contents |
|---|---|
| `framework/` | Evaluation framework, dimensions, scoring rubric, version history |
| `languages/` | Per-language profile pages and hypotheses |
| `claims/` | Atomic evidence claims, one YAML file per language; each claim cites a source and may carry a `counters:` link to the positive claim it opposes and a `backer:` annotation naming the specific library or steward |
| `sources/` | Per-language source registries (`<lang>-sources.yaml`) — citations, publication dates, reliability labels |
| `evaluations/` | Per-language scored evaluations across all 11 dimensions, with confidence and supporting-claims references |
| `comparisons/` | Cross-cutting reads — overview matrix, four lenses, agent-friendliness, dynamic-vs-static |
| `insights/` | Higher-order theses (agentic feedback loops, AI favors verifiability, safety pressure, incumbent risk) |
| `outputs/` | Report, story-driven report, deck outline, execution plan, confidence heatmap, review pass, deliverable PPTX |
| `scripts/` | `validate_evaluations.py`, `score_summary.py`, `confidence_heatmap.py` |

## Workflow

```text
Source → Claim → Criterion → Evaluation → Comparison → Insight → Output
```

Every score traces through `Insight → Evaluation → Claim → Source`. Counterclaims link to the positive claims they oppose. Adding or moving a score requires touching the upstream claim; the validator enforces the chain.

## Running the scripts

```bash
python scripts/validate_evaluations.py       # validates all 10 cohort evaluations
python scripts/score_summary.py              # prints weighted ranking
python scripts/confidence_heatmap.py         # regenerates outputs/confidence-heatmap.md
```

The validator checks: 11 dimensions present per language, half-point scores in `{1.0, 1.5, …, 5.0}`, every supporting-claim ID resolves, and every `counters:` reference resolves within the same language file.

## Outputs

- `outputs/report.md` — full report (analyst register)
- `outputs/report-story.md` — story-driven sibling using Pip Decks Stories That Explain
- `outputs/deck-outline.md` — 14-slide deck outline
- `outputs/programming-languages-ai-era.pptx` — generated deck
- `outputs/evidence-backed-research-execution-plan.md` — methodology and phase plan
- `outputs/reachability-analysis.md` — per-language gap walk: what would close each below-5 cell, plausibility verdict
- `outputs/confidence-heatmap.md` — per-cell rater confidence, regenerable
- `outputs/v0.3-review-pass.md` — formal Phase-7 review pass against v0.3
- `outputs/v0.5-review-pass.md` — formal Phase-7 review pass against v0.5

## Status

Single-rater draft, anchored in ~390 atomic claims with primary-source citations. Scores are intended to be falsifiable through the u
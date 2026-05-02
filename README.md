# Programming Languages in the AI Era

Research repository for evaluating programming languages against the demands of AI-assisted and AI-agentic software development.

**Framework version:** v0.4 (2026-05-02). Snapshot below; see `framework/evaluation-framework.md` for the full version history.

## Core thesis

The AI era will favor languages that are not merely easy to write, but easy to analyze, verify, refactor, test, and operate by both humans and machines — and whose load-bearing dependencies are resilient enough to underwrite that promise.

## Framing

**Greenfield.** Installed base, existing code volume, and incumbent gravity are not scored as advantages. Languages are credited for forward-looking properties (governance, future fit, AI-training-corpus representation, ecosystem velocity, library maturity for new projects). Maintenance-estate teams should re-weight.

**Native vs ecosystem.** AI-systems and structured-output capability are scored separately for what the language/runtime/stewards ship directly versus what the third-party ecosystem provides. A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers — the dependency-risk dimension records the difference.

## Cohort

Ten languages, chosen as the realistic greenfield decision set:

C++, .NET (C#), Elixir, Go, Java, Kotlin, Python, Rust, Swift, TypeScript.

(Mojo, Zig, Julia, and Haskell were dropped from the v0.3 cohort. Haskell/Julia/Mojo/Zig profile material remains in the repo as research, separate from the validated cohort.)

## Evaluation dimensions

Ten weighted dimensions on a 1.0–5.0 scale in 0.5-point increments. See `framework/dimensions.md` for criteria and `framework/scoring-rubric.md` for anchors.

| Dimension | Code | Weight |
|---|---|---:|
| Human cognition | HC | 15% |
| Machine cognition | MC | 15% |
| AI-agent operability | AO | 20% |
| Runtime / ecosystem | RE | 10% |
| Strategic viability | SV | 10% |
| AI-systems native | AIN | 7.5% |
| AI-systems ecosystem | AIE | 7.5% |
| Structured-output native | SON | 5% |
| Structured-output ecosystem | SOE | 5% |
| Ecosystem dependency risk (higher = lower risk) | EDR | 5% |

Four cross-cutting lenses overlay the dimensions: verification, agentic operability, safety pressure, abstraction compression. See `comparisons/lens-analysis.md`.

## v0.4 ranking (snapshot)

| Rank | Language | Weighted | v0.3 | Δ |
|---:|---|---:|---:|---:|
| 1 | Go | 4.04 | 4.17 (#3) | +2 ↑ |
| 2 | TypeScript | 4.01 | 4.38 (#1) | −1 ↓ |
| 3 | .NET (C#) | 3.96 | 4.00 (#4) | +1 ↑ |
| 4 | Kotlin | 3.85 | 3.88 (#6) | +2 ↑ |
| 5 | Rust | 3.75 | 3.90 (#5) | 0 |
| 6 | Python | 3.74 | 4.25 (#2) | −4 ↓ |
| 7 | Swift | 3.40 | 3.25 (#8/9) | +1 ↑ |
| 8 | Java | 3.38 | 3.50 (#7) | −1 ↓ |
| 9 | Elixir | 3.13 | 3.25 (#8/9) | −1 ↓ |
| 10 | C++ | 2.46 | 2.60 | 0 |

The Python −4 is the largest movement: v0.3 absorbed Pydantic + Instructor + Outlines + LangChain into the structured-output and AI-systems scores at full ecosystem weight. v0.4 splits each into native + ecosystem and adds dependency-risk, exposing that Python's ecosystem ride comes at a low-AIN/low-EDR cost. Go takes #1 because its HC=5/AO=5 lead carries unchanged at 35% combined weight while TypeScript's AIE=5/SOE=5 gains are diluted by the native halves. See `comparisons/overview.md` for the per-cell reasoning.

## Repository structure

| Folder | Contents |
|---|---|
| `framework/` | Evaluation framework, dimensions, scoring rubric, version history |
| `languages/` | Per-language profile pages and hypotheses |
| `claims/` | Atomic evidence claims, one YAML file per language; each claim cites a source and may carry a `counters:` link to the positive claim it opposes and a `backer:` annotation when it names a specific library |
| `sources/` | Per-language source registries (`<lang>-sources.yaml`) — citations, publication dates, reliability labels |
| `evaluations/` | Per-language scored evaluations across all 10 dimensions, with confidence and supporting-claims references |
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

The validator checks: 10 dimensions present per language, half-point scores in `{1.0, 1.5, …, 5.0}`, every supporting-claim ID resolves, and every `counters:` reference resolves within the same language file.

## Outputs

- `outputs/report.md` — full report (analyst register)
- `outputs/report-story.md` — story-driven sibling using Pip Decks Stories That Explain
- `outputs/deck-outline.md` — 13-slide deck outline
- `outputs/programming-languages-ai-era.pptx` — generated deck
- `outputs/evidence-backed-research-execution-plan.md` — methodology and phase plan
- `outputs/confidence-heatmap.md` — per-cell rater confidence, regenerable
- `outputs/v0.3-review-pass.md` — formal Phase-7 review against v0.3 (still load-bearing under v0.4)

## Status

v0.4 draft, single-rater, anchored in ~340 atomic claims with primary-source citations. Scores are intended to be falsifiable through the upstream claims. A v0.4 review pass and a Python/.NET counter-claim audit are open work items.

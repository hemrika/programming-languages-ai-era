"""Sensitivity analysis for the v0.6 weighted ranking.

Perturbs each dimension weight at +-2.5% and +-5% (with the remaining weights
rescaled proportionally so the total stays at 100%), recomputes the headline
ranking, and reports which language ranks are robust vs fragile.

Output: outputs/sensitivity-analysis.md.
"""
from datetime import date
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evaluations"
OUT_PATH = ROOT / "outputs" / "sensitivity-analysis.md"

COHORT = {
    "cpp", "dotnet", "elixir", "go", "java",
    "kotlin", "python", "rust", "swift", "typescript",
}

WEIGHTS = {
    "human_cognition": 0.15,
    "machine_cognition": 0.15,
    "ai_agent_operability": 0.20,
    "runtime_ecosystem": 0.10,
    "strategic_viability": 0.05,
    "ai_systems_native": 0.075,
    "ai_systems_ecosystem": 0.075,
    "structured_output_native": 0.05,
    "structured_output_ecosystem": 0.05,
    "ecosystem_dependency_risk": 0.05,
    "reachability_to_top_tier": 0.05,
}

DIMENSION_LABEL = {
    "human_cognition": "Human cognition (HC)",
    "machine_cognition": "Machine cognition (MC)",
    "ai_agent_operability": "AI-agent operability (AO)",
    "runtime_ecosystem": "Runtime / ecosystem (RE)",
    "strategic_viability": "Strategic viability (SV)",
    "ai_systems_native": "AI-systems native (AIN)",
    "ai_systems_ecosystem": "AI-systems ecosystem (AIE)",
    "structured_output_native": "Structured-output native (SON)",
    "structured_output_ecosystem": "Structured-output ecosystem (SOE)",
    "ecosystem_dependency_risk": "Ecosystem dependency risk (EDR)",
    "reachability_to_top_tier": "Reachability to top tier (Reach)",
}

PERTURBATIONS = [-0.05, -0.025, 0.0, 0.025, 0.05]


def load_scores():
    out = {}
    for path in sorted(EVAL_DIR.glob("*.yaml")):
        if path.stem not in COHORT:
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        out[data["language"]] = {
            dim: float(data["scores"][dim]["score"]) for dim in WEIGHTS
        }
    return out


def perturbed_weights(target_dim, delta):
    """Return weight dict where target_dim shifts by `delta` percentage points
    (delta is a fraction of the total, e.g. 0.025 = 2.5%); the rest of the
    weights are rescaled proportionally so the total stays at 1.0."""
    new = dict(WEIGHTS)
    new_target = new[target_dim] + delta
    if new_target < 0:
        new_target = 0.0
    rest_total_old = sum(v for k, v in new.items() if k != target_dim)
    rest_total_new = 1.0 - new_target
    if rest_total_old == 0:
        return new
    factor = rest_total_new / rest_total_old
    for k in new:
        if k == target_dim:
            new[k] = new_target
        else:
            new[k] = new[k] * factor
    return new


def weighted_score(scores, weights):
    return round(sum(scores[d] * weights[d] for d in weights), 4)


def rank_languages(score_table, weights):
    """Return list of (language, score) sorted high-to-low; ranks are dense
    so a tie shares the rank."""
    scored = [(lang, weighted_score(s, weights)) for lang, s in score_table.items()]
    scored.sort(key=lambda x: (-x[1], x[0]))
    # Compute dense ranks accounting for ties at the same numeric score.
    out = []
    rank = 0
    last_score = None
    skip = 0
    for lang, sc in scored:
        if sc != last_score:
            rank += 1 + skip
            skip = 0
            last_score = sc
        else:
            skip += 1
            # rank stays equal
        out.append((lang, sc, rank))
    return out


def main():
    score_table = load_scores()

    # Baseline ranking
    baseline = rank_languages(score_table, WEIGHTS)
    baseline_rank = {lang: rank for lang, _, rank in baseline}

    # Per-perturbation ranking grid: scenarios x languages
    scenarios = []
    for dim in WEIGHTS:
        for delta in PERTURBATIONS:
            if delta == 0.0:
                continue
            w = perturbed_weights(dim, delta)
            ranked = rank_languages(score_table, w)
            rank_map = {lang: rank for lang, _, rank in ranked}
            scenarios.append((dim, delta, rank_map, ranked))

    # Per-language stability: how often does each language hold its baseline rank?
    stability = {}
    rank_range = {}
    for lang in score_table:
        held = 0
        ranks = [baseline_rank[lang]]
        for _, _, rmap, _ in scenarios:
            if rmap[lang] == baseline_rank[lang]:
                held += 1
            ranks.append(rmap[lang])
        stability[lang] = (held, len(scenarios))
        rank_range[lang] = (min(ranks), max(ranks))

    # Smallest perturbation that flips a language's rank with a neighbor
    flip_at = {}
    for lang in score_table:
        bs = baseline_rank[lang]
        smallest = None
        for dim, delta, rmap, _ in scenarios:
            if rmap[lang] != bs:
                mag = abs(delta)
                if smallest is None or mag < smallest[0]:
                    smallest = (mag, dim, delta, rmap[lang])
        flip_at[lang] = smallest

    # Robust vs fragile findings
    robust_lines = []
    fragile_lines = []
    for lang in sorted(score_table, key=lambda l: baseline_rank[l]):
        held, total = stability[lang]
        rmin, rmax = rank_range[lang]
        if rmin == rmax:
            robust_lines.append(
                f"- **{lang} at rank {baseline_rank[lang]}** — holds rank in "
                f"all {total} perturbations (range {rmin}-{rmax})."
            )
        else:
            f = flip_at[lang]
            if f is not None:
                _, dim, delta, new_rank = f
                fragile_lines.append(
                    f"- **{lang} at rank {baseline_rank[lang]}** — held in "
                    f"{held}/{total} perturbations; range {rmin}-{rmax}; "
                    f"first flip at {DIMENSION_LABEL[dim]} {delta:+.1%} "
                    f"(moves to rank {new_rank})."
                )
            else:
                fragile_lines.append(
                    f"- **{lang} at rank {baseline_rank[lang]}** — held in "
                    f"{held}/{total} perturbations; range {rmin}-{rmax}."
                )

    # Per-language stability band table
    rank_table_lines = ["| Language | Baseline | Min rank | Max rank | Held |",
                       "|---|---:|---:|---:|---:|"]
    for lang in sorted(score_table, key=lambda l: baseline_rank[l]):
        held, total = stability[lang]
        rmin, rmax = rank_range[lang]
        rank_table_lines.append(
            f"| {lang} | {baseline_rank[lang]} | {rmin} | {rmax} | {held}/{total} |"
        )
    rank_table = "\n".join(rank_table_lines)

    baseline_lines = ["| Rank | Language | Weighted score |",
                      "|---:|---|---:|"]
    for lang, sc, rank in baseline:
        baseline_lines.append(f"| {rank} | {lang} | {sc:.2f} |")
    baseline_table = "\n".join(baseline_lines)

    # Per-dimension fragility: how many languages flip rank under any
    # perturbation of this dimension?
    dim_lines = ["| Dimension | Languages whose rank flips under +-5% |",
                 "|---|---|"]
    for dim in WEIGHTS:
        flipped = set()
        for d, delta, rmap, _ in scenarios:
            if d != dim:
                continue
            for lang, rank in rmap.items():
                if rank != baseline_rank[lang]:
                    flipped.add(lang)
        dim_lines.append(
            f"| {DIMENSION_LABEL[dim]} | "
            f"{', '.join(sorted(flipped)) if flipped else '(none)'} |"
        )
    dim_table = "\n".join(dim_lines)

    n_scenarios = len(scenarios)
    output = f"""# Sensitivity Analysis — Framework v0.6

*Generated by `scripts/sensitivity_analysis.py` on {date.today().isoformat()}.*

Each of the 11 dimension weights is perturbed at +-2.5% and +-5% (4 perturbations per dimension, {n_scenarios} scenarios total). The remaining weights are rescaled proportionally so total weight stays at 100%. The headline weighted ranking is recomputed under each scenario and compared to the baseline.

The point is not to declare any ranking objective — it is to make explicit which conclusions survive reasonable disagreement on weights, and which do not.

## Baseline

{baseline_table}

## Per-language stability band

{rank_table}

## Robust findings

A finding is "robust" if the language's rank holds across every one of the {n_scenarios} perturbation scenarios (no flip, anywhere, at any +-2.5% or +-5% shift).

{chr(10).join(robust_lines) if robust_lines else "_(none)_"}

## Fragile findings

A finding is "fragile" if the language's rank flips with at least one neighbor under some perturbation. Smaller flip thresholds mean more fragility; the listed flip is the smallest-magnitude perturbation that moved this language away from its baseline rank.

{chr(10).join(fragile_lines) if fragile_lines else "_(none)_"}

## Per-dimension fragility map

Which languages move rank when each dimension's weight is perturbed?

{dim_table}

## How to read this

A "robust" finding can be reported as a fact at v0.6 confidence: it survives every reasonable disagreement about how heavily to weight each dimension. A "fragile" finding should be reported with the perturbation footnote: "this rank holds at the chosen weights; under a +-X% shift on dimension Y, this language and Z swap." Reach/EDR/SV at 5% each are the most easily perturbed knobs; AO at 20% is the most load-bearing.

The robustness band published here is what v0.7 multi-rater work and v0.9 external review will adjust as the weights themselves come under scrutiny.
"""
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(output, encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(ROOT).as_posix()}")
    print(f"  baseline ranks: {[(l, r) for l, _, r in baseline]}")


if __name__ == "__main__":
    main()

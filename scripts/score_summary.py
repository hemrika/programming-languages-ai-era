from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evaluations"

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

def weighted_score(data):
    scores = data.get("scores", {})
    total = 0.0
    for key, weight in WEIGHTS.items():
        total += scores[key]["score"] * weight
    return round(total, 2)

def main():
    rows = []
    for path in sorted(EVAL_DIR.glob("*.yaml")):
        if path.stem not in COHORT:
            continue
        data = yaml.safe_load(path.read_text())
        rows.append((data["language"], weighted_score(data)))

    for language, score in sorted(rows, key=lambda item: item[1], reverse=True):
        print(f"{language}: {score}")

if __name__ == "__main__":
    main()

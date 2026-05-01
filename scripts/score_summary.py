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
    "runtime_ecosystem": 0.15,
    "strategic_viability": 0.10,
    "ai_systems_interoperability": 0.15,
    "structured_output_maturity": 0.10,
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
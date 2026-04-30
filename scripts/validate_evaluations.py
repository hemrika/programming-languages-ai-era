from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evaluations"

REQUIRED_DIMENSIONS = {
    "human_cognition",
    "machine_cognition",
    "ai_agent_operability",
    "runtime_ecosystem",
    "strategic_viability",
}

def validate_file(path: Path) -> list[str]:
    errors = []
    data = yaml.safe_load(path.read_text())

    if not data.get("language"):
        errors.append("missing language")

    scores = data.get("scores")
    if not isinstance(scores, dict):
        errors.append("missing scores")
        return errors

    missing = REQUIRED_DIMENSIONS - scores.keys()
    if missing:
        errors.append(f"missing dimensions: {sorted(missing)}")

    for dimension, value in scores.items():
        score = value.get("score")
        confidence = value.get("confidence")
        justification = value.get("justification")

        if not isinstance(score, int) or score < 1 or score > 5:
            errors.append(f"{dimension}: score must be integer 1-5")
        if confidence not in {"low", "medium", "high"}:
            errors.append(f"{dimension}: confidence must be low/medium/high")
        if not justification:
            errors.append(f"{dimension}: missing justification")

    return errors

def main():
    failed = False
    for path in sorted(EVAL_DIR.glob("*.yaml")):
        errors = validate_file(path)
        if errors:
            failed = True
            print(f"{path}:")
            for error in errors:
                print(f"  - {error}")

    if failed:
        sys.exit(1)

    print("All evaluations valid.")

if __name__ == "__main__":
    main()

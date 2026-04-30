from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evaluations"
CLAIMS_DIR = ROOT / "claims"

REQUIRED_DIMENSIONS = {
    "human_cognition",
    "machine_cognition",
    "ai_agent_operability",
    "runtime_ecosystem",
    "strategic_viability",
}

def load_claims_index(lang: str) -> dict:
    """Return {claim_id: dimension} for the given language, or {} if missing."""
    path = CLAIMS_DIR / f"{lang}.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    index = {}
    for claim in data.get("claims", []) or []:
        cid = claim.get("id")
        dim = claim.get("dimension")
        if cid:
            index[cid] = dim
    return index

def validate_file(path: Path) -> tuple[list[str], int, int]:
    """Validate a single evaluation file. Returns (errors, dims_validated, claim_refs_valid)."""
    errors = []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not data.get("language"):
        errors.append("missing language")

    scores = data.get("scores")
    if not isinstance(scores, dict):
        errors.append("missing scores")
        return errors, 0, 0

    missing = REQUIRED_DIMENSIONS - scores.keys()
    if missing:
        errors.append(f"missing dimensions: {sorted(missing)}")

    lang = path.stem
    claim_index = load_claims_index(lang)

    dims_validated = 0
    claim_refs_valid = 0

    for dimension, value in scores.items():
        score = value.get("score")
        confidence = value.get("confidence")
        justification = value.get("justification")
        supporting_claims = value.get("supporting_claims")

        if not isinstance(score, int) or score < 1 or score > 5:
            errors.append(f"{dimension}: score must be integer 1-5")
        if confidence not in {"low", "medium", "high"}:
            errors.append(f"{dimension}: confidence must be low/medium/high")
        if not justification:
            errors.append(f"{dimension}: missing justification")

        if "supporting_claims" not in value:
            errors.append(f"{dimension}: missing supporting_claims")
            continue
        if not isinstance(supporting_claims, list):
            errors.append(f"{dimension}: supporting_claims must be a list")
            continue

        dims_validated += 1
        for cid in supporting_claims:
            if cid not in claim_index:
                errors.append(f"{dimension}: supporting_claims references unknown id {cid}")
                continue
            actual_dim = claim_index[cid]
            if actual_dim != dimension:
                errors.append(
                    f"{dimension}: claim {cid} has dimension {actual_dim}, "
                    f"does not match referencing dimension {dimension}"
                )
                continue
            claim_refs_valid += 1

    return errors, dims_validated, claim_refs_valid

def main():
    failed = False
    for path in sorted(EVAL_DIR.glob("*.yaml")):
        errors, dims_validated, claim_refs_valid = validate_file(path)
        if errors:
            failed = True
            print(f"{path}:")
            for error in errors:
                print(f"  - {error}")
        else:
            rel = path.relative_to(ROOT).as_posix()
            print(f"{rel}: {dims_validated}/5 dimensions, {claim_refs_valid} claim refs valid")

    if failed:
        sys.exit(1)

    print("All evaluations valid.")

if __name__ == "__main__":
    main()

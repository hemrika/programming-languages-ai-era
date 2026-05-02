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
    "ai_systems_native",
    "ai_systems_ecosystem",
    "structured_output_native",
    "structured_output_ecosystem",
    "ecosystem_dependency_risk",
}

ALLOWED_BACKERS = {
    "language_stewards",
    "commercial_first_party",
    "commercial_third_party",
    "community_multi_maintainer",
    "community_single_maintainer",
    "research",
}

COHORT = {
    "cpp", "dotnet", "elixir", "go", "java",
    "kotlin", "python", "rust", "swift", "typescript",
}

ALLOWED_HALF_SCORES = {1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0}

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

def validate_claims_counters(lang: str) -> tuple[list[str], int]:
    path = CLAIMS_DIR / f"{lang}.yaml"
    errors: list[str] = []
    if not path.exists():
        return errors, 0
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    ids = {c.get("id") for c in (data.get("claims", []) or []) if c.get("id")}
    links = 0
    for claim in data.get("claims", []) or []:
        cid = claim.get("id")
        # Validate backer field if present (introduced in v0.4)
        if "backer" in claim:
            backer = claim["backer"]
            if backer not in ALLOWED_BACKERS:
                errors.append(
                    f"claims/{lang}.yaml::{cid}: backer must be one of "
                    f"{sorted(ALLOWED_BACKERS)}, got {backer!r}"
                )
        if "counters" not in claim:
            continue
        counters = claim["counters"]
        if not isinstance(counters, list):
            errors.append(f"claims/{lang}.yaml::{cid}: counters must be a list")
            continue
        for ref in counters:
            if not isinstance(ref, str):
                errors.append(f"claims/{lang}.yaml::{cid}: counters entry must be a string, got {type(ref).__name__}")
                continue
            if ref not in ids:
                errors.append(f"claims/{lang}.yaml::{cid}: counters references unknown id {ref}")
                continue
            links += 1
    return errors, links

def validate_file(path: Path) -> tuple[list[str], int, int]:
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

        if isinstance(score, bool):
            errors.append(f"{dimension}: score must be a number, not bool")
        elif isinstance(score, int):
            if score < 1 or score > 5:
                errors.append(f"{dimension}: integer score must be 1-5")
        elif isinstance(score, float):
            if score not in ALLOWED_HALF_SCORES:
                errors.append(
                    f"{dimension}: float score must be one of "
                    f"{sorted(ALLOWED_HALF_SCORES)}, got {score}"
                )
        else:
            errors.append(
                f"{dimension}: score must be int 1-5 or float in "
                f"{sorted(ALLOWED_HALF_SCORES)}"
            )
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

    total_counters_links = 0
    for path in sorted(CLAIMS_DIR.glob("*.yaml")):
        lang = path.stem
        if lang not in COHORT:
            continue
        errors, links = validate_claims_counters(lang)
        if errors:
            failed = True
            print(f"{path.relative_to(ROOT).as_posix()} (counters):")
            for error in errors:
                print(f"  - {error}")
        total_counters_links += links

    for path in sorted(EVAL_DIR.glob("*.yaml")):
        if path.stem not in COHORT:
            continue
        errors, dims_validated, claim_refs_valid = validate_file(path)
        if errors:
            failed = True
            print(f"{path}:")
            for error in errors:
                print(f"  - {error}")
        else:
            rel = path.relative_to(ROOT).as_posix()
            print(f"{rel}: {dims_validated}/10 dimensions, {claim_refs_valid} claim refs valid")

    if failed:
        sys.exit(1)

    print(f"All evaluations valid. {total_counters_links} counters links validated.")

if __name__ == "__main__":
    main()

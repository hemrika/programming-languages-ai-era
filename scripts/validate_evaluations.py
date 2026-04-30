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

def validate_claims_counters(lang: str) -> tuple[list[str], int]:
    """Validate the optional `counters:` field on each claim in claims/<lang>.yaml.

    When present, `counters` must be a list of strings, and each ID must
    resolve to a claim in the SAME language's claims file.
    Returns (errors, counters_links_validated).
    """
    path = CLAIMS_DIR / f"{lang}.yaml"
    errors: list[str] = []
    if not path.exists():
        return errors, 0
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    ids = {c.get("id") for c in (data.get("claims", []) or []) if c.get("id")}
    links = 0
    for claim in data.get("claims", []) or []:
        if "counters" not in claim:
            continue
        counters = claim["counters"]
        cid = claim.get("id")
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

    # Validate counters: field across all claim files (same-language reference resolution).
    total_counters_links = 0
    for path in sorted(CLAIMS_DIR.glob("*.yaml")):
        lang = path.stem
        errors, links = validate_claims_counters(lang)
        if errors:
            failed = True
            print(f"{path.relative_to(ROOT).as_posix()} (counters):")
            for error in errors:
                print(f"  - {error}")
        total_counters_links += links

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

    print(f"All evaluations valid. {total_counters_links} counters links validated.")

if __name__ == "__main__":
    main()

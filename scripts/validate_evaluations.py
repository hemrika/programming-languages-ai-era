"""v0.6 schema-lock validator for cohort claims and evaluations.

Errors (exit non-zero):
  - missing dimensions, malformed scores/confidence/justification
  - supporting_claims pointing at unknown ids or wrong-dimension claims
  - counters: links to unknown ids
  - backer not in the allowed set
  - claim missing source: (mandatory in v0.6)
  - positive claim that names a specific library (heuristic) missing backer:
  - evaluation file missing or stale framework_version stamp

Warnings (printed but do not fail the run; raised to errors in a later version):
  - evaluation cell with score >= 4.0 lacking any same-dimension counter-link
    pointing back to one of its supporting_claims (counter-link coverage gap).
"""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evaluations"
CLAIMS_DIR = ROOT / "claims"

# Framework version this validator expects to see stamped on every evaluation
# file. Bumped from v0.5 to v0.6 with the schema lock.
CURRENT_FRAMEWORK_VERSION = "v0.6"

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
    "reachability_to_top_tier",
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

# Library-marker heuristic for the "backer required when claim names a specific
# library" rule. Conservative by design: positive polarity only, and only when
# the claim contains a recognizable third-party SDK / library / package name.
# We do NOT flag negative claims (which often name libraries while asserting
# their absence: "no Pydantic-equivalent for Swift") or claims that merely
# mention a steward-shipped tool. Goal: catch new positive claims that forget
# backer:, not retroactively re-litigate the existing corpus.
LIBRARY_NAME_PATTERNS = [
    re.compile(r"\b(?:[A-Z][a-zA-Z]*){1,3}\.(?:js|ts|net|py|jl)\b"),
    re.compile(r"\bSDK\b"),
    re.compile(
        r"\b(?:Pydantic|FastAPI|LangChain|LangGraph|LlamaIndex|Instructor|Zod|"
        r"Vercel|Serde|schemars|Jackson|Newtonsoft|nlohmann|llama\.cpp|"
        r"Anthropic|OpenAI|Tokio|Axum|Hyper|Tower|Spring|Hibernate|Quarkus|"
        r"Micronaut|Pinecone|Weaviate|Qdrant|Chroma|pgvector|HuggingFace|"
        r"Pkl|Effect|Rig|swiftide|Semantic Kernel)\b"
    ),
]


def names_a_library(claim_text):
    if not isinstance(claim_text, str):
        return False
    return any(p.search(claim_text) for p in LIBRARY_NAME_PATTERNS)


def load_claims_index(lang):
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


def load_claims_full(lang):
    path = CLAIMS_DIR / f"{lang}.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data.get("claims", []) or []


def validate_claims_counters(lang):
    path = CLAIMS_DIR / f"{lang}.yaml"
    errors = []
    if not path.exists():
        return errors, 0
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    claims = data.get("claims", []) or []
    ids = {c.get("id") for c in claims if c.get("id")}
    links = 0
    for claim in claims:
        cid = claim.get("id")
        text = claim.get("claim", "")
        polarity = claim.get("polarity")
        # v0.6: source is mandatory on every claim.
        if not claim.get("source"):
            errors.append(f"claims/{lang}.yaml::{cid}: missing source (required in v0.6)")
        # backer field validation
        if "backer" in claim:
            backer = claim["backer"]
            if backer not in ALLOWED_BACKERS:
                errors.append(
                    f"claims/{lang}.yaml::{cid}: backer must be one of "
                    f"{sorted(ALLOWED_BACKERS)}, got {backer!r}"
                )
        else:
            if polarity == "positive" and names_a_library(text):
                errors.append(
                    f"claims/{lang}.yaml::{cid}: positive claim names a specific "
                    f"library; backer field is required (one of "
                    f"{sorted(ALLOWED_BACKERS)})"
                )
        if "counters" not in claim:
            continue
        counters = claim["counters"]
        if not isinstance(counters, list):
            errors.append(f"claims/{lang}.yaml::{cid}: counters must be a list")
            continue
        for ref in counters:
            if not isinstance(ref, str):
                errors.append(
                    f"claims/{lang}.yaml::{cid}: counters entry must be a string, "
                    f"got {type(ref).__name__}"
                )
                continue
            if ref not in ids:
                errors.append(
                    f"claims/{lang}.yaml::{cid}: counters references unknown id {ref}"
                )
                continue
            links += 1
    return errors, links


def validate_file(path):
    errors = []
    warnings = []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not data.get("language"):
        errors.append("missing language")

    fv = data.get("framework_version")
    if not fv:
        errors.append(
            f"missing framework_version (required in v0.6, expected "
            f"{CURRENT_FRAMEWORK_VERSION})"
        )
    elif fv != CURRENT_FRAMEWORK_VERSION:
        errors.append(
            f"framework_version is {fv!r}, expected {CURRENT_FRAMEWORK_VERSION!r}"
        )

    scores = data.get("scores")
    if not isinstance(scores, dict):
        errors.append("missing scores")
        return errors, warnings, 0, 0

    missing = REQUIRED_DIMENSIONS - scores.keys()
    if missing:
        errors.append(f"missing dimensions: {sorted(missing)}")

    lang = path.stem
    claim_index = load_claims_index(lang)
    full_claims = load_claims_full(lang)

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

        if isinstance(score, (int, float)) and not isinstance(score, bool) and float(score) >= 4.0:
            if isinstance(supporting_claims, list) and supporting_claims:
                supp_set = set(supporting_claims)
                has_counter = False
                for c in full_claims:
                    if c.get("dimension") != dimension:
                        continue
                    ctrs = c.get("counters") or []
                    if any(ref in supp_set for ref in ctrs):
                        has_counter = True
                        break
                if not has_counter:
                    warnings.append(
                        f"{dimension}: score {score} >= 4.0 but no same-dimension "
                        f"counterclaim links back to any of {supporting_claims} "
                        f"(counter-link coverage gap)"
                    )

    return errors, warnings, dims_validated, claim_refs_valid


def main():
    failed = False
    total_warnings = 0

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
        errors, warnings, dims_validated, claim_refs_valid = validate_file(path)
        rel = path.relative_to(ROOT).as_posix()
        if errors:
            failed = True
            print(f"{rel}:")
            for error in errors:
                print(f"  - ERROR {error}")
        else:
            print(f"{rel}: {dims_validated}/11 dimensions, {claim_refs_valid} claim refs valid")
        for w in warnings:
            print(f"  - WARN  {w}")
            total_warnings += 1

    if failed:
        sys.exit(1)

    print(
        f"All evaluations valid. {total_counters_links} counters links validated. "
        f"{total_warnings} warnings (counter-link coverage)."
    )


if __name__ == "__main__":
    main()

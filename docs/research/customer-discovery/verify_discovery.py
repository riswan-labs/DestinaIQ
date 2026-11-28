"""Verify the documentation-only CP-0.3 evidence package."""
import csv
from collections import Counter
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
MARKET_DIMENSIONS = ("demand", "complexity", "season", "value", "data", "acquisition", "opportunity")
SECONDARY_CLASSES = {
    "Official statistical evidence", "Published consumer research",
    "Publicly reported customer experience", "Observed public discussion",
    "Analyst inference", "Unvalidated hypothesis", "Unknown",
}
VOICE_CLASSES = {"Publicly reported customer experience", "Observed public discussion"}
KIT = {
    "RESEARCH_PLAN", "INTERVIEW_GUIDE", "CUSTOMER_SURVEY", "CONCEPT_TESTING",
    "PRICING_RESEARCH", "RECRUITMENT_TEMPLATES", "PARTICIPATION_NOTICE", "ANALYSIS_TEMPLATE",
}


def table(path):
    with path.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file, delimiter="\t"))
    assert rows and all(None not in row and all(row.values()) for row in rows), f"Incomplete table {path.name}"
    return rows


def unique(items, label):
    assert len(items) == len(set(items)), f"Duplicate {label}"
    return set(items)


def read(path):
    return path.read_text(encoding="utf-8")


def known_ids(text, pattern):
    return set(re.findall(rf"\b(?:{pattern})\b", text))


def check_sources(root, pains):
    evidence = table(root / "EVIDENCE_REGISTER.tsv")
    voice = table(root / "CUSTOMER_VOICE.tsv")
    ids = unique([row["evidence_id"] for row in evidence], "evidence ID")
    observations = unique([row["observation_id"] for row in voice], "observation ID")
    sources = {row["evidence_id"]: row for row in evidence}
    assert all(re.fullmatch(r"E\d{2}", key) for key in ids)
    assert all(re.fullmatch(r"V\d{2}", key) for key in observations)
    for row in evidence:
        assert row["classification"] in SECONDARY_CLASSES, "Unauthorized primary evidence classification"
        date.fromisoformat(row["observed_on"])
        url = urlparse(row["url"])
        assert "/user/" not in url.path and "/u/" not in url.path, "Profile URL in evidence"
        if url.scheme:
            assert url.scheme == "https" and url.hostname and not url.username, "Invalid public source URL"
        else:
            assert (root / row["url"]).is_file(), "Broken local evidence source"
    counts = Counter()
    for row in voice:
        assert row["classification"] in VOICE_CLASSES, "Unauthorized voice classification"
        assert row["evidence_id"] in ids and row["url"] == sources[row["evidence_id"]]["url"], "Unknown or mismatched voice source"
        date.fromisoformat(row["observed_on"])
        assert row["theme_code"] in pains and set(row["pain_ids"].split(",")) <= pains, "Unknown pain reference"
        counts[row["evidence_id"]] += 1
    for key, count in counts.items():
        assert sources[key]["sample"] == f"{count} distinct coded units", "Public source count mismatch"
    return ids, observations


def rounded_score(numerator, denominator):
    return str((Decimal(numerator) / denominator).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def check_markets(root, design, evidence):
    methodology = read(root / "METHODOLOGY.md")
    weights = dict((name, int(weight)) for name, weight in re.findall(r"^\| (\w+) \| (\d+) \|", methodology, re.M))
    assert set(weights) == set(MARKET_DIMENSIONS) and sum(weights.values()) == 100, "Invalid market weights"
    markets = table(root / "LAUNCH_MARKET_SCORECARD.tsv")
    assert unique([row["id"] for row in markets], "market ID") == {f"M{i:02}" for i in range(1, 21)}, "Candidate market IDs differ"
    candidate_line = re.search(r"^Candidate markets \(not commitments\): (.+?)\. Maintain", design, re.M)
    candidates = set(candidate_line[1].replace("UAE", "United Arab Emirates").split(", "))
    assert unique([row["market"] for row in markets], "market name") == candidates, "Candidate inventory differs"
    by_cohort = Counter(row["cohort"] for row in markets)
    assert by_cohort == {"First": 3, "Secondary": 7, "Conditional": 10}
    for row in markets:
        settings = {name: row[name] for name in MARKET_DIMENSIONS}
        assert all(value == "U" or re.fullmatch(r"[0-5]", value) for value in settings.values()), "Invalid dimension score"
        chosen = {name: int(value) for name, value in settings.items() if value != "U"}
        refs = known_ids(row["evidence"], r"[EV]\d{2}")
        assert refs <= evidence and (refs or not chosen), "Unsupported market score"
        covered = sum(weights[name] for name in chosen)
        numerator = sum(weights[name] * value for name, value in chosen.items())
        assert row["coverage_pct"] == str(covered), "Unknown values must not contribute weight"
        assert row["normalized"] == (rounded_score(numerator, covered) if covered else "U"), "Incorrect normalized score"
        assert row["sensitivity_low"] == rounded_score(numerator, 100)
        assert row["sensitivity_high"] == rounded_score(numerator + (100-covered)*5, 100)
    return markets


def verify(root=ROOT):
    docs = root.parents[1]
    product = docs / "product"
    design = read(product / "DESIGN.md")
    launch_text = read(product / "LAUNCH_SCOPE.md")
    launch = dict(re.findall(r"^## (L\d{2})\n\n\*\*(.+?)\*\*$", launch_text, re.M))
    assessed = re.findall(r"^\| \[(L\d{2})\]\([^)]+\) · (.+?) \|", read(root / "LAUNCH_CAPABILITY_VALIDATION.md"), re.M)
    assert len(assessed) == len(launch) == 15 and dict(assessed) == launch, "Launch capability coverage differs"
    segments = unique(re.findall(r"^\| (S\d{2}) · ", read(root / "CUSTOMER_SEGMENTS.md"), re.M), "segment ID")
    pains = unique(re.findall(r"^\| (P\d{2}) · ", read(root / "CUSTOMER_PAIN_POINTS.md"), re.M), "pain ID")
    assert segments == {f"S{i:02}" for i in range(1, 13)}
    assert pains == {f"P{i:02}" for i in range(1, 16)}
    evidence, observations = check_sources(root, pains)
    markets = check_markets(root, design, evidence | observations)
    fr = known_ids(read(product / "REQUIREMENTS.md"), r"FR-\d{3}")
    nfr = known_ids(read(docs / "engineering/TRACEABILITY.md"), r"NFR-\d{2}")
    roadmap = read(docs / "engineering/ROADMAP.md")
    checkpoints = known_ids(roadmap, r"CP-\d+\.\d+")
    decisions = known_ids(read(docs / "governance/DECISION_REGISTER.md"), r"D\d{2}")
    risks = known_ids(read(docs / "governance/RISK_REGISTER.md"), r"R\d{2}")
    for path in root.rglob("*.md"):
        content = read(path)
        for pattern, valid in (
            (r"[EV]\d{2}", evidence | observations), (r"FR-\d{3}", fr), (r"NFR-\d{2}", nfr),
            (r"L\d{2}", set(launch)), (r"S\d{2}", segments), (r"P\d{2}", pains),
            (r"CP-\d+\.\d+", checkpoints), (r"D\d{2}", decisions), (r"R\d{2}", risks),
        ):
            missing = known_ids(content, pattern) - valid
            assert not missing, f"Unknown reference in {path.name}: {sorted(missing)}"
    impact = read(root / "REQUIREMENTS_IMPACT.md")
    findings = re.findall(r"^\| (FCD\d{2}) \| .+$", impact, re.M)
    assert len(unique(findings, "finding ID")) >= 7
    assert len(re.findall(r"^\| FCD\d{2} .+\| Pending owner approval \|$", impact, re.M)) == len(findings), "Proposal prematurely approved"
    limitations = read(root / "RESEARCH_LIMITATIONS.md")
    assert "Zero interviews and zero survey responses" in limitations and "20–30 interviews" in limitations
    follow_up = read(root / "FOLLOW_UP.md")
    assert {"CP-0.3", "CP-0.4", "CP-0.8"} <= known_ids(follow_up, r"CP-\d+\.\d+")
    assert {path.stem for path in (root / "primary-research").glob("*.md")} == KIT
    print(f"{len(evidence)} source records; {len(observations)} public observations; zero primary interviews or surveys")
    print(f"{len(segments)} segments, {len(pains)} pains, {len(launch)} launch capabilities, {len(markets)} markets, {len(findings)} pending impacts")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without Python optimization.")
    verify()

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
    "Official statistical evidence", "Published consumer research", "Official transport guidance",
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
    cohorts = {
        "First": {"M02", "M06", "M07"},
        "Stress": {"M01"},
        "Secondary": {"M04", "M08", "M09", "M17", "M18", "M20"},
        "Conditional": {"M03", "M05", "M10", "M11", "M12", "M13", "M14", "M15", "M16", "M19"},
    }
    original = {row["id"]: row for row in table(root / "LAUNCH_MARKET_SCORECARD_INITIAL.tsv")}
    assert set(original) == {row["id"] for row in markets}, "Original market inventory differs"
    # Each changed score is limited to the documented, market-specific evidence for this closure.
    additions = {
        "M01": ("E68", {"complexity": "2", "data": "2"}),
        "M03": ("E55", {"demand": "1", "data": "1"}),
        "M06": ("E67", {"complexity": "3", "data": "2"}),
        "M09": ("E65", {"demand": "4"}),
        "M10": ("E57", {"demand": "4", "data": "1"}),
        "M11": ("E58", {"demand": "3", "data": "1"}),
        "M12": ("E59", {"data": "1"}),
        "M13": ("E60", {"demand": "5", "data": "1"}),
        "M14": ("E61", {"season": "2"}),
        "M15": ("E62", {"season": "2"}),
        "M16": ("E63", {"demand": "5", "data": "1"}),
        "M19": ("E64", {"season": "2"}),
        "M20": ("E66", {"demand": "5"}),
    }
    coverage = read(root / "MARKET_COVERAGE.md")
    covered_markets = re.findall(r"^\| (M\d{2}) · ([^|]+?) \| ([^|]+?) \| (.+) \|$", coverage, re.M)
    assert len(covered_markets) == 20, "Incomplete market coverage register"
    assert {(key, name, geography) for key, name, geography, _ in covered_markets} == {
        (row["id"], row["market"], row["geography"]) for row in markets
    }, "Market coverage register differs"
    assert all(len(details.split(" | ")) == 6 and all(details.split(" | "))
               for _, _, _, details in covered_markets), "Incomplete market dispositions"
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
        key = row["id"]
        assert key in cohorts.get(row["cohort"], set()), "Unauthorized market cohort or launch approval"
        prior = original[key]
        assert row["market"] == prior["market"] and row["geography"] == prior["geography"], "Market identity differs"
        assert known_ids(prior["evidence"], r"[EV]\d{2}") <= refs, "Original market evidence removed"
        source, changes = additions.get(key, (None, {}))
        expected = {name: prior[name] for name in MARKET_DIMENSIONS}
        expected.update(changes)
        assert settings == expected and (source is None or source in refs), "Unsupported market score"
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
    register = read(docs / "governance/DECISION_REGISTER.md")
    decisions = known_ids(register, r"D\d{2}")
    policy = register.partition("\n## D24\n")[2].strip()
    assert policy.startswith("**Approved by the project owner.**"), "Missing closure owner authorization"
    assert "D02 and D03 remain open." in policy and "D01–D18 and D22 remain **Open**." in register
    progress = read(docs / "engineering/PROGRESS.md")
    assert "Current checkpoint status — Under Review" in progress, "Unauthorized CP-0.3 transition"
    for field in (
        "CP-0.3 primary interviews — 0.",
        "CP-0.3 primary survey responses — 0.",
        "CP-0.3 acceptance — Pending owner review.",
    ):
        assert field in progress, "Unverified primary activity or acceptance"
    primary = read(root / "PRIMARY_RESEARCH_FOLLOW_UP.md")
    assert all(label in primary for label in (
        "Completed primary interviews: 0. |", "Completed primary surveys: 0. |",
        "Validated willingness to pay: No. Validated customer demand: No.",
    )), "Unverified primary research completion"
    assert all(label in primary for label in (
        "20–30 completed traveler interviews", "50–100 exploratory responses, subject to owner approval",
        "outside the public repository", "before public V1.0 launch",
        "owner review of actual evidence and explicit approval of limitations",
        "[CP-0.9]", "[CP-6.7]", "[CP-6.11]", "[CP-6.13]", "[CP-6.14]",
    )), "Missing primary research follow-up obligation"
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
    assert unique(findings, "finding ID") == {f"FCD{i:02}" for i in range(1, 8)}
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

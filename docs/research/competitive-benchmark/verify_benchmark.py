"""Check CP-0.2 research evidence and scorecard consistency without third-party packages."""
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
COMPETITORS = {
    "TI": "TRAVEL_INTEL", "TG": "TRIPGUARD_AI", "AU": "AURORA_TRAVEL",
    "SI": "SITATA", "WP": "WARNPOINT", "OR": "OUTROAD",
}
DIMENSIONS = {
    "accuracy": "Accuracy", "coverage": "Coverage", "freshness": "Freshness",
    "personalization": "Personalization", "completeness": "Completeness",
    "ux": "User experience", "transparency": "Source transparency",
    "value": "Pricing and value", "performance": "Observed performance",
}
OUTCOMES = ("Hands-on", "Documentation-only", "Restricted", "Untested")
EVIDENCE_CLASSES = {
    "Hands-on verified", "Official documentation verified", "Vendor-advertised only",
    "Third-party reported", "Access restricted", "Not tested", "Unknown",
}
MATRIX_CLASSES = {
    "Verified supported", "Partially supported", "Advertised but unverified",
    "Verified unsupported", "Unknown or inaccessible",
}
DOMAINS = set("Destination Season Safety Pulse Plan Transit Budget Experience Ready Care Circle Trust".split())


def read(root, name):
    return (root / name).read_text(encoding="utf-8")


def read_rows(root, name):
    with (root / name).open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file, delimiter="\t"))
    assert rows and all(None not in row and all(row.values()) for row in rows), f"Incomplete {name}"
    return rows


def unique(items, label):
    assert len(items) == len(set(items)), f"Duplicate {label}"
    return set(items)


def headings(text, pattern):
    return re.findall(rf"^## ({pattern})$", text, re.M)


def scorecard_rows(text):
    return [
        [cell.strip() for cell in line.strip("|").split("|")]
        for line in text.splitlines()
        if re.match(r"^\| (?:TI|TG|AU|SI|WP|OR) \|", line)
    ]


def verify(root=ROOT):
    repo = root.parents[2]
    methodology = read(root, "METHODOLOGY.md")
    assert "Review policy authorization — CP-0.2 Evidence Closure and Review Finalization, project-owner assignment" in methodology, "Missing owner review policy authorization"
    assert "at most 90 minutes" in methodology
    assert "Owner acceptance — Approved on 2026-11-27 for reviewed commit cad78ba6e9b4019034010a3e7cf3bcbbf9abbd40 in [PR #2]" in methodology
    weight_rows = re.findall(r"^\| ([^|]+?) \| (\d+)% \|", methodology, re.M)
    assert unique([name for name, _ in weight_rows], "dimension") == set(DIMENSIONS.values())
    weights = {name: int(weight) for name, weight in weight_rows}
    assert sum(weights.values()) == 100 and all(weights.values()), "Weights must total 100%"
    research_scenarios = read(root, "SCENARIOS.md")
    scenarios = unique(headings(research_scenarios, r"S\d{2}"), "scenario ID")
    assert scenarios == {f"S{i:02}" for i in range(1, 9)}
    fields = {}
    for scenario in scenarios:
        section = research_scenarios.split(f"## {scenario}\n", 1)[1].split("\n## ", 1)[0]
        fields[scenario] = re.search(r"^Inputs — (.+)\n\nExpected checks — (.+)$", section, re.M).groups()
    assert {path.stem for path in (root / "competitors").glob("*.md")} == set(COMPETITORS.values())

    evidence_rows = read_rows(root, "EVIDENCE_REGISTER.tsv")
    ids = unique([row["evidence_id"] for row in evidence_rows], "evidence ID")
    evidence = {row["evidence_id"]: row for row in evidence_rows}
    impact = read(root, "REQUIREMENTS_IMPACT.md")
    findings = unique(headings(impact, r"F\d{2}"), "finding ID")
    assert findings == {f"F{i:02}" for i in range(1, 14)}
    for row in evidence_rows:
        assert row["competitor"] in COMPETITORS and re.fullmatch(row["competitor"] + r"\d{2}", row["evidence_id"])
        assert row["classification"] in EVIDENCE_CLASSES and row["source_url"].startswith("https://")
        assert datetime.fromisoformat(row["observed_at_utc"]).utcoffset().total_seconds() == 0
        assert set(row["claim_ids"].split(",")) <= findings, "Unknown evidence claim"
    assert {row["competitor"] for row in evidence_rows} == COMPETITORS.keys()

    results = read_rows(root, "SCENARIO_RESULTS.tsv")
    pairs = unique([(row["competitor"], row["scenario"]) for row in results], "competitor scenario")
    assert pairs == {(c, s) for c in COMPETITORS for s in scenarios}, "Incomplete scenario grid"
    scores = set()
    totals = defaultdict(lambda: [0, 0])
    coverage = defaultdict(Counter)
    for row in results:
        competitor, scenario, outcome = (row[field] for field in ("competitor", "scenario", "outcome"))
        assert outcome in OUTCOMES
        assert (row["exact_scenario_inputs"], row["expected_behavior"]) == fields[scenario]
        refs = row["evidence_ids"].split(",")
        assert set(refs) <= ids, "Unknown scenario evidence"
        assert all(evidence[ref]["competitor"] == competitor for ref in refs)
        hands_on = {
            ref for ref in refs if evidence[ref]["classification"] == "Hands-on verified"
            and scenario in evidence[ref]["scenario_or_feature"].split(",")
        }
        if outcome == "Hands-on":
            assert hands_on, "Hands-on scenario requires matching evidence"
        coverage[competitor][outcome] += 1
        for key, name in DIMENSIONS.items():
            value = row[key]
            if value == "N/A":
                continue
            assert outcome == "Hands-on" and hands_on, "Ineligible scenario was scored"
            assert re.fullmatch(r"[0-5]", value), "Score outside 0–5"
            scores.add((competitor, scenario, name, str(weights[name]), value))
            totals[competitor][0] += weights[name]
            totals[competitor][1] += weights[name] * int(value)
    scorecard = scorecard_rows(read(root, "SCORECARD.md"))
    actual_scores = [tuple(row[:5]) for row in scorecard if len(row) == 6]
    assert unique(actual_scores, "scorecard row") == scores, "Score detail differs from results"
    result_index = {(row["competitor"], row["scenario"]): row for row in results}
    for row in scorecard:
        if len(row) == 6:
            refs = {ref.strip() for ref in row[5].split(",")}
            assert refs and refs <= set(result_index[row[0], row[1]]["evidence_ids"].split(","))
    summary = [tuple(row) for row in scorecard if len(row) == 7]
    expected = set()
    for competitor in COMPETITORS:
        denominator, numerator = totals[competitor]
        percentage = f"{100*numerator/(5*denominator):.1f}%" if denominator else "N/A"
        expected.add((competitor, *(str(coverage[competitor][s]) for s in OUTCOMES),
                      f"{denominator}/{100*len(scenarios)}", percentage))
    assert unique(summary, "summary row") == expected, "Weighted summary does not reproduce"

    fr = set(headings(read(repo, "docs/product/REQUIREMENTS.md"), r"FR-\d{3}"))
    nfr = set(re.findall(r"^### (NFR-\d{2})$", read(repo, "docs/engineering/TRACEABILITY.md"), re.M))
    launch = set(headings(read(repo, "docs/product/LAUNCH_SCOPE.md"), r"L\d{2}"))
    matrix = read_rows(root, "CAPABILITY_MATRIX.tsv")
    assert {row["domain"] for row in matrix} == {domain + " IQ" for domain in DOMAINS}
    unique([(row["domain"], row["capability"]) for row in matrix], "matrix capability")
    for row in matrix:
        assert row["destinaiq"] == "Planned by DestinaIQ"
        assert set(row["requirement_ids"].split(",")) <= fr, "Unknown matrix requirement"
        for competitor in COMPETITORS:
            status, _, cited = row[competitor].partition(" (")
            assert status in MATRIX_CLASSES
            refs = set(cited.removesuffix(")").split(",")) if cited else set()
            assert refs <= ids and all(evidence[ref]["competitor"] == competitor for ref in refs)
            assert refs or status == "Unknown or inaccessible"
            if status in {"Verified supported", "Partially supported"}:
                assert any(evidence[ref]["classification"] == "Hands-on verified" for ref in refs)
    assert set(re.findall(r"\bFR-\d{3}\b", impact)) == fr
    assert set(re.findall(r"\bNFR-\d{2}\b", impact)) == nfr
    assert set(re.findall(r"\bL\d{2}\b", impact)) == launch
    for finding in findings:
        section = impact.split(f"## {finding}\n", 1)[1].split("\n## ", 1)[0]
        refs = set(re.search(r"^- Evidence — (.+)\.$", section, re.M)[1].split(","))
        assert refs and refs <= ids, "Unknown finding evidence"
        assert all(finding in evidence[ref]["claim_ids"].split(",") for ref in refs)
        assert len(re.findall(r"^- Review disposition — \S.+$", section, re.M)) == 1, "Missing research disposition"
        assert re.findall(r"^- Approval — (.+)$", section, re.M) == ["Pending owner approval."], "Finding prematurely approved"
    counts = sum(coverage.values(), Counter())
    assert len(evidence) == 46 and tuple(counts[s] for s in OUTCOMES) == (8, 18, 8, 14), "Accepted evidence coverage changed"
    executive = read(root, "EXECUTIVE_SUMMARY.md")
    coverage_text = (
        f"{counts['Hands-on']} partial hands-on, {counts['Documentation-only']} documentation-only, "
        f"{counts['Restricted']} restricted, {counts['Untested']} untested"
    )
    assert "0 fully verified" in executive and "Retain the existing 15 V1.0 launch capabilities without expansion" in executive
    follow_up = read(root, "FOLLOW_UP.md")
    follow_rows = re.findall(r"^\| (Q\d{2}) \| (.+) \|$", follow_up, re.M)
    assert len(unique([key for key, _ in follow_rows], "follow-up ID")) >= 8, "Missing follow-up records"
    for _, cells in follow_rows:
        fields = cells.split(" | ")
        assert len(fields) == 9 and all(fields)
        assert set(re.findall(r"\bS\d{2}\b", fields[0])) <= scenarios
        assert re.search(r"\bS\d{2}\b", fields[0])
        refs = set(re.findall(r"\b(?:TI|TG|AU|SI|WP|OR)\d{2}\b", fields[1]))
        assert refs and refs <= ids, "Unknown follow-up evidence"
        assert re.search(r"\[CP-\d+\.\d+\]", fields[6])
    assert all(f"[{cp}]" in follow_up for cp in ("CP-0.3", "CP-0.4", "CP-0.8"))
    assert coverage_text in executive, "Executive coverage differs from the log"
    print(f"{len(COMPETITORS)} competitors, {len(scenarios)} scenarios, {len(results)} pairs; {coverage_text}")
    print(f"{len(evidence)} evidence records, {len(matrix)} capability rows, {len(findings)} proposals, {len(scores)} scored slices")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run the benchmark verifier without Python optimization.")
    verify()

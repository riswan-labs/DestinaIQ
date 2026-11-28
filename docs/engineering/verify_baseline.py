"""Verify the Checkpoint 0.1 documentation against the archived Design V3 source."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
BASELINE_HASH = "2d831b2f36644b79fc32831d352f3b9548dd67324e3596bbb837c40cf599538c"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def blocks(markdown, heading):
    matches = list(re.finditer(heading, markdown, re.M))
    sections = {
        match[1]: markdown[match.end():matches[index + 1].start()]
        if index + 1 < len(matches) else markdown[match.end():]
        for index, match in enumerate(matches)
    }
    assert len(sections) == len(matches), "Duplicate registry headings"
    return sections


def source_paragraph(node):
    parts = []
    for element in node.iter():
        if element.tag == W + "t":
            parts.append(element.text or "")
        elif element.tag == W + "br" and element.get(W + "type") != "page":
            parts.append("\n")
    return "".join(parts)


def source_documents(original_path=None):
    original = ROOT / "docs/product/design-v3.docx"
    assert sha256(original.read_bytes()).hexdigest() == BASELINE_HASH, "Authoritative DOCX hash mismatch"
    if original_path is not None:
        assert original.read_bytes() == Path(original_path).read_bytes(), "Original DOCX differs"
    with ZipFile(original) as package:
        body = ET.fromstring(package.read("word/document.xml")).find(W + "body")
    design = read("docs/product/DESIGN.md").split("\n## Conversion record\n")[0]
    markdown_blocks = design.strip().split("\n\n")
    required = {}
    launches = {}
    table_count = 0
    position = 0
    section = ""
    for node in body:
        if node.tag == W + "p":
            expected = source_paragraph(node).strip()
            if not expected:
                continue
            if re.match(r"^\d+\. ", expected):
                section = expected.split(".")[0]
            actual = re.sub(r"^#{1,6} ", "", markdown_blocks[position])
            actual = actual.replace("<br>\n", "\n")
            assert actual == expected, (section, expected, actual)
        elif node.tag == W + "tbl":
            table_count += 1
            rows = [
                ["\n".join(source_paragraph(p) for p in c.findall(W + "p"))
                 for c in row.findall(W + "tc")]
                for row in node.findall(W + "tr")
            ]
            actual = markdown_blocks[position].splitlines()
            del actual[1]
            expected_rows = [
                "| " + " | ".join(c.replace("|", r"\|").replace("\n", "<br>") for c in row) + " |"
                for row in rows
            ]
            assert actual == expected_rows, (section, table_count)
            if section == "21":
                for req, title, release, criterion in rows[1:]:
                    assert req not in required
                    required[req] = (title, "V" + release, criterion)
            if section == "16" and rows[0][0] == "Launch ID":
                for launch, _, mapping in rows[1:]:
                    launches[launch] = {f"FR-{number}" for number in re.findall(r"\d{3}", mapping)}
        else:
            continue
        position += 1
    assert position == len(markdown_blocks)
    print(f"DOCX SHA-256 {BASELINE_HASH}; {position} body blocks and {table_count} tables match")
    return required, launches


def heading_anchors(markdown):
    counts = Counter()
    anchors = set()
    for heading in re.findall(r"^#{1,6} (.+)$", markdown, re.M):
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        count = counts[slug]
        anchors.add(f"{slug}-{count}" if count else slug)
        counts[slug] += 1
    return anchors


def check_links():
    files = {p: p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md") if ".git" not in p.parts}
    anchors = {p: heading_anchors(body) for p, body in files.items()}
    total = 0
    for path, body in files.items():
        for link in re.findall(r"\]\(([^)\s]+)\)", body):
            if "://" in link or link.startswith("mailto:"):
                continue
            target, _, anchor = unquote(link).partition("#")
            resolved = (path.parent / target).resolve() if target else path
            assert resolved.is_file(), f"Broken documentation link in {path.relative_to(ROOT)}: {link}"
            assert not anchor or anchor in anchors.get(resolved, set()), (path.relative_to(ROOT), link)
            total += 1
    print(f"{total} internal links and anchors resolve across {len(files)} Markdown files")


CHECKPOINT_COUNTS = (9, 11, 12, 15, 14, 15, 14, 11, 14, 13, 14, 11, 13)
CHECKPOINT_LINK = r"\[(CP-\d+\.\d+)\]"
FR_LINK = r"\[(FR-\d{3})\]"
NFR_LINK = r"\[(NFR-\d{2})\]"
RELEASES = ("V1.0", "V1.1", "V1.2", "V1.3", "V2.0", "V3.0")


def links(pattern, body):
    return set(re.findall(pattern, body))


def field(body, name):
    values = re.findall(rf"^- {re.escape(name)} — (.+)$", body, re.M)
    assert len(values) == 1, f"Missing or duplicate field {name}"
    return values[0]


def rows(markdown, expression):
    parsed = {}
    for line in markdown.splitlines():
        cells = [value.strip() for value in line.strip("|").split("|")]
        match = re.match(expression, cells[0])
        if match:
            key = match[1]
            assert key not in parsed, f"Duplicate table entry {key}"
            parsed[key] = cells
    return parsed


def check_dependencies(graph, label):
    for node, dependencies in graph.items():
        missing = dependencies - graph.keys()
        assert not missing, f"Invalid {label} dependencies for {node}: {sorted(missing)}"
    remaining = set(graph)
    while remaining:
        ready = {node for node in remaining if not (graph[node] & remaining)}
        assert ready, f"{label} dependency cycle among {sorted(remaining)}"
        remaining -= ready


def checkpoint_closure(graph, roots):
    seen = set()
    pending = set(roots)
    while pending:
        current = pending.pop()
        seen.add(current)
        pending.update(graph[current] - seen)
    return seen


def check_roadmap():
    roadmap = read("docs/engineering/ROADMAP.md")
    phases = blocks(roadmap, r"^## Phase (\d+) — .+$")
    assert set(phases) == set(map(str, range(13))), "Expected all 13 engineering phases"
    checkpoints = blocks(roadmap, r"^### (CP-\d+\.\d+)$")
    exact_ids = [
        f"CP-{phase}.{index}"
        for phase, count in enumerate(CHECKPOINT_COUNTS)
        for index in range(1, count + 1)
    ]
    assert list(checkpoints) == exact_ids, "Incorrect checkpoint counts, IDs or order"
    inventory = [line.split("\t") for line in read("docs/engineering/CHECKPOINT_INVENTORY.tsv").splitlines()]
    assert [key for key, _ in inventory] == exact_ids, "Supplied inventory IDs differ"
    for key, title in inventory:
        phase = key.split(".")[0].removeprefix("CP-")
        assert f"### {key}\n" in phases[phase], f"Checkpoint outside its phase: {key}"
        assert f"\n**{title}**\n" in checkpoints[key], f"Supplied title differs: {key}"
    graph = {}
    targets = {}
    for key, body in checkpoints.items():
        for heading in ("Objective", "Scope", "Exclusions", "Deliverables", "Acceptance criteria", "Exit gate"):
            field(body, heading)
        graph[key] = links(CHECKPOINT_LINK, field(body, "Dependencies"))
        assert key == "CP-0.1" or graph[key], f"Missing dependencies for {key}"
        targets[key] = links(r"(V\d\.\d)", field(body, "Target product release"))
        assert targets[key] and targets[key] <= set(RELEASES), f"Invalid target release for {key}"
    check_dependencies(graph, "Checkpoint")
    crosswalk = rows(roadmap, r"^([A-N])$")
    assert set(crosswalk) == set("ABCDEFGHIJKLMN"), "Incomplete A–N crosswalk"
    for key, cells in crosswalk.items():
        mapped = links(CHECKPOINT_LINK, cells[2])
        assert mapped and mapped <= checkpoints.keys(), f"Invalid A–N mapping for {key}"
    progress = read("docs/engineering/PROGRESS.md")
    status = field(progress, "Status")
    assert field(progress, "Current checkpoint") == "CP-0.1" and field(progress, "Current phase").startswith("Phase 0,")
    assert status in {"In Progress", "Under Review", "Accepted"}, "CP-0.1 requires owner acceptance"
    if status == "Accepted":
        assert field(progress, "Project-owner acceptance") == "Approved."
        assert field(progress, "Acceptance date") == "2026-11-27."
        assert field(progress, "Reviewed commit") == "bef820bbf3484c90acf260b724600b23cfb2c7e1."
        assert field(progress, "Pull request") == "[PR #1](https://github.com/riswan-labs/DestinaIQ/pull/1)."
        assert field(progress, "Final owner acceptance and merge authorization") == (
            "Granted for PR #1 after required verification."
        )
    else:
        assert field(progress, "Project-owner acceptance") == "Pending."
        assert field(progress, "Final owner acceptance and merge authorization") == "Pending."
    assert "D20 and D21 approved. D01–D18 and D22 remain open" in field(progress, "Decisions")
    assert field(progress, "Application implementation") == "Not Started."
    assert field(progress, "Application automated verification") == "Pending."
    assert field(progress, "Documentation verification").startswith(
        "Pending" if status == "In Progress" else "Passed"
    ), "Documentation verification conflicts with checkpoint status"
    counts = rows(progress, r"^(\d+)$")
    assert set(counts) == set(phases), "Progress tracker phase inventory differs"
    for phase, expected in enumerate(CHECKPOINT_COUNTS):
        phase_status = f"1 {status}; 8 Not Started" if phase == 0 else "Not Started"
        assert counts[str(phase)][1:] == [str(expected), phase_status], f"Progress tracker mismatch in Phase {phase}"
    for key, body in checkpoints.items():
        expected = status if key == "CP-0.1" else "Not Started"
        assert field(body, "Implementation status") == expected + ".", f"Incorrect implementation status for {key}"
    print(f"{len(checkpoints)} unique checkpoints across 13 phases: {', '.join(map(str, CHECKPOINT_COUNTS))}")
    print(f"{sum(CHECKPOINT_COUNTS[:7])} pre-launch phase entries, {sum(CHECKPOINT_COUNTS[7:])} post-launch phase entries")
    print(f"{sum(map(len, graph.values()))} valid checkpoint dependency edges, no cycles, and all 14 A–N mappings")
    return checkpoints, graph, targets


def check_traceability(source, launches):
    checkpoints, graph, targets = check_roadmap()
    requirements = blocks(read("docs/product/REQUIREMENTS.md"), r"^## (FR-\d{3})$")
    scope_doc = read("docs/product/LAUNCH_SCOPE.md")
    scope = blocks(scope_doc.split("\n## Launch controls", 1)[0], r"^## (L\d{2})$")
    gates = blocks(read("docs/product/RELEASE_STRATEGY.md"), r"^## Gate (V\d\.\d)$")
    trace = read("docs/engineering/TRACEABILITY.md")
    assert "All release gates are pending." in read("docs/product/RELEASE_STRATEGY.md")
    controls = blocks(trace, r"^### (NFR-\d{2})$")
    index = rows(trace.split("## Non-functional register")[0], r"^\[(FR-\d{3})\]")
    recon = rows(read("docs/product/RELEASE_RECONCILIATION.md"), r"^\[(FR-\d{3})\]")
    decisions = read("docs/governance/DECISION_REGISTER.md")
    decision_sections = blocks(decisions, r"^## (D\d{2})$")
    assert set(decision_sections) == {"D19", "D20", "D21", "D22"}
    for decision in ("D19", "D20", "D21"):
        assert decision_sections[decision].lstrip().startswith("**Approved by the project owner.**"), (
            f"Incorrect approval status for {decision}"
        )
    assert decision_sections["D22"].lstrip().startswith("**Open.**")
    decision_rows = rows(decisions, r"^(D\d{2})$")
    assert set(decision_rows) == {f"D{i:02}" for i in range(1, 19)}
    assert "D01–D18 and D22 remain **Open**." in decisions
    deferred_conditions = "explicit owner authorization, security and privacy assessment, commercial justification and applicable release gates"
    assert deferred_conditions in decision_rows["D17"][2]
    for fact in (
        f"{len(CHECKPOINT_COUNTS)} engineering phases", f"{sum(CHECKPOINT_COUNTS)} engineering checkpoints",
        f"{sum(CHECKPOINT_COUNTS[:7])} pre-launch checkpoints", f"{sum(CHECKPOINT_COUNTS[7:])} post-launch checkpoints",
        f"{len(source)} functional requirements", f"{len(controls)} non-functional requirements",
        f"{len(launches)} launch capabilities",
    ):
        assert fact in decision_sections["D20"], f"Incorrect approved baseline: {fact}"
    assert all(phrase in decision_sections["D21"] for phrase in (
        "explicit task-level authorization", "verified dependencies", "bounded pull request scope",
    ))
    assert set(requirements) == set(source) == {f"FR-{i:03}" for i in range(1, 81)}
    assert set(index) == set(recon) == set(source), "Missing FR table mappings"
    assert set(gates) == set(RELEASES)
    assert set(controls) == {f"NFR-{i:02}" for i in range(1, 15)}
    assert set(scope) == set(launches) == {f"L{i:02}" for i in range(1, 16)}
    readiness = {}
    for release, body in gates.items():
        exits = links(CHECKPOINT_LINK, re.search(r"^Exit checkpoints (.+)$", body, re.M)[1])
        assert exits and exits <= checkpoints.keys() and all(release in targets[c] for c in exits)
        readiness[release] = checkpoint_closure(graph, exits)
        for checkpoint in readiness[release]:
            assert min(RELEASES.index(r) for r in targets[checkpoint]) <= RELEASES.index(release), (
                f"{release} depends on later-release checkpoint {checkpoint}"
            )
        assert links(FR_LINK, body) == {req for req, (_, r, _) in source.items() if r == release}, (
            f"Inconsistent release assignments in {release} gate"
        )

    roles = ("FR primary", "FR support", "FR verification", "NFR implementation", "NFR verification")
    reverse = {cp: {role: set() for role in roles} for cp in checkpoints}
    fr_dependencies = {}
    release_counts = Counter()
    mapped = {}
    approved_slices = {
        "FR-022": "V1.1", "FR-025": "V1.1", "FR-030": "V1.1", "FR-050": "V1.2",
        "FR-054": "V1.3", "FR-055": "V1.1", "FR-056": "V1.1",
    }
    approved_rows = rows(decision_sections["D21"], r"^(FR-\d{3}) ")
    assert {req: cells[1] for req, cells in approved_rows.items()} == approved_slices
    deferred = {f"FR-{n:03}" for n in range(67, 73)}
    for req, (title, release, criterion) in source.items():
        body = requirements[req]
        assert f"**{title}**" in body and field(body, "Acceptance criterion") == criterion
        assert links(r"\[Gate (V\d\.\d)\]", field(body, "Target release and gate")) == {release}, (
            f"Inconsistent release assignment for {req}"
        )
        mapping = [
            links(CHECKPOINT_LINK, field(body, name))
            for name in ("Primary implementation", "Supporting implementation", "Verification checkpoint")
        ]
        primary, supporting, verification = mapping
        assert len(primary) == len(verification) == 1 and supporting, f"Missing requirement mappings for {req}"
        assert primary.isdisjoint(supporting), f"Repeated primary as supporting for {req}"
        all_mapped = primary | supporting | verification
        assert all_mapped <= checkpoints.keys(), f"Invalid checkpoint references for {req}"
        assert all_mapped <= readiness[release], (
            f"{req} mapped outside its {release} release gate: {sorted(all_mapped - readiness[release])}"
        )
        for role, group in zip(roles, mapping):
            for checkpoint in group:
                reverse[checkpoint][role].add(req)
        mapped[req] = mapping
        assert [links(CHECKPOINT_LINK, cell) for cell in index[req][2:5]] == mapping
        assert index[req][5] == f"TEST-{req} pending" and f"[Gate {release}]" in index[req][6]
        assert field(body, "Verification").startswith("Pending automated verification with ")
        assert f"TEST-{req}." in field(body, "Verification")
        assert field(body, "Status") == "Not Started"
        assert re.search(r"^.+, P[0-3]", field(body, "Domain and priority"))
        dependency = field(body, "Dependencies")
        prerequisite_checkpoints = links(CHECKPOINT_LINK, dependency)
        assert supporting <= prerequisite_checkpoints <= checkpoints.keys()
        fr_dependencies[req] = links(FR_LINK, dependency)
        assert recon[req][1] == recon[req][3] == release, f"Inconsistent reconciliation release for {req}"
        assert links(CHECKPOINT_LINK, recon[req][2]) == primary and len(recon[req]) == 7
        assert all(recon[req][4:])
        if req in approved_slices:
            assert release == approved_slices[req] and recon[req][6] == "Approved scheduling (D21)", (
                f"Incorrect scheduling approval for {req}"
            )
        if req in deferred:
            assert release == "V3.0" and recon[req][6] == "Open scope" and "D17" in recon[req][5]
            assert deferred_conditions in recon[req][5]
            assert (primary | verification).isdisjoint(set().union(*(readiness[r] for r in RELEASES[:-1])))
        release_counts[release] += 1

    check_dependencies(fr_dependencies, "FR")
    for req, dependencies in fr_dependencies.items():
        assert all(RELEASES.index(source[d][1]) <= RELEASES.index(source[req][1]) for d in dependencies), (
            f"{req} depends on a later-release FR"
        )
    for launch, expected in launches.items():
        body = scope[launch]
        found = links(FR_LINK, body)
        assert found == expected, f"Missing or incorrect launch capability mapping for {launch}"
        assert all(source[req][1] == "V1.0" and f"[{launch}]" in requirements[req] for req in found)
        delivery, verification = re.search(r"Delivery (.+)\. Verification (.+)\.", body).groups()
        assert links(CHECKPOINT_LINK, delivery) == set().union(*(mapped[r][0] | mapped[r][1] for r in found))
        assert links(CHECKPOINT_LINK, verification) == set().union(*(mapped[r][2] for r in found))
    support = links(FR_LINK, scope_doc.split("## Launch controls", 1)[1].split("## Coverage", 1)[0])
    assert support == {"FR-023", "FR-024", "FR-026", "FR-028", "FR-029"}
    assert set().union(*launches.values(), support) == {r for r, (_, release, _) in source.items() if release == "V1.0"}

    for req, body in controls.items():
        field(body, "Acceptance")
        assert f"TEST-{req} pending" in field(body, "Verification")
        assert field(body, "Status") == "Not Started"
        for role, name in zip(roles[3:], ("Implementation checkpoints", "Verification checkpoints")):
            mapping = links(CHECKPOINT_LINK, field(body, name))
            assert mapping and mapping <= checkpoints.keys(), f"Missing or invalid {req} {name}"
            for checkpoint in mapping:
                reverse[checkpoint][role].add(req)
        linked_releases = links(r"\[Gate (V\d\.\d)\]", field(body, "Release gates"))
        assert linked_releases and linked_releases == {
            release for release, gate in gates.items() if req in links(NFR_LINK, gate)
        }
    for cp, assignments in reverse.items():
        for role, expected in assignments.items():
            pattern = FR_LINK if role in roles[:3] else NFR_LINK
            assert links(pattern, field(checkpoints[cp], role)) == expected, (
                f"Broken bidirectional mapping for {cp} {role}"
            )

    print("80 FRs with primary, supporting and verification mappings; 14 NFRs with implementation and verification mappings")
    print("15 launch capabilities, six source release gates, seven approved cross-phase FRs and six deferred scope FRs")
    print("Release counts " + ", ".join(f"{release}={count}" for release, count in sorted(release_counts.items())))


def main():
    if not __debug__:
        raise SystemExit("Run the verification without Python optimization.")
    source, launches = source_documents(sys.argv[1] if len(sys.argv) == 2 else None)
    check_traceability(source, launches)
    check_links()


if __name__ == "__main__":
    main()

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


def source_documents():
    original = ROOT / "docs/product/design-v3.docx"
    assert sha256(original.read_bytes()).hexdigest() == BASELINE_HASH
    if len(sys.argv) == 2:
        assert original.read_bytes() == Path(sys.argv[1]).read_bytes()
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
            assert resolved.is_file(), (path.relative_to(ROOT), link)
            assert not anchor or anchor in anchors.get(resolved, set()), (path.relative_to(ROOT), link)
            total += 1
    print(f"{total} internal links and anchors resolve across {len(files)} Markdown files")


def check_traceability(source, launches):
    requirements = blocks(read("docs/product/REQUIREMENTS.md"), r"^## (FR-\d{3})$")
    scope = blocks(read("docs/product/LAUNCH_SCOPE.md"), r"^## (L\d{2})$")
    roadmap = read("docs/engineering/ROADMAP.md")
    checkpoints = blocks(roadmap, r"^### (CP-\d+\.\d+)$")
    release_strategy = read("docs/product/RELEASE_STRATEGY.md")
    gates = blocks(release_strategy, r"^## Gate (V\d\.\d)$")
    trace = read("docs/engineering/TRACEABILITY.md")
    controls = blocks(trace, r"^### (NFR-\d{2})$")
    assert set(requirements) == set(source) == {f"FR-{i:03}" for i in range(1, 81)}
    assert len(gates) == 6 and len(controls) == 14
    assert set(scope) == set(launches) == {f"L{i:02}" for i in range(1, 16)}
    assert set(re.findall(r"^\| ([A-N]) \|", roadmap, re.M)) == set("ABCDEFGHIJKLMN")
    assert set(re.findall(r"^## Phase (\d+) ", roadmap, re.M)) == set(map(str, range(13)))
    release_counts = Counter()
    dependency_graph = {}
    for req, (title, release, criterion) in source.items():
        section = requirements[req]
        assert f"**{title}**" in section
        assert f"- Acceptance criterion — {criterion}\n" in section
        assert f"[Gate {release}]" in section and f"[{req}]" in gates[release]
        checkpoint = re.search(r"- Implementation phase and checkpoint — Phase (\d+), \[(CP-\d+\.\d+)\]", section)
        assert checkpoint and checkpoint[2].startswith(f"CP-{checkpoint[1]}.")
        assert f"[{req}]" in checkpoints[checkpoint[2]]
        assert f"TEST-{req}." in section and f"TEST-{req} pending" in trace
        assert "- Status — Not Started" in section
        assert re.search(r"^- Domain and priority — .+, P[0-3]", section, re.M)
        deps = re.search(r"^- Dependencies — (.+)$", section, re.M)
        assert deps
        dependency_graph[req] = re.findall(r"\[(FR-\d{3})\]", deps[1])
        assert all(dep in requirements for dep in dependency_graph[req])
        release_counts[release] += 1
    remaining = set(dependency_graph)
    while remaining:
        resolved = {req for req in remaining if not remaining.intersection(dependency_graph[req])}
        assert resolved, f"FR dependency cycle among {sorted(remaining)}"
        remaining -= resolved
    for launch, ids in launches.items():
        mapping = set(re.findall(r"\[(FR-\d{3})\]", scope[launch].split("\n## ", 1)[0]))
        assert mapping == ids, (launch, mapping, ids)
        assert all(f"[{launch}]" in requirements[req] for req in ids)
    for nfr, section in controls.items():
        assert "- Acceptance — " in section and f"TEST-{nfr} pending" in section
        checkpoint = re.search(r"\[(CP-\d+\.\d+)\]", section)[1]
        assert f"[{nfr}]" in checkpoints[checkpoint]
        assert any(f"[{nfr}]" in gate for gate in gates.values())
    print(f"80 FRs, 80 unique IDs and 80 criteria, release and checkpoint assignments; {len(launches)} launch capabilities")
    print(f"{len(controls)} NFRs, {len(checkpoints)} checkpoints, 13 phases, 14 A–N mappings; no missing references or FR dependency cycles")
    print("Release counts " + ", ".join(f"{release}={count}" for release, count in sorted(release_counts.items())))


if __name__ == "__main__":
    reqs, launch_scope = source_documents()
    check_traceability(reqs, launch_scope)
    check_links()

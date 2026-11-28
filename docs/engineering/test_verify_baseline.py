"""Mutation tests for the documentation verifier. Each case uses an isolated copy."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import verify_baseline as verifier

ROADMAP = "docs/engineering/ROADMAP.md"
REQS = "docs/product/REQUIREMENTS.md"
LAUNCH = "docs/product/LAUNCH_SCOPE.md"
RECON = "docs/product/RELEASE_RECONCILIATION.md"


class BaselineVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        shutil.copytree(verifier.ROOT / "docs", self.root / "docs")
        for path in verifier.ROOT.glob("*.md"):
            shutil.copyfile(path, self.root / path.name)
        mock = patch.object(verifier, "ROOT", self.root)
        mock.start()
        self.addCleanup(mock.stop)

    def edit(self, path, old, new):
        file = self.root / path
        before = file.read_text(encoding="utf-8")
        self.assertIn(old, before)
        file.write_text(before.replace(old, new, 1), encoding="utf-8")

    def verify(self):
        with redirect_stdout(StringIO()):
            source, launch = verifier.source_documents()
            verifier.check_traceability(source, launch)
            verifier.check_links()

    def reject(self, reason):
        with self.assertRaisesRegex(AssertionError, reason):
            self.verify()

    def test_unmodified_baseline_passes(self):
        self.verify()

    def test_duplicate_requirement_identifier(self):
        self.edit(REQS, "## FR-002\n", "## FR-001\n")
        self.reject("Duplicate registry headings")

    def test_duplicate_checkpoint_identifier(self):
        self.edit(ROADMAP, "### CP-0.3\n", "### CP-0.2\n")
        self.reject("Duplicate registry headings")

    def test_missing_requirement_mapping(self):
        self.edit(
            REQS,
            "- Primary implementation — [CP-2.9](../engineering/ROADMAP.md#cp-29)",
            "- Primary implementation — Unassigned",
        )
        self.reject("Missing requirement mappings")

    def test_invalid_checkpoint_reference(self):
        self.edit(ROADMAP, "- Dependencies — [CP-0.1](#cp-01)", "- Dependencies — [CP-99.1](#cp-991)")
        self.reject("Invalid Checkpoint dependencies")

    def test_circular_checkpoint_dependencies(self):
        self.edit(ROADMAP, "- Dependencies — [CP-0.1](#cp-01)", "- Dependencies — [CP-0.2](#cp-02)")
        self.reject("Checkpoint dependency cycle")

    def test_missing_launch_capability_mapping(self):
        self.edit(LAUNCH, "[FR-001](../product/REQUIREMENTS.md#fr-001), ", "")
        self.reject("Missing or incorrect launch capability mapping")

    def test_inconsistent_release_assignment(self):
        self.edit(
            RECON,
            "| V1.1 | [CP-5.4](../engineering/ROADMAP.md#cp-54) | V1.1 |",
            "| V1.1 | [CP-5.4](../engineering/ROADMAP.md#cp-54) | V1.0 |",
        )
        self.reject("Inconsistent reconciliation release for FR-022")

    def test_broken_documentation_link(self):
        self.edit("README.md", "(docs/product/DESIGN.md)", "(docs/product/missing.md)")
        self.reject("Broken documentation link")

    def test_incorrect_checkpoint_count(self):
        self.edit(ROADMAP, "### CP-12.13\n", "#### CP-12.13\n")
        self.reject("Incorrect checkpoint counts")

    def test_unauthorized_docx_change(self):
        archive = self.root / "docs/product/design-v3.docx"
        archive.write_bytes(archive.read_bytes() + b"changed")
        self.reject("Authoritative DOCX hash mismatch")

    def test_missing_reverse_mapping(self):
        self.edit(
            ROADMAP,
            "- FR primary — [FR-001](../product/REQUIREMENTS.md#fr-001).",
            "- FR primary — None directly assigned.",
        )
        self.reject("Broken bidirectional mapping")

    def test_incorrect_scheduling_approval(self):
        self.edit(RECON, "| Approved scheduling (D21) |", "| Approved |")
        self.reject("Incorrect scheduling approval for FR-022")

    def test_incorrect_approved_checkpoint_total(self):
        self.edit("docs/governance/DECISION_REGISTER.md", "166 engineering checkpoints", "162 engineering checkpoints")
        self.reject("Incorrect approved baseline")

    def test_reopened_scheduling_decision(self):
        self.edit(
            "docs/governance/DECISION_REGISTER.md",
            "## D21\n\n**Approved by the project owner.**",
            "## D21\n\n**Open.**",
        )
        self.reject("Incorrect approval status for D21")

    def test_missing_nonfunctional_verification(self):
        self.edit(
            "docs/engineering/TRACEABILITY.md",
            "- Verification checkpoints — [CP-6.5](ROADMAP.md#cp-65).",
            "- Verification checkpoints — Unassigned.",
        )
        self.reject("Missing or invalid NFR-01 Verification checkpoints")

    def test_later_feature_added_to_launch_exit(self):
        self.edit(
            ROADMAP,
            "- Dependencies — [CP-6.13](#cp-613)",
            "- Dependencies — [CP-6.13](#cp-613), [CP-5.4](#cp-54)",
        )
        self.reject("V1.0 depends on later-release checkpoint CP-5.4")

    def test_unauthorized_progress(self):
        for status in ("In Progress", "Blocked", "Under Review"):
            field = f"- Implementation status — {status}."
            if field in (self.root / ROADMAP).read_text(encoding="utf-8"):
                self.edit(ROADMAP, field, "- Implementation status — Accepted.")
                break
        self.reject("Incorrect implementation status for CP-0.2")


if __name__ == "__main__":
    unittest.main()

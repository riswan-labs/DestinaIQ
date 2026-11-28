"""Regression fixtures for CP-0.3 documentation checks."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest

import verify_discovery as discovery

EVIDENCE = "EVIDENCE_REGISTER.tsv"
VOICE = "CUSTOMER_VOICE.tsv"
MARKETS = "LAUNCH_MARKET_SCORECARD.tsv"


class DiscoveryVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.docs = Path(temporary.name) / "docs"
        self.root = self.docs / "research/customer-discovery"
        source_docs = discovery.ROOT.parents[1]
        for name in ("product", "engineering", "governance"):
            shutil.copytree(source_docs / name, self.docs / name, ignore=shutil.ignore_patterns("__pycache__"))
        (self.docs / "research/competitive-benchmark").mkdir(parents=True)
        shutil.copyfile(source_docs / "research/competitive-benchmark/README.md",
                        self.docs / "research/competitive-benchmark/README.md")
        shutil.copytree(discovery.ROOT, self.root, ignore=shutil.ignore_patterns("__pycache__"))

    def edit(self, name, old, new):
        path = self.root / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def reject(self, reason):
        with redirect_stdout(StringIO()), self.assertRaisesRegex(AssertionError, reason):
            discovery.verify(self.root)

    def test_baseline(self):
        with redirect_stdout(StringIO()):
            discovery.verify(self.root)

    def test_duplicate_evidence(self):
        self.edit(EVIDENCE, "\nE02\t", "\nE01\t")
        self.reject("Duplicate evidence ID")

    def test_unapproved_primary_class(self):
        self.edit(EVIDENCE, "Official statistical evidence", "Primary interview evidence")
        self.reject("Unauthorized primary evidence classification")

    def test_unlinked_voice(self):
        self.edit(VOICE, "\nV01\tE25\t", "\nV01\tE99\t")
        self.reject("Unknown or mismatched voice source")

    def test_invalid_pain_reference(self):
        self.edit(VOICE, "\tP09\t", "\tP99\t")
        self.reject("Unknown pain reference")

    def test_missing_market(self):
        path = self.root / MARKETS
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        self.reject("Candidate market IDs differ")

    def test_unknown_treated_as_zero(self):
        self.edit(MARKETS, "Sovereign city-state\t4\t3\tU", "Sovereign city-state\t4\t3\t0")
        self.reject("Unknown values must not contribute weight")

    def test_score_arithmetic(self):
        self.edit(MARKETS, "\t80\t3.19\t2.55\t3.55\t", "\t80\t3.00\t2.55\t3.55\t")
        self.reject("Incorrect normalized score")

    def test_weight_sum(self):
        self.edit("METHODOLOGY.md", "| demand | 25 |", "| demand | 24 |")
        self.reject("Invalid market weights")

    def test_authoritative_capability_title(self):
        self.edit("LAUNCH_CAPABILITY_VALIDATION.md", " · Basic AI itinerary planning |", " · Autonomous booking |")
        self.reject("Launch capability coverage differs")

    def test_specification_proposal_approval(self):
        self.edit("REQUIREMENTS_IMPACT.md", "| Pending owner approval |", "| Approved |")
        self.reject("Proposal prematurely approved")

    def test_unmapped_followup(self):
        self.edit("FOLLOW_UP.md", "[CP-0.8]", "[CP-99.1]")
        self.reject("Unknown reference in FOLLOW_UP.md")

    def test_fabricated_primary_completion(self):
        self.edit("PRIMARY_RESEARCH_FOLLOW_UP.md", "Completed primary interviews: 0.", "Completed primary interviews: 20.")
        self.reject("Unverified primary research completion")

    def test_unsupported_score_with_correct_arithmetic(self):
        self.edit(MARKETS, "federation\tU\tU\tU\tU\tU\tU\tU\t0\tU\t0.00\t5.00",
                  "federation\t1\tU\tU\tU\tU\tU\tU\t25\t1.00\t0.25\t4.00")
        self.reject("Unsupported market score")

    def test_market_approval(self):
        self.edit(MARKETS, "\tStress\t", "\tApproved for launch\t")
        self.reject("Unauthorized market cohort or launch approval")

    def test_missing_followup_gate(self):
        self.edit("PRIMARY_RESEARCH_FOLLOW_UP.md", "[CP-6.14]", "[CP-6.12]")
        self.reject("Missing primary research follow-up obligation")

    def test_unauthorized_checkpoint_acceptance(self):
        self.edit("../../engineering/PROGRESS.md", "Current checkpoint status — Under Review", "Current checkpoint status — Accepted")
        self.reject("Unauthorized CP-0.3 transition")

    def test_owner_authorization_required(self):
        decision = self.root / "../../governance/DECISION_REGISTER.md"
        self.edit(decision, "## D24\n\n**Approved by the project owner.**", "## D24\n\n**Proposed.**")
        self.reject("Missing closure owner authorization")


if __name__ == "__main__":
    unittest.main()

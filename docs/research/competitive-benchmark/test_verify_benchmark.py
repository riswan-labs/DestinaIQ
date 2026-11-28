"""Negative cases use isolated research fixtures and preserve baseline files."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest

import verify_benchmark as benchmark

EVIDENCE = "EVIDENCE_REGISTER.tsv"
RESULTS = "SCENARIO_RESULTS.tsv"


class BenchmarkVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name) / "repo"
        self.root = self.repo / "docs/research/competitive-benchmark"
        shutil.copytree(benchmark.ROOT, self.root, ignore=shutil.ignore_patterns("__pycache__"))
        for name in ("docs/product/REQUIREMENTS.md", "docs/product/LAUNCH_SCOPE.md", "docs/engineering/TRACEABILITY.md"):
            path = self.repo / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(benchmark.ROOT.parents[2] / name, path)

    def replace(self, name, old, new):
        file = self.root / name
        content = file.read_text(encoding="utf-8")
        self.assertIn(old, content)
        file.write_text(content.replace(old, new, 1), encoding="utf-8")

    def reject(self, reason):
        with redirect_stdout(StringIO()), self.assertRaisesRegex(AssertionError, reason):
            benchmark.verify(self.root)

    def test_unchanged_benchmark(self):
        with redirect_stdout(StringIO()):
            benchmark.verify(self.root)

    def test_duplicate_evidence(self):
        self.replace(EVIDENCE, "TI02\tTI\t", "TI01\tTI\t")
        self.reject("Duplicate evidence ID")

    def test_duplicate_scenario(self):
        self.replace("SCENARIOS.md", "## S02", "## S01")
        self.reject("Duplicate scenario ID")

    def test_duplicate_finding(self):
        self.replace("REQUIREMENTS_IMPACT.md", "## F02", "## F01")
        self.reject("Duplicate finding ID")

    def test_missing_pair(self):
        file = self.root / RESULTS
        lines = file.read_text(encoding="utf-8").splitlines()
        file.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        self.reject("Incomplete scenario grid")

    def test_missing_evidence(self):
        self.replace(RESULTS, "TI03,TI11,TI02,TI15\t", "TI03,TI99\t")
        self.reject("Unknown scenario evidence")

    def test_untested_zero(self):
        file = self.root / RESULTS
        lines = file.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            if line.startswith("TI\tS06\t"):
                lines[index] = line.removesuffix("\tN/A") + "\t0"
        file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.reject("Ineligible scenario was scored")

    def test_score_out_of_range(self):
        self.replace(RESULTS, "\t5\tN/A\tN/A\n", "\t6\tN/A\tN/A\n")
        self.reject("Score outside")

    def test_invalid_weights(self):
        self.replace("METHODOLOGY.md", "| Accuracy | 20% |", "| Accuracy | 19% |")
        self.reject("Weights must total 100%")

    def test_incorrect_weighted_result(self):
        self.replace("SCORECARD.md", "40/800 | 100.0%", "40/800 | 99.0%")
        self.reject("Weighted summary does not reproduce")

    def test_premature_approval(self):
        self.replace("REQUIREMENTS_IMPACT.md", "Approval — Pending owner approval.", "Approval — Approved.")
        self.reject("Finding prematurely approved")

    def test_missing_review_policy_authorization(self):
        self.replace("METHODOLOGY.md", "project-owner assignment", "unattributed assignment")
        self.reject("Missing owner review policy authorization")

    def test_missing_follow_up_disposition(self):
        file = self.root / "FOLLOW_UP.md"
        lines = file.read_text(encoding="utf-8").splitlines()
        file.write_text("\n".join(line for line in lines if not line.startswith("| Q01 |")) + "\n", encoding="utf-8")
        self.reject("Missing follow-up records")

    def test_bad_requirement(self):
        self.replace("CAPABILITY_MATRIX.tsv", "FR-001,FR-002,FR-003", "FR-001,FR-002,FR-999")
        self.reject("Unknown matrix requirement")


if __name__ == "__main__":
    unittest.main()

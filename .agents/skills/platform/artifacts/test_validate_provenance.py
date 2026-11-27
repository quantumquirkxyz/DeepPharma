import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from validate_provenance import _digest_file, validate_artifact, write_report


class ArtifactProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.source = self.root / "docs" / "requirements" / "source.md"
        self.source.parent.mkdir(parents=True)
        self.source.write_text("approved source\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def artifact(self, digest=None):
        digest = digest or _digest_file(self.source)
        path = self.root / "artifact.json"
        path.write_text(
            json.dumps(
                {
                    "artifactType": "requirements-artifact",
                    "sourceArtifacts": ["docs/requirements/source.md"],
                    "sourceDigests": {"docs/requirements/source.md": digest},
                }
            ),
            encoding="utf-8",
        )
        return path

    def test_matching_digest_passes(self):
        result = validate_artifact(self.artifact(), self.root)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["checks"][0]["status"], "passed")

    def test_digest_mismatch_fails(self):
        wrong = "sha256:" + "0" * 64
        result = validate_artifact(self.artifact(wrong), self.root)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["checks"][0]["status"], "mismatch")

    def test_missing_source_fails_without_exception(self):
        artifact = self.artifact()
        self.source.unlink()
        result = validate_artifact(artifact, self.root)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["checks"][0]["status"], "missing-source")

    def test_invalid_json_is_reported(self):
        path = self.root / "broken.json"
        path.write_text("{broken", encoding="utf-8")
        result = validate_artifact(path, self.root)
        self.assertEqual(result["status"], "invalid")
        self.assertTrue(result["errors"])

    def test_report_is_written_atomically(self):
        report_path = self.root / "reports" / "provenance.json"
        report = validate_artifact(self.artifact(), self.root)
        write_report(report_path, report)
        saved = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(saved["reportType"], "artifact-provenance-validation")
        self.assertEqual(saved["status"], "passed")


if __name__ == "__main__":
    unittest.main()

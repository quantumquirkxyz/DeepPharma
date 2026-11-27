#!/usr/bin/env python3
"""Validate source provenance for a JSON artifact.

The validator deliberately has no third-party dependencies so it can be used
by local gates and CI before the rest of the project is installed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SHA256_PREFIX = "sha256:"
SHA256_LENGTH = len(SHA256_PREFIX) + 64


@dataclass(frozen=True)
class Check:
    source: str
    status: str
    expected: str | None = None
    actual: str | None = None
    error: str | None = None

    def as_dict(self) -> dict[str, str]:
        result = {"source": self.source, "status": self.status}
        for key, value in (
            ("expected", self.expected),
            ("actual", self.actual),
            ("error", self.error),
        ):
            if value is not None:
                result[key] = value
        return result


def _is_sha256(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != SHA256_LENGTH:
        return False
    digest = value.removeprefix(SHA256_PREFIX)
    return value.startswith(SHA256_PREFIX) and all(
        character in "0123456789abcdef" for character in digest
    )


def _digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"{SHA256_PREFIX}{digest.hexdigest()}"


def _artifact_digest(artifact: dict[str, Any]) -> str:
    """Hash the artifact excluding a self-referential artifactDigest field."""
    canonical = dict(artifact)
    canonical.pop("artifactDigest", None)
    payload = json.dumps(
        canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return f"{SHA256_PREFIX}{hashlib.sha256(payload).hexdigest()}"


def validate_artifact(artifact_path: Path, root: Path) -> dict[str, Any]:
    checks: list[Check] = []
    errors: list[str] = []

    try:
        with artifact_path.open(encoding="utf-8") as handle:
            artifact = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return {
            "status": "invalid",
            "artifact": str(artifact_path),
            "artifactDigest": None,
            "checks": [],
            "errors": [f"cannot parse artifact: {exc}"],
        }

    if not isinstance(artifact, dict):
        errors.append("artifact root must be a JSON object")
        return {
            "status": "invalid",
            "artifact": str(artifact_path),
            "artifactDigest": None,
            "checks": [],
            "errors": errors,
        }

    sources = artifact.get("sourceArtifacts")
    digests = artifact.get("sourceDigests")
    if not isinstance(sources, list) or not sources:
        errors.append("sourceArtifacts must be a non-empty array")
    if not isinstance(digests, dict) or not digests:
        errors.append("sourceDigests must be a non-empty object")

    if isinstance(sources, list) and isinstance(digests, dict):
        for source in sources:
            if not isinstance(source, str) or not source:
                errors.append("sourceArtifacts entries must be non-empty strings")
                continue
            expected = digests.get(source)
            if expected is None:
                checks.append(
                    Check(source, "missing-declaration", error="no matching sourceDigest")
                )
                continue
            if not _is_sha256(expected):
                checks.append(
                    Check(source, "invalid-declaration", expected=str(expected), error="expected sha256:<64 lowercase hex>")
                )
                continue
            source_path = (root / source).resolve()
            try:
                source_path.relative_to(root.resolve())
            except ValueError:
                checks.append(Check(source, "invalid-path", expected=expected, error="source escapes repository root"))
                continue
            if not source_path.is_file():
                checks.append(Check(source, "missing-source", expected=expected, error="source file does not exist"))
                continue
            actual = _digest_file(source_path)
            checks.append(
                Check(source, "passed" if actual == expected else "mismatch", expected, actual)
            )

    if errors:
        status = "invalid"
    elif all(check.status == "passed" for check in checks) and checks:
        status = "passed"
    else:
        status = "failed"

    return {
        "status": status,
        "artifact": str(artifact_path),
        "artifactDigest": _artifact_digest(artifact),
        "checks": [check.as_dict() for check in checks],
        "errors": errors,
    }


def write_report(report_path: Path, report: dict[str, Any]) -> None:
    """Write atomically so a failed validation never leaves a partial report."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "schemaVersion": "1.0",
        "reportType": "artifact-provenance-validation",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        **report,
    }
    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{report_path.name}.", dir=report_path.parent
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary_name, report_path)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="JSON artifact to validate")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    parser.add_argument("--report", type=Path, help="optional JSON report output")
    args = parser.parse_args(argv)

    report = validate_artifact(args.artifact, args.root)
    report["root"] = str(args.root.resolve())
    if args.report:
        write_report(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())

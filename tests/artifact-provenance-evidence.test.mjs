import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

test('issue 25 includes a passing provenance evidence report', () => {
  const report = JSON.parse(fs.readFileSync(
    '.agents/skills/platform/artifacts/provenance/issue-25-validation-report.json',
    'utf8',
  ));
  assert.equal(report.reportType, 'artifact-provenance-validation');
  assert.equal(report.status, 'passed');
  assert.ok(report.checks.length > 0);
  assert.ok(report.checks.every((check) => check.status === 'passed'));
});

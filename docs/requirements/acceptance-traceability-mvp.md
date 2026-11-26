# Acceptance traceability — MVP inventory and operational risk

**Status:** Consolidated; execution evidence remains partial
**Scope:** AC-01–AC-14 from `docs/spec/mvp-inventory-risk.md`

| Criterion | Requirement / decision | Test or evidence seam | Status |
|---|---|---|---|
| AC-01 | US-01 schema and type validation | `test_dataset_validation_persists_valid_source`; Pydantic `DatasetPayload` | Partial |
| AC-02 | US-01 references, duplicates and quantities | `test_invalid_dataset_does_not_change_inventory` | Partial |
| AC-03 | US-01 rejected load does not mutate inventory | `test_invalid_dataset_does_not_change_inventory` | Executed |
| AC-04 | US-01 provenance, version and state | `test_dataset_validation_persists_valid_source`; `ConjuntoDatos` persistence | Partial |
| AC-05 | US-02 versioned model or deterministic fallback | `test_risk_evaluation_creates_prediction_and_critical_alert` | Partial |
| AC-06 | US-02 prediction metadata and limitations | `PredictionRead`; risk integration test | Partial |
| AC-06a | Temporal partitions and ML metrics | `ADR-017`; future experiment runner | Not executed |
| AC-06b | Auditable deterministic fallback | `ADR-024`; `baseline-rules-1` integration test | Partial |
| AC-06c | Result lineage and non-silent recalculation | `ADR-025`; no executable lineage test yet | Not executed |
| AC-06d | Quality and drift monitoring | `ADR-026`; no executable monitoring test yet | Not executed |
| AC-06e | Operational explanation without causal claim | `ADR-028`; no executable explanation test yet | Not executed |
| AC-06f | Human review and no irreversible automatic action | `ADR-029`; no executable authorization-action test yet | Not executed |
| AC-06g | Append-only audit with integrity | Alert history endpoint and `ADR-030`; partial | Partial |
| AC-06h | Scoped audit authorization and rejection logging | `ADR-031`; authorization tests are partial | Partial |
| AC-06i | Authorized kill switch and safe fallback | `ADR-035`; no executable test yet | Not executed |
| AC-07 | Re-evaluation does not duplicate active alerts | `test_risk_evaluation_creates_prediction_and_critical_alert` | Executed |
| AC-08 | Authorized alert state changes | `test_token_scopes_follow_user_role` and alert patch integration | Partial |
| AC-09 | Transition actor, old/new state and comment | Alert history assertions in risk integration test | Executed |
| AC-10 | Terminal alerts cannot change | `ADR-018`; no terminal-state test yet | Not executed |
| AC-11 | Simulated external adapter implements port | `ADR-004`; adapter test not present | Not executed |
| AC-12 | Source failure does not silently mutate inventory | `ADR-004`; failure integration test not present | Not executed |
| AC-13 | Synchronization source, result and error | `ADR-004`; synchronization test not present | Not executed |
| AC-14 | Simulated notifications, retry and audit | `ADR-019`; notification adapter test not present | Not executed |

## Interpretation

The table is a bidirectional planning index, not a claim that every criterion
is implemented. `Executed` means the named test provides direct evidence for
the criterion; `Partial` means the tracer bullet covers only part of the
criterion; `Not executed` means the design or ADR exists without executable
evidence.

Requirements remain blocked for publication until each criterion intended for
the MVP has an approved owner, executable oracle and evidence reference.

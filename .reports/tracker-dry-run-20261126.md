# Tracker publication dry-run — 2026-11-26

**Status:** `ready-for-remote-approval-under-ADR-060`
**Mutation performed:** no

## Resolved read-only facts

- Owner: `quantumquirkxyz`
- Repository: `quantumquirkxyz/DeepPharma`
- Proposed Project: `DeepPharma — MVP`
- Exact-title existing Project: not found
- Repository visibility observed: public
- Proposed Project visibility: private
- Existing GitHub Projects inspected: 24

## Proposed scope

- Views: Board Delivery, Table Traceability, Table Blocked/Triage
- Milestones: M0 through M4 as documented in
  `docs/engineering/tracker-design.md`
- No duplicate Priority/Risk/Phase custom fields
- No items until approved Parent Specs, Sub-Specs and Tickets exist

## Blocking findings

1. The repository is public while the Project will be private; this is now an
   explicit, accepted distinction.
2. The requirements and architecture artifacts are not approved.
3. Native sub-issue depth and status synchronization are not verified.
4. The publication policy forbids remote mutation before baseline approval.
5. Final SDD artifacts now have aligned approval state and AC-01–AC-14
   traceability; automatic-refinement review remains a separate gate.
6. ADR-060 records the approved manual exception; automatic-refinement remains
   `blocked` and is not represented as successful.

## Decision

The exact-title Project is absent, the repository is public, and the requested
Project visibility is private. The dry-run is ready for a separately approved
remote mutation after the refinement review completes.

Read-only capability checks:

- native sub-issue summary is available through GitHub GraphQL;
- native Issue Types are limited to `Task`, `Bug` and `Feature`;
- `type:spec` and `type:sub-spec` therefore remain canonical labels.

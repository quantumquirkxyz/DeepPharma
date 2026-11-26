# Domain docs

DeepPharma uses a single-context documentation layout.

## Before exploring

Read `CONTEXT.md` at the repository root and any ADRs in `docs/adr/` that touch the area being changed. If a file is absent, proceed without treating its absence as an error.

## File structure

```text
/
├── CONTEXT.md
├── docs/adr/
└── src/
```

Use the vocabulary defined by `CONTEXT.md` in issue titles, proposals, refactors, and tests. If a needed concept is not defined there, record the gap for domain modeling rather than silently inventing terminology.

If a proposed change conflicts with an existing ADR, surface the conflict explicitly instead of overriding it silently.

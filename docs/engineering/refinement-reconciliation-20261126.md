# Reconciliación de refinamiento — 2026-11-26

**Estado:** `blocked` con excepción manual aprobada por `ADR-060`

La revisión independiente invalidó la primera versión de los artefactos por
trazabilidad incompleta, estados contradictorios y digests no verificables.
La versión actual incorpora cada criterio AC-01–AC-14, owners, estados,
oráculos, riesgos y hashes de fixed point.

## Decisión

- Los artefactos `*-approved.json` históricos quedan `superseded`.
- Los artefactos `*-final.json` son la única versión candidata vigente.
- No se crea Project, Milestone, Issue, Sub-Spec, Ticket, rama ni PR.
- No se emite `refined-awaiting-review`.
- La excepción manual de `ADR-060` permite planificación y publicación
  jerárquica, pero no convierte el refinamiento automático en exitoso.

## Trabajo requerido

1. Reconciliar la spec con `requirements-review.md`.
2. Completar requisitos, criterios, pruebas y trazabilidad bidireccional
   (la matriz AC-01–AC-14 ya fue consolidada; la evidencia ejecutable sigue
   incompleta).
3. Obtener aprobación formal de requisitos y arquitectura.
4. Generar nuevos artefactos con fixed point y digests verificables.
5. Reejecutar critic, verifier y `automatic-refinement`.

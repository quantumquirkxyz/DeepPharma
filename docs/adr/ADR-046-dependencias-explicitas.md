# ADR-046 — Dependencias explícitas separadas de la jerarquía

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

La relación Parent Spec → Sub-Spec → Ticket expresa jerarquía y no implica
bloqueo. Solo se crearán dependencias nativas `blocked_by` cuando exista una
precondición real de ejecución.

El cuerpo de cada work item conservará también:

- `Blocked by`;
- `Blocks`;
- explicación de la precondición;
- evidencia necesaria para liberar el bloqueo.

## Consecuencias

- El DAG de implementación no se infiere artificialmente desde la jerarquía.
- `to-tickets` debe justificar cada arista de bloqueo.
- El Project puede mostrar jerarquía y bloqueo como dimensiones distintas.

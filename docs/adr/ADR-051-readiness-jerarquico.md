# ADR-051 — Readiness jerárquico

**Estado:** Aceptada para el flujo del tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

- Parent Spec inicia en `status:triage` y pasa a `status:ready` solo después de
  aprobación.
- Sub-Spec no puede pasar a `status:ready` antes que su Parent Spec.
- Ticket solo puede pasar a `status:ready` cuando tiene criterios concretos,
  seam explícito, pruebas, evidencia y blockers resueltos.

La jerarquía de readiness no sustituye las dependencias nativas; ambas deben
ser coherentes.

## Consecuencias

- `implement` solo recibe Tickets listos y trazables.
- El Project puede mostrar la frontera real de trabajo ejecutable.
- Un Issue bloqueado permanece en `status:blocked`, aunque su padre esté listo.

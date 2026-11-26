# ADR-052 — Especificación por niveles

**Estado:** Aceptada para el flujo SDD/tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada Parent Spec se publicará primero mediante `to-spec` con un
`RequirementsArtifact` válido, aprobado y no stale. Después de aprobar el
Parent Spec, sus Sub-Specs se derivarán con el mismo contrato de requisitos y
se vincularán mediante sub-issues nativos.

`to-tickets` solo generará Tickets después de que el Sub-Spec correspondiente
sea concreto, aprobado y tenga su arquitectura/diseño handoff válido.

## Consecuencias

- La jerarquía remota conserva provenance por nivel.
- No se crean Tickets desde una conversación sin spec aprobada.
- Cada nivel puede tener criterios, riesgos y evidencia propios.

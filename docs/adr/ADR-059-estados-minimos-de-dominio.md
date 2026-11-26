# ADR-059 — Estados mínimos de dominio del MVP

**Estado:** Aceptada para el MVP
**Fecha:** 2026-11-26
**Decisor:** Propietario técnico

## Decisión

El MVP usará estas máquinas mínimas:

- Dataset: `PENDIENTE → VALIDANDO → VALIDO | INVALIDO → APLICADO`.
- Riesgo: `PENDIENTE → CALCULADO | INDETERMINATE | FALLBACK_DETERMINISTA`.
- Inventario: `ACTUAL | DESACTUALIZADO`.
- Alertas: `NUEVA → RECONOCIDA → EN_REVISION → RESUELTA` o
  `DESCARTADA`, conforme a `ADR-018`.

Las transiciones inválidas se rechazan sin mutación y cada transición
auditable conserva actor, fecha, estado anterior, estado nuevo y motivo cuando
aplique.

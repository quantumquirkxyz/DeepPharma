# ADR-060 — Excepción gobernada para automatic-refinement

**Estado:** Aceptada como excepción temporal
**Fecha:** 2026-11-26
**Decisor:** Propietario del proyecto

## Contexto

El host no proporciona leasing aislado ni handoffs tipados suficientes para
emitir el `RefinementArtifact` automático en estado
`refined-awaiting-review`. La skill debe permanecer `blocked` y no puede
simular una ejecución exitosa.

Existen dos revisiones independientes read-only del fixed point final. Ambas
confirman que los artefactos son coherentes para planificación, pero mantienen
explícitos los criterios parciales/no ejecutados y los límites del benchmark.

## Decisión

Se acepta una excepción manual y temporal:

1. `automatic-refinement` conserva estado `blocked`; no se renombra ni se
   presenta como ejecutado correctamente.
2. Las dos revisiones independientes y sus resultados se usan como gate manual
   de planificación.
3. Se permite continuar con `work-item-router`, `make-project`, Milestones y
   Parent Specs.
4. Cada Sub-Spec y Ticket debe conservar requisitos, criterios, evidencia
   esperada y riesgos; no se permite implementar desde criterios
   `not-executed` sin un Ticket `status:ready`.
5. La excepción no autoriza claims de cumplimiento productivo ni sustituye
   pruebas, seguridad, ML, auditoría o verificación de operación.
6. La excepción caduca cuando el host proporcione el runtime requerido o al
   cerrar el MVP, lo que ocurra primero.

## Consecuencias

- El flujo queda trazable y reversible sin falsear el estado automático.
- La publicación remota puede comenzar por el Project y la jerarquía de Specs.
- `to-tickets` debe registrar esta ADR como excepción upstream y mantener
  bloqueados los tickets sin handoff verificable.
- Toda implementación continúa obligada a pasar pruebas y revisión.

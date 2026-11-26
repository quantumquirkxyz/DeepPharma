# ADR-043 — Identidad del GitHub Project del MVP

**Estado:** Aceptada para preparación; creación remota pendiente
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El Project del MVP tendrá:

- **Owner:** `quantumquirkxyz`;
- **Repositorio:** `quantumquirkxyz/DeepPharma`;
- **Título:** `DeepPharma — MVP`;
- **Visibilidad inicial:** privada.

El alcance incluirá el board, sus campos/vistas aprobados, Milestones,
Parent Specs, Sub-Specs, Tickets y relaciones de Development que existan
después de implementar.

## Consecuencias

- El board no se crea hasta aprobar la visibilidad y el alcance completo.
- Debe ejecutarse primero un dry-run que detecte proyectos existentes con el
  mismo título.
- La creación de Project, campos, vínculos e ítems requiere aprobaciones
  separadas según `make-project`.

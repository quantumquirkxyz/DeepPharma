# ADR-044 — Milestones del MVP

**Estado:** Aceptada para preparación del tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El MVP se organizará en cinco Milestones:

1. `M0 — Baseline y gobierno`;
2. `M1 — Datos e inventario`;
3. `M2 — Riesgo ML y fallback`;
4. `M3 — Alertas, auditoría y notificaciones`;
5. `M4 — Seguridad, operación y verificación`.

Cada Milestone tendrá exactamente un Parent Spec, sus Sub-Specs y sus Tickets
relacionados. La creación remota queda pendiente del cierre de
`grill-with-docs`, revisión de `automatic-refinement` y aprobación de la línea
base.

## Consecuencias

- El trabajo tiene entregas verticales y trazables.
- M0 puede contener trabajo documental y de gobernanza sin confundirse con
  implementación.
- Las dependencias entre Milestones deben ser explícitas y no asumirse solo
  por el orden numérico.

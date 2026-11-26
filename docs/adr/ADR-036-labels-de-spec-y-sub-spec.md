# ADR-036 — Labels explícitos para Specs y Sub-Specs

**Estado:** Aceptada para el flujo del tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

DeepPharma extiende la familia canónica `type:*` con:

- `type:spec` para Parent Specs;
- `type:sub-spec` para Sub-Specs.

Ambos usan `area:requirements` y un único label `status:*`. `type:documentation`
queda reservado para documentación que no sea una especificación.

No se asignarán simultáneamente `type:documentation` y `type:spec` o
`type:sub-spec`, porque cada work item debe tener un único tipo principal.

## Consecuencias

- La jerarquía de Issues es visible sin depender únicamente de la relación
  nativa de sub-issues.
- `to-spec` debe usar la taxonomía local de DeepPharma, aunque su valor
  genérico mencione `type:documentation`.
- La creación remota de labels requiere una operación posterior y aprobada.
- Las diferencias frente a defaults genéricos se consolidan en
  `docs/reference/agents/skill-contract-overrides.md`.

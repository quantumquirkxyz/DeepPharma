# ADR-042 — Metadata compartida entre Issues, PRs y Project

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

La metadata común de Issues, PRs y elementos del Project se expresará mediante
labels:

- `status:*`;
- `type:*`;
- `area:*`;
- `priority:*`;
- `risk:*`.

Issues y PRs son los objetos que poseen los labels. El campo nativo `Labels`
del Project los proyecta. El campo nativo `Status` del Project se mantendrá
sincronizado con `status:*`; no se duplicarán Priority o Risk como campos
personalizados.

La sincronización será una regla operativa verificable, no una afirmación de
que GitHub comparte físicamente el mismo campo entre objetos.

## Consecuencias

- Issues, PRs y Project pueden filtrarse con la misma semántica.
- Los cambios de estado deben actualizar el Issue/PR y el Project.
- La automatización de sincronización debe verificarse; no se presume que
  GraphQL la cree automáticamente.
- El ciclo específico Ticket–PR está definido en `ADR-055`.

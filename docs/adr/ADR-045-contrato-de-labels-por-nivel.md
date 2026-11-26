# ADR-045 — Contrato de labels por nivel

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

La metadata mínima por nivel será:

| Nivel | Labels obligatorios |
|---|---|
| Parent Spec | `type:spec`, `area:requirements`, `status:*`, `priority:*`, `risk:*` |
| Sub-Spec | `type:sub-spec`, `area:requirements`, `status:*`, `priority:*`, `risk:*` |
| Ticket | `type:*` específico, `area:requirements`, `status:*`, `priority:*`, `risk:*` |
| PR | Labels del Ticket vinculado; estado de revisión actualizado cuando aplique |

El cuerpo de cada Issue conserva requisitos, alcance, dependencias, criterios,
validación, evidencia y referencias documentales. Los labels no sustituyen el
contenido trazable.

## Consecuencias

- La taxonomía puede validarse automáticamente antes de publicar.
- Un Ticket sin `risk:*` o `priority:*` no está listo para publicación.
- Un PR no puede convertirse en una fuente de metadata independiente del
  Ticket.

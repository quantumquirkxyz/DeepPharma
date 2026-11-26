# ADR-055 — Ciclo sincronizado Ticket–PR

**Estado:** Aceptada para el flujo de entrega
**Fecha:** 2026-11-26
**Decisor:** Propietario del proyecto

## Decisión

| Evento | Ticket | PR | Project |
|---|---|---|---|
| PR abierto | `status:review` | `status:review` | `Review` |
| Cambios solicitados | `status:review` | `status:review` | `Review` |
| Merge y criterios verificados | `status:done` | `status:done` | `Done` |
| PR cerrado sin merge | `status:in-progress` o `status:blocked` | estado cerrado | proyección correspondiente |

El PR copia los labels del Ticket. El cierre final requiere verificación de
criterios y evidencia; el merge por sí solo no sustituye la verificación.

## Consecuencias

- Ticket, PR y Project mantienen una narrativa única de entrega.
- La automatización debe ser idempotente y detectar divergencias.
- Un PR cerrado sin merge no completa el Ticket automáticamente.

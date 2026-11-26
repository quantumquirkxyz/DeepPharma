# ADR-047 — Trazabilidad Ticket → rama → PR

**Estado:** Aceptada para el flujo de entrega
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada Ticket tendrá como máximo un PR de implementación vinculado. La rama
seguirá la convención:

```text
issue/<number>-<slug>
```

El PR copiará los labels y Milestone del Ticket. `Closes #N` solo se usará
cuando el cierre automático sea deseado y compatible con el flujo de
verificación y `ship-subissue`.

## Consecuencias

- Un PR no puede ocultar cambios de múltiples Tickets sin justificación.
- La rama no sustituye el vínculo Issue–PR.
- La publicación del PR sigue siendo responsabilidad separada de
  `implement`.

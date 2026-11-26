# ADR-040 — Sub-issues obligatorios para la jerarquía

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada Sub-Spec será un sub-issue nativo de su Parent Spec y cada Ticket será un
sub-issue nativo de su Sub-Spec. La jerarquía Issue será la fuente de verdad
para la relación padre-hijo.

Si la capacidad o profundidad disponible de GitHub no permite representar la
jerarquía acordada, la publicación se bloqueará. No se sustituirá
silenciosamente por listas Markdown, títulos o enlaces informales.

## Consecuencias

- La publicación debe verificar primero la capacidad de sub-issues.
- Cada Issue conservará además referencias textuales al Parent Spec y
  Sub-Spec para trazabilidad humana.
- Las dependencias `blocked_by` se modelan aparte; ser hijo no implica estar
  bloqueado.

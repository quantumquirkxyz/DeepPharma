# ADR-056 — Mapeo opcional de Issue Types nativos

**Estado:** Aceptada como política de compatibilidad
**Fecha:** 2026-11-26
**Decisor:** Propietario del proyecto

## Decisión

Los labels `type:*` son obligatorios y canónicos. Los Issue Types nativos de
GitHub son opcionales:

- se usan solo si están disponibles;
- requieren un mapeo exacto y documentado;
- no pueden contradecir el label;
- un mapeo parcial o ambiguo bloquea el dry-run;
- si no están disponibles, no se inventa una sustitución.

## Consecuencias

- La taxonomía local permanece portable.
- `make-project` y la publicación deben verificar capacidades antes de mutar.
- La ausencia de Issue Types nativos no bloquea la jerarquía de labels.

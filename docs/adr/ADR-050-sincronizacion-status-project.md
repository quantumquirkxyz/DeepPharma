# ADR-050 — Sincronización verificable de Status

**Estado:** Aceptada como diseño; automatización pendiente
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

La correspondencia entre labels `status:*` y el campo nativo `Status` del
Project se implementará mediante una automatización verificable, usando
GitHub Actions o reglas configuradas en la interfaz de GitHub según las
capacidades disponibles.

`make-project` no afirmará crear automatizaciones mediante GraphQL cuando la
API no las soporte. Mientras la automatización no esté verificada, la
sincronización se marcará como pendiente y no se presentará como garantizada.

## Consecuencias

- La automatización necesita pruebas de ida y vuelta y manejo de duplicados.
- Los cambios manuales incompatibles deben detectarse o rechazarse.
- La configuración de Actions o UI será un artefacto operativo separado del
  Project base.

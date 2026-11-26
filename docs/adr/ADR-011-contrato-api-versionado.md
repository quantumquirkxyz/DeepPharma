# ADR-011 — Contrato API versionado

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

La API pública del MVP usa `/api/v1`, OpenAPI como contrato, errores
estructurados con `traceId`, paginación y límites máximos en colecciones, y
claves de idempotencia para operaciones mutantes que puedan reintentarse.

## Consecuencias

- Los cambios incompatibles requieren nueva versión o período de
  compatibilidad.
- Los consumidores no dependen de mensajes de error libres.
- La API debe rechazar cargas que excedan límites documentados.
- El contrato se prueba con validación de esquema y pruebas de integración.

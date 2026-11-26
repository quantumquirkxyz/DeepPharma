# ADR-030 — Auditoría append-only e íntegra

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Los eventos de auditoría de importaciones, predicciones, degradaciones,
transiciones de alerta y decisiones humanas serán append-only. Cada evento
conservará actor o sistema originador, acción, timestamp, `traceId`, contexto
mínimo y resultado.

Las correcciones se registrarán como nuevos eventos relacionados; no se
editarán silenciosamente registros históricos. La integridad debe poder
verificarse mediante identificador, hash o mecanismo equivalente documentado.

## Consecuencias

- La auditoría puede reconstruir la secuencia de una operación.
- La eliminación o retención debe respetar la política de datos aplicable.
- Las pruebas deben detectar mutaciones directas y relaciones rotas.

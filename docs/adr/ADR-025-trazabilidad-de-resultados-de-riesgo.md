# ADR-025 — Trazabilidad de resultados de riesgo

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada resultado de riesgo registrará:

- origen: `MODELO_ML` o `FALLBACK_DETERMINISTA`;
- versión del artefacto;
- dataset y experimento cuando corresponda;
- horizonte;
- timestamp;
- `traceId`;
- configuración relevante y limitaciones.

Los resultados históricos no se recalculan silenciosamente cuando cambia el
modelo, el dataset o la configuración. Toda recalculación debe ser una nueva
ejecución identificable.

## Consecuencias

- Se puede reconstruir qué produjo una alerta.
- Las comparaciones entre modelos conservan su contexto.
- El almacenamiento y los contratos API deben incluir metadatos de linaje.

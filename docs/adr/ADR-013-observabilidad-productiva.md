# ADR-013 — Diseño de observabilidad productiva

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

DeepPharma diseñará observabilidad productiva con:

- logs estructurados y redacción de secretos;
- `traceId` y correlación de peticiones;
- métricas de latencia, errores, volumen, jobs, datos y alertas;
- trazas distribuidas cuando existan procesos separados;
- dashboards operativos;
- alertas sobre errores, degradación, fuentes externas y jobs;
- auditoría de acciones sensibles.

Los valores numéricos de SLO, umbrales y ventanas de alerta se definirán tras
medir el entorno objetivo. No se inventan SLOs.

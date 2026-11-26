# ADR-026 — Monitoreo de calidad y deriva ML

**Estado:** Aceptada para MVP sintético
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El MVP incluirá un seam de monitoreo para registrar:

- calidad y completitud de entradas;
- distribución de variables;
- distribución de la variable objetivo cuando esté disponible;
- cambios entre dataset de referencia y dataset de ejecución;
- métricas de desempeño por partición;
- estado del modelo y alertas de degradación.

Con datos sintéticos se validará el flujo técnico y las reglas de comparación,
sin presentar sus resultados como deriva institucional. Los umbrales
operativos deberán ser configurables y no se inventarán como evidencia real.

## Consecuencias

- La evaluación ML incorpora calidad de datos, no solo métricas del modelo.
- El monitoreo debe conservar dataset, referencia y timestamp.
- El MVP requiere fixtures de cambio controlado para probar detección.

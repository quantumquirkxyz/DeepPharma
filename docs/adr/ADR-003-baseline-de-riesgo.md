# ADR-003 — ML reproducible y baseline de riesgo operativo

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Contexto

El MVP debe demostrar el flujo ML, pero no dispone de una base institucional
autorizada ni puede afirmar validez clínica. Se necesita separar el modelo ML
reproducible del fallback determinista.

## Decisión

El MVP incluirá un pipeline ML reproducible con datos sintéticos o públicos
autorizados, registro de dataset, configuración, semillas, métricas, versión
del modelo y limitaciones. También conservará `baseline-rules-1` como fallback
determinista y referencia de comparación:

- `0–10`: `CRITICA`, probabilidad operativa `0.95`;
- `11–30`: `MEDIA`, probabilidad operativa `0.65`;
- mayor que `30`: `BAJA`, probabilidad operativa `0.15`.

Estas cifras son parámetros operativos del fallback, no métricas de precisión
ni afirmaciones clínicas. El objetivo del modelo ML será clasificar riesgo
futuro simulado de desabastecimiento en un horizonte configurable, registrado
en cada ejecución. La etiqueta se construirá desde escenarios sintéticos de
demanda, stock y reposición, no desde el mismo umbral del fallback. El modelo
ML solo podrá declararse evaluado con resultados efectivamente ejecutados y
archivados.

Cuando un modelo ML aprobado no esté disponible, falle su carga o sea retirado,
el sistema podrá usar explícitamente `baseline-rules-1` como fallback. La
degradación deberá registrar causa, momento, versión del baseline y `traceId`;
nunca se presentará el resultado como inferencia ML.

## Consecuencias

- El flujo es reproducible y testeable sin datos institucionales.
- El fallback permite operar el tracer bullet si el modelo no está disponible.
- Las métricas ML no se interpretan como validez clínica.
- La degradación es visible y auditable para operadores y revisores.

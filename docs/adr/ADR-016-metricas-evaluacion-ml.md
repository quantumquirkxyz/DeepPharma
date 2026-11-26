# ADR-016 — Métricas de evaluación ML

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada experimento de clasificación de riesgo reportará, cuando corresponda:

- precisión;
- recall;
- F1;
- matriz de confusión;
- PR-AUC;
- comparación contra `baseline-rules-1`;
- distribución de clases y limitaciones.

No se usará accuracy como única métrica. Los umbrales para aprobar un modelo
quedan abiertos hasta contar con datos, contexto y criterio de dominio
suficientes.

## Consecuencias

- Los experimentos serán comparables.
- Los resultados deben conservar dataset, partición y configuración.
- Las métricas no prueban validez clínica ni institucional.

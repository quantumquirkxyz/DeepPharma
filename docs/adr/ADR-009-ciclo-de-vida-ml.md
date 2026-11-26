# ADR-009 — Ciclo de vida de modelos ML

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Todo modelo debe conservar dataset, configuración, semilla, métricas,
limitaciones y versión. Sus estados son:

```text
ENTRENADO → EVALUADO → APROBADO → RETIRADO
```

Solo un modelo `APROBADO` puede utilizarse para inferencia operativa. El
baseline determinista se mantiene como fallback separado y no se registra como
modelo ML aprobado.

La transición `EVALUADO → APROBADO` exige un reporte reproducible con métricas,
comparación contra el fallback, validación temporal, limitaciones y revisión
humana explícita. No se fijan umbrales numéricos universales hasta disponer de
datos y criterio de dominio suficientes.

## Consecuencias

- Se evita activar automáticamente un modelo no evaluado.
- Las métricas deben provenir de ejecuciones reales.
- Retirar un modelo no elimina su historial ni predicciones anteriores.
- El MVP necesita entidades o contratos para experimentos y modelos aunque el
  entrenamiento inicial use fixtures.

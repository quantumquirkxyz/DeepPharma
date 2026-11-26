# ADR-028 — Explicabilidad operativa de resultados ML

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada resultado generado por un modelo ML aprobado ofrecerá una explicación
operativa de las variables influyentes, el horizonte, las limitaciones y el
origen del resultado. La explicación debe distinguirse de una justificación
causal o clínica.

La técnica concreta de explicabilidad se seleccionará según el modelo y se
documentará junto con el experimento; no se impone SHAP ni otra técnica antes
de conocer el pipeline implementado.

## Consecuencias

- Farmacéuticos y revisores pueden interpretar el resultado con contexto.
- Las explicaciones deben conservar la versión del modelo y la configuración.
- Una explicación no autoriza por sí sola una acción operativa.

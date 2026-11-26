# ADR-015 — Dataset sintético para el primer experimento ML

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El primer experimento ML utilizará un dataset sintético reproducible que simule
stock, demanda, reposición y ocurrencia futura de desabastecimiento. La
variable objetivo será el riesgo futuro dentro de un horizonte configurable.

La etiqueta no se derivará directamente de las clases del fallback
`baseline-rules-1`; el fallback se utilizará como referencia comparativa.

## Reproducibilidad

Cada dataset conservará semilla, generador y versión, parámetros de simulación,
versión de esquema, fecha de generación, hash y particiones de entrenamiento,
validación y prueba.

## Limitaciones

El dataset sintético permite probar ingeniería, flujo y evaluación
reproducible, pero no demuestra validez institucional, clínica ni capacidad de
generalización a datos reales.

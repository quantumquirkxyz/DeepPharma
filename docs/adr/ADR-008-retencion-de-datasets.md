# ADR-008 — Retención y versionado de datasets

**Estado:** Aceptada para fixtures sintéticos; retención institucional pendiente
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto; responsable de privacidad pendiente para datos institucionales

## Contexto

Los datasets necesitan procedencia y reproducibilidad, pero no se ha definido
retención, archivado, eliminación ni clasificación de datos.

## Decisión

Los datasets serán inmutables por versión y conservarán fuente, esquema,
estado, hash, actor y fecha. La política de retención, clasificación y
eliminación deberá aprobarse antes de usar datos institucionales.

Para el MVP con fixtures sintéticos se permitirá almacenamiento local
controlado únicamente durante el ciclo de desarrollo/evaluación. Cada dataset
podrá eliminarse mediante una operación documentada; esto no define el plazo
de retención de producción ni de datos institucionales.

## Consecuencias

- Se puede reproducir una validación.
- La retención no se inventa sin dueño de datos.
- Se requiere un registro de hash y un mecanismo de consulta antes de
  declarar trazabilidad completa.
- La reproducibilidad de un experimento sintético requiere conservar su
  configuración, semilla y hash antes de eliminar el dataset.

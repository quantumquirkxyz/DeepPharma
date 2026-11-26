# ADR-005 — Jobs para evaluación y procesamiento pesado

**Estado:** Aceptada con alcance diferido
**Fecha:** 2026-11-25
**Decisor:** Pendiente de aprobación de arquitectura

## Contexto

La evaluación de riesgo, el preprocesamiento y el futuro entrenamiento pueden
procesar muchos registros y no deben bloquear la API ni depender de una
petición HTTP larga.

## Decisión

El MVP ejecutará entrenamiento y evaluación de forma síncrona y controlada,
con límites explícitos de tamaño y tiempo. Se mantendrá un seam de servicio
para poder introducir un worker posteriormente. La separación mediante jobs con:

- solicitud idempotente;
- estado `PENDIENTE`, `EJECUTANDO`, `COMPLETADO`, `FALLIDO`;
- progreso y error persistidos;
- worker separado del proceso web;
- endpoint de creación y consulta de estado.

queda como evolución posterior, no como requisito de infraestructura inicial.

## Consecuencias

- Mejor aislamiento de API y procesamiento.
- Requiere persistencia de jobs, reintentos y observabilidad.
- El MVP debe declarar límites de tamaño y tiempo mientras el worker no exista.

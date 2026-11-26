# ADR-010 — Estrategia de pruebas trazables

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada requisito se verificará mediante una combinación adecuada de:

1. pruebas unitarias para reglas y unidades de dominio;
2. pruebas de integración para persistencia, migraciones y adaptadores;
3. pruebas de sistema para flujos completos;
4. pruebas de aceptación para escenarios y objetivos de actores.

Cada prueba conservará requisito, escenario, versión, entorno, entrada,
resultado esperado, resultado obtenido, estado y evidencia. Un caso diseñado
no se marca aprobado sin ejecución verificable.

## Consecuencias

- La cobertura se evalúa por riesgo y trazabilidad, no solo por porcentaje.
- CU-06/SUS conserva evidencia separada de pruebas automatizadas.
- Los defectos y limitaciones se registran sin ocultarlos.

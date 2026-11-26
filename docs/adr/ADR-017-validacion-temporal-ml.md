# ADR-017 — Validación temporal y prevención de fuga

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Los datos de inventario y riesgo se particionarán respetando el orden temporal.
Las variables, transformaciones y estadísticas se ajustarán solo con datos
disponibles en el período de entrenamiento. Cada experimento registrará
particiones, ventanas, semilla y controles de fuga.

## Consecuencias

- Se evita evaluar con información del futuro.
- El dataset sintético debe generar tiempos y eventos coherentes.
- Las métricas no se comparan entre experimentos con particiones distintas sin
  documentar la diferencia.

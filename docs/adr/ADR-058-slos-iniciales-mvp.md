# ADR-058 — SLO iniciales de evaluación

**Estado:** Aceptada para benchmark del MVP, no para producción
**Fecha:** 2026-11-26
**Decisor:** Propietario del proyecto

## Decisión

El benchmark reproducible del MVP usará estos objetivos iniciales:

- p95 de lectura de inventario: ≤ 500 ms;
- p95 de validación de una carga de 1.000 filas: ≤ 2 s;
- throughput mínimo: ≥ 10 solicitudes/s;
- disponibilidad durante el benchmark: ≥ 99%.

Estos valores son umbrales de evaluación del entorno aprobado, no una
declaración de disponibilidad productiva.

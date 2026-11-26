# ADR-034 — Respuesta a incidentes de datos

**Estado:** Aceptada como requisito operativo
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto; obligaciones legales externas pendientes

## Decisión

Todo acceso no autorizado, pérdida, corrupción o exposición de datasets activa:

1. registro del incidente;
2. contención;
3. preservación de evidencia;
4. evaluación de alcance e impacto;
5. comunicación al responsable correspondiente;
6. recuperación y verificación;
7. revisión posterior y acciones correctivas.

El proceso no inventa plazos ni obligaciones legales; estos se incorporarán
cuando el responsable institucional y el marco aplicable estén confirmados.

## Consecuencias

- La respuesta no depende únicamente de logs técnicos.
- Las copias y exportaciones forman parte del alcance del incidente.
- La restauración debe verificar integridad antes de reanudar el uso.

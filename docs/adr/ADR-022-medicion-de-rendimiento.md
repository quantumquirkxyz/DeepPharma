# ADR-022 — Medición reproducible de rendimiento

**Estado:** Aceptada; objetivos iniciales fijados por ADR-058
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El MVP tratará latencia, throughput, tamaño de carga y tiempo de
entrenamiento como hipótesis medibles. Los benchmarks deberán registrar:

- versión del código;
- entorno y recursos;
- dataset y volumen;
- configuración;
- carga aplicada;
- percentiles y errores;
- resultado y limitaciones.

Los resultados solo se convertirán en SLO productivos después de seleccionar
un entorno representativo y revisar la evidencia. ADR-058 fija únicamente
objetivos iniciales de evaluación; no se presentan como disponibilidad
productiva.

## Consecuencias

- Las comparaciones entre ejecuciones requieren condiciones equivalentes.
- El rendimiento local no se presenta como rendimiento productivo.
- Los límites operativos deben documentarse junto con las respuestas de error.

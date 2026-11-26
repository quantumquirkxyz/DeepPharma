# ADR-033 — Protección de datasets restringidos

**Estado:** Aceptada como requisito técnico; parámetros institucionales pendientes
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El repositorio de datasets originales restringidos debe exigir:

- cifrado en reposo;
- cifrado en tránsito;
- mínimo privilegio;
- registro de accesos;
- rotación documentada de credenciales;
- separación de secretos por entorno;
- prohibición de secretos dentro del repositorio Git.

Los algoritmos, proveedor y períodos concretos se definirán según el entorno
aprobado y la política institucional.

## Consecuencias

- Los fixtures locales no deben normalizar prácticas inseguras.
- Las restauraciones y exportaciones requieren controles equivalentes.
- La evidencia de acceso debe respetar la clasificación del dataset.

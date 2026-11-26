# ADR-004 — SALMI detrás de un adaptador sustituible

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisión:** Equipo DeepPharma

## Contexto

No existe todavía un contrato técnico autorizado para conectar SALMI. Acoplar
el dominio a una API hipotética produciría una falsa integración y riesgo de
datos.

## Decisión

El MVP define un puerto `ExternalInventorySource` y usa un adaptador simulado
con fixtures sintéticos. Los errores de la fuente se registran y no modifican
el inventario silenciosamente.

## Consecuencias

- El dominio puede probarse sin SALMI.
- El contrato real podrá sustituir el adaptador sin rediseñar el dominio.
- La integración real permanece bloqueada hasta recibir autorización y
  contrato verificable.

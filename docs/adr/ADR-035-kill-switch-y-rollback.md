# ADR-035 — Kill switch y rollback auditable

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El MVP tendrá mecanismos explícitos para desactivar:

- un modelo ML;
- el envío de notificaciones;
- una integración externa defectuosa.

Cuando se desactive una capacidad, el sistema deberá aplicar el fallback
correspondiente o dejar el flujo en estado seguro. Cada acción registrará
autorización, motivo, timestamp, actor, alcance y resultado.

## Consecuencias

- La contención puede ejecutarse sin modificar código.
- El rollback no borra resultados históricos ni evidencia.
- Las pruebas deben cubrir activación, desactivación, recuperación y permisos.

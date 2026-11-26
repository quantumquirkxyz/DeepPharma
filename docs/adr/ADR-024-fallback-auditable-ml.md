# ADR-024 — Fallback auditable ante indisponibilidad ML

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Si el modelo ML aprobado no está disponible, falla su carga o fue retirado,
DeepPharma podrá ejecutar `baseline-rules-1`. Cada resultado degradado debe
registrar causa, momento, versión del baseline y `traceId`.

El resultado debe identificarse como `FALLBACK_DETERMINISTA`; nunca puede
presentarse como inferencia ML ni como evidencia de desempeño del modelo.

## Consecuencias

- El sistema conserva continuidad controlada.
- Operadores pueden distinguir degradación de operación normal.
- Las pruebas deben cubrir fallo de carga, retiro y recuperación del modelo.

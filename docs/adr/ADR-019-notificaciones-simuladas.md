# ADR-019 — Notificaciones simuladas

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Las alertas críticas podrán activar un adaptador de notificaciones simulado.
El adaptador registrará destinatario lógico, evento, intento, resultado,
error, `traceId` y estado de reintento, sin enviar mensajes reales.

## Reglas

- Una alerta no equivale a una notificación enviada.
- Un reintento debe ser idempotente.
- Los fallos no cambian silenciosamente el estado de la alerta.
- Los canales institucionales requieren contrato, autorización y configuración
  externa.

## Consecuencias

- El flujo puede probarse sin credenciales ni proveedores reales.
- Se requiere un puerto de notificación sustituible.
- Las métricas de entrega del fixture no se presentan como disponibilidad real.

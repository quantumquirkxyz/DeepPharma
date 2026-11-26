# ADR-020 — Denegación por defecto de endpoints de datos

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Todo endpoint que exponga o modifique datos requiere autenticación y
autorización. Esto incluye catálogos, inventario, datasets, predicciones,
alertas, auditoría e integraciones.

Solo se consideran públicos:

- health/readiness mínimos;
- emisión de token, con protección contra abuso y credenciales externas.

## Consecuencias

- La interfaz no puede usarse como única barrera de seguridad.
- Las pruebas deben cubrir acceso anónimo, rol insuficiente y ámbito
  incorrecto.
- El catálogo deja de ser una excepción implícita.

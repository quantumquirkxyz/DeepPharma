# ADR-006 — Autorización por ámbito de centro de salud

**Estado:** Aceptada como principio técnico; asignaciones institucionales pendientes
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto; responsable institucional pendiente

## Contexto

RBAC define capacidades, pero no determina qué centros de salud puede
consultar o modificar cada usuario.

## Decisión propuesta

Separar:

1. **rol:** qué operación puede ejecutar;
2. **ámbito:** sobre qué centros puede ejecutarla.

Las consultas y mutaciones deben filtrar por asignaciones explícitas de usuario
a centro. La ausencia de asignación debe producir rechazo, no acceso global.

## Consecuencias

- Evita exposición entre centros.
- Requiere asignaciones, pruebas de acceso cruzado y administración de ámbito.
- La matriz RBAC seguirá provisional hasta recibir confirmación institucional.

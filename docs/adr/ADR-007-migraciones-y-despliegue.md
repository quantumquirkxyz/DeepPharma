# ADR-007 — Alembic como autoridad de esquema

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Contexto

El proyecto contiene migraciones Alembic y el arranque actual también usa
`Base.metadata.create_all`. Tener dos autoridades puede ocultar drift y crear
esquemas distintos entre entornos.

## Decisión propuesta

Alembic será la única autoridad para crear y modificar el esquema. La
aplicación no ejecutará `create_all` en startup. El despliegue ejecutará:

1. validar configuración;
2. aplicar migraciones;
3. iniciar API/worker;
4. ejecutar health/readiness checks.

## Consecuencias

- Mayor reproducibilidad.
- Los tests usarán migraciones o fixtures explícitos.
- El desarrollo local requerirá un comando de inicialización documentado.

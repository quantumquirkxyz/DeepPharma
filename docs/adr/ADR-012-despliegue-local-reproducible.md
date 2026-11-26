# ADR-012 — Despliegue local reproducible

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El MVP tendrá un entorno local reproducible mediante Docker/Compose con web,
API y base de datos. Las migraciones Alembic se ejecutarán como paso explícito.
No se fija todavía una plataforma productiva ni se presentan resultados
locales como disponibilidad productiva.

## Consecuencias

- El equipo podrá ejecutar una instalación consistente.
- Los secretos se suministran por entorno y nunca se incluyen en Compose.
- La configuración local debe distinguirse de producción.
- CI podrá reutilizar el mismo entorno para pruebas de integración.

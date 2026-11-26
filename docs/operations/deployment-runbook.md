# Runbook de despliegue

**Estado:** Propuesta operativa aceptada para entorno local; producción pendiente.

## Precondiciones

- configuración suministrada fuera del repositorio;
- `SECRET_KEY` configurada con longitud segura;
- base de datos accesible;
- versión de código identificable;
- backup y rollback definidos.

## Secuencia propuesta

1. Validar configuración sin imprimir secretos.
2. Ejecutar `alembic upgrade head`.
3. Ejecutar health/readiness checks.
4. Iniciar API y worker con versiones identificables.
5. Verificar endpoints y migración aplicada.
6. Registrar evidencia del despliegue.

## Rollback

No se ejecutará downgrade automático sin una estrategia de datos revisada.
El rollback debe definir compatibilidad de aplicación, esquema y datos.

## Pendientes

- entorno objetivo;
- Docker/Compose o plataforma;
- health/readiness separados;
- observabilidad;
- backups y RPO/RTO;
- política de rollback.

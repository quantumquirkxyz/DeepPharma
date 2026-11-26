# Constitución SDD de DeepPharma

**Versión:** 0.1
**Estado:** Línea base propuesta
**Fecha:** 2026-11-25

## 1. Alcance

El MVP ejecutable cubre inventario, validación e importación de datos,
predicción baseline, alertas auditables, RBAC y un adaptador SALMI simulado.
El entrenamiento ML reproducible con datos sintéticos o públicos autorizados
forma parte del MVP. Quedan fuera los datos institucionales no autorizados y
la integración SALMI real sin contrato autorizado.

## 2. Invariantes arquitectónicos

1. El dominio no depende de frameworks ni de integraciones externas.
2. Las operaciones mutantes dejan evidencia auditable.
3. Los datos externos pasan validación antes de afectar inventario o riesgo.
4. El baseline determinista no se presenta como modelo ML validado.
5. SALMI permanece detrás de un puerto y un adaptador sustituible.
6. Los permisos se derivan del rol y se verifican en el backend.
7. Las migraciones son reproducibles y no se sustituyen por cambios manuales.

## 3. Calidad obligatoria

- Pruebas automatizadas para cada slice.
- Lint y typecheck/build del frontend.
- `git diff --check`.
- No se inventan métricas, datos institucionales ni resultados de modelos.
- No se almacenan secretos en el repositorio.
- Las interfaces de usuario deben conservar estados de carga, error y vacío.

## 4. Trazabilidad

Cada cambio debe enlazar requisito, caso de uso, tarea, código, prueba y
evidencia. Las divergencias entre spec, plan, tareas e implementación bloquean
el cierre del slice.

## 5. Datos y privacidad

El desarrollo usa datos sintéticos, públicos o autorizados. La procedencia,
versión y estado de validación se conservan. Los secretos se suministran por
variables de entorno o un gestor externo.

## 6. Definition of Done

Un slice está terminado cuando:

- cumple sus criterios de aceptación;
- tiene pruebas automatizadas;
- actualiza la documentación y trazabilidad;
- pasa los quality gates;
- declara riesgos o pendientes residuales.

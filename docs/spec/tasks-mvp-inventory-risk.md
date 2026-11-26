# Tareas SDD — MVP de inventario y riesgo

**Estado:** Borrador local; todavía no son tickets de GitHub

| ID | Slice | Especificación | Evidencia |
|---|---|---|---|
| T-01 | Importación | US-01, AC-01–AC-02 | tests de esquema, tipos, referencias y duplicados |
| T-02 | Persistencia de datasets | US-01, AC-04 | migración y tests de procedencia/estado |
| T-03 | Rechazo seguro | US-01, AC-03 | test de rollback sin cambios en inventario |
| T-04 | Aplicación válida | US-01, AC-03–AC-04 | integración de carga válida |
| T-05 | Riesgo versionado | US-02, AC-05–AC-07 | tests de regla, versión e idempotencia |
| T-06 | Alertas auditables | US-03, AC-08–AC-10 | tests de permisos y transiciones |
| T-07 | Puerto SALMI | US-04, AC-11–AC-13 | fixture simulado y test de fallo |
| T-08 | Pipeline ML reproducible | US-02, AC-05–AC-06 | experimento, métricas, modelo y limitaciones |
| T-09 | Notificaciones simuladas | US-03/US-04, AC-08–AC-10, AC-14 | adaptador, idempotencia, fallos y auditoría |
| T-10 | Verificación final | Todas | matriz, gates, documentación y revisión de divergencias |

## Orden de ejecución

`T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07 → T-08 → T-09 → T-10`

Cada tarea debe permanecer pequeña, ser reversible y terminar con evidencia
ejecutable antes de iniciar la siguiente.

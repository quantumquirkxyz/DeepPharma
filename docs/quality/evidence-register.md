# Registro de evidencia de calidad

**Estado:** Inicial; evidencia ejecutada archivada parcialmente; no todos los
casos han sido ejecutados.

| Evidencia | Alcance | Estado | Fuente |
|---|---|---|---|
| API unit/integration smoke tests | tracer bullet API | Ejecutada; PASS (12 passed) | `.reports/execution/20261126/api-pytest.txt` |
| Frontend lint | aplicación web | Ejecutada; PASS | `.reports/execution/20261126/web-lint.txt` |
| Frontend production build | aplicación web | Ejecutada; PASS | `.reports/execution/20261126/web-build.txt` |
| Migraciones Alembic en SQLite | esquema local aislado | Ejecutada; PASS en base temporal; la base local existente falla por estado previo | `.reports/execution/20261126/alembic-upgrade-isolated.txt`, `.reports/execution/20261126/alembic-upgrade.txt` |
| Casos CP-CU01 a CP-CU19 | catálogo académico | Diseñada, no ejecutada | `docs/quality/test-catalog.md` |
| Pruebas SUS | CU-06 | No ejecutada | `docs/requirements/use-cases/CU-06.md` |
| Carga/concurrencia | RNF de rendimiento | No ejecutada | `docs/architecture/quality-scenarios.md` |
| Seguridad externa | seguridad y privacidad | No ejecutada | `docs/quality/test-plan.md` |
| Aprobación de modelo ML | reporte reproducible, comparación, revisión humana | No ejecutada | `docs/adr/ADR-009-ciclo-de-vida-ml.md` |
| Benchmark de rendimiento | entorno, volumen, percentiles, errores y configuración | No ejecutada | `docs/adr/ADR-022-medicion-de-rendimiento.md` |
| Benchmark parcial de lectura de inventario | 100 solicitudes, TestClient e SQLite en memoria | Parcial; no es entorno aprobado | `.reports/execution/20261126/benchmark-inventory-read.txt` |
| Benchmark completo local | Validación de 1.000 filas y 100 lecturas; p95 63,605 ms / 13,717 ms; éxito 100% | Parcial; métricas cumplen umbrales iniciales, entorno no aprobado | `.reports/execution/20261126/benchmark-full-mvp.txt` |
| Benchmark HTTP aprobado de evaluación | Medición inicial p95 654,627 ms concurrente | Superseded; arnés inválido por crear un cliente por solicitud | `.reports/execution/20261126/benchmark-approved-http.txt` |
| Benchmark HTTP corregido de evaluación | Validación p95 84,724 ms; lectura concurrente p95 73,018 ms; disponibilidad sostenida 100% | Ejecutada; **PASS de umbrales iniciales** | `.reports/execution/20261126/benchmark-approved-http-final.txt` |
| Evaluación SUS | protocolo, participantes, tareas, instrumento y resultados | No ejecutada | `docs/adr/ADR-023-evaluacion-sus-separada.md` |
| Fallback ML | fallo/retiro de modelo, degradación visible y recuperación | No ejecutada | `docs/adr/ADR-024-fallback-auditable-ml.md` |
| Linaje de riesgo | origen, artefacto, dataset, horizonte, timestamp y `traceId` | No ejecutada | `docs/adr/ADR-025-trazabilidad-de-resultados-de-riesgo.md` |
| Monitoreo ML | calidad, distribución, referencia y cambio controlado | No ejecutada | `docs/adr/ADR-026-monitoreo-de-deriva-ml.md` |
| Reproducibilidad ML | código, dependencias, semilla, configuración, dataset y entorno | No ejecutada | `docs/adr/ADR-027-reproducibilidad-de-experimentos-ml.md` |
| Explicabilidad ML | variables influyentes, limitaciones y origen sin causalidad | No ejecutada | `docs/adr/ADR-028-explicabilidad-operativa-ml.md` |
| Revisión humana | predicción no ejecuta acciones automáticas y decisión auditada | No ejecutada | `docs/adr/ADR-029-revision-humana-obligatoria.md` |
| Auditoría | eventos append-only, integridad y correcciones por nuevos eventos | No ejecutada | `docs/adr/ADR-030-auditoria-inmutable.md` |
| Acceso a auditoría | rol, ámbito, rechazo y trazabilidad de consultas | No ejecutada | `docs/adr/ADR-031-acceso-restringido-auditoria.md` |
| Separación de datos | original restringido, proyección mínima y acceso excepcional | No ejecutada | `docs/adr/ADR-032-dataset-original-restringido.md` |
| Protección de datos restringidos | cifrado, acceso, auditoría y rotación sin secretos en Git | No ejecutada | `docs/adr/ADR-033-proteccion-de-datasets-restringidos.md` |
| Incidente de datos | contención, evidencia, evaluación, comunicación y recuperación | No ejecutada | `docs/adr/ADR-034-incidentes-de-datos.md` |
| Kill switch y rollback | permisos, desactivación, fallback, recuperación y auditoría | No ejecutada | `docs/adr/ADR-035-kill-switch-y-rollback.md` |

## Regla

Un caso diseñado no es evidencia de cumplimiento. Cada nueva evidencia debe
registrar fecha, entorno, versión, entrada, resultado, estado y artefacto
reproducible.

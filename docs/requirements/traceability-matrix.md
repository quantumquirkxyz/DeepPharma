# Matriz de trazabilidad

**Versión:** 0.2
**Estado:** Trazabilidad documental consolidada; evidencia de ejecución parcial
o pendiente
**Fuente:** matriz académica `SRC-04` y requisitos registrados

## 1. Trazabilidad de requisitos

| Necesidad | Característica | Requisito | Caso de uso | Escenario | Prueba diseñada / evidencia |
|---|---|---|---|---|---|
| NEC-01 Anticipar desabastecimiento | CAR-01 Predicción de riesgo | RF-03, RNF-03 | CU-03 | ESC-CU03-01 | CP-CU03-01; no ejecutada |
| NEC-02 Conocer inventario actual | CAR-02 Gestión de inventario | RF-05, RNF-05 | CU-05, CU-13 | ESC-CU05-01 | CP-CU05-01; ejecutada parcialmente |
| NEC-03 Usar datos históricos confiables | CAR-03 Calidad de datos | RF-01, RF-07, RF-08 | CU-01, CU-07, CU-08 | ESC-CU01-01, ESC-CU07-01 | CP-CU01-01, CP-CU07-01; no ejecutadas |
| NEC-04 Evaluar modelos | CAR-04 Ciclo de vida ML | RF-02, RF-10, RF-11 | CU-02, CU-10, CU-11 | ESC-CU02-01, ESC-CU10-01 | CP-CU02-01, CP-CU10-01; no ejecutadas |
| NEC-05 Actuar sobre riesgos | CAR-05 Alertas accionables | RF-04, RF-14, RF-15 | CU-04, CU-14, CU-15, CU-16 | ESC-CU04-01, ESC-CU15-01 | CP-CU04-01, CP-CU15-01; ejecutadas parcialmente |
| NEC-06 Validar usabilidad | CAR-06 Evaluación del producto | RF-06, RNF-06 | CU-06 | ESC-CU06-01 | CP-CU06-01; no ejecutada |
| NEC-07 Integrar fuentes | CAR-07 Interoperabilidad | RF-09, RF-18, RNF-09 | CU-09, CU-19 | ESC-CU09-01 | CP-CU09-01; no ejecutada |
| NEC-08 Proteger información | CAR-08 Acceso y auditoría | RF-17, RNF-18, RNF-19 | CU-18 | ESC-CU18-01 | CP-CU18-01; ejecutada parcialmente |
| NEC-09 Explicar resultados | CAR-09 Transparencia | RF-12, RNF-12 | CU-12 | ESC-CU12-01 | CP-CU12-01; no ejecutada |
| NEC-10 Informar decisiones | CAR-10 Reportes | RF-16, RNF-17 | CU-17 | ESC-CU17-01 | CP-CU17-01; no ejecutada |

## 2. Reglas de trazabilidad

- Todo requisito aprobado debe relacionarse con al menos un caso de uso, escenario, decisión arquitectónica o prueba.
- Todo caso de uso debe tener requisitos relacionados.
- Todo escenario aprobado debe tener al menos un caso de prueba.
- Todo mensaje de interacción debe poder rastrearse a una responsabilidad.
- Las referencias inexistentes bloquean la aprobación del artefacto.
- `No ejecutada` indica que existe diseño de prueba, pero no evidencia de
  ejecución.
- `Ejecutada parcialmente` indica evidencia del tracer bullet, no del
  escenario académico completo.

## 3. Estado

Esta matriz es una primera proyección técnica. Debe alinearse con la matriz académica oficial cuando se extraigan sus columnas definitivas y después de validar requisitos con stakeholders.

## 4. Cobertura de decisiones técnicas y criterios añadidos

La trazabilidad criterio por criterio de AC-01–AC-14 se mantiene en
`docs/requirements/acceptance-traceability-mvp.md`.

| Decisión / criterio | Artefacto relacionado | Verificación diseñada | Evidencia |
|---|---|---|---|
| Dataset validado antes de aplicar | ADR-002, RF-01 | integración de carga válida/inválida | Parcial |
| ML reproducible y fallback auditable | ADR-003, ADR-024, AC-06b | entrenamiento, fallo de carga y degradación | Pendiente |
| Ciclo y aprobación humana de modelos | ADR-009, ADR-029 | transición de estados y no automatización | Pendiente |
| Validación temporal y métricas ML | ADR-016, ADR-017 | evaluación temporal y reporte de métricas | Pendiente |
| Linaje de resultados | ADR-025, AC-06c | persistencia de origen, versión, dataset y `traceId` | Pendiente |
| Monitoreo de deriva | ADR-026, AC-06d | fixture con cambio controlado | Pendiente |
| Alertas y notificaciones | ADR-018, ADR-019 | tabla de transiciones y adaptador simulado | Parcial |
| RBAC, ámbito y auditoría | ADR-006, ADR-020, ADR-030, ADR-031 | acceso anónimo, rol insuficiente y ámbito incorrecto | Parcial |
| Datos restringidos | ADR-021, ADR-032, ADR-033 | separación, cifrado y acceso excepcional | Pendiente |
| Recuperación y rollback | ADR-014, ADR-034, ADR-035 | restore, incidente y kill switch | Pendiente |
| Rendimiento y SUS | ADR-022, ADR-023 | benchmark y protocolo académico | Pendiente |

La matriz académica conserva sus referencias y no convierte estos criterios
técnicos en resultados ejecutados.

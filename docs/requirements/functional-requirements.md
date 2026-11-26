# Requisitos funcionales

**Versión:** 0.1
**Estado:** Propuesta de línea base
**Fuente:** casos de uso `CU-01` a `CU-19`, `SRC-01`, `SRC-04`, `SRC-05`

| ID | Requisito | Caso de uso | Estado |
|---|---|---|---|
| RF-01 | El sistema debe registrar conjuntos históricos de inventario con procedencia, versión, período y estado. | CU-01 | Propuesto |
| RF-02 | El sistema debe entrenar y evaluar modelos utilizando conjuntos validados y configuraciones registradas. | CU-02 | Propuesto |
| RF-03 | El sistema debe generar predicciones de riesgo mediante un modelo aprobado y registrar su trazabilidad. | CU-03 | Propuesto |
| RF-04 | El sistema debe permitir consultar, filtrar y gestionar alertas priorizadas dentro del ámbito autorizado. | CU-04, CU-14, CU-15 | Propuesto |
| RF-05 | El sistema debe registrar y consultar inventario actual por medicamento y centro de salud. | CU-05, CU-13 | Propuesto |
| RF-06 | El proyecto debe ejecutar una evaluación SUS documentada sobre el prototipo. | CU-06 | Académico |
| RF-07 | El sistema debe validar conjuntos de datos contra un esquema versionado. | CU-07 | Propuesto |
| RF-08 | El sistema debe generar versiones reproducibles de datos preprocesados. | CU-08 | Propuesto |
| RF-09 | El sistema debe sincronizar inventario mediante adaptadores de fuentes externas autorizadas. | CU-09 | Propuesto |
| RF-10 | El sistema debe producir reportes de evaluación de modelos. | CU-10 | Propuesto |
| RF-11 | El sistema debe registrar el ciclo de vida de modelos aprobados. | CU-11 | Propuesto |
| RF-12 | El sistema debe mostrar explicaciones disponibles de predicciones con su modelo y versión. | CU-12 | Candidato |
| RF-13 | El sistema debe mostrar el detalle y la procedencia de una alerta. | CU-14 | Candidato |
| RF-14 | El sistema debe registrar reconocimiento, escalamiento y resolución de alertas. | CU-15 | Candidato |
| RF-15 | El sistema debe notificar condiciones críticas mediante canales autorizados. | CU-16 | Propuesto |
| RF-16 | El sistema debe generar reportes de inventario, riesgo y gestión. | CU-17 | Candidato |
| RF-17 | El sistema debe administrar usuarios, roles y ámbitos de acceso. | CU-18 | Candidato |
| RF-18 | El sistema debe permitir configurar fuentes e integraciones versionadas. | CU-19 | Candidato |

## Criterios

- Cada requisito debe mantenerse atómico, verificable y trazable.
- “Propuesto” no significa aprobado por stakeholders.
- Los requisitos candidatos se consolidarán después de revisar duplicaciones y alcance del MVP.
- `CU-06` es una exigencia académica de validación, no necesariamente una funcionalidad del MVP.

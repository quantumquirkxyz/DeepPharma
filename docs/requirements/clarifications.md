# Registro de aclaraciones pendientes

**Estado:** Abierto; cada punto bloquea únicamente las decisiones que indica.

| ID | Pregunta | Responsable | Bloquea | Estado |
|---|---|---|---|---|
| CL-01 | ¿Cuál es la fuente autorizada y la unidad institucional de inventario? | Stakeholder institucional | Validación de datos reales | Abierta |
| CL-02 | ¿Cómo se define desabastecimiento observado y cuál es su horizonte? | Responsable de dominio | Modelo ML y métricas | Abierta |
| CL-03 | ¿Qué centros puede consultar y modificar cada rol? | Responsable institucional de seguridad | Autorización por ámbito | Abierta |
| CL-04 | ¿Cuál es la política concreta de retención y eliminación de datos institucionales? | Responsable de datos/privacidad | Dataset institucional y despliegue | Abierta; controles mínimos definidos en ADR-021 y retención provisional en ADR-008 |
| CL-05 | ¿Qué contrato técnico autorizado expone SALMI? | Responsable de integración | Integración real | Abierta |
| CL-06 | ¿Qué entorno y límites de capacidad se usarán para medir rendimiento? | Responsable técnico | RNF y SLO | Abierta; estrategia de medición definida en ADR-022 |
| CL-07 | ¿Qué protocolo y muestra se usarán para CU-06/SUS? | Responsable académico | Evidencia académica SUS | Abierta; separación y requisitos mínimos definidos en ADR-023 |
| CL-08 | ¿Qué formatos de entrada se aprobarán primero: CSV/XLSX, JSON u otro? | Responsable técnico/ académico | Contrato de importación | Abierta |
| CL-09 | ¿El período 2019–2023 es un dato confirmado o solo una hipótesis de trabajo? | Stakeholder institucional | CU-01 y dataset histórico | Abierta |
| CL-10 | ¿Qué dataset institucional, si alguno, reemplazará posteriormente al dataset sintético y qué validación tendrá? | Responsable de datos/ML | Generalización institucional | Abierta |
| CL-11 | ¿Qué umbrales mínimos numéricos de evaluación se adoptarán cuando exista contexto de dominio? | Responsable de datos/ML | Política cuantitativa futura; el proceso de aprobación ya está definido | Abierta |

## Regla

Mientras una aclaración permanezca abierta, el proyecto puede usar fixtures
sintéticos y propuestas técnicas, pero no puede presentar la decisión como
institucionalmente aprobada ni cerrar el requisito dependiente.

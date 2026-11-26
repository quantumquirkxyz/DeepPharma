# Registro de riesgos arquitectónicos

**Versión:** 0.1
**Estado:** Registro inicial; riesgos abiertos hasta evidencia

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Evidencia de cierre |
|---|---|---:|---:|---|---|
| RSK-01 | El contrato de SALMI no está disponible | Alta | Alta | Adaptador simulado y puerto estable | Contrato autorizado o simulación documentada |
| RSK-02 | Datos históricos insuficientes o no autorizados | Media | Alta | Dataset público/sintético, procedencia y validación | Registro de fuente y calidad |
| RSK-03 | El modelo predictivo no alcanza desempeño útil | Media | Alta | Modelo base, métricas y límites explícitos | Reporte reproducible |
| RSK-04 | El monolito se vuelve altamente acoplado | Media | Media | Módulos, contratos, revisión de dependencias | Revisión arquitectónica |
| RSK-05 | Documentación, diagramas y código divergen | Alta | Alta | Trazabilidad y quality gates | Matriz actualizada y revisión |
| RSK-06 | Exposición de datos sensibles | Baja | Alta | Datos autorizados, RBAC y revisión de secretos | Scan y evidencia de permisos |
| RSK-07 | Entrenamiento compite con la API | Media | Media | Worker separado y límite operativo | Prueba de carga |
| RSK-08 | Requisitos académicos y MVP entran en conflicto | Media | Alta | Separar obligatorio y complementario | Auditoría contra rúbrica |

## Estados

- `abierto`
- `mitigado`
- `aceptado`
- `cerrado`

Todos los riesgos comienzan en estado `abierto` hasta presentar evidencia.

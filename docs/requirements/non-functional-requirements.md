# Requisitos no funcionales

**Versión:** 0.1
**Estado:** Propuesta de línea base
**Fuente:** `SRC-01`, `SRC-03`, `SRC-11`, `SRC-14`, `SRC-15`

| ID | Categoría | Requisito verificable | Estado |
|---|---|---|---|
| RNF-01 | Rendimiento | Registrar un conjunto estándar de hasta 50.000 registros en menos de 5 minutos, cuando la capacidad sea aprobada y medida. | Propuesto |
| RNF-02 | Rendimiento ML | Completar entrenamiento dentro del límite aprobado para el entorno documentado. | Pendiente de medición |
| RNF-03 | Rendimiento ML | Completar una ejecución de predicción dentro del tiempo objetivo aprobado. | Pendiente de medición |
| RNF-04 | Rendimiento UI | Cargar el dashboard dentro del tiempo objetivo aprobado bajo una carga definida. | Pendiente de medición |
| RNF-05 | Rendimiento | Reflejar una actualización de inventario dentro del tiempo objetivo aprobado. | Pendiente de medición |
| RNF-06 | Usabilidad | Obtener y documentar la evaluación SUS bajo el protocolo aprobado. | Académico |
| RNF-07 | Reproducibilidad | Repetir una validación con la misma versión y configuración produciendo un resultado explicable. | Propuesto |
| RNF-08 | Reproducibilidad ML | Repetir procesamiento y entrenamiento con dataset, configuración y semillas registradas. | Propuesto |
| RNF-09 | Integración | Registrar timeout, error y recuperación de fuentes externas sin pérdida silenciosa de datos válidos. | Propuesto |
| RNF-10 | Evaluación ML | Conservar métricas, dataset, versión, configuración y limitaciones de cada evaluación. | Propuesto |
| RNF-11 | Auditabilidad | Conservar decisiones de aprobación, promoción y retiro de modelos. | Propuesto |
| RNF-12 | Transparencia | Identificar modelo, versión, fecha y limitaciones de una predicción mostrada. | Candidato |
| RNF-13 | Consulta | Aplicar un objetivo de respuesta medido para consultas de inventario. | Pendiente de medición |
| RNF-14 | Trazabilidad | Relacionar alertas con predicciones, modelos, datos y fechas. | Propuesto |
| RNF-15 | Auditoría | Registrar actor, fecha, estado anterior y nuevo en acciones de alertas. | Propuesto |
| RNF-16 | Notificaciones | Registrar entrega, fallo, reintento y destinatario dentro del tiempo objetivo aprobado. | Pendiente de medición |
| RNF-17 | Reportes | Generar reportes dentro del tiempo objetivo definido para cada volumen. | Pendiente de medición |
| RNF-18 | Seguridad | Aplicar autenticación, autorización RBAC, mínimo privilegio y auditoría de cambios de acceso. | Propuesto |
| RNF-19 | Seguridad | No exponer secretos, credenciales ni datos no autorizados en código, logs o reportes. | Propuesto |
| RNF-20 | Mantenibilidad | Mantener separación entre dominio, adaptadores, persistencia e interfaces mediante contratos versionados. | Propuesto |
| RNF-21 | Disponibilidad | Informar degradación o indisponibilidad de fuentes externas sin presentar datos desactualizados como actuales. | Propuesto |
| RNF-22 | Accesibilidad | Aplicar criterios de accesibilidad aprobados al dashboard y prototipos evaluados. | Candidato |

Los valores definitivos de rendimiento requieren medición, hardware, volumen y condiciones de prueba documentadas.

# Catálogo de escenarios

**Versión:** 0.1
**Estado:** Catálogo inicial de trazabilidad
**Fuente:** especificaciones `CU-01` a `CU-19` y `SRC-06`

| ID | Caso de uso | Tipo | Descripción | Prueba |
|---|---|---|---|---|
| ESC-CU01-01 | CU-01 | Principal | Registrar un archivo histórico válido | CP-CU01-01 |
| ESC-CU01-02 | CU-01 | Excepción | Rechazar formato no soportado | CP-CU01-02 |
| ESC-CU01-03 | CU-01 | Alterno | Registrar datos desde fuente externa disponible | CP-CU01-03 |
| ESC-CU01-04 | CU-01 | Excepción | Gestionar fuente externa no disponible | CP-CU01-04 |
| ESC-CU02-01 | CU-02 | Principal | Entrenamiento reproducible con datos válidos | CP-CU02-01 |
| ESC-CU02-02 | CU-02 | Excepción | Rechazar fuga de información | CP-CU02-02 |
| ESC-CU02-03 | CU-02 | Excepción | Ningún modelo alcanza el criterio mínimo | CP-CU02-03 |
| ESC-CU02-04 | CU-02 | Alterno | Registrar modelo recomendado pendiente de aprobación | CP-CU02-04 |
| ESC-CU03-01 | CU-03 | Principal | Generación programada exitosa | CP-CU03-01 |
| ESC-CU03-02 | CU-03 | Alterno | Ejecución manual autorizada | CP-CU03-02 |
| ESC-CU03-03 | CU-03 | Excepción | Datos insuficientes para una entidad | CP-CU03-03 |
| ESC-CU03-04 | CU-03 | Excepción | Ausencia de modelo aprobado | CP-CU03-04 |
| ESC-CU03-05 | CU-03 | Excepción | Fallo con predicción anterior disponible | CP-CU03-05 |
| ESC-CU04-01 | CU-04 | Principal | Consultar alertas críticas | CP-CU04-01 |
| ESC-CU04-02 | CU-04 | Alterno | Consultar sin resultados | CP-CU04-02 |
| ESC-CU04-03 | CU-04 | Alterno | Revisar detalle de alerta | CP-CU04-03 |
| ESC-CU04-04 | CU-04 | Alterno | Reconocer una alerta | CP-CU04-04 |
| ESC-CU04-05 | CU-04 | Excepción | Consultar predicción desactualizada | CP-CU04-05 |
| ESC-CU04-06 | CU-04 | Alterno | Exportar alertas filtradas | CP-CU04-06 |
| ESC-CU05-01 | CU-05 | Principal | Registrar actualización válida | CP-CU05-01 |
| ESC-CU05-02 | CU-05 | Excepción | Rechazar cantidad negativa | CP-CU05-02 |
| ESC-CU05-03 | CU-05 | Alterno | Consultar inventario por centro y medicamento | CP-CU05-03 |
| ESC-CU05-04 | CU-05 | Excepción | Resolver conflicto de concurrencia | CP-CU05-04 |
| ESC-CU05-05 | CU-05 | Alterno | Recibir datos mediante adaptador externo | CP-CU05-05 |
| ESC-CU06-01 | CU-06 | Principal | Evaluación SUS completada | CP-CU06-01 |
| ESC-CU06-02 | CU-06 | Excepción | Respuestas incompletas | CP-CU06-02 |
| ESC-CU06-03 | CU-06 | Excepción | Muestra insuficiente | CP-CU06-03 |
| ESC-CU06-04 | CU-06 | Alterno | Hallazgo asociado a una pantalla | CP-CU06-04 |
| ESC-CU07-01 | CU-07 | Principal | Validación exitosa | CP-CU07-01 |
| ESC-CU07-02 | CU-07 | Excepción | Columnas obligatorias faltantes | CP-CU07-02 |
| ESC-CU07-03 | CU-07 | Excepción | Datos duplicados y nulos | CP-CU07-03 |
| ESC-CU07-04 | CU-07 | Alterno | Revalidación de versión corregida | CP-CU07-04 |
| ESC-CU08-01 | CU-08 | Principal | Preprocesamiento reproducible exitoso | CP-CU08-01 |
| ESC-CU08-02 | CU-08 | Excepción | Bloqueo por conjunto no validado | CP-CU08-02 |
| ESC-CU08-03 | CU-08 | Excepción | Rechazo por fuga de información | CP-CU08-03 |
| ESC-CU08-04 | CU-08 | Alterno | Reprocesamiento con nueva versión | CP-CU08-04 |
| ESC-CU09-01 | CU-09 | Principal | Sincronización completa exitosa | CP-CU09-01 |
| ESC-CU09-02 | CU-09 | Alterno | Sincronización incremental | CP-CU09-02 |
| ESC-CU09-03 | CU-09 | Alterno | Uso del adaptador simulado | CP-CU09-03 |
| ESC-CU09-04 | CU-09 | Excepción | Fuente externa no disponible | CP-CU09-04 |
| ESC-CU09-05 | CU-09 | Excepción | Respuesta incompatible | CP-CU09-05 |
| ESC-CU10-01 | CU-10 | Principal | Evaluación exitosa de un modelo | CP-CU10-01 |
| ESC-CU10-02 | CU-10 | Alterno | Comparación de modelos candidatos | CP-CU10-02 |
| ESC-CU10-03 | CU-10 | Excepción | Detección de fuga de información | CP-CU10-03 |
| ESC-CU10-04 | CU-10 | Excepción | Desempeño insuficiente | CP-CU10-04 |
| ESC-CU10-05 | CU-10 | Alterno | Métricas por segmento | CP-CU10-05 |
| ESC-CU11-01 | CU-11 | Principal | Aprobar modelo evaluado | CP-CU11-01 |
| ESC-CU11-02 | CU-11 | Excepción | Reporte incompleto | CP-CU11-02 |
| ESC-CU11-03 | CU-11 | Alterno | Retirar modelo vigente | CP-CU11-03 |
| ESC-CU11-04 | CU-11 | Alterno | Reemplazar modelo conservando historial | CP-CU11-04 |
| ESC-CU12-01 | CU-12 | Principal | Consultar explicación local | CP-CU12-01 |
| ESC-CU12-02 | CU-12 | Alterno | Consultar metadata del modelo | CP-CU12-02 |
| ESC-CU12-03 | CU-12 | Alterno | Consultar predicción con modelo retirado | CP-CU12-03 |
| ESC-CU12-04 | CU-12 | Excepción | Explicación no disponible | CP-CU12-04 |
| ESC-CU13-01 | CU-13 | Principal | Consulta por centro y medicamento | CP-CU13-01 |
| ESC-CU13-02 | CU-13 | Alterno | Consulta sin resultados | CP-CU13-02 |
| ESC-CU13-03 | CU-13 | Excepción | Consulta de dato desactualizado | CP-CU13-03 |
| ESC-CU13-04 | CU-13 | Alterno | Consulta de historial | CP-CU13-04 |
| ESC-CU13-05 | CU-13 | Excepción | Ámbito no autorizado | CP-CU13-05 |
| ESC-CU14-01 | CU-14 | Principal | Detalle con evidencia completa | CP-CU14-01 |
| ESC-CU14-02 | CU-14 | Excepción | Predicción desactualizada | CP-CU14-02 |
| ESC-CU14-03 | CU-14 | Alterno | Explicación vinculada | CP-CU14-03 |
| ESC-CU14-04 | CU-14 | Excepción | Acceso no autorizado | CP-CU14-04 |
| ESC-CU15-01 | CU-15 | Principal | Reconocer alerta | CP-CU15-01 |
| ESC-CU15-02 | CU-15 | Alterno | Escalar alerta | CP-CU15-02 |
| ESC-CU15-03 | CU-15 | Alterno | Registrar acción de reposición externa | CP-CU15-03 |
| ESC-CU15-04 | CU-15 | Alterno | Resolver alerta | CP-CU15-04 |
| ESC-CU15-05 | CU-15 | Excepción | Transición inválida | CP-CU15-05 |
| ESC-CU16-01 | CU-16 | Principal | Notificación crítica entregada | CP-CU16-01 |
| ESC-CU16-02 | CU-16 | Alterno | Alerta visible en dashboard | CP-CU16-02 |
| ESC-CU16-03 | CU-16 | Excepción | Servicio externo no disponible | CP-CU16-03 |
| ESC-CU16-04 | CU-16 | Alterno | Reintento sin duplicación | CP-CU16-04 |
| ESC-CU16-05 | CU-16 | Excepción | Destinatario no configurado | CP-CU16-05 |
| ESC-CU17-01 | CU-17 | Principal | Reporte de alertas por centro | CP-CU17-01 |
| ESC-CU17-02 | CU-17 | Principal | Reporte de inventario por período | CP-CU17-02 |
| ESC-CU17-03 | CU-17 | Excepción | Reporte sin datos | CP-CU17-03 |
| ESC-CU17-04 | CU-17 | Alterno | Exportación autorizada | CP-CU17-04 |
| ESC-CU17-05 | CU-17 | Excepción | Rechazo por ámbito | CP-CU17-05 |
| ESC-CU18-01 | CU-18 | Principal | Crear usuario farmacéutico | CP-CU18-01 |
| ESC-CU18-02 | CU-18 | Alterno | Asignar ámbito por centro | CP-CU18-02 |
| ESC-CU18-03 | CU-18 | Alterno | Desactivar usuario | CP-CU18-03 |
| ESC-CU18-04 | CU-18 | Excepción | Rechazar elevación de privilegios | CP-CU18-04 |
| ESC-CU19-01 | CU-19 | Principal | Configurar adaptador simulado | CP-CU19-01 |
| ESC-CU19-02 | CU-19 | Alterno | Probar fuente sin activarla | CP-CU19-02 |
| ESC-CU19-03 | CU-19 | Principal | Activar fuente autorizada | CP-CU19-03 |
| ESC-CU19-04 | CU-19 | Alterno | Rotar credenciales | CP-CU19-04 |
| ESC-CU19-05 | CU-19 | Excepción | Contrato incompatible | CP-CU19-05 |

## 2. Reglas

- Un escenario describe un camino concreto, no el caso de uso completo.
- Los escenarios principales, críticos y de excepción tienen prioridad para pruebas.
- Cada escenario debe derivar de un flujo numerado de su caso de uso.
- Los identificadores son estables y no se reutilizan.

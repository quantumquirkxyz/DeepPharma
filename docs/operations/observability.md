# Diseño de observabilidad

**Estado:** Diseño productivo aceptado; SLOs numéricos pendientes de medición.

## Señales

| Señal | Contenido | Uso |
|---|---|---|
| Logs | evento, nivel, actor anonimizado, `traceId`, duración, resultado | diagnóstico |
| Métricas | requests, errores, latencia, filas, jobs, alertas | capacidad y salud |
| Trazas | API, persistencia, importación, ML y adaptadores | causalidad |
| Auditoría | actor, acción, estado anterior/nuevo, fuente | cumplimiento |

## Dashboards

- salud de API y base de datos;
- validación/importación;
- entrenamiento/evaluación ML;
- alertas y transiciones;
- fuentes externas;
- seguridad y errores de autorización.

## Alertas

Los umbrales deben aprobarse tras medición. Las reglas deben evitar alertas
duplicadas, incluir contexto y enlazar un runbook.

## No hacer

- registrar secretos;
- registrar datos sensibles sin clasificación;
- presentar una métrica de desarrollo como SLO productivo;
- cerrar un incidente sin evidencia.

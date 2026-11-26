# Glosario de dominio DeepPharma

**Estado:** Borrador controlado pendiente de validación con stakeholders
**Versión:** 0.2
**Fuente:** Contexto académico, SDD y ADR-002–ADR-004

| Término | Definición provisional | Estado |
| --- | --- | --- |
| Medicamento | Producto del cuadro básico cuya disponibilidad se controla en un centro de salud | Pendiente de fuente oficial |
| Centro de salud | Instalación donde se almacena, dispensa o registra inventario de medicamentos | Pendiente de validación |
| Inventario histórico | Registros fechados de existencias y consumo utilizados para análisis y entrenamiento | Confirmado conceptualmente |
| Inventario actual | Estado más reciente conocido de existencias por medicamento y centro de salud | Confirmado conceptualmente |
| Stock | Cantidad disponible de un medicamento en un momento determinado | Pendiente de unidad y reglas |
| Consumo | Cantidad utilizada o dispensada durante un período | Pendiente de fuente y periodicidad |
| Días de cobertura | Tiempo estimado durante el cual el stock disponible cubre el consumo esperado | Pendiente de fórmula |
| Tiempo de reposición / lead time | Tiempo entre la solicitud de reposición y la disponibilidad efectiva del medicamento | Pendiente de fuente normativa |
| Desabastecimiento | Situación en que la disponibilidad no satisface la demanda o el umbral operativo definido | Requiere criterio verificable |
| Riesgo crítico | Clasificación de riesgo que requiere atención prioritaria | Umbral pendiente de validación |
| Riesgo medio | Clasificación intermedia que requiere seguimiento | Umbral pendiente de validación |
| Riesgo OK | Clasificación sin riesgo operativo según el umbral vigente | Umbral pendiente de validación |
| Baseline determinista de riesgo operativo | Regla determinista versionada para apoyar la anticipación operativa sin afirmar desempeño ML ni predicción clínica | Aceptado para MVP; no clínico |
| Conjunto de datos | Carga inmutable de registros con fuente, versión, estado y errores de validación | Aceptado para MVP |
| Estado de validación | Resultado técnico de revisar un conjunto: `VALIDO` o `RECHAZADO` | Aceptado para MVP |
| Gestión de alerta | Transición auditada del estado de una alerta ejecutada por un actor autorizado | Aceptado para MVP |
| Predicción | Resultado calculado por un modelo para un horizonte futuro definido | Confirmado conceptualmente |
| Alerta | Notificación accionable derivada de una condición de riesgo | Confirmado conceptualmente |
| Modelo aprobado | Versión de un modelo que cumple los criterios de evaluación y puede usarse para inferencia | Criterios pendientes |
| Experimento ML | Ejecución reproducible de entrenamiento o evaluación con dataset, configuración, semilla y métricas | Aceptado para MVP |
| Modelo ML retirado | Modelo que conserva historial pero ya no puede seleccionarse para nueva inferencia | Aceptado para MVP |
| Entrenamiento | Proceso de ajustar un modelo con datos históricos disponibles | Confirmado conceptualmente |
| Inferencia | Ejecución de un modelo aprobado sobre datos para producir predicciones | Confirmado conceptualmente |
| Datos públicos | Datos cuya publicación y reutilización están autorizadas | Requiere verificar licencia |
| Datos sintéticos | Datos generados artificialmente para desarrollo o demostración sin representar registros reales identificables | Confirmado conceptualmente |
| Datos institucionales | Datos proporcionados por una institución y sujetos a autorización y restricciones de uso | Confirmado conceptualmente |

## Términos que no deben mezclarse

- **Stock** no es sinónimo de **días de cobertura**.
- **Predicción** no es sinónimo de **alerta**: una predicción puede no generar una alerta.
- **Entrenamiento** no es sinónimo de **inferencia**.
- **Desabastecimiento observado** no es automáticamente igual a **riesgo predicho**.
- **Actor externo** no es sinónimo de **proceso automático interno**.
- **Baseline de riesgo** no es sinónimo de **modelo ML aprobado** ni de precisión clínica.

## Regla de vocabulario

`Medicamento`, `Centro de salud`, `Inventario`, `Stock` y `Desabastecimiento`
mantienen definiciones operativas provisionales para el MVP sintético. No se
interpretan como definiciones normativas o institucionales hasta incorporar
una fuente oficial.

## Pendientes críticos

- Definir formalmente la variable objetivo de desabastecimiento.
- Confirmar unidades, periodicidad y calidad del consumo.
- Definir fórmula de días de cobertura.
- Confirmar umbrales de riesgo y si son configurables.
- Confirmar horizonte de predicción y tolerancia operacional.
- Identificar las fuentes institucionales que autorizan medicamentos, centros y tiempos de reposición.

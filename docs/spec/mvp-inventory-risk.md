# Especificación SDD — MVP de inventario y riesgo

**Estado:** Baseline aprobada para planificación; no publicada en GitHub
**Alcance:** MVP ejecutable

> **Estado de handoff:** `blocked` hasta completar el benchmark aprobado y la
> aprobación formal de la baseline.

## Problema

Los usuarios necesitan registrar inventario por medicamento y centro de salud,
validar cargas de datos, detectar riesgo de desabastecimiento y gestionar
alertas con evidencia auditable.

## Objetivos

- Registrar inventario actual sin duplicar la combinación medicamento-centro.
- Validar datos importados antes de persistirlos.
- Entrenar/evaluar un modelo ML reproducible con datos sintéticos o públicos
  autorizados y conservar un baseline determinista como fallback.
- Gestionar alertas dentro del ámbito autorizado.
- Mantener trazabilidad de actor, fuente, versión y estado.

## Historias y criterios

### US-01 — Importar datos

Como administrador, quiero cargar un conjunto de inventario para validarlo y
conocer errores antes de aplicarlo.

- AC-01: se valida esquema y tipos.
- AC-02: se detectan referencias inexistentes, duplicados y cantidades inválidas.
- AC-03: una carga rechazada no modifica el inventario actual.
- AC-04: la carga conserva procedencia, versión y estado.

### US-02 — Evaluar riesgo

Como farmacéutico, quiero consultar el riesgo del inventario actual.

- AC-05: la evaluación usa un modelo versionado y reproducible o el fallback
  determinista documentado.
- AC-06: cada predicción registra nivel, probabilidad, horizonte configurable,
  modelo, versión, dataset y limitaciones.
- AC-06a: el experimento registra particiones temporales, controles de fuga y
  precisión, recall, F1, matriz de confusión y PR-AUC cuando apliquen.
- AC-06b: si el modelo ML no está disponible, el sistema puede usar
  `baseline-rules-1`, registrando la degradación como
  `FALLBACK_DETERMINISTA`, causa, versión y `traceId`.
- AC-06c: cada resultado registra origen, versión, dataset/experimento,
  horizonte, timestamp y `traceId`; una recalculación crea un resultado nuevo.
- AC-06d: el MVP registra calidad, distribución y comparación contra una
  referencia para detectar cambios controlados en datos o desempeño.
- AC-06e: los resultados ML aprobados incluyen explicación operativa,
  variables influyentes, horizonte, limitaciones y origen, sin afirmar
  causalidad.
- AC-06f: ningún resultado ML o fallback ejecuta automáticamente una acción
  clínica, reposición institucional o mutación irreversible; toda acción
  requiere revisión humana autorizada y auditoría.
- AC-06g: los eventos de dominio y decisiones humanas se registran como
  auditoría append-only, con `traceId` e integridad verificable.
- AC-06h: la consulta de auditoría respeta rol y ámbito; una consulta fuera de
  autorización se rechaza y también queda registrada.
- AC-06i: el sistema puede desactivar modelo, notificaciones o integración
  defectuosa mediante una acción autorizada, aplicar el fallback o estado
  seguro y registrar la operación.
- AC-07: reevaluar no duplica alertas activas.

### US-03 — Gestionar alertas

Como farmacéutico, quiero reconocer y resolver alertas.

- AC-08: solo roles autorizados cambian estados.
- AC-09: cada transición registra actor, estado anterior, nuevo estado y comentario.
- AC-10: alertas cerradas no pueden modificarse.

### US-04 — Integración simulada

Como operador, quiero probar una fuente externa sin depender todavía de SALMI.

- AC-11: el adaptador simulado cumple el puerto de integración.
- AC-12: fallos no modifican silenciosamente el inventario.
- AC-13: cada sincronización registra fuente, resultado y error.
- AC-14: las notificaciones simuladas registran intento, resultado, error y
  reintento sin enviar mensajes institucionales.

## No objetivos del MVP

- Afirmar precisión clínica o validez institucional sin datos y evaluación
  documentados.
- Conectar SALMI real sin contrato técnico autorizado.
- Notificar a canales institucionales reales.
- Sustituir decisiones clínicas o de abastecimiento humano.

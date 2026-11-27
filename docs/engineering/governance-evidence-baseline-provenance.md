# Sub-Spec: Governance Evidence and Baseline Provenance

**Estado:** Borrador de sub-spec; ejecución parcial; no certifica producción.
**Traza:** Parent Spec #2 → Sub-Spec #7 → Ticket #25.
**Criterios:** AC-01–AC-14, ADR-060.
**Versión:** 0.1
**Fecha:** 2026-11-27

## 1. Problema

DeepPharma necesita una base de gobernanza y trazabilidad duradera y revisable antes de que se considere ejecutado cualquier requisito del MVP. La evidencia de ejecución actual es parcial: algunos criterios tienen pruebas trazables, otros solo tienen diseño académico sin ejecución, y ninguno puede afirmarse completo sin un oracle de prueba y un registro de evidencia explícito.

Este sub-spec define los requisitos atómicos, los criterios de aceptación observables, la seam de verificación, el oracle de prueba y la expectativa de evidencia para cada criterio AC-01–AC-14, bajo la excepción gobernada de ADR-060.

## 2. Objetivos

- Definir requisitos atómicos trazables al Parent Spec #2 y a los criterios nombrados (AC-01–AC-14, ADR-060).
- Identificar, para cada criterio, la seam explícita, el oracle de prueba y la expectativa de evidencia antes de declarar readiness.
- Marcar el comportamiento no ejecutado como tal, de modo que no pueda presentarse como completo.
- Conservar la excepción de ADR-060 sin presentar como cumplimiento automático lo que sigue bloqueado o parcial.

## 3. No objetivos

- Certificación de producción.
- Validez clínica o institucional.
- Integraciones fuera del Parent Spec (SALMI real, notificaciones institucionales, datos no autorizados).
- Implementación de comportamiento de producto más allá del alcance de trazabilidad y evidencia.

## 4. Criterios de aceptación (rastreabilidad a AC-01–AC-14)

Cada criterio declara: requisito atómico, seam de verificación, oracle de prueba, expectativa de evidencia y estado actual. El estado refleja la evidencia ejecutada, no la intención de diseño.

| ID | Requisito atómico | Seam | Oracle de prueba | Expectativa de evidencia | Estado | Fuente de estado |
|----|-------------------|------|------------------|--------------------------|--------|------------------|
| AC-01 | Validación de esquema y tipos (US-01) | `Pydantic DatasetPayload` / API validación | `test_dataset_validation_persists_valid_source` | Persistencia de origen válido | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-02 | Detección de referencias inexistentes, duplicados y cantidades inválidas (US-01) | `DatasetValidator` | `test_invalid_dataset_does_not_change_inventory` | Inventario sin mutación en carga inválida | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-03 | Carga rechazada no modifica inventario (US-01) | Transacción de aplicación con rollback | `test_invalid_dataset_does_not_change_inventory` | Sin cambios en inventario tras rechazo | Executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-04 | Procedencia, versión y estado de la carga (US-01) | Persistencia `ConjuntoDatos` | `test_dataset_validation_persists_valid_source` | Registro de origen, versión y estado | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-05 | Modelo versionado reproducible o fallback determinista (US-02) | `RiskEvaluator` | `test_risk_evaluation_creates_prediction_and_critical_alert` | Predicción y alerta crítica creadas | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06 | Metadatos de predicción y limitaciones (US-02) | `PredictionRead` | Integración de riesgo | Nivel, probabilidad, horizonte, modelo, versión, dataset, limitaciones | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06a | Particiones temporales y métricas ML | `ADR-017`; experiment runner futuro | No ejecutada aún | Métricas de evaluación temporal | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06b | Fallback determinista auditable | `ADR-024`; `baseline-rules-1` | Integración fallback | Registro `FALLBACK_DETERMINISTA`, causa, versión, `traceId` | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06c | Linaje de resultados y recálculo no silencioso | `ADR-025` | No hay prueba de linaje ejecutable aún | Origen, versión, dataset, horizonte, timestamp, `traceId` | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06d | Calidad y monitoreo de deriva | `ADR-026` | No hay prueba de monitoreo ejecutable aún | Fixture con cambio controlado | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06e | Explicación operativa sin causalidad | `ADR-028` | No hay prueba de explicabilidad ejecutable aún | Variables influyentes, limitaciones, origen | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06f | Revisión humana y sin acción automática irreversible | `ADR-029` | No hay prueba de autorización-acción ejecutable aún | Decisión humana auditada | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06g | Auditoría append-only con integridad | Historial de alertas; `ADR-030` | Parcial | Eventos append-only con `traceId` e integridad verificable | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06h | Consulta de auditoría con ámbito y registro de rechazo | `ADR-031` | Parcial | Consulta fuera de ámbito rechazada y registrada | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-06i | Kill switch autorizado y fallback seguro | `ADR-035` | No hay prueba ejecutable aún | Desactivación autorizada, fallback o estado seguro, operación registrada | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-07 | Reevaluación no duplica alertas activas (US-03) | Integración de riesgo | `test_risk_evaluation_creates_prediction_and_critical_alert` | Sin duplicación de alertas activas | Executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-08 | Cambios de estado de alerta autorizados (US-03) | `test_token_scopes_follow_user_role` y parche de alerta | Parcial | Solo roles autorizados cambian estados | Partial | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-09 | Transición: actor, estado previo, nuevo estado, comentario (US-03) | Aserciones de historial en integración de riesgo | Parcial | Transición registrada completamente | Executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-10 | Alertas cerradas no modificables | `ADR-018` | No hay prueba de estado terminal ejecutable aún | Alertas cerradas inmutables | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-11 | Adaptador simulado cumple puerto de integración (US-04) | `ADR-004` | No hay prueba de adaptador presente aún | Adaptador cumple el puerto | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-12 | Fallo de fuente no muta silenciosamente inventario (US-04) | `ADR-004` | No hay prueba de integración de fallo aún | Inventario sin mutación silenciosa | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-13 | Sincronización registra fuente, resultado y error (US-04) | `ADR-004` | No hay prueba de sincronización aún | Registro de fuente, resultado y error | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |
| AC-14 | Notificaciones simuladas: intento, resultado, error, reintento (US-04) | `ADR-019` | No hay prueba de adaptador de notificaciones aún | Registro sin envío institucional real | Not executed | `docs/requirements/acceptance-traceability-mvp.md` |

**Leyenda de estado:** `Executed` = prueba con evidencia directa para el criterio; `Partial` = tracer bullet cubre solo parte del criterio; `Not executed` = diseño o ADR existe sin evidencia ejecutable.

## 5. Seam de verificación y oracle de prueba

**Seam principal:** validación de procedencia de artefactos JSON mediante el validador dependencia-free de SHA-256 con comprobación de contención de rutas y escritura atómica de reportes (implementado en Ticket #25, branch `issue/25-artifact-provenance-validation`).

- Entrada: artefacto JSON con `sourceArtifacts` y `sourceDigests` (`sha256:<64 hex>`).
- Oracle: el validador calcula SHA-256 sobre los bytes actuales y lo compara con el digest declarado; devuelve `0` solo cuando todas las referencias pasan.
- Estados de reporte: `passed`, `failed`, `invalid`; un fallo parcial se conserva como auditable y no se confunde con éxito.

**Seam secundaria (donde aplique):** comportamiento de API mediante `uv run pytest` en `apps/api`.

**Comandos de validación:**
- `python3 -m json.tool` sobre artefactos JSON de requisitos y arquitectura.
- `python3 .agents/skills/platform/artifacts/validate_provenance.py <artefacto> --root . --report <reporte>`
- `uv run pytest` (solo para comportamiento de API donde aplique).
- `git diff --check`.

## 6. Traza y dependencias

- Parent Spec #2 debe mantener `status:ready` o superior. (Pendiente de verificar: este diff no enlaza ni comprueba que Parent Spec #2 sea `status:ready`; la aserción no es evidencia verificable.)
- La jerarquía solo no implica bloqueo de ejecución; se requiere un prerequisito de ejecución real para cada criterio.
- Ticket #25 (artefacto de procedencia) es el consumidor inmediato y ya implementa el validador de seam.
- ADR-060 registra la excepción temporal de refinamiento automático; este sub-spec la conserva y no la presenta como ejecución exitosa.

## 7. Riesgos

- Riesgo medio: requiere evidencia de revisión antes de la implementación.
- La cobertura parcial existente no debe confundirse con cobertura completa.
- SHA-256 demuestra integridad accidental o deliberada del contenido, no autentica al productor ni establece que la fuente declarada sea autoritativa.
- Los criterios `Not executed` no pueden declararse completos sin prueba ejecutable y evidencia.

## 8. Validación

- `git diff --check`: debe pasar sobre el árbol modificado.
- `python3 -m json.tool` sobre cada artefacto JSON de referencia.
- Ejecución del validador de procedencia con reporte de validación archivado.
- `uv run pytest` para comportamiento de API donde aplique (regresión de la suite existente).

## 9. Evidencia asociada

- `docs/requirements/acceptance-traceability-mvp.md`: matriz AC-01–AC-14 con estados.
- `docs/quality/evidence-register.md`: registro de evidencia ejecutada y no ejecutada.
- `docs/adr/ADR-060-excepcion-gobernada-refinement.md`: excepción de refinamiento.
- `.agents/skills/platform/artifacts/provenance/issue-25-validation-report.json`: reporte de validación de procedencia archivado.
- `docs/engineering/baseline-closure-checklist.md`: checklist de cierre del refinamiento documental.

## 10. Definition of Done para este sub-spec

- Cada requisito atómico tiene seam, oracle y expectativa de evidencia declarados.
- Cada criterio AC-01–AC-14 tiene estado explícito (`Executed`, `Partial` o `Not executed`).
- El comportamiento no ejecutado está marcado y no se presenta como completo.
- `git diff --check` pasa sobre el árbol modificado.
- Los artefactos JSON de referencia validan con `python3 -m json.tool`.

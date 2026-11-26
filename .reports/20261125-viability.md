# Project Viability Assessment

**Repository:** DeepPharma
**Date:** 2026-11-25
**Assessed against:** `CONTEXT.md`, `docs/adr/`, `docs/spec/`, architecture and
current implementation

## Pre-flight Summary

- `CONTEXT.md`: presente y actualizado.
- `docs/adr/`: presente con ADR-002–ADR-004; ADR-001 permanece en
  `docs/architecture/`.
- Assessment confidence: **High** for current implementation; **Medium** for
  production readiness because CI, load and deployment evidence are absent.

## Executive Summary

| Dimension | Rating | Score | Reason | Confidence |
|---|---|---:|---|---|
| Viability | Conditional | 3/5 | La arquitectura puede soportar el MVP, pero la línea base no está cerrada. | High |
| Functionality | Partial | 3/5 | Inventario, RBAC, baseline y alertas funcionan; importación completa y SALMI faltan. | High |
| Scalability | Bounded | 3/5 | El monolito es adecuado para MVP, pero faltan límites, jobs, tenancy y almacenamiento escalable. | High |

**Overall posture:** proyecto viable como tracer bullet controlado; no autorizado
todavía como línea base de implementación completa ni como sistema de producción.

## Findings

### Viability

- La especificación, el plan y las tareas identifican explícitamente el
  alcance y los no objetivos, pero la línea de refinamiento mantiene abiertos
  trazabilidad, contratos, seguridad, retención y despliegue
  (`docs/engineering/refinement-baseline.md:20-69`). **Confidence: High;
  Risk: High.**
- La constitución exige migraciones reproducibles, pero la aplicación ejecuta
  `Base.metadata.create_all` al iniciar (`docs/spec/constitution.md:14-22`,
  `apps/api/app/main.py:29`). **Confidence: High; Risk: High.**
- La validación previa y el adaptador SALMI están bien delimitados
  (`docs/adr/ADR-002-validacion-de-datasets.md`,
  `docs/adr/ADR-004-salmi-adaptable.md`). **Confidence: High; Risk: Low.**

### Functionality

- Inventario, autenticación, RBAC, baseline de riesgo y gestión auditada de
  alertas tienen implementación y pruebas (`apps/api/app/inventory.py`,
  `apps/api/app/auth.py`, `apps/api/app/risk.py`,
  `apps/api/tests/test_health.py`). **Confidence: High; Risk: Low.**
- La spec requiere aplicar conjuntos válidos, pero solo existe validación y
  persistencia; falta `InventoryImportService` y endpoint transaccional
  (`docs/spec/mvp-inventory-risk.md:22-30`,
  `apps/api/app/datasets.py:106-129`). **Confidence: High; Risk: High.**
- El adaptador SALMI simulado, su puerto, sincronización y manejo de fallos no
  existen todavía (`docs/adr/ADR-004-salmi-adaptable.md:13-24`,
  `docs/spec/mvp-inventory-risk.md:48-54`). **Confidence: High; Risk: High.**
- La validación acepta diccionarios genéricos y convierte strings numéricos con
  `int(...)`, por lo que todavía no es un contrato de tipos estrictos
  (`apps/api/app/datasets.py:14-18,48-67`). **Confidence: High; Risk: Medium.**

### Scalability

- El monolito modular es una elección razonable para el MVP
  (`docs/architecture/ADR-001-monolito-modular-en-capas.md:11-22`). **Confidence:
  High; Risk: Low.**
- Las colecciones no tienen paginación ni límites y la evaluación de riesgo es
  síncrona para todo el inventario (`apps/api/app/inventory.py:14-20`,
  `apps/api/app/risk.py:63-73`). **Confidence: High; Risk: High.**
- La validación almacena el conjunto completo como JSON y no existe worker,
  scheduler ni job-status (`apps/api/app/datasets.py:106-129`,
  `docs/architecture/architecture-document.md:44-55`). **Confidence: High;
  Risk: High.**
- RBAC no contiene todavía asignación ni filtrado por centro de salud
  (`apps/api/app/models.py:25-32`, `apps/api/app/inventory.py:14-20`,
  `docs/architecture/quality-scenarios.md:11-14`). **Confidence: High;
  Risk: High.**

## Priority Matrix

| Action | Impact | Effort | Priority | Risk |
|---|---|---|---|---|
| Cerrar spec, trazabilidad, contratos y ADRs | High | Medium | P0 | High |
| Implementar aplicación transaccional de datasets válidos | High | Medium | P0 | High |
| Implementar puerto y adaptador SALMI simulado | High | Medium | P0 | High |
| Eliminar `create_all` y definir política Alembic | High | Low | P1 | High |
| Definir alcance por centro de salud | High | Medium | P1 | High |
| Añadir paginación, límites y jobs | High | High | P1 | High |
| Añadir frontend de importación, historial y alertas completas | Medium | Medium | P1 | Medium |

## Validation Notes

- Tres evaluaciones independientes fueron comparadas.
- Quality gate de evidencias: **passed**; los hallazgos citan documentos,
  código o baseline.
- Conflict resolution: aplicado; la dimensión más restrictiva es
  `Conditional/Partial`.
- No se publicaron Issues, Milestones, Projects ni PRs.
- Baseline automatizado: API **12 tests passed**; frontend lint/build
  aprobados; aproximadamente **1,350 líneas** en `apps/api/app`,
  `apps/api/tests` y `apps/web/app`; CI no detectado.
- No se ejecutaron pruebas de carga, concurrencia, seguridad externa o
  despliegue productivo.

## Verdict

La refinación **todavía no está cerrada**. El repositorio tiene una base
académica y técnica sólida para continuar, pero antes de crear la línea base
oficial se deben cerrar los P0, actualizar la matriz de trazabilidad y
aprobar arquitectura, contratos y criterios operativos.

## Next Step

Continuar con la fase documental: resolver los P0 mediante ADRs, contratos,
matrices y revisión de consistencia. Después solicitar aprobación explícita
para publicar la Spec Issue y crear el Milestone, Project y tickets.

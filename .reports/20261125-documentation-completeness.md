# Auditoría de completitud documental de Ingeniería de Software

**Repositorio:** DeepPharma
**Fecha:** 2026-11-25
**Alcance:** documentación académica, contexto, arquitectura, SDD y
documentación de implementación
**Estado:** auditoría inicial; aún no es una línea base aprobada

Después de esta auditoría se añadieron README, índices documentales y el ADR
canónico. El veredicto sigue vigente hasta cerrar los gaps académicos y de
arquitectura.

## Veredicto

**Incompleta — base avanzada, pero no cerrada.**

Los artefactos mínimos principales están presentes, pero la mayoría conserva
estado de propuesta o borrador. No existe todavía un paquete documental
aprobado y coherente que pueda gobernar Issues, tickets y PRs.

## 1. Entregables académicos

| Entregable | Evidencia | Estado |
|---|---|---|
| Matriz de trazabilidad | `docs/requirements/traceability-matrix.md` | Existe, pero las pruebas están `Pendiente` |
| Modelo general de casos de uso | `docs/design/use-case-diagrams/` | Existe; requiere revisión final contra catálogo |
| Especificaciones de casos de uso | `docs/requirements/use-cases/` | 19 existen; permanecen en refinamiento |
| Escenarios de uso/calidad | `docs/requirements/scenario-catalog.md`, `docs/architecture/quality-scenarios.md` | Existen; faltan metas medidas y cierre |
| Prototipos de pantallas | No se encontró paquete documental formal de prototipos | Faltante académico |
| Arquitectura RUP | `docs/architecture/architecture-document.md` | Existe, pero es propuesta |
| VOPC, secuencia, colaboración y clases | `docs/analysis/vopc/`, `docs/design/` | Existen para dos realizaciones; requieren auditoría UML y trazabilidad |
| Vista lógica | `docs/architecture/views/logical-view.svg` | Existe |
| Vista de despliegue | `docs/architecture/views/deployment-view.svg` | Existe; falta cerrar operación |
| Casos de prueba | `docs/quality/test-plan.md`, `test-catalog.md` | Existen; faltan resultados ejecutados y matriz de evidencia |
| Coevaluación | No se encontró documento o plantilla de coevaluación | Faltante académico |
| Estructura formal del trabajo | No se encontró documento final consolidado | Faltante académico |

## 2. Contexto y documentación general

| Área | Estado | Hallazgo |
|---|---|---|
| `CONTEXT.md` | Parcial | Ahora contiene alcance y workflow, pero todavía mezcla contexto de skills con contexto de producto |
| `README.md` raíz | Incompleto | Solo contiene el título `# DeepPharma` |
| Glosario | Parcial | Tiene vocabulario útil, pero varios términos siguen pendientes de validación |
| Registro de fuentes | Bueno, no cerrado | La jerarquía es clara; faltan decisiones sobre fuentes externas y licencias |
| Guía de contribución | Faltante | No existe una guía completa para ejecutar, probar, documentar y proponer cambios |
| Documentación de usuario | Faltante | No existe guía del farmacéutico, administrador u operador |
| Documentación de desarrollo | Parcial | Hay README de API y apps, pero no existe una guía única de desarrollo |

## 3. ADRs y arquitectura

| Área | Estado | Hallazgo |
|---|---|---|
| ADR de estilo arquitectónico | Parcial | `docs/architecture/ADR-001...` está separado del directorio canónico `docs/adr/` y sigue como propuesta |
| ADR de datasets | Existe | Requiere vincularse a requisitos, casos y migraciones |
| ADR de baseline | Existe | Define demo operativa, no modelo ML validado |
| ADR de SALMI | Existe | El adaptador simulado aún no está documentado como contrato ejecutable |
| ADR de jobs/workers | Faltante | La arquitectura menciona tareas, pero no existe decisión formal |
| ADR de autorización por ámbito | Faltante | RBAC existe, pero el alcance por centro no está diseñado |
| ADR de almacenamiento/retención | Faltante | No hay decisión de retención, archivado ni tamaño de datasets |
| ADR de migraciones/despliegue | Faltante | El runtime todavía usa `create_all` además de Alembic |
| Modelo físico de datos | Incompleto | Faltan índices, cardinalidades físicas, restricciones y retención |
| Contrato API | Incompleto | Faltan OpenAPI versionado, paginación, códigos de error y política de auth completa |

## 4. SDD

| Artefacto | Estado |
|---|---|
| Constitución | Existe como borrador |
| Spec | Existe como borrador local; no publicada |
| Plan | Existe como borrador |
| Tasks | Existe como borrador; no son tickets |
| Verification artifact | No existe |
| Análisis spec-plan-tasks | No ejecutable todavía porque no hay ticket set publicado |
| Aprobación | No registrada |

## 5. Implementación y operación

Faltan o están incompletos:

- CI/CD.
- Docker/Compose o despliegue reproducible.
- `.env.example` y configuración documentada sin secretos.
- Runbook operativo.
- Observabilidad y health/readiness.
- Política de backups y recuperación.
- Pruebas frontend.
- Pruebas de migraciones, contratos, seguridad y carga.
- Aplicación transaccional de datasets válidos.
- Adaptador SALMI simulado.
- Historial y consulta de datasets en frontend/API.

## 6. Gaps bloqueantes antes de la línea base

1. Crear prototipos académicos y documentar su relación con CU-04/CU-05.
2. Completar la matriz de trazabilidad sin `Pendiente` no justificado.
3. Consolidar ADRs bajo `docs/adr/` y asignar estado, decisor y evidencia.
4. Separar contexto de producto, contexto académico y contexto de skills.
5. Crear README raíz completo y guía de desarrollo.
6. Cerrar arquitectura de despliegue, datos, seguridad, retención y workers.
7. Crear documento formal de pruebas y evidencia ejecutada.
8. Crear el paquete formal del trabajo académico y coevaluación.
9. Revisar todos los casos de uso contra la rúbrica y marcar aprobados,
   propuestos o fuera de MVP.
10. Solo después aprobar la línea base y pasar a Milestone, Project, Spec
    Issue, tickets y PRs.

## Conclusión

La documentación no está vacía ni desorganizada: existe una base importante.
Sin embargo, todavía es una **base de trabajo**, no una línea base formal de
Ingeniería de Software. La siguiente fase debe ser documental y de
consistencia; no debe agregar funcionalidades.

## Correcciones documentales ya aplicadas

- README raíz ampliado con alcance, navegación, ejecución y seguridad.
- Índice general `docs/README.md` creado.
- READMEs de requisitos, arquitectura, calidad, implementación y paquete
  académico creados.
- ADR-001 consolidado bajo `docs/adr/` con vista de compatibilidad preservada.

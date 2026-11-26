# Revisión de línea base arquitectónica

**Estado:** Arquitectura MVP aprobada para planificación; riesgos de
implementación y evidencia permanecen abiertos.

## Correspondencia

| Elemento | Documento | Estado |
|---|---|---|
| Estilo | `docs/adr/ADR-001-monolito-modular-en-capas.md` | Aceptada para MVP |
| Validación de datos | `docs/adr/ADR-002-validacion-de-datasets.md` | Aceptada para MVP |
| Riesgo baseline | `docs/adr/ADR-003-baseline-de-riesgo.md` | Aceptada para MVP |
| SALMI | `docs/adr/ADR-004-salmi-adaptable.md` | Aceptada como límite |
| Jobs | `docs/adr/ADR-005-jobs-y-evaluacion-asincrona.md` | Aceptada con alcance diferido |
| Ámbito | `docs/adr/ADR-006-autorizacion-por-ambito.md` | Aceptada como principio técnico |
| Migraciones | `docs/adr/ADR-007-migraciones-y-despliegue.md` | Aceptada |
| Retención | `docs/adr/ADR-008-retencion-de-datasets.md` | Aceptada para fixtures sintéticos |

## Vistas verificadas

- casos de uso;
- lógica;
- procesos;
- implementación;
- despliegue;
- datos;
- modelo físico.

Las fuentes PlantUML de las vistas existentes se renderizan correctamente.

## Gaps de línea base

- contrato de jobs aún no implementado;
- autorización por ámbito no modelada físicamente;
- política de retención pendiente;
- paginación y límites API pendientes;
- OpenAPI versionado pendiente;
- worker y scheduler pendientes;
- `create_all` debe eliminarse antes de una línea base de despliegue;
- escenarios de calidad necesitan medidas y entorno.

## Criterio de aprobación

La arquitectura se considera aceptada para planificación porque:

1. los ADR relevantes tienen decisor y límites explícitos;
2. el modelo físico y contratos API tienen una correspondencia documentada;
3. los riesgos de migración, autorización y retención tienen mitigaciones
   trazables;
4. existe una estrategia de despliegue reproducible;
5. los escenarios de calidad tienen pruebas diseñadas y objetivos iniciales.

Los gaps restantes son restricciones de implementación y tickets de
verificación, no supuestos silenciosos ni autorización para afirmar
cumplimiento productivo.

La trazabilidad de requisitos no convierte esta propuesta en una arquitectura
aprobada: los gaps de autorización, retención, API, jobs y operación siguen
requiriendo decisiones, diseño detallado o evidencia.

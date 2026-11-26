# Checklist de cierre del refinamiento documental

**Estado:** Criterio aceptado; ejecución del checklist pendiente
**Fecha:** 2026-11-25

## Condición de cierre

El refinamiento documental puede cerrarse cuando exista consistencia entre:

- `CONTEXT.md`;
- ADRs aceptados y propuestas explícitamente marcadas;
- requisitos, reglas, actores y casos de uso;
- arquitectura, datos, seguridad y operación;
- constitución, spec, plan y tareas SDD;
- matriz de trazabilidad;
- catálogo y registro de evidencia.

## Reglas del veredicto

1. Una decisión externa pendiente no invalida la consistencia técnica si está
   identificada, asignada y vinculada a su impacto.
2. Una prueba no ejecutada no puede marcarse como aprobada.
3. Un gap de implementación debe distinguirse de un defecto documental.
4. El veredicto debe listar bloqueadores para implementación, publicación y
   producción por separado.
5. El cierre documental no autoriza por sí mismo Issues, Milestones,
   Projects, ramas o PRs; esos pasos requieren una decisión posterior.

## Evidencia mínima

- `git diff --check`;
- validación JSON de artefactos;
- renderización de fuentes PlantUML;
- gates del backend y frontend;
- revisión de referencias y estados;
- informe final con pendientes, responsables e impacto.

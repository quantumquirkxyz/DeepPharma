# Índice de gobernanza de work items

## Fuente canónica

DeepPharma usa GitHub Issues como tracker para requisitos, especificaciones,
decisiones y tickets de implementación. El repositorio es
`quantumquirkxyz/DeepPharma`.

## Flujo obligatorio

1. **Refinar:** grill-with-docs identifica decisiones, límites y riesgos.
2. **Especificar:** to-spec publica una especificación verificable.
3. **Planificar:** se documentan arquitectura, seams y validación.
4. **Descomponer:** to-tickets crea slices trazables y dependencias.
5. **Implementar:** implement trabaja únicamente tickets `status:ready`.
6. **Verificar:** se revisa la correspondencia entre spec, tickets y código.
7. **Publicar:** la publicación de PR es una operación separada.

## Reglas de tracker

- No implementar una feature sin Issue o ticket asociado.
- Cada ticket debe declarar requisitos, criterios de aceptación, dependencias y
  evidencia esperada.
- Las decisiones no resueltas permanecen como bloqueos o preguntas; no se
  convierten en supuestos silenciosos.
- Un Issue de spec precede a sus tickets hijos.
- Parent Specs y Sub-Specs se distinguen mediante `type:spec` y
  `type:sub-spec`, según `docs/adr/ADR-036-labels-de-spec-y-sub-spec.md`.
- Cada nivel de especificación debe tener un handoff SDD válido antes de
  generar sus Tickets.
- Las mutaciones remotas requieren evidencia del repositorio y etiquetas
  canónicas.

## Habilidades downstream

| Solicitud | Skill |
|---|---|
| Refinar una idea o plan | `grill-with-docs` |
| Publicar una spec | `to-spec` |
| Crear tickets desde una spec | `to-tickets` |
| Crear o configurar un board | `make-project` |
| Implementar un ticket listo | `implement` |
| Auditar spec, plan y tickets | `analyze-artifacts` |
| Publicar un PR terminado | `publish-open-pr` |

## Documentos relacionados

- `docs/reference/agents/issue-tracker.md`
- `docs/reference/agents/triage-labels.md`
- `docs/reference/agents/work-item-format.md`
- `docs/reference/agents/skill-contract-overrides.md`
- `docs/reference/agents/domain.md`
- `CONTEXT.md`

# Diseño del tracker del MVP

**Estado:** Diseño cerrado y publicado en el GitHub Project MVP
**Fecha:** 2026-11-25

## Project

- **Owner:** `quantumquirkxyz`
- **Repository:** `quantumquirkxyz/DeepPharma`
- **Title:** `DeepPharma — MVP`
- **Visibility:** pública
- **Views:** `Board Delivery`, `Delivery Table`, `Blocked and Triage` y
  `Traceability`

## Milestones

1. `M0 — Baseline y gobierno`
2. `M1 — Datos e inventario`
3. `M2 — Riesgo ML y fallback`
4. `M3 — Alertas, auditoría y notificaciones`
5. `M4 — Seguridad, operación y verificación`

Cada Milestone tendrá un Parent Spec.

## Jerarquía

```text
Milestone
└── Parent Spec (Issue type:spec)
    └── Sub-Spec (Issue type:sub-spec)
        └── Ticket
            └── Branch
                └── Pull Request
```

Las relaciones Parent Spec → Sub-Spec → Ticket deben usar sub-issues nativos.
Las dependencias de ejecución se expresan aparte mediante `blocked_by`.

## Labels canónicos

Cada work item usa:

- un `status:*`;
- un `type:*`;
- `area:requirements`;
- un `priority:*`;
- un `risk:*`.

Priority and Risk are mandatory for publishable MVP work items; use
`risk:unknown` when risk has not yet been evaluated.

### Tipos

- Parent Spec: `type:spec`;
- Sub-Spec: `type:sub-spec`;
- Ticket: tipo específico;
- documentación no especulativa: `type:documentation`.

Native GitHub Issue Types are optional. If available, they must map exactly to
these labels; otherwise labels remain the only classification mechanism.

### Riesgo

`risk:critical`, `risk:high`, `risk:medium`, `risk:low`,
`risk:unknown`.

### Sincronización

Issues y PRs poseen los labels. El Project proyecta Labels y mantiene su
campo nativo `Status` alineado con `status:*`. Priority y Risk no se duplican
como campos personalizados.

Status also includes `status:needs-info`; it is distinct from
`area:requirements`. `status:blocked` remains transversal and
`status:out-of-scope` terminal.

La sincronización se implementará mediante una automatización verificable de
GitHub Actions o reglas de la UI; no se asumirá que GraphQL la crea.

## Reglas de entrega

- Tracker y PRs en inglés.
- Máximo un PR por Ticket.
- Rama: `issue/<number>-<slug>`.
- El PR copia labels y Milestone del Ticket.
- `Closes #N` solo cuando el cierre automático sea intencional.
- PR abierto: Ticket y PR en `status:review`; merge verificado: ambos en
  `status:done`; cierre sin merge no completa el Ticket.
- No crear nada remotamente hasta aprobar la línea base y ejecutar el flujo
  de publicación correspondiente.

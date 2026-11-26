# ADR-053 — Orden de publicación del tracker

**Estado:** Aceptada para preparación; mutaciones remotas pendientes
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Después de aprobar la línea base:

1. `make-project` crea y configura `DeepPharma — MVP`;
2. se crean los cinco Milestones;
3. `to-spec` publica un Parent Spec por Milestone;
4. se publican los Sub-Specs como sub-issues nativos;
5. `to-tickets` publica los Tickets como sub-issues de Sub-Specs;
6. `implement` trabaja únicamente Tickets `status:ready`.

Cada operación conserva su propia aprobación, checkpoint y evidencia.

## Consecuencias

- El Project existe antes de poblar la jerarquía de trabajo.
- Un fallo parcial no autoriza repetir mutaciones a ciegas.
- La publicación sigue separada de implementación y PRs.

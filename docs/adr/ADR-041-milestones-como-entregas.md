# ADR-041 — Milestones como entregas

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada Milestone representa una entrega del MVP con:

- nombre estable;
- objetivo;
- alcance;
- fecha opcional;
- criterio de cierre.

El Parent Spec, sus Sub-Specs y sus Tickets compartirán el Milestone
correspondiente. El Milestone agrupa la entrega, pero no sustituye la relación
Parent Spec → Sub-Spec → Ticket.

No se usarán Milestones para representar fases como Spec, Implementación o
Review; esas fases pertenecen a los estados y labels del tracker.

## Consecuencias

- El avance del Milestone puede medirse por sus Issues hijos.
- Un ticket no debe pertenecer a un Milestone distinto de su Parent Spec sin
  una decisión explícita.
- Crear o modificar Milestones requiere aprobación remota separada.

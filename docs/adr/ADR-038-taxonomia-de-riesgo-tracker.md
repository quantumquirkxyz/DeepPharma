# ADR-038 — Taxonomía de riesgo del tracker

**Estado:** Aceptada para el flujo del tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Los work items podrán llevar exactamente un label `risk:*`:

- `risk:critical`;
- `risk:high`;
- `risk:medium`;
- `risk:low`;
- `risk:unknown`.

`risk:unknown` se usa cuando todavía no existe evaluación suficiente. La
prioridad (`priority:*`) y el riesgo (`risk:*`) son dimensiones independientes.

## Consecuencias

- La prioridad expresa urgencia o precedencia.
- El riesgo expresa impacto o incertidumbre técnica/operativa.
- El Project puede filtrar ambas dimensiones sin mezclarlas.
- Todo riesgo deberá explicarse también en el cuerpo del Issue.

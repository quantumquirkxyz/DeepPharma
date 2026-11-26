# ADR-039 — Área de requisitos para la jerarquía de trabajo

**Estado:** Aceptada para el flujo inicial del MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Parent Specs, Sub-Specs y Tickets del MVP usarán `area:requirements` para
mantener visible su pertenencia a la cadena de requisitos.

El `type:*` seguirá expresando la naturaleza del work item:

- `type:spec` para Parent Specs;
- `type:sub-spec` para Sub-Specs;
- `type:feature`, `type:bug`, `type:architecture` u otro tipo válido para
  Tickets según corresponda.

La clasificación más detallada de módulos, pruebas o seguridad permanecerá en
el cuerpo, criterios, referencias y Project, no en otra área obligatoria.

## Consecuencias

- La jerarquía se puede filtrar de forma uniforme.
- Se evita dividir artificialmente la cadena de requisitos entre áreas.
- La taxonomía `area:*` podrá ampliarse después mediante una decisión separada.

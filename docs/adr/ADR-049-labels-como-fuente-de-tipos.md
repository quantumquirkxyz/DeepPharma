# ADR-049 — Labels como fuente canónica de tipos

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Los labels `type:spec`, `type:sub-spec` y los demás `type:*` serán la fuente
canónica de clasificación de work items. Si GitHub ofrece Issue Types nativos,
solo se usarán cuando exista un mapeo exacto y no se cree una segunda semántica.

No se asignarán automáticamente dos clasificaciones contradictorias al mismo
Issue o PR.

## Consecuencias

- La taxonomía local sigue siendo portable y verificable.
- El dry-run debe comprobar la disponibilidad y compatibilidad de Issue Types.
- Los labels continúan siendo obligatorios aunque exista soporte nativo
  parcial.

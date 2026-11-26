# ADR-021 — Gobernanza de datos institucionales

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Ningún dato institucional entra al sistema sin:

- autorización documentada;
- clasificación;
- fuente y licencia o permiso;
- responsable de datos;
- finalidad de uso;
- política de retención;
- controles de acceso;
- registro de procedencia.

Hasta cumplir esas condiciones se usan fixtures sintéticos o datos públicos
autorizados.

Cuando se requiera conservar el dataset fuente completo, se aplicará la
separación de `ADR-032`: original restringido y proyección operativa mínima.

## Consecuencias

- La ausencia de datos institucionales no se oculta como fallo del modelo.
- Los datasets sintéticos deben permanecer identificados.
- La incorporación posterior requiere revisión de privacidad y seguridad.

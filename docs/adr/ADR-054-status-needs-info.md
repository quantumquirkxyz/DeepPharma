# ADR-054 — Estado `status:needs-info`

**Estado:** Aceptada para el tracker
**Fecha:** 2026-11-26
**Decisor:** Propietario del proyecto

## Decisión

`status:needs-info` será un estado canónico separado de `area:requirements`.
Representará un work item que espera aclaraciones o información antes de poder
continuar.

La máquina de estados será:

```text
status:triage → status:needs-info → status:ready
status:triage → status:ready
status:ready → status:in-progress → status:review → status:done
```

`status:blocked` es transversal y `status:out-of-scope` es terminal. La razón
de `needs-info` o `blocked` debe constar en el cuerpo del Issue.

## Consecuencias

- `area:requirements` conserva su significado disciplinar.
- Los filtros del Project pueden distinguir triage, espera de información y
  bloqueo real.
- Un work item no pasa a `status:ready` sin resolver la información requerida.

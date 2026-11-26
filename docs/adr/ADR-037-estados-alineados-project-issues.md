# ADR-037 — Estados alineados entre Issues y Project

**Estado:** Superseded by ADR-054
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Los Issues usarán la máquina de estados:

```text
status:triage → status:ready → status:in-progress → status:review → status:done
                         └──→ status:blocked
```

`status:out-of-scope` representa una salida terminal. El campo nativo `Status`
del GitHub Project reflejará estos estados y no se creará una fase paralela
que pueda divergir.

> Esta versión queda supersedida por `ADR-054`, que añade
> `status:needs-info` entre triage y ready.

## Consecuencias

- El label del Issue es la semántica canónica del tracker.
- El Project es una proyección operativa y visual.
- Los cambios de estado deben conservar coherencia entre Issue y Project.
- Los estados nativos exactos se mapearán durante el dry-run de `make-project`.

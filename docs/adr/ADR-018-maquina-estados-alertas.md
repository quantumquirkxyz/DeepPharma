# ADR-018 — Máquina de estados de alertas

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Estados

```text
NUEVA → RECONOCIDA → EN_REVISION → RESUELTA
  └──────────────→ DESCARTADA
  └────→ EN_REVISION
```

`DESCARTADA` puede alcanzarse desde estados abiertos. `RESUELTA` y
`DESCARTADA` son terminales.

## Reglas

- Toda transición válida conserva actor, fecha, comentario y estados.
- Las transiciones inválidas se rechazan sin mutar la alerta.
- Una alerta terminal no puede modificarse.
- Reconocer no equivale a resolver.

## Consecuencias

- Las pruebas de transición usan tablas y cobertura de estados.
- El frontend debe mostrar acciones según estado.
- Las alertas reabiertas requieren una decisión explícita posterior.
